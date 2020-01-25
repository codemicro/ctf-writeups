from bs4 import BeautifulSoup as bs
import re

urls = [
    "uwu",
    "omgmeow",
    "pandaaaaaaa",
    "you-better-wash-your-rice",
    "footprint",
    "uwustorage"
]

for url in urls:
    soup = bs(open(f"pages/{url}.html", "rb").read().decode(), features="lxml")
    results = [result.getText() for result in soup.findAll("main", {"role" : "main"})]

    for result in results:
        og = result
        result = result.replace("ᵘ", "u").replace("ʷ", "w").lower()
        result = result.replace("uwu", "")
        result = result.strip()
        result = " ".join(result.split())
        print(f"{url}: {result}\n")

        if "rtcp" in result:
            for r in re.findall(r"(rtcp{.*})", og):
                print(f"!!!FLAG!!! {url}: {r}")
                input("Press enter to continue search")
                print("\n")
            
input("\nPRESS ENTER TO EXIT")
