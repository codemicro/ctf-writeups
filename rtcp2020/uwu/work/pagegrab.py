import requests

urls = [
    "uwu",
    "omgmeow",
    "pandaaaaaaa",
    "you-better-wash-your-rice",
    "footprint",
    "uwustorage"
]

for url in urls:
    print(url)
    r = requests.get(f"https://riceteacatpanda.wtf/{url}", allow_redirects=False)
    open(f"pages/{url}.html", "wb").write(r.text.encode())
