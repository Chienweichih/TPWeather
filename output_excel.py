# -*- coding: utf-8 -*-

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
    from xlwt import Workbook
    
    chineseByte = 3
    
    wb = Workbook()
    s = wb.add_sheet('sheet1')
    
    spotList = []
    for key in SchoolToSpot:
        spotList = spotList + SchoolToSpot[key]
    for index,item in enumerate(spotList,1):
        s.write(index, 0, item)

    for dateIndex,date in enumerate(sorted([d for d in os.listdir(dirName)]), 1):
        dateDir = dirName + '/' + date
        splitDate = re.split('_', date)
        dateStr = splitDate[1][1] + u"月" + splitDate[2] + u"日"
        s.write(0, dateIndex, dateStr)
        for fileName in sorted([f for f in os.listdir(dateDir)]):
            absoluteFileName = dateDir + '/' + fileName   
            school = unicode(fileName[:chineseByte*4].decode('utf-8'))
            for line in reversed(open(absoluteFileName).readlines()[:-1]):
                data = line.rstrip()
                splited = re.split(' : ', data)
                if splited[0] in ['降雨量']:
                    rainData = splited[1]
                    break
            for spotName in SchoolToSpot[school]:
                for index,item in enumerate(spotList,1):
                    if spotName == item:
                        s.write(index, dateIndex, rainData)
                        break
    wb.save(u'降雨量_until_0601.xls')

if __name__ == '__main__':
    read_data('TPWeatherData')
