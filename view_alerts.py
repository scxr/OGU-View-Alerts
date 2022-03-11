import requests
import time
from bs4 import BeautifulSoup
import requests
wh = input("Enter discord webhook: ")
def alertBlocked():
    poglul = {
        "avatar_url":"https://pbs.twimg.com/profile_images/930577665643438080/VVjqz6XO.jpg",
        "name":"Alert logger",
        "embeds": [
            {
                "title": "New alert found",
                "description": f"CF has been blocked, please enter new token in terminal",
                "color": 16304348,
                "footer":{
                    "text":"made by t.me/protective"
                    },

            }
        ]
    }
    req = requests.post(wh, json=poglul)
def postDisc(user_from, alert_text, icon) :
    poglul = {
        "avatar_url":"https://pbs.twimg.com/profile_images/930577665643438080/VVjqz6XO.jpg",
        "name":"Alert logger",
        "embeds": [
            {
                "title": "New alert found",
                "description": f"From User: {user_from}\nAlert : {alert_text}",
                "color": 16304348,
                "footer":{
                    "text":"made by t.me/protective"
                    },

                "thumbnail": {
                    "url": icon
                }
            }
        ]
    }
    req = requests.post(wh, json=poglul)
def main():
    tts = input("Time between checking for alerts (in seconds) : ")
    cf_clearance = input("Please enter cookie value of 'cf_clearance' : ")
    token = input("Please enter cookie value of 'ogusersmybbuser' : ")

    while 1:
        headers = {
            'authority': 'ogusers.com',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
            'accept': '*/*',
            'x-requested-with': 'XMLHttpRequest',
            'sec-ch-ua-mobile': '?0',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://ogusers.com/',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'cookie': f'ogusersmybb[lastvisit]=1636628803; _ga=GA1.2.847331408.1636628807; ogusersmybb[lastactive]=1636628810; ogusersloginattempts=1; __stripe_mid=0; ogusersmybbuser={token}; ogusersmultiquote=; cf_clearance={cf_clearance}; ogusersupgrade=go; oguserssid=0',
        }

        params = (
            ('action', 'modal'),
            ('ret_link', 'https://ogusers.com/index.php'),
        )

        response = requests.get('https://ogusers.com/alerts.php', headers=headers, params=params)
        if response.status_code == 403:
            print("Blocked")
            cf_clearance = input("Please enter cookie value of 'cf_clearance' : ")

        soup = BeautifulSoup(response.text, "html.parser")
        alerts = soup.find_all("tr")
        tracked = []

        for alert in alerts[::-1]:
            user =""
            alert_text = ""
            user_icon = ""
            is_read = True
            user_span = alert.find("span")
            if (user_span != None):
                user = user_span.text
                if alert["class"][1] == "alert--unread":
                    is_read = False
                alert_text = str(alert).split("</span>")[1].split("</b>")[0].replace("<b>", "")
                user_icon = alert.find_all("a", {"class":"avatar"})[0].find_all("img")[0]["src"]
                print(f"{user} : {alert_text.lstrip()} : Unread: {is_read}")
                if f"{user} : {alert_text.lstrip()}" not in tracked:
                    postDisc(user, alert_text.lstrip(), user_icon)
                    tracked.append(f"{user} : {alert_text.lstrip()}")

        time.sleep(tts)
main()
