from django.shortcuts import render
from main.extraMethods import userDetails, convertUnixTime, getTags, contestDetails

# Create your views here.


def index(request):
    return render(request, 'login.html', {'giveError': False})


def login(request):
    userInfo = False
    if('refresh' in request.POST):
        userInfo = userDetails(request.POST.get('username'), False)
    else:
        userInfo = userDetails(request.POST.get('username'), True)

    if(userInfo == False):
        return render(request, 'login.html', {'giveError': True})

    dt_object = convertUnixTime(userInfo['lastOnlineTimeSeconds'])

    weakTags = getTags(userInfo['handle'], userInfo['rating'])

    return render(request, 'profile.html', {'user': userInfo, 'lastOnline': dt_object, 'tags': weakTags})


def futureContests(request):
    contestsList = contestDetails()
    return render(request, 'contests.html', {'contests': contestsList})
