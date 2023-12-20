import pandas as pd
import numpy as np
from scipy.optimize import minimize
from scipy.optimize import LinearConstraint
import copy

from src.useful_functions import *

import warnings
warnings.filterwarnings("ignore")


class ReturnValueEstimateC:
    def __init__(self, C, C_proxy, u, dCanberra, dCos, dAbsolute):
        self.C = C
        self.C_proxy = C_proxy
        self.u = u
        self.dCanberra = dCanberra
        self.dCos = dCos
        self.dAbsolute = dAbsolute

def EstimateC(CM_all, selected_hd, dist = "Cos", name = "T"):
    '''Computes the approximation of the contact matrix given the population matrix and the activity profiles

    Use: EstC = EstimateC(CM_all, selected_hd)

    Inputs:
        * CM_all (list of classes): contains the contact matrices of all households-deployment pairs
        * selected_hd (list of lists): it is a list of (h,d) pairs

    Optional inputs:
        * dist (string): if "Cos" the algorithm optimizes the cosine similarity, otherwise, if "Canberra" it optimizes the Canberra similarity
        * name (string): declares the type of matrix (T or P) used for the optimization. Set by default to T

    Outputs:
        * EstC.C (array): input matrix to be estimated
        * EstC.C_proxy (array): estimated contact matrix
        * EstC.u (array): activity vector
        * EstC.dCanberra (float): Canberra similarity with the target matrix
        * EstC.Cos (float): Cosine similarity with the target matrix'''

    n_age_p, _ = CM_all[0,0].C_counts.shape
    all_H_both = np.unique([x[0] for x in CM_all.keys()])

    # Build C and T
    C = np.zeros((n_age_p, n_age_p))
    T = np.zeros((n_age_p, n_age_p))

    for i in range(len(selected_hd)):
        h_index = all_H_both[selected_hd[i][0]]
        wave = selected_hd[i][1]
        C += CM_all[h_index, wave].C_counts/len(selected_hd)
        if name == "T":
            T += CM_all[h_index, wave].T/len(selected_hd)
        if name == "P":
            T += CM_all[h_index, wave].P/len(selected_hd)


    u0 = np.ones(n_age_p)

    # Minimize the cost function
    cons = {'type':'eq', 'fun': _norm}
    res = minimize(_cost, np.abs(u0), args = (C,T, dist), constraints = cons, method = 'SLSQP')
    u = np.reshape(np.abs(res.x), (n_age_p,1))

    # Obtain the output results
    C_proxy = T*(u@u.T)
    dCos = CosineSimilarityMat(C.values, C_proxy.values)
    dCanberra = 1-CanberraDistance(C.values, C_proxy.values)
    dAbsolute = 1-AbsoluteDistance(C.values, C_proxy.values)

    return ReturnValueEstimateC(C, C_proxy, u, dCanberra, dCos, dAbsolute)

def _norm(x):
    return np.sum(np.abs(x))-len(x)

def _cost(u, C, T,  dist = "Cos"):

    u = np.reshape(np.abs(u), (len(u),1))
    M = T*(u@u.T)

    if dist == "CanberraDistance":
        return CanberraDistance(C.values, M.values)
    if dist == "Cos":
        return 1-CosineSimilarityMat(C.values, M.values)
    if dist == "Absolute":
        return AbsoluteDistance(C.values,M.values)

def formCompleteHousehold(CM, n_households, dep = None):
    '''This functions selects at random n_households pairs (h,d) under the constraint that there is at least one member in each age group

    Use: selected_hd = formCompleteHousehold(CM, n_households)

    Inputs:
        * CM (dictionary of classes): household-deployment contact matrices
        * n_household (integer): number of (h,d) pairs considered

    Optional inputs:
        * dep (list): if dep = None (default) then different deployments can be considered at once. On the opposite, if dep \in {0,1,2} the function will only select households from that deployment


    Use = selected_hd (list of tuples): list of (h,d) pairs'''

    # number of age bins
    n_age_p, _ = CM[0,0].C_counts.shape
    n_waves = len(np.unique([x[1] for x in CM.keys()]))

    # we create a dictionary for each household and deployment. The elements are vectors defined on the age bins with 0, 1 values 
    # indicating whether or not there is someone in that age bin
    Φ = dict(zip(list(CM.keys()), [np.sign(CM[idx].T@np.ones(n_age_p)) for idx in list(CM.keys())]))

    # (household-deployment) pairs
    selected_hd = []

    # we intialize an indicator function which is equal to 0 if that age group was taken and it equal 1 otherwise
    indicator = np.zeros(n_age_p)

    for i in range(n_households):

        # all households to sample from
        all_households = np.unique([x[0] for x in Φ.keys()])

        # select a deployment
        if dep == None:
            # select a random deployment
            d = np.random.choice(np.arange(n_waves))
        else:
            # select at random from the available deployments
            d = np.random.choice(dep)

        # if the household is not complete, we select among those that can make it complete
        if sum(indicator) < n_age_p:

            # select at random one of the missing age groups
            r = np.random.choice(np.arange(n_age_p)[indicator == 0])

            # select a random household that in deployment t can contribute to class r
            eligible_households = [x for x in all_households if Φ[x, d][r] > 0]
            h = np.random.choice(eligible_households)

            # update the indicator vector and drop the pair (h,d)
            indicator = np.sign(indicator + Φ[h, d])

            if (i == n_households - 1) and (np.sum(indicator) != n_age_p):
                print("WARNING: the household is not complete! Increase the value of n_households" )

        # otherwise we choose a random (h,d) pair
        else:
            h = np.random.choice(all_households)
            indicator = np.sign(indicator + Φ[h, d])

        # remove household from all deployments
        del Φ[h, 0]
        del Φ[h, 1]
        del Φ[h, 2]
        selected_hd.append(tuple([h,d]))

    return selected_hd

