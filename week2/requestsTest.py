import requests
import json

log = True

url = "https://cloud.culture.tw/frontsite/trans/SearchShowAction.do?method=doFindTypeJ&category=5"
data = requests.get(url)

print(type(data))

datainfo = json.loads(data.text)

if log:
    print(type(datainfo))
    print(len(datainfo))

# write json file
with open("music_show.json", "w") as outputFile:
    json.dump(datainfo, outputFile)
    outputFile.close()

#read json file
with open("music_show.json", "r") as inputFile:
    data = json.load(inputFile)

if log:
    print(type(data))
    print(type(data[1]))

# write txt
with open("music_show.txt", "w", encoding = 'utf-8') as outputFile:
    
    for i in range(len(data)):
        title = data[i]["title"]
        startDate = data[i]["startDate"]
        endDate = data[i]["endDate"]
        outputFile.write("%s : %s ~ %s\n" % (title,startDate,endDate))
    outputFile.close()

