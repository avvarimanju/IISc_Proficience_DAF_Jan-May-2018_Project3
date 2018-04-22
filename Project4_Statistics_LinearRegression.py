# -*- coding: utf-8 -*-
"""
Basic Statistic Functions and Simple Linear Regression with Bivariant Data

Function included
    Mean
    Variance
    CoVariance
    Standard Deviation
    Correlation Coefficient
    Threshold
    Calculate M & C to fit straight line
"""

import numpy as np
import matplotlib.pyplot as plot

# Calculate Mean
def get_mean(ds):
    #Sum of dataset
    ds_tot = sum(ds)
    #Count of Dataset
    cnt_of_ds = len(ds)
    #Mean of Dataset
    mean = ds_tot / float(cnt_of_ds)
    return mean    

# Calculate Variance
def get_variance(ds):
    #Calculate Mean
    row_mean = get_mean(ds)
    # pow((row - row_mean), 2) ==> (X - X Mean)^2
    mean_difference_squared_ds = [pow((row - row_mean), 2) for row in ds]
    # Sum of (X - X Mean)^2
    tot_diff_sqrd_values = sum(mean_difference_squared_ds)
    # variance (X - X Mean)^2 / N -1
    variance = tot_diff_sqrd_values / float(len(ds) - 1)    
    return variance

# Calculate Covariance
def get_covariance(ds_x, ds_y):    
    # Calculate mean for X
    ds_x_mean = get_mean(ds_x)
    # Calculate mean for Y
    ds_y_mean = get_mean(ds_y)
    #Count of Dataset
    ds_size = len(ds_x)    
    # tot_difference_values ==> sum of (X - X Mean) * (Y - Y Mean)
    tot_difference_values = 0.0
    for i in range(0, ds_size):
        tot_difference_values += (ds_x[i] - ds_x_mean) * (ds_y[i] - ds_y_mean)
    # covariance ==> sum of (X - X Mean) * (Y - Y Mean) / N-1
    covariance = tot_difference_values / float(ds_size - 1)    
    return covariance

# Calculate Standard Deviation
def get_StandardDeviation(ds):
    #Calculate Variance
    variance = get_variance(ds)
    # Calculate Standard Deviation ==> Squareroot of Variance
    StandardDeviation = np.sqrt(variance)
    return StandardDeviation

# Calculate Correlation Coefficient
def get_CorrelationCoefficient(ds_x, ds_y):
    # Calculate Covariance
    cov_xy = get_covariance(ds_x, ds_y)
    # Calculate Standard Deviation of X
    StdDev_x = get_StandardDeviation(ds_x)
    # Calculate Standard Deviation of Y
    StdDev_y = get_StandardDeviation(ds_y)
    # Calculate Correlation Coefficient
    CorCof = cov_xy / (StdDev_x * StdDev_y)
    return CorCof
    
# Calculate Threshold
def get_threshold(ds):
    #Count of Dataset
    ds_size = len(ds)
    # Calculate Threshold
    threshold = 1.96 / np.sqrt(ds_size)
    return threshold


# calculate M & C using Least Squares Method
def get_mc(ds_x, ds_y):
    # Calculate Sum of X
    tot_ds_x = sum(ds_x)
    # Calculate Sum of Y
    tot_ds_y = sum(ds_y)
    # Calculate X square ==> (X * X)
    tot_ds_x_sqr = ds_x.dot(ds_x)
    # Calculate X * Y
    tot_ds_xy = ds_x.dot(ds_y)
    #Count of Dataset
    n = len(ds_x)
    # Calculate M
    # M = N * Sum of XY - Sum of X * Sum of Y / n*Sum of X square - Sum of X^2
    m = ((n * tot_ds_xy) - (tot_ds_x  * tot_ds_y)) / ((n * tot_ds_x_sqr) - (pow((tot_ds_x), 2)))
    # Calculate C
    # C = Sum of Y - m * Sum of X / n
    c = (tot_ds_y - (m * tot_ds_x)) / n
    return m, c
 
##import data from csv
#X = []
#Y = []
#for line in open('sample.csv'):
#    x, y = line.split(',')
#    X.append(float(x))
#    Y.append(float(y))
#    
##make the imported data into arrays
#X = np.array(X)
#Y = np.array(Y)
#
## Calculate M and C
#m, c =get_mc(X,Y)
#
##Fitting Straigt Line
## Calculate the predicted Y values
#Yp = m*X + c
#
#print ('X Mean: ', get_mean(X))
#print ('Y Mean: ', get_mean(Y))
#print ('X Variance: ', get_variance(X))
#print ('Y Variance: ', get_variance(Y))
#print ('CoVariance: ', get_covariance(X,Y))
#print ('X StandardDeviation: ', get_StandardDeviation(X))
#print ('Y StandardDeviation: ', get_StandardDeviation(Y))    
#print ('CorrelationCoefficient: ', get_CorrelationCoefficient(X,Y))    
#print ('Threshold: ', get_threshold(X))
#print ('M: ', m)
#print ('C: ', c)
#    
## Plot the data in scatter chart
#plot.scatter(X, Y)
#plot.show()
#
## Plot the data in scatter chart with predicted Y values
#plot.scatter(X, Y)
#plot.plot(X, Yp)
#plot.show()