from urllib.request import urlopen, Request
import json
import ssl
from subfolder.acuuid import accountID
from subfolder.searchItemsBazar import bz_recombobulator



# looks up profile of a specified uuid ("4fedebb2-4665-47f4-9c0c-9dce77cc66dc" or Zaxium in my case, also try opening it to see what it does.)
link11 = "https://sky.shiiyu.moe/api/v2/profile/" + accountID

m = urlopen(Request(link11, headers={'User-Agent': 'Mozilla'}))
myfile2 = m.read()
profile3 = json.loads(myfile2)

# add 50 to recom price.
item_recom = profile3["profiles"]["aaac8eafc6204b5095f52aaf23b36806"]["items"]["inventory"][0]["recombobulated"]

if item_recom:
    price1 = 50 + bz_recombobulator
else:
    pass 

