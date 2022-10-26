from urllib.request import urlopen, Request
import ssl
from urllib.request import urlopen
import json
from uuidStuff.profileUuid import profile3
from uuidStuff.profileUuid import profile_uuid
from enchantPrices.recomPrice import price1

item = input("Please enter the item first word in name:\n")

slot_1_item = profile3["profiles"][profile_uuid]["items"]["inventory"]


for x in slot_1_item:
  if "tag" in x:
    slotitem = x
    slotitem1 = slotitem["display_name"]
    first_word = slotitem1.split()[0]
    no_caps = first_word.lower()
    if no_caps == item.lower():
      break 

if no_caps != item.lower():
  print("No items found...")

print(slotitem1)