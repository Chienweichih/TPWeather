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
date = [2.0,2.0,
        2.0,1.0,1.0,1.0,1.0,2.0,2.0,
        2.0,1.0,1.0,1.0,1.0,2.0,
        2.0,1.0,1.0,1.0,1.0,2.0,2.0,
        2.0,1.0,1.0,1.0,1.0,2.0,2.0,
        2.0,1.0]

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
    
def printSummary(POIName,data,index):
    import statsmodels.formula.api as sm
    import numpy as np
    from numpy.linalg import inv
    import pandas as pd
    
    facebook_M = normalizedMatrix(data[0][index])
    rain_M = normalizedMatrix(data[1][index])
    heat_M = normalizedMatrix(data[2][index])
    date_M = normalizedMatrix(date)
    '''
    test = np.array([[1., 2.], [3., 4.]])
    test = np.arange(1,5).reshape((2, 2))
    invTest = inv(test)
    '''
    df = pd.DataFrame({'checkIn':facebook_M.tolist()[0],
                       'date':date_M.tolist()[0],
                       'rain':rain_M.tolist()[0],
                       'heat':heat_M.tolist()[0]})
    
    results = sm.ols(formula="checkIn ~ date + rain + heat", data=df).fit()

    print POIName.encode("utf8")
    print results.summary()
    coef = results.params
    with open("OLS_Regression.txt","a") as f:
        f.write("{}\nR-squared:{:f}\ncheckIn() = [{:f} {:f} {:f} {:f}] [1 date() rain() heat()]^T\n"
                .format(POIName.encode("utf8"),results.rsquared,coef[0],coef[1],coef[2],coef[3])) 

def main():
    fileNames = ["Facebook_0616.csv","Rain_0616.csv","Heat_0616.csv"]
    float_data = getSortedFloatList(fileNames)

    for POIIndex in range(len(POI)):
        printSummary(POI[POIIndex],float_data,POIIndex)

if __name__ == '__main__':
    main()
