## Setting Up the Computing Environment



1. Download and install the conda package manager

https://docs.conda.io/en/latest/miniconda.html



2. Create a new virtual environment



conda create -n hotspot python=3.9

conda activate hotspot

```
conda config --add channels conda-forge
```



3. Install Python libraries



conda install scikit-learn==1.1.2 jupyterlab watermark==2.3.1 matplotlib==3.5.3 pandas==1.4.4 --yes



4. Start JupyterLab and use notebooks



jupyterlab