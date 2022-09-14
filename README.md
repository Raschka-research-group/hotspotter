## Setting Up the Computing Environment



1. Download and install the conda package manager

https://docs.conda.io/en/latest/miniconda.html



2. Create a new virtual environment



conda create -n hotspot python=3.9

conda activate hotspot

```
conda config --add channels conda-forge
```



## Hotspotter script





## Experiments



3. Install Python libraries



conda install scikit-learn==1.1.2 jupyterlab watermark==2.3.1 matplotlib==3.5.3 pandas==1.4.4 mlxtend==0.21.0 --yes



4. Start JupyterLab and use notebooks



jupyterlab



## Developers and Contributors



Please install the pre-commits before making commits and submitting Pull Requests



conda install pre-commit

pre-commit install



