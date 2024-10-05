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


if __name__ == '__main__':
    app.run()