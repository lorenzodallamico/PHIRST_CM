# Estimating household contact matrices structure from easily collectable metadata



We here share the contact matrices measured by the [PHIRST](https://crdm.nicd.ac.za/projects/phirst-c/) project with the [SocioPatterns](http://www.sociopatterns.org/) collaboration in South-Africa. The contact matrices are aggregated by household and deployment.

If you make use of this dataset, please reference the following is referred to the following article which the data refer to.

```
@article{DallAmico2024Estimating,
    doi = {10.1371/journal.pone.0296810},
    author = {Dall’Amico, Lorenzo AND Kleynhans, Jackie AND Gauvin, Laetitia AND Tizzoni, Michele AND Ozella, Laura AND Makhasi, Mvuyo AND Wolter, Nicole AND Language, Brigitte AND Wagner, Ryan G. AND Cohen, Cheryl AND Tempia, Stefano AND Cattuto, Ciro},
    journal = {PLOS ONE},
    publisher = {Public Library of Science},
    title = {Estimating household contact matrices structure from easily collectable metadata},
    year = {2024},
    month = {03},
    volume = {19},
    url = {https://doi.org/10.1371/journal.pone.0296810},
    pages = {1-13},
    abstract = {Contact matrices are a commonly adopted data representation, used to develop compartmental models for epidemic spreading, accounting for the contact heterogeneities across age groups. Their estimation, however, is generally time and effort consuming and model-driven strategies to quantify the contacts are often needed. In this article we focus on household contact matrices, describing the contacts among the members of a family and develop a parametric model to describe them. This model combines demographic and easily quantifiable survey-based data and is tested on high resolution proximity data collected in two sites in South Africa. Given its simplicity and interpretability, we expect our method to be easily applied to other contexts as well and we identify relevant questions that need to be addressed during the data collection procedure.},
    number = {3},

}
```
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
