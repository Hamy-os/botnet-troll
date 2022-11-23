wanted_item = ["Green Ultimate Dragon Face", "Silver Emperor of the Night", "Green Queen of the Night", "Blue Queen of the Night", "Radioactive Beast Mode", "Catching Snowflakes", "Supa Dupa Fly Cap", "ROBLOX Madness Face", "Purple Bubble Trouble", "Virtual Commando", "Green Bubble Trouble", "Adurite King of the Night", "Playful Vampire", "Adurite Antlers", "Tentacles Junior", "Gold King of the Night", "Valkyrie Helm", "Blizzard Beast Mode", "Neon Green Beautiful Hair", "Traffic Cone", "Dominus Formidulosus", "Super Super Happy Face", "Black Iron Horns", "Gold Emperor of the Night", "Perfectly Legitimate Business Hat", "Beautiful Hair for Beautiful Space People", "Brilliant Bombastique", "Silver King of the Night", "The Classic ROBLOX Fedora", "Silverthorn Antlers", "Green Wistful Wink", "Purple Wistful Wink", "Blue Wistful Wink", "Blue Bubble Trouble", "Evil Skeptic", "Bubble Trouble"] 
power_limit = 2.1 # the limit of power (2.1/k) you want to buy for normal items ( make it .1 higher)
power_limit_rare = 2.3 # same as above but for wanted_item (make it .1 higher)
price_limit = 40.0 # max price for an item
price_limit_rare = 500.0 # max price for a wanted item 
wallet_limit = 20.0 # wallet balance will never go under this 
token = "eyJhbGciOiJIUzI1NiJ9.YjljZDc4YjYwZjNjOWIyNjczYzRlM2VlMGFhNDNkNzkuN2RhZDlmOWM0NTIxNWE0ZGQ5YjE1YmJjZjNmOTVlMDk1N2U5NWZiMjE5MjIyOWQ5YjY0YmJkNzNlNzRmMjRkNDBiZjhkNmRiNTljMTM2NmY5MzBlZjFjNjQ0MDY3Yzg1NjBhMmFiYjVhNGI0ZWEyOTYwYWQ1YzhiNWJjNzgwMDBiNjNhM2RjYTlkZGQwMmRmMzFkZjkzMWU0ZmVjZjM3YTYwNzdiYTZmMTg5ZGRkZmYzZmU4NGU3YzU1ZjZkZjc5NTczMTlmNGYzMjRhNTJkOWMwNTU1MzhjZmY1ZTM2NGFjOTFkM2RlOWI5MmE0NmNjNDcxODNiZjY4OGY2NjIyMDI1M2VlOThjOTVmNTM4ZDZjNzA2MzVmNzVkYzg2NDcxN2UzNWM5M2YxNTQ1OGE4NWZkMDlkMGRlN2E3MWFlNDhmYTU5NzQxYWIyOWY0M2ZkMjEyZWNlMDRmZDkxNjE1M2FmOWZmNDU4OWFkZTQ1YTFmNzUxMmE4MjRlODIyZGY1ZTA1ZmE1MmJmMDQ4ZTg4ZGY1ZWI3OGU0YTI0YjhhZTUwOTVmNzYxYjQxZGUyMTFiZDE4Y2ViZDgyZjE3YTFkYjEzMmU0MTgyMTM3MTJkZjVjZTA1Zjg5OGU5MjhkYWI0Y2QwZTRiNzQ2NWM0Mjg4NzY3ZjM5MmExMzIyZmVjMTM5ZDA0ZGFkYmY0YTZlZTY2ZWE1Nzc5NDM2OGE5YjVkZWM0MjZiMWJmM2Q0NGNlNTJjNGEwNTAxZWYwYzU2OTM1ZGE2MTFjZTk5ZDgyNmYxZTNjMmYxYTA0MTI5MzI5OWVhZDYwNDkwYzkwMzRjZjIxNmFiNWU5NDBlODQzNmNhMGNhOGJkY2I4ZGZhYzg4YTcyYzlkYWI3MDgyMTU1ZjlkZDQxZmIzOWNjMGYyOTUzOGM2MjQ1OWY4NjFhYjhmYjc0MTkxMGMyNmFlYzkxY2UyZmI5N2JhMTA1OWZiMDhhNDMxNGI1OGRkYWE5NTJjOWIxMDlhZDRlYjhkNWM2OGVmNjY1YTE5NjVmMTZlMzRiZWE3ZDRhNDJkNmI5MWE0YTJlNzNjYmQzNDBiZDNhY2U3ODJkZWMyN2M1YmNlN2Q5ODE3ZTY3Mjk2NjlmZDVmNjdlZjhiZmI1YWFkYzY5MTE3OTE1MDYwYjA2ZWI4MDYwY2JhMDE2MTk0NGQyNTQzZmFhN2Y3Mzc0ZDU3ZmNjY2FmZTRmZmFjZDgyYzM2MDIzMjc1MmE1NzA4NjA0ODg2Yzg2YjJlMTk2NjRjZTVhMTZiN2Y5ZDFhZTkzODNkMjE0MWE5MjcwN2ZjODA4NTIwZjNlOWM2YmNiNTNiMDZhMjQwNTg5Y2JiN2FlNzk5YjU5ZGNkZDRhMjg1YmI3ZmExMTE5NzNlNjY4N2Q3MTY1MTViYWFkY2ZhNDhlNmI5ZjFhYjljMjA4M2Q5NmVlZDQ4N2ZmODRlMzJmY2ZlYzBkNTY3MjdkODhkOTBmZTNiYjY3NDgwODI2ZGRlNjY0ZjJjYmU4YjBiNGVhOWE0ZTE3Y2FlY2RkYzAzNWU3NThkZTc1YzJkN2U1NmRmNzIzN2RmM2Y5YjZhMzIzMTJmNzg5YmUwNGJmYTc3NGRjYjVlNjVjMzAxMTFhOTg0NTE0ZjdlYmZlZWEyYzlkOWZkODk2NTE3OWJhZjMzZDc3YTI0OGVmNzZlZmFhNWMxMzI0MjZhNDFlMjUzYmU3MjAyMDJlNDEyMDVmZTgwZWQ5NmNiNTkyZmIyMzhlZjcxNzYxYjY2YjA4YzA1NjBlNjIxYWI2NzRjMTBiZGI1NjAzZjQ3OTI0ZTBmYjRmYTY2ZDdkZWFiMmRkM2E3OWQ2ZjU2OGVjYmU4ZmRjNGMwYzEyMzMwMjVhMjY3NWEzNjhlMTM0YzIwNjk1Yzk1MGNiNzY1ZGQ3MDYyMDljMGZhMzFiZDMxZjhkZTA4NTZlNTM3N2YzY2VjZTQ2NzdjNDRhMmY5MWU2NWMzMGQ2OThmZWUyZDEyMDhlZjNkZTBiOTU2YjE1NGQzYWQxNzdjOWY4YzEyYzg4NzA2MzVjNDBjZDY1ZWRmOGM4ZTIwMmJjYmQyMzQ3OGU4YTY4YjI1YWFlMTZhYjFhYzAyM2RhYzA4OTdiZDEwZDI4MjdmMDJhYjAwNGI5Zjc2NTAwMDgxMGE0MzQ3NGJhYzMxMzMyNjM2YjM2ZjhmZDAwZWJlNjUxYmQ3NGViY2Y3MDNiNjQ3ZTgzODRhYTFmMzJiODk3Y2Q2OGRmYTUyYmQ5OA.d3YxKvmywSS3b6qFJXI9we5aWyWQV50gnYZXfvah1B4"
url = "https://discord.com/api/webhooks/1041778715123777706/oxOfi_0c1RefxnLXa1WJJno19gcmrjoO_OMhyT6l0scCd2a6kGOhvYxYrct0I4sFsmvm" # webhook url
import requests
import time

headers = {
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q=0.8",
    "origin": "https://rbxflip.com",
    "referer": "https://rbxflip.com/",
    "sec-ch-ua": '"Brave";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "Windows",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    'sec-fetch-site': "same-site",
    "sec-gpc": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
}


headers2 = {
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q=0.8",
    "authorization": "Bearer " + token,
    "origin": "https://rbxflip.com",
    "referer": "https://rbxflip.com/",
    "sec-ch-ua": '"Brave";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "Windows",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    'sec-fetch-site': "same-site",
    "sec-gpc": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
    "x-socket-id": "YNEKrX6GT94Cip3sAOPM"
}

headers3 = {
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q=0.8",
    "authorization": "Bearer " + token,
    "content-length": "72",
    "content-type": "application/json",
    "origin": "https://rbxflip.com",
    "referer": "https://rbxflip.com/",
    "sec-ch-ua": '"Brave";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "Windows",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    'sec-fetch-site': "same-site",
    "sec-gpc": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
    "x-socket-id": "YNEKrX6GT94Cip3sAOPM"
}

headers4 =  {
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q=0.8",
    "authorization": "Bearer " + token,
    "content-length": "40",
    "content-type": "application/json",
    "origin": "https://rbxflip.com",
    "referer": "https://rbxflip.com/",
    "sec-ch-ua": "'Brave';v='107', 'Chromium';v='107', 'Not=A?Brand';v='24'",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "Windows",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "sec-gpc": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
    "x-socket-id": "WNc6TwmO-T0iBjFYAYd_",
}

headers5 =  {
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q=0.8",
    "authorization": "Bearer " + token,
    "origin": "https://rbxflip.com",
    "referer": "https://rbxflip.com/",
    "sec-ch-ua": "'Brave';v='107', 'Chromium';v='107', 'Not=A?Brand';v='24'",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "Windows",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "sec-gpc": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
    "x-socket-id": "WNc6TwmO-T0iBjFYAYd_",
}


def sell(id):
    try:
        print(id)
        res = requests.post("https://api.rbxflip.com/roblox/shop/list", headers=headers4, json=[{"userAssetId": int(id), "rate": power_limit}])
        print(res.text)
        if res.json()["statusCode"] == 403:
            requests.post(url, data={"content": "account is moderated."})
            return
        else:
            requests.post(url, data={"content": f"<@305143655159693313> Sold {name} for 2.1/1k"})
    except:
        pass

def sell_rare(id):
    try:
        print(id)
        res = requests.post("https://api.rbxflip.com/roblox/shop/list", headers=headers4, json=[{"userAssetId": int(id), "rate": power_limit_rare}])
        print(res.text)
        if res.json()["statusCode"] == 403:
            requests.post(url, data={"content": "account is moderated."})
            return
        else:
            requests.post(url, data={"content": f"<@305143655159693313> Sold {name} for 2.3/1k"})
    except:
        pass
end = False
blacklist = []
check = 0
wallet = requests.get("https://api.rbxflip.com/wallet/balance", headers=headers2).json()
initial_balance = float(wallet["balance"])
while not end:
    check += 1
    ################### GET BALANCE ###################
    wallet = requests.get("https://api.rbxflip.com/wallet/balance", headers=headers2).json()
    balance = float(wallet["balance"])
    if wallet["locked"] == True:
        print("Cookie is locked.")
    elif initial_balance - balance > 100:
        print("Made 100 dollar profit.")
        end = True
        break
    else:
        print("Wallet balance: " + str(balance))
    ################### GET ITEMS ###################
    shop_items = requests.get("https://api.rbxflip.com/roblox/shop").json()
    print("Items in shop: " + str(len(shop_items)))
    items = []
    items_rare = []
    for item in shop_items:
        if item["userAsset"]["asset"]["name"] in wanted_item:
            if item["rate"] < power_limit_rare and item["price"] <= price_limit_rare:
                if balance - item["price"] < wallet_limit:
                    print("Not enough money to buy " + item["userAsset"]["asset"]["name"])
                else:
                    if item["userAsset"]["userAssetId"] in blacklist:
                        pass
                    else:
                        items_rare.append(item)
                        print("Found wanted item: " + item["userAsset"]["asset"]["name"])
                        blacklist.append(item["userAsset"]["userAssetId"])
        elif item["rate"] < power_limit and item["price"] <= price_limit:
            if balance - item["price"] > wallet_limit:
                if item["userAsset"]["userAssetId"] in blacklist:
                    pass
                else:
                    items.append(item)
                    print("Added " + item["userAsset"]["asset"]["name"] + " for " + str(item["price"]) + " to items list")
            else:
                print("Not enough money to buy " + item["userAsset"]["asset"]["name"])
    print("Items to buy: " + str(len(items)))
    print("Rare Items to buy: " + str(len(items_rare)))
    ################### BUY ITEMS ###################
    if len(items_rare) > 0:
        for rare in items_rare:
            userId = rare["userAsset"]["userId"]
            name = rare["userAsset"]["asset"]["name"]
            userAssetId = rare["userAsset"]["userAssetId"]
            power = rare["rate"]
            expectedPrice = rare["price"]
            print(f"Buying {name} for {expectedPrice} with id {userAssetId}")
            response = requests.post("https://api.rbxflip.com/roblox/shop/buy", headers=headers3, json=[{"userId": userId, "userAssetId":  userAssetId, "expectedPrice": expectedPrice}])
            response = response.json()
            print(response)
            try:
                if response["statusCode"] == 400:
                    print("Cannot buy from yourself")
                    blacklist.append(userAssetId)
                if response["ok"] == False:
                    print("Cannot buy item")
                    blacklist.append(userAssetId)
                if response["ok"] == "false":
                    print("Cannot buy item")
                    blacklist.append(userAssetId)
            except:
                print("Bought " + name + " for " + str(expectedPrice))
                requests.post(url, data={"content": f"<@305143655159693313> Bought rare {name} for {expectedPrice} and power {power}"})
                sell_rare(userAssetId)
    if len(items) > 0:
        for item in items:
            userId = item["userAsset"]["userId"]
            name = item["userAsset"]["asset"]["name"]
            userAssetId = item["userAsset"]["userAssetId"]
            power = item["rate"]
            expectedPrice = item["price"]
            print(f"Buying {name} for {expectedPrice} with id {userAssetId}")
            response = requests.post("https://api.rbxflip.com/roblox/shop/buy", headers=headers3, json=[{"userId": userId, "userAssetId":  userAssetId, "expectedPrice": expectedPrice}])
            response = response.json()
            print(response)
            try:
                if response["statusCode"] == 400:
                    print("Cannot buy from yourself")
                    blacklist.append(userAssetId)
                if response["ok"] == False:
                    print("Cannot buy item")
                    blacklist.append(userAssetId)
                if response["ok"] == "false":
                    print("Cannot buy item")
                    blacklist.append(userAssetId)
            except:
                print("Bought " + name + " for " + str(expectedPrice))
                requests.post(url, data={"content": f"<@305143655159693313> Bought {name} for {expectedPrice} and power {power}"})
                sell(userAssetId)
    # check if any unsold items
    print("{} Checking..." .format(check))
    if check == 10:
        try:
            r = requests.get("https://api.rbxflip.com/roblox/items", headers=headers5)
            response = r.json()
            for item in response:
                if item["asset"]["name"] in wanted_item:
                    print("Added id {} to array for {}".format(userAssetId, power_limit_rare))
                    sell_rare(userAssetId)
                if "isProjected" in item["asset"]:
                    pass
                elif item["asset"]["value"] < 1000:
                    pass
                else:
                    userAssetId = item["userAssetId"]
                    print("Added id {} to array for 2.1".format(userAssetId))
                    sell(userAssetId)
        except:
            pass
        check = 0