## Setting Up the Computing Environment



1. Download and install the conda package manager

https://docs.conda.io/en/latest/miniconda.html



2. Create a new virtual environment



conda create -n hotspot python=3.9

conda activate hotspot

```
conda config --add channels conda-forge
```



## Use the Hotspotter Script





Get usage information by running `python hotspotter.py --help`:



```
$ cd hotspotter
$ python hotspotter.py --help
[OK] Your Python version is 3.9.13 | packaged by conda-forge | (main, May 27 2022, 17:01:00) 
[Clang 13.0.1 ]
[OK] sklearn 1.1.2
[OK] numpy 1.23.3
[OK] joblib 1.1.0
[OK] pandas 1.4.4
usage: hotspotter.py [-h] --csv_path CSV_PATH [--trained_model TRAINED_MODEL]
                     [--trained_model_sequence_only TRAINED_MODEL_SEQUENCE_ONLY] [--sequence-only {true,false}]

optional arguments:
  -h, --help            show this help message and exit
  --csv_path CSV_PATH   Path to the CSV file
  --trained_model TRAINED_MODEL
                        Path to the trained model
  --trained_model_sequence_only TRAINED_MODEL_SEQUENCE_ONLY
                        Path to the trained model for --sequence_only prediction.
  --sequence_only {true,false}
  --print_row_numbers {true,false}
```



You CSV file should contain the same columns as the [[hotspotter/TestDataset.csv](hotspotter/TestDataset.csv)] file. If you are running the hotspotter in `--sequence-only true` mode, your CSV file does not have to contain the `secondary structure` column.

If your CSV file contains additional columns, it doesn't matter. Also, the column order does not matter.

If the conditions above are met, you can run the hotspotter as follows

```
python hotspotter.py --csv_path TestDataset.csv
```

(Note that `TestDataset.csv` is an example dataset we provide.)



The results will be formatted as follows:

```python hotspotter.py --csv_path TestDataset.csv 
==========
RESULTS
==========
1
1
1
0
0
...
1

```

Where each line corresponds to one row in the CSV file (1=hotspot, 0=not hotspot).



## Use the Experiments Notebooks



3. Install Python libraries



conda install scikit-learn==1.1.2 jupyterlab watermark==2.3.1 matplotlib==3.5.3 numpy==1.23.3 pandas==1.4.4 mlxtend==0.21.0 --yes



4. Start JupyterLab and use notebooks



jupyterlab



## Developers and Contributors



Please install the pre-commits before making commits and submitting Pull Requests



conda install pre-commit

pre-commit install



