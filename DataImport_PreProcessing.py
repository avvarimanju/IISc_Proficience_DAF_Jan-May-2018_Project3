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
    
    result.data = data
    return result

def preprocessXlData():
    
    result = holder()

    return result


def getColumn(i):
    print([row[i] for row in rs.data])
#############   Data Import Function  Ends   ##########

def checkNull(i):
    column = getColumn(i)
    indices = [i for i,x in enumerate(column) if x == '']
    if indices:
        print(indices)
    else:
        print('Column', i, 'does not contain missing values')
    
if __name__ == "__main__":
    path = r"TestData_Module3.xlsx"
    rs = readXlfile(path,'Sheet1')
    #getColumn(0)
    for i in range(4):
        checkNull(i)    
