import requests

payload = {'SchoolID':'383606'}
res = requests.get('http://weather.tp.edu.tw/school/school.html', params=payload)

print res.text.encode("utf-8")
print "Hello! Nice to meet U."
print "Hello! You can GIT now!!"

print "add -> commit -> push"
print "pull"


print "Thanks for my dear. :)"

while True:
    print "my love"
