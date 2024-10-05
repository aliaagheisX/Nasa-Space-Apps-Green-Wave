# Nasa Space Apps Green Wave
* Challenge: Leveraging Earth Observation data for informed Agriculture Decision-Making <br/>
 **Empowering Farmers with Real-Time Satellite Data Insights for Optimized Crop Management**

## 🌟 Project Summary

Our Project is a mobile-based solution that leverages satellite data to provide farmers with real-time insights on soil moisture and plant health. Utilizing data from NASA’s Terra satellite (MODIS) and SMAP sensor, the system enables farmers to make informed decisions to improve water usage and boost crop yields. Through our user-friendly Flutter app, farmers can access crucial information about soil conditions and vegetation health directly from their smartphones. Our solution aims to enhance agricultural productivity while promoting sustainable farming practices. 🌱📈

## 🌟 Key Benefits

- **🚿 Optimized Irrigation**: Adjust water usage based on real-time soil moisture levels.
- **🌿 Improved Crop Health**: Detect crop stress early and intervene quickly to maintain plant health.
- **📈 Increased Productivity**: Ensure crops get the right amount of water and nutrients, boosting yields and productivity.
- **📱 User-Friendly**: Complex satellite data is translated into clear messages and visualizations for easy understanding.
## 🛠️ Architecture
This is the block diagram of our program
![image](https://github.com/user-attachments/assets/d95da488-c529-4d4a-814c-9dcedeb7a55d)

# 📱 How It Works
## Requirements
* python 3.10 or later
* Jupyter Notbook
* PyHDF
* gcc
* Flask
* MongoDB
### Install Python using MiniConda
1. Download and install MiniConda from [here](https://docs.anaconda.com/miniconda/#quick-command-line-install)
2. create new environment
    ```bash
    conda create -n nasa python=3.10
    ```
3. activate environment
    ```bash
    conda activate nasa
    ```
### Install `PyHDF`

#### 1. install `pyhdf` using conda use one of commands
    
```bash
conda install conda-forge::pyhdf
```
    
```bash
conda install conda-forge/label/cf201901::pyhdf
```
```bash
conda install conda-forge/label/cf202003::pyhdf
```
```bash
conda install conda-forge/label/gcc7::pyhdf 
```

if all doesn't work try

```bash
pip install pyhdf
```
### 3. install h5py
```bash
conda install h5py
```
### Install Flask 
- Create a Virtual Environment (Optional but Recommended):
  ```sh
  python -m venv venv
  ```
- If you are on Windows use this command:
  ```sh
  venv\Scripts\activate
  ```
- Install flask:
  ```sh
  pip install Flask
  ```
  
### Install Jupyter Notebook
to see examples 

## Installation
* Install the required packages
    ```bash
    pip install -r requirements.txt
    ```
## 🎯 Future Goals

Our vision is to continue evolving AgriMonitor into a comprehensive farming assistant by:

- 🌾 Providing **crop recommendations** based on soil and vegetation data.
- 🤖 Integrating a **chatbot** to answer common agricultural queries and offer personalized suggestions.

