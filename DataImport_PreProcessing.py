# -*- coding: utf-8 -*-
"""
Created for Data Import and Preprocessing model for Data Anlytics

@authors: Bhupal,Manjunath,Moumita and Ayushi
"""

#############   External Library Import Section  Starts   ##########


import xlrd


#############   External Library Import Section  Ends   ##########


#############   Class holder for results   ##########
class holder:
    1

#############   Data Import Function Starts   ##########
def readXlfile(filePath,sheetName):
    
    result = holder()
    book = xlrd.open_workbook(filePath)
    sheet = book.sheet_by_name(sheetName)
    result.varNames = sheet.row(0)
    result.ipDataType = sheet.row(1)
    data = [] #make a data store
    for i in range(2,sheet.nrows):
        data.append(sheet.row_values(i)) #drop all the values in the rows into data
    print('Loaded data file {0} with {1} rows and {2} columns').format(filePath, len(dataset), len(dataset[0]))
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
    indices = [i for i,x in enumerate(column) if x == '']
    if indices:
        #print(indices)
        print('Column', rs.varNames[i], 'contains missing values with indices',indices)
    else:
        print('Column', i, 'does not contain missing values')
#
        
def checkOutliers(i,rs):
    
    column = getColumn(i)
    datamean = mean(rs.data)
    datastd = stdev(rs.data)
        
    indices = [i for i,x in enumerate(column) if ~ ((datamean - 3*datastd )<= x<= datamean + 3 * datastd)]
    if indices:
        #print(indices)
        print('Column', rs.varNames[i], 'contains outliers with indices',indices)
    else:
        print('Column', i, 'does not contain outliers')

            
            
            
   
    
    
#def checkDataType(i, rs):
#    for 
    
if __name__ == "__main__":
    filename = r"TestData_Module3.xlsx"
    rs = readXlfile(filename,'Sheet1')
    #getColumn(0)
    for i in range(len(rs.varNames)):
        checkNull(i,rs)    
