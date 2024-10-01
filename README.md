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

*  For Windows
    
    download `WSL` and follow instruction or get creative and follow steps [here](https://hdfeos.org/software/pyhdf.php) 
*  For Linux
    1. Install Requirments
        * JPEG distribution release 6b or later.
        ```bash
        sudo apt-get install libjpeg-dev
        ```
        * ZLIB 1.1.4(libz.a) or later.  
        ```bash
        sudo apt-get install zlib1g-dev
        ```
        * numpy
        ```bash
        conda install numpy
        ```
        * setuptools
        ```bash
        conda install setuptools
        ```
    2. download hdf4
        ```bash
        cd vendor
        ```
        ```bash
        curl -L  https://github.com/HDFGroup/hdf4/archive/refs/tags/hdf4.3.0.tar.gz -o hdf4.3.0.tar.gz
        ```
        ```bash
        tar -xvf hdf4.3.0.tar.gz
        ```
    3. Install hdf4
        ```bash
        cd vendor/hdf4-hdf4.3.0/
        ```
        ```bash
        ./configure
        ```
        ```bash
        sudo make install
        ```
### Install Jupyter Notebook
to see examples 

## Installation
* Install the required packages
    ```bash
    pip install -r requirements.txt
    ```
## Example
* download example dataset
    ```bash
    cd datasets && curl -L https://gamma.hdfgroup.org/ftp/pub/outgoing/NASAHDF/AIRS.2002.08.01.L3.RetStd_H031.v4.0.21.0.G06104133732.hdf -o AIRS.2002.08.01.L3.RetStd_H031.v4.0.21.0.G06104133732.hdf
    ```