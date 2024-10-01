# Nasa Space Apps Green Wave
Leveraging Earth Observation data for informed Agriculture Decision-Making

## Requirements
* python 3.10 or later
* Jupyter Notbook
* PyHDF
* gcc
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

#### 2. Install & Download `Hdf4`
you can download latest `hdf4` from [here](https://support.hdfgroup.org/downloads/hdf4/hdf4_3_0.html) 

*  For Linux
    ```bash
    cd vendor
    ```
    ```bash
    curl -L  https://github.com/HDFGroup/hdf4/archive/refs/tags/hdf4.3.0.tar.gz -o hdf4.3.0.tar.gz
    ```
    ```bash
    tar -xvf hdf4.3.0.tar.gz
    ```
    ```bash
    tar -xvf ./hdf4/HDF-4.3.0-Linux.tar.gz
    ```

### Install Jupyter Notebook
## Installation
1. Install the required packages
    ```bash
    pip install -r requirements.txt
    ```
2. Setup the environment variables
    ```bash
    cp .env.example .env
    ```
    and set your environment variable in the `.env` file.