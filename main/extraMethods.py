import json
from django.utils import timezone
import datetime as dt
import requests
import random


def userDetails(codeforcesHandle, clearPastProblems):
    url = requests.get(
        'https://codeforces.com/api/user.info?handles='+codeforcesHandle)
    jsonData = url.json()
    data = json.dumps(jsonData)
    codeforcesHandle = json.loads(data)
    if(codeforcesHandle['status'] != "OK"):
        return False
    if(clearPastProblems):
        completedProblems.clear()
    return codeforcesHandle['result'][0]


def convertUnixTime(unixtime):
    date = dt.datetime.fromtimestamp(unixtime).strftime('%Y-%m-%d')
    time = dt.datetime.fromtimestamp(unixtime).strftime('%H:%M:%S')
    date_time_obj = dt.datetime.strptime(date+" "+time, '%Y-%m-%d %H:%M:%S')
    time = date_time_obj.time()
    time = str((dt.datetime.combine(dt.date(1, 1, 1), time) +
                dt.timedelta(hours=5, minutes=30)).time())
    return date+" "+time


def convertToHour(secondsTime):
    return str(dt.timedelta(seconds=secondsTime))


def contestDetails():
    url = requests.get('https://codeforces.com/api/contest.list')
    jsonData = url.json()
    data = json.dumps(jsonData)
    contests = json.loads(data)
    contestList = []
    count = 0
    for contest in contests['result']:
        if(contest['phase'] == "FINISHED"):
            break
        else:
            contest['startTimeSeconds'] = convertUnixTime(
                contest['startTimeSeconds'])
            contest['durationSeconds'] = convertToHour(
                contest['durationSeconds'])
            contestList.append(contest)
            count += 1
    contestList = contestList[::-1]
    return contestList[0:5]


completedProblems = {}


def getTags(codeforcesHandle, rank):
    url = requests.get(
        'https://codeforces.com/api/user.status?handle='+codeforcesHandle)
    jsonData = url.json()
    data = json.dumps(jsonData)
    submissions = json.loads(data)
    submissions = submissions['result']
    wrongSubmissions = {}
    for problem in submissions:
        if(problem['verdict'] != 'OK'):
            for tags in problem['problem']['tags']:
                if(tags not in wrongSubmissions):
                    wrongSubmissions[tags] = 1
                else:
                    wrongSubmissions[tags] += 1
        else:
            completedProblems[problem['problem']['name']] = 1
    weakTags = {}
    minSolvedCount = 0
    maxSolvedCount = 35000
    if(rank < 1200):
        minSolvedCount = 12000
        maxSolvedCount = 14000
    elif(rank < 1400):
        minSolvedCount = 9500
        maxSolvedCount = 12000
    elif(rank < 1600):
        minSolvedCount = 8500
        maxSolvedCount = 11000
    elif(rank < 1900):
        minSolvedCount = 7800
        maxSolvedCount += 10000
    elif(rank < 2100):
        minSolvedCount = 6900
        maxSolvedCount = 9000
    elif(rank < 2400):
        minSolvedCount = 4000
        maxSolvedCount = 7000
    elif(rank < 2600):
        minSolvedCount = 2000
        maxSolvedCount = 4000
    elif(rank < 3000):
        minSolvedCount = 500
        maxSolvedCount = 2000
    else:
        minSolvedCount = 0
        maxSolvedCount = 1000
    for tags in sorted(wrongSubmissions.items(), key=lambda x: x[1], reverse=True):
        weakTags[tags[0]] = getProblems(
            tags[0], rank, minSolvedCount, maxSolvedCount)
        if(len(weakTags) == 4):
            break
    return weakTags


def getProblems(tag, rank, minSolvedCount, maxSolvedCount):
    problems = []
    url = requests.get(
        'https://codeforces.com/api/problemset.problems?tags='+tag)
    jsonData = url.json()
    data = json.dumps(jsonData)
    allData = json.loads(data)
    allProblems = allData['result']['problems']
    allproblemStatistics = allData['result']['problemStatistics']

    count = 0
    lengthOfProblemSet = len(allProblems)
    j = 0
    alreadySuggested = {}
    while(j < lengthOfProblemSet):
        j += 1
        i = random.randint(0, lengthOfProblemSet-1)
        if tag in allProblems[i]['tags']:
            if((allProblems[i]['name'] not in alreadySuggested) and (allProblems[i]['name'] not in completedProblems) and allproblemStatistics[i]['solvedCount'] >= minSolvedCount and allproblemStatistics[i]['solvedCount'] <= maxSolvedCount):
                alreadySuggested[allProblems[i]['name']] = 1
                tempList = []
                tempList.append(allProblems[i]['name'])
                tempList.append('https://codeforces.com/problemset/problem/' +
                                str(allProblems[i]['contestId'])+'/'+allProblems[i]['index'])
                problems.append(tempList)
                count += 1
        if(count == 6):
            break
    return problems
