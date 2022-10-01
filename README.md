# Hotspotter



## Setting Up the Computing Environment



1. Download and install the conda package manager from https://docs.conda.io/en/latest/miniconda.html



2. Create a new virtual environment


```
conda create -n hotspot python=3.9
conda activate hotspot
conda config --add channels conda-forge
```



## Use the Hotspotter Script


Install additional Python libraries via

```
conda install scikit-learn==1.1.2 numpy==1.23.3 pandas==1.4.4 --yes
```

Then navigate into the `hotspotter` subfolder:

```
cd hotspotter
```

and use the `hotspotter.py` script.

Get usage information by running `python hotspotter.py --help`:

```
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

<br>
<br>
<br>


You can run the hotspotter with 4 different classification models


1. `mlp-allfeatures.joblib`: the multilayer perceptron trained with the best hyperparameter settings on the training set and as evaluated in the research paper. This Model requires the feature columns  "avg bond number", "Hbond", "residue", "Hphob", "consurf", "B' side chain", "secondary structure",  "asa". See the   [[hotspotter/TestDataset.csv](hotspotter/TestDataset.csv)] file for details.

Run as

    python hotspotter.py \
    --csv_path TestDataset.csv \
    --trained_model mlp-allfeatures.joblib

---

2. `mlp-allfeatures-alldata.joblib`: Similar to above but trained on the combined training + test dataset.

Run as

    python hotspotter.py \
    --csv_path TestDataset.csv \
    --trained_model mlp-allfeatures-alldata.joblib

---

3. `mlp-seqfeatures.joblib`: Similar to `mlp-allfeatures.joblib`, but only requires sequence features: "residue", "consurf", "secondary structure".

Run as

    python hotspotter.py \
    --csv_path TestDataset.csv \
    --trained_model mlp-seqfeatures.joblib \
    --sequence_only true

---

4. `mlp-seqfeatures-alldata.joblib`: Similar to above but trained on the combined training + test dataset.

Run as

    python hotspotter.py \
    --csv_path TestDataset.csv \
    --trained_model mlp-seqfeatures-alldata.joblib \
    --sequence_only true

---

(Note that `TestDataset.csv` is an example dataset we provide.)



The results will be formatted as follows:

```
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

In order to run the code in the experiment notebooks, install the following additional Python libraries:

```
conda install \
scikit-learn==1.1.2 \
jupyterlab \
watermark==2.3.1 \
matplotlib==3.5.3 \
numpy==1.23.3 \
pandas==1.4.4 \
mlxtend==0.21.0 \
--yes
```


Next, start JupyterLab and use notebooks via the command


```
jupyter lab
```


## Developers and Contributors



Please install the pre-commits before making commits and submitting Pull Requests


```
conda install pre-commit --yes
pre-commit install
```

