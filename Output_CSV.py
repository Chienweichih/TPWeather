# -*- coding: utf-8 -*-
import csv

SchoolToSpot = {u'至善國中':[u'順益台灣原住民博物館',u'National Palace Museum'],
                u'國語實小':[u'Chunghwa Postal Museum',u'National Museum of History'],
                u'福林國小':[u'Shilin Night Market'],
                u'光復國小':[u'國立國父紀念館National Dr.Sun Yat-sen Memorial Hall'],
                u'大龍國小':[u'Taipei Fine Arts Museum'],
                u'五常國小':[u'Hsing Tian Kong'],
                u'吳興國小':[u'象山'],
                u'市大附小':[u'中正紀念堂 Chiang Kai-shek Memorial Hall',u'National Taiwan Museum',u'國軍歷史文物館'],
                u'博愛國小':[u'Taipei 101 Observatory'],
                u'老松國小':[u'Mengjia Longshan Temple'],
                u'指南國小':[u'台北木柵動物園',u'貓空邀月'],
                u'逸仙國小':[u'北投溫泉博物館 Beitou Hot Spring Museum'],
                u'三玉國小':[u'Tianmu Baseball Stadium'],
                u'湖田國小':[u'陽明山竹子湖海芋田'],
                u'中正國小':[u'袖珍博物館'],
                u'龍安國小':[u'Museum of Drinking Water']}

def read_data(dirName):
    import os
    import re
    
    chineseByte = 3
    csvData = [[u"景點"]]
    
    spotList = []
    for key in SchoolToSpot:
        spotList = spotList + SchoolToSpot[key]
    for item in spotList:
        csvData.append([item])
    
    for date in sorted([d for d in os.listdir(dirName)]):
        dateDir = dirName + '/' + date
        splitDate = re.split('_', date)
        for hour in range(0, 24, 1):
            for minute in range(0,60,5):
                csvData[0].append('%01d/%02d/%02d:%02d' % 
                                  (int(splitDate[1]),int(splitDate[2]),hour,minute))

        for fileName in sorted([f for f in os.listdir(dateDir)]):
            absoluteFileName = dateDir + '/' + fileName   
            school = unicode(fileName[:chineseByte*4].decode('utf-8'))
            
            rainData = []
            
            for line in open(absoluteFileName).readlines()[:-1]:
                data = line.rstrip()
                splited = re.split(' : ', data)
                if splited[0] in ['酷熱指數']:
                    rainData.append(splited[1])

            for spotName in SchoolToSpot[school]:
                index = spotList.index(spotName)+1
                csvData[index] = csvData[index] + rainData
                
    return csvData

def output_csv():
    csvData = read_data('TPWeatherData')
    with open("酷熱指數.csv", "w") as f:
        for row in csvData:
            for data in row[:-1]:
                f.write(data.encode('UTF-8') + ",")
            f.write(row[-1].encode('UTF-8') + "\n")

if __name__ == '__main__':
    output_csv()