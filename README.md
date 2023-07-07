# HCM dataset

We here share the contact matrices measured by the [PHIRST](https://crdm.nicd.ac.za/projects/phirst-c/) project with the [SocioPatterns](http://www.sociopatterns.org/) collaboration in South-Africa. The contact matrices are aggregated by household and deployment.

If you make use of this dataset, please reference to the following article (https://doi.org/10.21203/rs.3.rs-2108731/v1).

> Dall’Amico et al: *Estimating household contact matrices structure from easily collectable metadata,* (2022)

## Content

* `Package`: this folder contains the file `contact_matrices.py` which is a source file to easily use the code.
* `CM.pkl`: pickle file containing the contact matrices.
* `PHIRST contact matrices.ipynb`: jupyter notebook containing the instructions to use and access the data. Note that `C_sec = S` and `C_counts = C` according to the current paper notation
* `csv`: in this folder there are 4 compressed *zip* files, named `C, S, P, T`, containing the respective HCM for all household-deployment pairs in *csv* format.

## Requirements

The codes run on `Python 3.9.7`. Provided that you installed [Anaconda](https://www.anaconda.com/products/distribution), you can obtain it creating an environment as follows

```
conda create -n environment_name python=3.9.7

conda activate environment_name
conda install jupyter
jupyter notebook
```

in between you will be required to install some packages and you should accept to go on. We used the following packages

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
