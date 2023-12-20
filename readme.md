# Estimating household contact matrices structure from easily collectable metadata



We here share the contact matrices measured by the [PHIRST](https://crdm.nicd.ac.za/projects/phirst-c/) project with the [SocioPatterns](http://www.sociopatterns.org/) collaboration in South-Africa. The contact matrices are aggregated by household and deployment.

If you make use of this dataset, please reference the following is referred to the following article which the data refer to.

> Dall’Amico et al: *Estimating household contact matrices structure from easily collectable metadata,* (2022)

## Content

* `src`: this folder contains the python scripts with the relevant codes to reproduce the result in our paper
* `csv`: in this folder we stored the household contact matrices aggregated per household and deployment. There are 4 folders: `C`, `S`, `T`, `P` in which we stored the matrices `C_counts`,`C_sec`, `T`, `P` respectively. Each household-deployment pair is saved in a separate `csv` file named `h_dep.csv`, where `h` is the household number (randomized for privacy reasons between 0 and 59) and `dep` is the deployment number between 0 and 2.
* `example.ipynb`: in this notebook we show how to load and use the contact matrices we shared
* `results.ipynb`: in this notebook we provide the code to reproduce the main results of our paper.

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