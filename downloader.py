import requests

headers = {
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/85.0.4183.102 Safari/537.36 "
}

pages = [line.strip() for line in open("webpages2.txt")]
i = 1777
for p in pages:
    r = requests.get(p, headers=headers)
    with open("interface/" + str(i) + ".png", "wb") as f:
        f.write(r.content)
    i += 1
print("下载完成")
