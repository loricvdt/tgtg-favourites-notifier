# *TooGoodToGo* favourites notifier

Python script notifying if an item becomes available in your favourites on *TooGoodToGo*

It works by fetching the available favourites from *TooGoodToGo*, checking against saved items in `list.json` if they have been sent a notification, if not it will send them according to **your notification method**. Finally, it saves the new available favourites in `list.json` for the next run

**Works with at most 400 favourites (API limit)**

## Installation 

This script should be ran using a task scheduler (such as [cron](https://en.wikipedia.org/wiki/Cron)) to check availability periodically using this command:

`python3 tgtg-notifier.py`

### Requirements:

- Python 3
- [tgtg](https://pypi.org/project/tgtg/) (*TooGoodToGo* API)
- [pytz](https://pypi.org/project/pytz/) (to handle timezones)
- [currency-symbols](https://pypi.org/project/currency-symbols/) (to display currency correctly)

### Connecting your TooGoodToGo account

Using the [tgtg](https://pypi.org/project/tgtg/) package, you can retrieve your `user_id` and an `access_token` ([more info on tgtg's pypi page](https://pypi.org/project/tgtg/)) using:

```python
client = TgtgClient(email="YOUR EMAIL ADDRESS", password="YOUR PASSWORD")
client._login()
print("user_id: " + client.user_id)
print("access_token: " + client.access_token)
```

You can then write them in the beginning of the script here:

```python
# https://pypi.org/project/tgtg/
client = TgtgClient(
    access_token="",
    user_id=""
)
```

### Adding your notification method

In this part of the code you can add your custom notification method instead of the `print()` statements. It's up to you to choose how you wish to be notified (by email, with a push notification, etc...)

```python
############################################################################
# ADD NOTIFICATION COMMANDS HERE (SEND EMAIL, SEND PUSH NOTIFICATION, ...) #
############################################################################
print(item["display_name"] + " | TooGoodToGo")
print("From " + start + " to " + end + " - " + price)

```

