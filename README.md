# HCM dataset

We here share the contact matrices measured by the [PHIRST](https://crdm.nicd.ac.za/projects/phirst-c/) project with the [SocioPatterns](http://www.sociopatterns.org/) collaboration in South-Africa. The contact matrices are aggregated by household and deployment.

If you make use of this dataset, please reference the following is referred to the following article which the data refer to.

> Dall’Amico et al: *Estimating household contact matrices structure from easily collectable metadata,* (2022)

## Content

* `Package`: this folder contains the file `contact_matrices.py` which is a source file to easily and use the code.
* `CM.pkl`: pickle file containing the contact matrices.
* `PHIRST contact matrices.ipynb`: jupyter notebook containing the instructions to use and access the data.

## Requirements

The codes run on `Python 3.9.7`. Provided that you installed [Anaconda](), you can obtain it creating an environment as follows

```
conda create -n environment_name python=3.9.7

conda activate environment_name
conda install jupyter
jupyter notebook
```

in between you will be required to install some packages and you should accept to go one. We used the following packages

> - pickle==4.0
> - numpy==1.20.3
> - matplotlib==3.4.3
> - pandas==1.3.4

if any of this packages is missing, you can installing typing

```
pip install packagename==version
```

## Contact

lorenzo.dallamico@isi.it
