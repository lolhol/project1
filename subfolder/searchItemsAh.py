from urllib.request import urlopen, Request
import ssl
from urllib.request import urlopen
import json

# Opens this link to check bz prices
ah_link = "https://sky.coflnet.com/api/auctions/tag/" + "Spirit%20Sceptre" + "/active/bin"

ah_urlopen = urlopen(
    Request(ah_link, headers={'User-Agent': 'Mozilla'}))
ah_url_file = ah_urlopen.read()
ah_item_price = json.loads(ah_url_file)

# Finds the EXACT price of a given item
# ah_spiritScepte = bz["products"]["RECOMBOBULATOR_3000"]["quick_status"]["buyPrice"]

# Prints the EXACT price of the given item
print(ah_item_price)

# https://api.hypixel.net/skyblock/auctions