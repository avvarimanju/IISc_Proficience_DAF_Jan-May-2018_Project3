# -*- coding: utf-8 -*-
"""
Created for Data Import and Preprocessing model for Data Anlytics

@authors: Bhupal,Manjunath,Moumita and Ayushi
"""

#############   External Library Import Section  Starts   ##########
import numpy as np
import xlrd
from Project4_Statistics_LinearRegression import *

#############   External Library Import Section  Ends   ##########


#############   Class holder for results   ##########
class holder:
    1

#############   Data Import Function Starts   ##########
def readXlfile(filePath,sheetName):
    
    result = holder()
    book = xlrd.open_workbook(filePath)
    sheet = book.sheet_by_name(sheetName)
    result.varNames = sheet.row_values(0)
    result.ipDataType = sheet.row_values(1)
    data = [] #make a data store
    for i in range(2,sheet.nrows):
        data.append(sheet.row_values(i)) #drop all the values in the rows into data
#    print('Loaded data file {0} with {1} rows and {2} columns').format(filePath, len(data), len(data[0]))
    result.data = data
    return result

def preprocessXlData():
    
    result = holder()

    return result


def getColumn(i):
    return([row[i] for row in rs.data])
    
#############   Data Import Function  Ends   ##########

def checkNull(i,rs):
    
    column = getColumn(i)
    indices = [j for j,x in enumerate(column) if x == '']
    if indices:
        #print(indices)
        print('Column', rs.varNames[i],'contains',round(len(indices)*100/len(column),4), '% of missing values with indices',indices)
    else:
        print('Column', i, 'does not contain missing values')
#
        
def checkOutliers(i,rs):
    
    column = getColumn(i)
    datamean = get_mean(column)
    datastd = get_StandardDeviation(column)
        
    indices = [j for j,x in enumerate(column) if ((datamean + 3*datastd )<= x<= (datamean - 3 * datastd))]
    if indices:
        #print(indices)
        print('Column', rs.varNames[i],'contains',round(len(indices)*100/len(column),4), '% of outliers with indices',indices)
    else:
        print('Column', i, 'does not contain outliers')
        
def checkInputDatatypes(i,rs):
    
    column = np.asarray(getColumn(i))
    dataType = rs.ipDataType[i]
    
    if dataType == 'int':
        if column.dtype == 'float64':
            indices =[]
#            print('column',i,'is float64')
            for x in column:
                if int(float(x)*10) != int(float(x))*10:
                    indices.append(list(column).index(x))
        else:
            indices =[]
#            print('column',i,'is not float64')
            for x in column:
                if x.isalpha():
                    indices.append(list(column).index(x))
                elif int(float(x)*10) != int(float(x))*10:
                    indices.append(list(column).index(x))
                
        if indices:
            #print(indices)
            print('Column', rs.varNames[i],'contains',round(len(indices)*100/len(column),4), '% of non integers with indices',indices)
        else:
            print('Column', i, 'does not contain non integers')
    elif dataType == 'float':
        if column.dtype != 'float64':          
            indices =[]
            for x in column:
                if x.isalpha():
                    indices.append(list(column).index(x))
            if indices:
                #print(indices)
                print('Column', rs.varNames[i],'contains',round(len(indices)*100/len(column),4), '% of non floats with indices',indices)
            else:
                print('Column', i, 'does not contain non floats')
    elif dataType == 'str':           
        indices = [j for j,x in enumerate(column) if x.replace('.','',1).isdigit()]
        if indices:
            #print(indices)
            print('Column', rs.varNames[i], 'contains',round(len(indices)*100/len(column),4), '% of non strings with indices',indices)
        else:
            print('Column', i, 'does not contain non strings')

            
def zscoreNormalize(i,rs):
    
    result = holder()
    column = np.asarray(getColumn(i))
    datamean = get_mean(column)
    datastd = get_StandardDeviation(column)
    result = (column - datamean)/datastd
    return result

def minmaxNormalize(i,rs):
    
    result = holder()
    column = np.asarray(getColumn(i))
    datamax = max(column)
    datamin = min(column)
    result = (column - datamin)/(datamax-datamin)
    return result
        
           
            
   
    
    
#def checkDataType(i, rs):
#    for 
    
if __name__ == "__main__":
    filename = "TestData_Module3_test.xlsx"
    rs = readXlfile(filename,'Sheet1')
#    rsN = minmaxNormalize(3,rs)
    #getColumn(0)
    for i in range(len(rs.varNames)):
        checkInputDatatypes(i,rs)    
