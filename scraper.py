import requests

req = requests.Session()

open("proxies.txt", "a").write("")
def getProxy():
    r = req.get("https://api.proxyscrape.com?request=getproxies&proxytype=http&timeout=1950&country=all&anonymity=all&ssl=all").text.splitlines()
    for x in r:
        if "</" not in x and "Updated" not in x and "'" not in x and "margin" not in x and "(" not in x and "=" not in x: open('proxies.txt', "a").write(f"{x}\n")

getProxy()

file = open("proxies.txt", "r")
line_count = 0
for line in file:
    if line != "\n":
        line_count += 1
file.close()

print(line_count, 'proxies have been scraped')