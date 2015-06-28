# -*- coding: utf-8 -*-

POI = (u'順益台灣原住民博物館',u'National Palace Museum',u'Chunghwa Postal Museum',
       u'National Museum of History',u'Shilin Night Market',u'國立國父紀念館National Dr.Sun Yat-sen Memorial Hall',
       u'Taipei Fine Arts Museum',u'Hsing Tian Kong',u'象山',
       u'中正紀念堂 Chiang Kai-shek Memorial Hall',u'National Taiwan Museum',u'國軍歷史文物館',
       u'Taipei 101 Observatory',u'Mengjia Longshan Temple',u'台北木柵動物園',
       u'貓空邀月',u'北投溫泉博物館 Beitou Hot Spring Museum',u'Tianmu Baseball Stadium',
       u'陽明山竹子湖海芋田',u'袖珍博物館',u'Museum of Drinking Water')

######  S  M  T  W  T  F  S
######                15 16
###### 17 18 19 20 21 22 23
###### 24 25 26 27 28  X 30
###### 31  1  2  3  4  5  6
######  7  8  9 10 11 12 13
###### 14 15
date = [# all same
        [1.0,1.0,
        1.0,1.0,1.0,1.0,1.0,1.0,1.0,
        1.0,1.0,1.0,1.0,1.0,1.0,
        1.0,1.0,1.0,1.0,1.0,1.0,1.0,
        1.0,1.0,1.0,1.0,1.0,1.0,1.0,
        1.0,1.0],
        # weekday,weekend
        [1.0,2.0,
        2.0,1.0,1.0,1.0,1.0,1.0,2.0,
        2.0,1.0,1.0,1.0,1.0,2.0,
        2.0,1.0,1.0,1.0,1.0,1.0,2.0,
        2.0,1.0,1.0,1.0,1.0,1.0,2.0,
        2.0,1.0],
        # monday
        [1.0,1.0,
        1.0,2.0,1.0,1.0,1.0,1.0,1.0,
        1.0,2.0,1.0,1.0,1.0,1.0,
        1.0,2.0,1.0,1.0,1.0,1.0,1.0,
        1.0,2.0,1.0,1.0,1.0,1.0,1.0,
        1.0,2.0],
        # tuesday
        [1.0,1.0,
        1.0,1.0,2.0,1.0,1.0,1.0,1.0,
        1.0,1.0,2.0,1.0,1.0,1.0,
        1.0,1.0,2.0,1.0,1.0,1.0,1.0,
        1.0,1.0,2.0,1.0,1.0,1.0,1.0,
        1.0,1.0],
        # wednesday
        [1.0,1.0,
        1.0,1.0,1.0,2.0,1.0,1.0,1.0,
        1.0,1.0,1.0,2.0,1.0,1.0,
        1.0,1.0,1.0,2.0,1.0,1.0,1.0,
        1.0,1.0,1.0,2.0,1.0,1.0,1.0,
        1.0,1.0],
        # thursday
        [1.0,1.0,
        1.0,1.0,1.0,1.0,2.0,1.0,1.0,
        1.0,1.0,1.0,1.0,2.0,1.0,
        1.0,1.0,1.0,1.0,2.0,1.0,1.0,
        1.0,1.0,1.0,1.0,2.0,1.0,1.0,
        1.0,1.0],
        # friday
        [2.0,1.0,
        1.0,1.0,1.0,1.0,1.0,2.0,1.0,
        1.0,1.0,1.0,1.0,1.0,1.0,
        1.0,1.0,1.0,1.0,1.0,2.0,1.0,
        1.0,1.0,1.0,1.0,1.0,2.0,1.0,
        1.0,1.0],
        # saturday
        [1.0,2.0,
        1.0,1.0,1.0,1.0,1.0,1.0,2.0,
        1.0,1.0,1.0,1.0,1.0,2.0,
        1.0,1.0,1.0,1.0,1.0,1.0,2.0,
        1.0,1.0,1.0,1.0,1.0,1.0,2.0,
        1.0,1.0],
        # sunday
        [1.0,1.0,
        2.0,1.0,1.0,1.0,1.0,1.0,1.0,
        2.0,1.0,1.0,1.0,1.0,1.0,
        2.0,1.0,1.0,1.0,1.0,1.0,1.0,
        2.0,1.0,1.0,1.0,1.0,1.0,1.0,
        2.0,1.0]]
date_name = ['all_same','weekday_weekend',
             'monday','tuesday','wednesday','thursday','friday','saturday','sunday']

def main():
    fileNames = ["Facebook_0616.csv","Rain_0616.csv","Heat_0616.csv"]
    float_data = getSortedFloatList(fileNames)
    
    ADDMUL = ["ADD","MUL"]
    for formulaIndex in range(2):
        for i,date_date in enumerate(date):
            results = []
            for POIIndex in range(len(POI)):
                results.append(OLSResults(float_data,POIIndex,date_date,formulaIndex))
            printResults(results,"OLS/" + ADDMUL[formulaIndex] + "/OLS_Regression_" + date_name[i] + ".txt")

def getSortedFloatList(fileNames):
    import csv
        
    noneValue = [0,0,30]

    raw_data = []
    for file_name in fileNames:
        reader = csv.reader(open(file_name,"rb"),delimiter=',')
        raw_data.append([[x.decode('big5') for x in line] for line in reader])
    
    sorted_data = []
    for data in raw_data:
        sorted_data.append(sorted(data[1:], key=lambda x:POI.index(x[0])))
    
    float_data = []
    for data in sorted_data:
        float_data.append([[float(x) if x != u'None' else noneValue[sorted_data.index(data)] 
                            for x in line[2:]] for line in data])
    
    return float_data

def normalizedMatrix(matrix):
    from sklearn.preprocessing import normalize
    normed_matrix = normalize(matrix, axis=1, norm='l1')
    return normed_matrix
    
def OLSResults(data,index,date_data,formulaIndex):
    import statsmodels.formula.api as sm
    from numpy.linalg import inv
    import pandas as pd
    import numpy as np
    
    myFormula = ["checkIn ~ rain + heat + date","CdD ~ rain + heat"]
    
    facebook_M = normalizedMatrix(data[0][index])
    rain_M = normalizedMatrix(data[1][index])
    heat_M = normalizedMatrix(data[2][index])
    date_M = normalizedMatrix(date_data)
    cdd_M = np.dot(facebook_M,inv(np.diag(date_M[0])))
    
    print cdd_M
    
    '''
    test = np.array([[1., 2.], [3., 4.]])
    test = np.arange(1,5).reshape((2, 2))
    invDate = inv(date_M)
    '''
    if formulaIndex == 0:
        df = pd.DataFrame({'checkIn':facebook_M.tolist()[0],
                           'rain':rain_M.tolist()[0],
                           'heat':heat_M.tolist()[0],
                           'date':date_M.tolist()[0]})
    else:
        df = pd.DataFrame({'CdD':cdd_M.tolist()[0],
                           'rain':rain_M.tolist()[0],
                           'heat':heat_M.tolist()[0]})
    results = sm.ols(formula=myFormula[formulaIndex], data=df).fit()
    return results 

def printResults(OLSResults,fileName):
    with open(fileName,"w") as f:
        for index,results in enumerate(OLSResults):
            print POI[index].encode("utf8")
            print results.summary()
            coef = results.params
            if fileName[4] == 'A':
                f.write("{}\nR-squared:{:f}\ncheckIn() = [{:f} {:f} {:f} {:f}] [1 rain() heat() date()]^T\n"
                        .format(POI[index].encode("utf8"),results.rsquared,coef[0],coef[1],coef[2],coef[3]))
            else:
                f.write("{}\nR-squared:{:f}\ncheckIn() = [{:f} {:f} {:f}] [1 rain() heat()]^T\n"
                        .format(POI[index].encode("utf8"),results.rsquared,coef[0],coef[1],coef[2]))

if __name__ == '__main__':
    main()
