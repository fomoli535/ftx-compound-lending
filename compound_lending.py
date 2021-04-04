from datetime import datetime
from ftx import FtxClient

api = "YOUR_API_KEY"
secret = "YOUR_SECRET"

client = FtxClient(api, secret)
lending_info = client.get_lending_info()

log = open("log.txt", "a")

for r in lending_info:
    try:
        now = datetime.now()
        coin = r["coin"]
        lendable = float(r["lendable"])
        offered = float(r["offered"])
        min_rate = float(r["minRate"])
        if lendable > 0 and offered > 0:
            s = now.strftime("%Y-%m-%d %H:%M:%S") + " - Currently lending " + str(offered) + " " + coin + " at minimum rate of " + str(min_rate) + ". " + str(lendable) + " " + coin +" available to lend."
            print(s)
            log.write(s + "\n")
        if lendable > 0 and offered > 0 and offered < lendable:
            client.submit_lending_offer(coin, lendable, min_rate)
            s = now.strftime("%Y-%m-%d %H:%M:%S") + " - Offer submitted to lend " + str(lendable) + " at minimum rate of " + str(min_rate)
            print(s)
            log.write(s + "\n")
    except:
        pass
