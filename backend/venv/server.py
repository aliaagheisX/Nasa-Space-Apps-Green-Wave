from flask import Flask, render_template, request, redirect, session,abort
from flask import jsonify
import random
import requests
import json
import datetime
import numpy as np
import matplotlib.pyplot as plt
from pymongo import MongoClient
from crontab import CronTab
from datetime import datetime
from flask_pymongo import PyMongo
import h5py 
from src.download_SPL3SMP import cmr_download, cmr_search
import math 
from mpl_toolkits.basemap import Basemap
import os
from datetime import datetime, timedelta



# # Create a new CronTab instance for the current user
# cron = CronTab(user=True)

# # Create a new job that echoes "hello_world" every minute
# job = cron.new(command=getEVI())
# job2=cron.new(command=)
# job.minute.every(1)

# # Write the job to the crontab
# cron.write()

app=Flask(__name__)
# Connect to MongoDB
client = MongoClient('mongodb+srv://mennamohamed0207:PZN2oliMRnf8KqmL@cluster0.ue0sm7q.mongodb.net/NasaSpaceApp')
db = client['farm_data']
collection = db['locations']
messages=db['messages']



@app.route('/add_location', methods=['POST'])
def add_location():
    data = request.get_json()
    lon = data.get('long')
    lat = data.get('lat')
    username = data.get("username", "default_farmer")

    # Check if the location with the same username, latitude, and longitude already exists
    existing_location = collection.find_one({"username": username, "location": [lon, lat]})

    if existing_location:
        # Location already exists, so don't insert again
        return jsonify({"message": "Location already exists for this user!"}), 409  # 409 Conflict

    # Proceed to insert the new location
    checkNDVI = getNDVI(lon, lat)
    print(checkNDVI)
    location = {
        "username": username,
        "location": [lon, lat]
    }
    collection.insert_one(location)
    return jsonify({"message": "Location added successfully!"}), 201

def getEVI(lon,lat):
    url = "https://modis.ornl.gov/rst/api/v1/"
    header = {'Accept': 'application/json'} # Use following for a csv response: header = {'Accept': 'text/csv'}
    try:
        response = requests.get(f'https://modis.ornl.gov/rst/api/v1/MOD13Q1/dates?latitude={lat}&longitude={lon}', headers=header)
        dates = json.loads(response.text)['dates']
        start_date, end_data = dates[-2]['modis_date'],  dates[-1]['modis_date']
        band = '250m_16_days_EVI'

        response = requests.get(f'https://modis.ornl.gov/rst/api/v1/MOD13Q1/subset?latitude={lat}&longitude={lon}&startDate={start_date}&endDate={end_data}&band={band}&kmAboveBelow=70&kmLeftRight=70', headers=header)

        subset = json.loads(response.text)
    except:
        return jsonify({"message":"API didn't make it 🤯"})
    data = subset['subset'][0]['data']
    data = np.array(data).reshape(subset['nrows'], -1)
    data_null = data.min()
    print(data.max(), data.min(), data.mean(), (data == data_null).sum() / (len(data)))
    data[data==data_null] = 0
    print(float(data.mean())*float(subset['scale']))
    return float(data.mean())*float(subset['scale'])

def getNDVI(lon,lat):
    url = "https://modis.ornl.gov/rst/api/v1/"
    header = {'Accept': 'application/json'} # Use following for a csv response: header = {'Accept': 'text/csv'}
    response = requests.get(f'https://modis.ornl.gov/rst/api/v1/MOD13Q1/dates?latitude={lat}&longitude={lon}', headers=header)
    print(response.text)
    dates = json.loads(response.text)['dates']
    start_date, end_data = dates[-2]['modis_date'],  dates[-1]['modis_date']
    band = '250m_16_days_NDVI'

    response = requests.get(f'https://modis.ornl.gov/rst/api/v1/MOD13Q1/subset?latitude={lat}&longitude={lon}&startDate={start_date}&endDate={end_data}&band={band}&kmAboveBelow=70&kmLeftRight=70', headers=header)
    subset = json.loads(response.text)
    data = subset['subset'][0]['data']
    data = np.array(data).reshape(subset['nrows'], -1)
    data_null = data.min()
    print(data.max(), data.min(), data.mean(), (data == data_null).sum() / (len(data)))
    data[data==data_null] = 0
    print(float(data.mean())*float(subset['scale']))
    return float(data.mean())*float(subset['scale'])
#get NVDI from longitide and latitde 

good_messages = [
    "المحصول بخير ومش محتاج تسميد دلوقتي! 🌿",
    "الأرض صافية والمزروعات قوية، مفيش داعي للتسميد. 💪🌾",
    "المحصول صحي ومش محتاج أي تدخلات، خليها على طبيعتها! 🍀",
    "الأرض بتقولك: مش عايزة تسميد، كله تمام! 🥒👍",
    "ما شاء الله، النباتات قوية وصحية، مش محتاجين سماد دلوقتي. 🌻👌",
    "الأرض في أفضل حالاتها، مفيش حاجة للتسميد. 🥦💚",
    "مش محتاج تحط سماد، المحصول في حالة ممتازة! 🌽✨",
    "النباتات صحية وجاهزة للإنتاج، مش محتاجين إضافات تانية. 🌿😊",
    "مفيش مشاكل، المحصول بخير ومش محتاج سماد! 🌱✨",
    "المحصول مستقر ومش محتاج تسميد حاليًا، ربنا يبارك! 🌾🙏"
]
# List of warning messages in Egyptian Arabic
fertilizer_messages = [
    "المحصول محتاج تسميد، نقص العناصر الغذائية ممكن يأثر على النمو. 💡",
    "النباتات شكلها تعبان، محتاج تضيف سماد لزيادة الإنتاجية. 🌱",
    "في نقص في العناصر الغذائية، يفضل تضيف سماد علشان تحسن صحة النبات. 🌾",
    "لاحظنا إن المحصول مش واخد كفايته من التغذية، ياريت تضيف شوية سماد. 🧪",
    "الأرض محتاجة شوية سماد، علشان النباتات تكمل نموها بشكل سليم. 🌿",
    "النباتات محتاجة تسميد علشان تتغلب على نقص العناصر، ممكن تستعمل سماد نيتروجين. 🥬",
    "الزرع محتاج دعم بالتسميد، ممكن تحط سماد فوسفور علشان تنشط الجذور. 🌱",
    "في ضعف في النمو بسبب نقص العناصر، ياريت تشوف نوع السماد المناسب. 💧",
    "لاحظنا إن المحصول مش بيكبر كويس، يفضل تسميد الأرض بسرعة. 🔧",
    "التربة ناقصة عناصر غذائية، ياريت تضيف سماد بوتاسيوم لتحسين الحالة العامة. 🧪",
    "النباتات مش بتكبر بشكل كويس، محتاجة تسميد علشان تكمل نموها. 🌽",
    "التربة ضعيفة ومحتاجة تسميد فوري، علشان المحصول يكمل على خير. 🌾",
    "الزرع في حالة إجهاد، محتاج تسميد علشان يرجع لطبيعته. 💪",
    "المحصول مش واخد كفايته من التغذية، يفضل تضيف سماد عضوي لدعمه. 🥦",
    "لاحظنا نقص في العناصر، ياريت تستعمل سماد متكامل لدعم النمو. 🌱",
]
@app.route('/getMessage',methods=['POST'])
def getMessages():
    req = request.get_json()
    username = req.get("username", "menna")
    
    user_messages = list(messages.find({"username": username}))
    # Convert each message document to a format that can be serialized
    serialized_messages = []
    for message in user_messages:
        # Convert ObjectId to string and append to serialized list
        message['_id'] = str(message['_id'])
        serialized_messages.append(message)

    # Return the messages as a JSON response
    return jsonify({"messages": serialized_messages})
    

    
@app.route('/fertilizers',methods=['POST'])
def getFertilizerInfo():
    req = request.get_json()
    if request.method == 'POST':
        long = req.get('long')
        lat = req.get("lat")
        username=req.get("username","menna")
        
        # Call the Python code (replace NDVI with the actual calculation)
        
        NDVI = getNDVI(long, lat)  # This needs to be replaced with actual NDVI value calculation
        EVI=getEVI(long,lat)
        print("NDVI is ",NDVI)
        if NDVI > 0.5 and NDVI < 1 and EVI>0.5 and EVI <1:
            selected_message = random.choice(good_messages)
            data = {"message": selected_message}
        elif NDVI > 0.2 and NDVI < 0.5 and EVI>0.2 and EVI <0.5:
            selected_message = random.choice(fertilizer_messages)
            data = {"message": selected_message}
        elif NDVI < 0.2 and NDVI > 0 and EVI<0.2 and EVI >0:
            selected_message = "الأرض فاضية تقريبًا، مفيش نباتات مزروعة أو النباتات لسه في بداية النمو."
            data = {"message": selected_message}
        else:
            return jsonify({"message":"Not found"}),404
        current_time=datetime.now().strftime("%Y-%m-%d")
        messages=db.messages
        messages.insert_one({"message":selected_message,"time":current_time,"username":username})
        return jsonify(data)
    else:
        return jsonify({"message": "error has occurred"})
    
@app.route('/update_location', methods=['POST'])
def update_location():
    # Parse the incoming request data
    data = request.get_json()
    username = data.get("username","menna")
    new_lon = data.get("long")
    new_lat = data.get("lat")

    # Check if all required fields are provided
    if not username or new_lon is None or new_lat is None:
        return jsonify({"message": "Invalid input data. Make sure 'username', 'long' and 'lat' are provided."}), 400

    # Update the location in the MongoDB collection
    result = collection.update_one(
        {"username": username},  # Filter condition
        {"$set": {"location": [new_lon, new_lat]}}  # Update condition
    )

    # Check if the update was successful
    if result.matched_count > 0:
        return jsonify({"message": "Location updated successfully!"}), 200
    else:
        return jsonify({"message": "No matching user found to update."}), 404

def get_bounding_box(lat, lon, above_below_km, left_right_km):
    # Latitude and longitude change calculations
    lat=float(lat)
    lon=float(lon)
    lat_change = above_below_km / 111
    lon_change = left_right_km / (111 * math.cos(math.radians(lat)))
    
    # Bounding box coordinates
    min_lat = lat - lat_change #S
    max_lat = lat + lat_change #N
    min_lon = lon - lon_change #W
    max_lon = lon + lon_change #E
    
    return min_lon, min_lat, max_lon, max_lat

def get_bounding_box_str(lat, lon, above_below_km, left_right_km):
    min_lon, min_lat, max_lon, max_lat = get_bounding_box(lat, lon, above_below_km, left_right_km)
    return f"{min_lon},{min_lat},{max_lon},{max_lat}"
def get_soil_moist_from_path(path, bounding_box, is_am = True):
    with h5py.File(path, mode="r") as f:
        field_time = 'AM' if is_am else "PM"
        name = f'/Soil_Moisture_Retrieval_Data_{field_time}/soil_moisture'

        data = f[name][:]
        _FillValue = f[name].attrs['_FillValue']
        valid_max = f[name].attrs['valid_max']
        valid_min = f[name].attrs['valid_min']        
        
        invalid = np.logical_or(data > valid_max,
                                data < valid_min)
        invalid = np.logical_or(invalid, data == _FillValue)
        
        data[invalid] = 0 # to ignore in getting average
        # get 
        latitude = f['/Soil_Moisture_Retrieval_Data_AM/latitude'][:]
        longitude = f['/Soil_Moisture_Retrieval_Data_AM/longitude'][:]
        min_lon, min_lat, max_lon, max_lat = bounding_box
        print(min_lon,min_lat,max_lon,max_lat)
        
        n, m = data.shape
        plot(path,(min_lon,max_lon),(min_lat,max_lat))
        sum, cnt = 0,0
        for i in range(n):
            for j in range(m):
                if (min_lon <= longitude[i][j] <= max_lon) and (min_lat <= latitude[i][j] <= max_lat) and (data[i][j] != 0):
                    sum += data[i][j]
                    cnt += 1
        return sum, cnt

def plot(path, lon_range=None, lat_range=None):
    """
    Plots soil moisture data from the given HDF5 file path, filtering by longitude and latitude if provided.

    Parameters:
        path (str): Path to the HDF5 file.
        lon_range (tuple, optional): A tuple of (min_longitude, max_longitude) to filter data by longitude.
        lat_range (tuple, optional): A tuple of (min_latitude, max_latitude) to filter data by latitude.
    """
    with h5py.File(path, mode="r") as f:
        # Load the soil moisture data
        name = '/Soil_Moisture_Retrieval_Data_AM/soil_moisture'
        data = f[name][:]
        
        # Load metadata attributes
        units = f[name].attrs['units'].decode('ascii', 'replace')
        long_name = f[name].attrs['long_name'].decode('ascii', 'replace')
        _FillValue = f[name].attrs['_FillValue']
        valid_max = f[name].attrs['valid_max']
        valid_min = f[name].attrs['valid_min']
        
        # Mask invalid data
        invalid = np.logical_or(data > valid_max, data < valid_min)
        invalid = np.logical_or(invalid, data == _FillValue)
        data[invalid] = np.nan
        data = np.ma.masked_where(np.isnan(data), data)
        
        # Get the geolocation data
        latitude = f['/Soil_Moisture_Retrieval_Data_AM/latitude'][:]
        longitude = f['/Soil_Moisture_Retrieval_Data_AM/longitude'][:]

        # Filter data based on the provided latitude and longitude ranges
        if lon_range:
            lon_mask = (longitude >= lon_range[0]) & (longitude <= lon_range[1])
        else:
            lon_mask = np.ones_like(longitude, dtype=bool)  # Include all data if not specified
        
        if lat_range:
            lat_mask = (latitude >= lat_range[0]) & (latitude <= lat_range[1])
        else:
            lat_mask = np.ones_like(latitude, dtype=bool)  # Include all data if not specified
        
        # Combine masks
        combined_mask = lon_mask & lat_mask

        # Apply combined mask to filter data and locations
        filtered_data = data[combined_mask]
        filtered_longitude = longitude[combined_mask]
        filtered_latitude = latitude[combined_mask]

        # Plotting using Basemap
        m = Basemap(projection='cyl', resolution='l',
                    llcrnrlat=-90, urcrnrlat=90,
                    llcrnrlon=-180, urcrnrlon=180)
        m.drawcoastlines(linewidth=0.5)
        m.drawparallels(np.arange(-90, 91, 45))
        m.drawmeridians(np.arange(-180, 180, 45), labels=[True, False, False, True])
        
        # Plot the filtered soil moisture data
        scatter = m.scatter(filtered_longitude, filtered_latitude, c=filtered_data, s=1, cmap=plt.cm.jet,
                            edgecolors=None, linewidth=0)
        cb = m.colorbar(scatter, location="bottom", pad='10%')
        cb.set_label(units)
        
        # Save plot
        basename = os.path.basename(path)
        plt.title(f'{basename}\n{long_name}')
        plt.savefig(f"../../assets/plots/{basename}.png")
        plt.show()

    
def fetch_data(lat, lon, folder_path="datasets/smap", time_start = '2024-10-01T00:00:00Z', time_end = '2024-10-02T21:48:13Z'):
    short_name = 'SPL3SMP'
    version = '009'
    polygon = ''
    filename_filter = ''
    url_list = []
    bounding_box = get_bounding_box_str(lat, lon, 100, 100)
    force = False
    quiet = False
    
    try:
        url_list = cmr_search(short_name, version, time_start, time_end,
                              bounding_box=bounding_box, polygon=polygon,
                              filename_filter=filename_filter, quiet=quiet)
        cmr_download(url_list, force=force, quiet=quiet, folder_path=folder_path)
    except KeyboardInterrupt: # to graceful shutdown when intrrput
        quit()

    return url_list
@app.route("/moisture",methods=['POST'])
def getMoisture():
    data=request.get_json()
    lat=data.get("lat")
    lon=data.get("lon")
    # Get today's date
    today = datetime.utcnow()

    # Calculate yesterday's date
    yesterday = today - timedelta(days=1)

    # Format it in the desired format: YYYY-MM-DDTHH:MM:SSZ
    yesterday_formatted = yesterday.strftime('%Y-%m-%dT00:00:00Z')
    
    sum, cnt = 0, 1e-9
    folder_path = "datasets/smap"
    url_list = fetch_data(lat, lon)
    for url in url_list:
        if url[-2:] == 'h5':
            file_name = url.split('/')[-1]
            path = folder_path + "/" + file_name
            bounding_box = get_bounding_box(lat, lon, 100, 100)
            partial_sum, partial_cnt = get_soil_moist_from_path(path, bounding_box)
            sum += partial_sum
            cnt += partial_cnt
    answer = sum / cnt
    return jsonify(answer)
    
        
        

if __name__ == '__main__':
    app.run()