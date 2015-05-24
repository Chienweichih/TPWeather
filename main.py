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

def checkBeforeWrite(myFile, string):
    if isinstance(string, str) or isinstance(string, unicode):
        myFile.write(string)
    else:
        myFile.write(str(string))
        
def writeToFile(fileName, data):
    with codecs.open(fileName, "w", "utf-8") as output:
        for result in data:
            for key in result:
                checkBeforeWrite(output, key)
                output.write(" : ")
                checkBeforeWrite(output, result[key])
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