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
### 3. install h5py
```bash
conda install h5py
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

* open `notebooks/example_load_visualize_dataset.ipynb` using Jupyter Notebook 