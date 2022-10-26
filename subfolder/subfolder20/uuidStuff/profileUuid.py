import profile
from urllib.request import urlopen, Request
import json
import ssl
from subfolder20.uuidStuff.acuuid import accountID


def profileUuid():
# apiKey = input("Please enter api key:\n")


# looks up profile of a specified uuid ("4fedebb2-4665-47f4-9c0c-9dce77cc66dc" or Zaxium in my case, also try opening it to see what it does.)
    link11 = "https://sky.shiiyu.moe/api/v2/profile/" + accountID

    m = urlopen(Request(link11, headers={'User-Agent': 'Mozilla'}))
    myfile2 = m.read()
    profile3 = json.loads(myfile2)

    profile_uuid_pre = profile3["profiles"]



    profile_uuid0 = list(profile_uuid_pre.keys())[0]
    profile_uuid1 = list(profile_uuid_pre.keys())[1]

    for x in profile_uuid_pre:
        profile5 = profile_uuid_pre[x]
        if profile5["current"] == False:
            pass
        if profile5["current"] == True:
            profile_uuid = x
        break




