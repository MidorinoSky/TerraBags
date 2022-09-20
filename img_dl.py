import requests
import os

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
}

webpng = [line.strip() for line in open("webpages.txt")]

webpng[42:]
webpng[59]
"""i = 60
for png in webpng[59:]:
    r = requests.get(png, headers=headers)
    file = "item/"+str(i)+".png"
    with open(file, 'wb') as f:
        f.write(r.content)  # 写入二进制内容
    i += 1
"""
# wb 以二进制打开文件并写入，文件名不存在会创建

# "https://terraria.wiki.gg/images/thumb/c/c6/Map_Icon_Queen_Bee.png/24px-Map_Icon_Queen_Bee.png"
# "https://terraria.wiki.gg/images/6/6d/Treasure_Bag_%28Moon_Lord%29.png"
pages = [
    "https://terraria.wiki.gg/images/thumb/c/c6/Map_Icon_Queen_Bee.png/24px-Map_Icon_Queen_Bee.png"
    "https://terraria.wiki.gg/images/thumb/f/f4/Map_Icon_Skeletron.png/24px-Map_Icon_Skeletron.png"
    "https://terraria.wiki.gg/images/thumb/c/c9/Map_Icon_Deerclops.png/24px-Map_Icon_Deerclops.png"
    "https://terraria.wiki.gg/images/thumb/d/d4/Map_Icon_Wall_of_Flesh.png/24px-Map_Icon_Wall_of_Flesh.png"
]
url = "https://terraria.wiki.gg/images/f/fe/Skeletron_Mask.png"
r = requests.get(url, headers=headers)
file = "item/"+str(126) + ".png"
with open(file, 'wb') as f:
    f.write(r.content)

import requests
import os
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
}
pages_2 = [line.strip() for line in open("webs_2.txt")]
i = 131
for url in pages_2[:]:
    r = requests.get(url, headers=headers)
    file = "item/"+str(i) + ".png"
    with open(file, 'wb') as f:
        f.write(r.content)  # 写入二进制内容
    i += 1

from PIL import Image
from PIL.Image import ANTIALIAS

for i in range(1, 8):
    im = Image.open(str(i) + ".png")
    im = im.resize((24, 24), resample=ANTIALIAS)
    im.save(str(i) + ".png")

0<=0<0


