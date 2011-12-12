#!/usr/bin/python

import simplejson as json


#utility functions
def getTime( obj ):
    return obj['endTime'] - obj['startTime']


#__ main __

#vars
outputDict = {}
layoutCount = 0
recalculateCount = 0
paintCount = 0
totalLayoutTime = 0
totalRecalculateTime = 0
totalPaintTime = 0
# test = json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
log = open('log.json','r')
data = log.read()
timelineJson = json.loads(data);


for item in timelineJson :
    if 'type' in item:
        if item['type'] == 'Paint':
            paintCount += 1
            totalPaintTime += getTime(item)
        elif item['type'] == 'RecalculateStyles':
            recalculateCount += 1
            totalRecalculateTime += getTime(item)
        elif item['type'] == 'Layout':
            layoutCount += 1
            totalLayoutTime += getTime(item)



#print
outputDict['paintCount'] = paintCount
outputDict['totalPaintTime'] = totalPaintTime
outputDict['recalculateCount'] = recalculateCount
outputDict['totalRecalculateTime'] = totalRecalculateTime
outputDict['layoutCount'] = layoutCount
outputDict['totalLayoutTime'] = totalLayoutTime
print json.dumps(outputDict)
