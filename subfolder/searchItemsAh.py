from urllib.request import urlopen, Request
import ssl
from urllib.request import urlopen
import json
from uuidStuff.profileUuid import profile3
from uuidStuff.profileUuid import profile_uuid
from enchantPrices.recomPrice import price1

########################################################################################################################

slot_1_item = profile3["profiles"][profile_uuid]["items"]["inventory"][0]["display_name"]

slot_1_item_reforge_pre = profile3["profiles"][profile_uuid]["items"]["inventory"][0]["extra"]["reforge"]

slot_1_item_reforge = slot_1_item_reforge_pre.title()

slottest = slot_1_item.replace(slot_1_item_reforge + " ", "")

for i in range(5):
    slottest = slottest.replace("✪", "")

slottest = slottest.strip()

slottest = slottest.replace(" ", "%20")

########################################################################################################################

ah_link = "https://sky.coflnet.com/api/auctions/tag/" + slottest + "/active/bin"

ah_urlopen = urlopen(
    Request(ah_link, headers={'User-Agent': 'Mozilla'}))
ah_url_file = ah_urlopen.read()
ah_item_price = json.loads(ah_url_file)

# Finds the EXACT price of a given item
ah_item_price_final = ah_item_price[1]["startingBid"]

total_cost = ah_item_price_final + price1

print(total_cost)