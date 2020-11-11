import os

os.chdir(os.getenv("HOMEDRIVE") + os.getenv("HOMEPATH") + "\\Documents" + r"\SEGA\PHANTASYSTARONLINE2\log")

import glob

search = input("検索したい文字列を入力：")
for filepath in glob.glob("./*"):
    #print(filepath)
    try:
        fr = open(filepath, "r",encoding="utf-16")
        for text in fr.readlines():
            if search in text:
                print(text)
    except:
        pass
input("")