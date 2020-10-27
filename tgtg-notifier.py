import traceback
import time
import datetime
from pytz import timezone
from currency_symbols import CurrencySymbols
import json
from tgtg import TgtgClient

try:
	# https://pypi.org/project/tgtg/
	client = TgtgClient(
		access_token="",
		user_id=""
	)

	# Getting favourites available
	items = client.get_items(page_size=400)
	items = [item for item in items if item["items_available"] > 0]

	print(items[0])

	# Getting saved IDs
	try:
		with open("list.json", "r") as file:
			json_ids = json.load(file)
	except:
		with open("list.json", "w") as file:
			json.dump([], file)
			json_ids = []

	# Comparing new IDs to old ones
	ids = [item["item"]["item_id"] for item in items]
	new_ids = [id for id in ids if id not in json_ids]

	# Notifying
	for item in items:
		if item["item"]["item_id"] in new_ids:
			# Timezone conversion are kinda broken but are fixable easily
			time_format = "%d/%m at %H:%M"
			tz = timezone('Europe/Brussels')
			# The Z in the times is not parsed (no time zone information in datetime)
			start = datetime.datetime.strptime(item["pickup_interval"]["start"], "%Y-%m-%dT%H:%M:%SZ").astimezone(tz).strftime(time_format)
			end = datetime.datetime.strptime(item["pickup_interval"]["end"], "%Y-%m-%dT%H:%M:%SZ").astimezone(tz).strftime(time_format)

			price_data = item["item"]["price_including_taxes"]
			price = str(price_data["minor_units"] / (10**price_data["decimals"])) + CurrencySymbols.get_symbol(price_data["code"])

			############################################################################
			# ADD NOTIFICATION COMMANDS HERE (SEND EMAIL, SEND PUSH NOTIFICATION, ...) #
			############################################################################
			print(item["display_name"] + " | TooGoodToGo")
			print("From " + start + " to " + end + " - " + price)

			time.sleep(1)

	# Saving new IDs
	with open("list.json", "w") as file:
		json.dump(ids, file)

except:
	# You may wish to get notified if something goes wrong
	traceback.print_exc()
