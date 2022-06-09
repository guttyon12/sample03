from importlib.resources import path
import os
import chardet
import unicodedata

f = open('mozi.txt', mode='w')
mozi = input("何か入力してください")
f.write(mozi)

with open('mozi.txt', 'rb') as f:
    print(chardet.detect(f.read())['encoding'])

    if str.isdigit(mozi) == True:
        print("数字です")
    else:
        print("文字列です")

    hanbetu = unicodedata.east_asian_width(list(mozi)[0])

    if hanbetu == ("F") or hanbetu == ("W"):
        print("全角です。")
    else:
        print("半角です")

os.remove('mozi.txt')


f.close
