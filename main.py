import requests
import codecs
import json

payload = {'SchoolID':'383606'}
res = requests.get('http://weather.tp.edu.tw/school/school.html', params=payload)
res.encoding = "utf-8"
print res.text
