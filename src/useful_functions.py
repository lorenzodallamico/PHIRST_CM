import pandas as pd
import numpy as np


def linear_fit(x,y):
    '''Performs a linear fit between a set of points x and y

    Use: ω, b = linear_fit(x,y)

    Inputs:
        * x (array): x coordinates
        * y (array): y coordinates

    Outputs:
        * ω (float): slope
        * b (float): constraint

    '''

    y_b = np.mean(y)
    x_b = np.mean(x)
    n = len(x)

    ω = (y@x/n-y_b*x_b)/(x@x/n - x_b**2)
    b = y_b - ω*x_b

    return ω, b


def CosineSimilarityMat(A,B):
    ''' Returns the cosine similarity between two matrices

    Usage: d = CosineSimilarityMat(A, B)

    Inputs:
        * A, B (array): two square matrices of the same size

    Outputs:
        * d (float): the cosine similarity

    '''
    n = np.shape(A)[0]
    idx_l = np.tril_indices(n)

    x = A[idx_l]
    y = B[idx_l]

    return x@y/np.sqrt(x@x*y@y)


def CanberraDistance(A,B):
    ''' Returns the Canberra distance  between two matrices

    Usage: d = CanberraDistance(A, B)

    Inputs:
        * A, B (array): two square matrices of the same size

    Outputs:
        * d (float): the Canberra distance

    '''

    n = np.shape(A)[0]
    idx_l = np.tril_indices(n)

    x = A[idx_l]
    y = B[idx_l]
    x /= np.mean(x)
    y /= np.mean(y)

    return np.sum(np.abs(x-y)/(np.abs(x) + np.abs(y) + 10**(-9)))/len(x)


def AbsoluteDistance(A,B):

    n = np.shape(A)[0]
    idx_l = np.tril_indices(n)

    x = A[idx_l]
    y = B[idx_l]
    x /= np.mean(x)
    y /= np.mean(y)

    return np.sum(np.abs(x-y)/(np.max(np.abs(x) + np.abs(y))))/len(x)

def DayActivity(data, ID, wave):
    """Computes the day activity profile of a members a household in a particular wave

    Use: time_v_h = DayActivityAge(data, ID, wave)

    Inputs:
        * data (class): the input data class
        * ID (string): study id of the person considered
        * wave (int): the number of the deployment

    Outputs:
        * day_activity (array): vector in R^24 containg the cumulative daily activity profile of id
    """

    h = ID.split("-")[0]
    site = data.site_names_short.index(h.split("2")[0])
    df = data.df_collection[site][wave]

    # Select only the interactions involving id
    idx = (df.stid1 == ID) | (df.stid2 == ID)
    df = df[idx]

    # vector spanning all day with the resolution of one second
    time_range = list(pd.date_range("00:00:00", "23:59:59", freq = "S").time)

    # beginning of the interactions
    t0 = pd.to_datetime(df["t"])

    # end of the interactions
    tf = (t0 + pd.to_timedelta(df["duration_sec"], unit = "sec")).dt.time
    t0 = t0.dt.time

    # we convert everything into seconds
    tinit = [time_range.index(t0.values[i]) for i in range(len(t0))]
    tend = [time_range.index(tf.values[i]) for i in range(len(t0))]

    # now we store this into a single vector
    time_v = np.zeros(len(time_range))
    for a in range(len(tinit)):
        time_v[tinit[a]:tend[a]] += 1 # indicator function of a single interaction

    # we group the activity by hours
    time_v_h = np.zeros(24)
    for j in range(24):
        time_v_h[j] = np.sum(time_v[j*3600:(j+1)*3600])

    return time_v_h
