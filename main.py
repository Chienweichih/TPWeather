# -*- coding: utf-8 -*-
import requests
import time
import datetime
import json
import codecs

'''''''''''''''''''''
* Time Setting
'''''''''''''''''''''

startTimeStr = '2015-05-20'
endTimeStr = '2015-05-21'
timeFilter = '%Y-%m-%d'

startTime = datetime.datetime.strptime(startTimeStr,timeFilter)
endTime = datetime.datetime.strptime(endTimeStr,timeFilter)

startTimeStamp = time.mktime(startTime.timetuple()) * 1000
endTimeStamp = time.mktime(endTime.timetuple()) * 1000

'''''''''''''''''''''
* School Id
'''''''''''''''''''''
schoolID = {u'至善國中':'413504',u'市大附小':'353608',u'國語實小':'353604',
            u'博愛國小':'323609',u'老松國小':'373609',u'指南國小':'383612',
            u'光復國小':'323603',u'福林國小':'413603',u'中正國小':'343602',
            u'龍安國小':'333601',u'三玉國小':'413619',u'吳興國小':'323606',
            u'五常國小':'343607',u'逸仙國小':'423602',u'湖田國小':'423605'}

'''''''''''''''''''''
* Get requests
'''''''''''''''''''''
payload = {'id'         : schoolID[u'至善國中'],
           'by'         : 'minute',
           'start'      : str(startTimeStamp),
           'end'        : str(endTimeStamp)}
res = requests.get('http://weather.tp.edu.tw/Ajax/jsonp/table.ashx', params=payload)

'''''''''''''''''''''
* JSON Operate
'''''''''''''''''''''
data = json.loads(res.text)
#print data['result'][-1][u'開始時間']

def writeFile(f,s):
    if isinstance(s, str) or isinstance(s, unicode):
        f.write(s)
    else:
        f.write(str(s))

with codecs.open("output.txt","w","utf-8") as file:
        for result in data['result']:
                for key in result:
                    writeFile(file,key)
                    file.write(" : ")
                    writeFile(file,result[key])
                    file.write("\n")
                file.write("=====================================================\n")
