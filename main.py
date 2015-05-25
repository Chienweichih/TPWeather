# -*- coding: utf-8 -*-
import requests
import time
import datetime
import json
import codecs

'''''''''''''''''''''
* School Id
'''''''''''''''''''''
schoolID = {u'至善國中':'413504',u'國語實小':'353604',u'福林國小':'413603',
            u'光復國小':'323603',u'大龍國小':'363607',u'五常國小':'343607',
            u'吳興國小':'323606',u'市大附小':'353608',u'博愛國小':'323609',
            u'老松國小':'373609',u'指南國小':'383612',u'逸仙國小':'423602',
            u'三玉國小':'413619',u'湖田國小':'423605',u'中正國小':'343602',
            u'龍安國小':'333601'}

weatherOrder = [u"開始時間",u"結束時間",u"學校名稱",u"Id",u"降雨量",u"降雨速率",
                u"濕度",u"最高濕度",u"氣溫",u"最高溫",u"最低溫",u"酷熱指數",
                u"最高酷熱指數",u"紫外線",u"最高紫外線",u"氣壓",u"最高氣壓",u"最低氣壓",
                u"輻射",u"最高輻射",u"最低濕度",u"風速",u"最大風速",u"風向",
                u'StartStamp',u'EndStamp',u'CreateOn',u'Disable']

def getTimeStamp(startTimeStr, endTimeStr, timeFilter):
    startTime = datetime.datetime.strptime(startTimeStr,timeFilter)
    endTime = datetime.datetime.strptime(endTimeStr,timeFilter)
    
    startTimeStamp = time.mktime(startTime.timetuple()) * 1000
    endTimeStamp = time.mktime(endTime.timetuple()) * 1000
    
    return (startTimeStamp, endTimeStamp)

def getRequests(schoolID, startTimeStamp, endTimeStamp):
    payload = {'id'     : schoolID,
               'by'     : 'minute',
               'start'  : str(startTimeStamp),
               'end'    : str(endTimeStamp)}
    res = requests.get('http://weather.tp.edu.tw/Ajax/jsonp/table.ashx', params=payload)
    return res

def checkBeforeWrite(outputFile, string):
    if isinstance(string, str) or isinstance(string, unicode):
        outputFile.write(string)
    else:
        outputFile.write(str(string))
        
def writeToFile(fileName, wholeDayData):
    with codecs.open(fileName, "w", "utf-8") as output:
        for every5minsData in wholeDayData:
            sortedList = sorted(every5minsData.items(), key=lambda x:weatherOrder.index(x[0]))
            for sortedTuple in sortedList:
                checkBeforeWrite(output, sortedTuple[0])
                output.write(" : ")
                checkBeforeWrite(output, sortedTuple[1])
                output.write("\n")
            output.write("=====================================================\n")

def main():

    startTimeStr = '2015-05-20'
    endTimeStr = '2015-05-21'
    timeFilter = '%Y-%m-%d'

    startTimeStamp, endTimeStamp = getTimeStamp(startTimeStr, endTimeStr, timeFilter)
    
    res = getRequests(schoolID[u'至善國中'], startTimeStamp, endTimeStamp)
    data = json.loads(res.text) #JSON Operate
   
    writeToFile("output.txt", data['result'])

if __name__ == "__main__":
    main()