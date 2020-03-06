# def count():
#     def add(j):
#         s = j*j
#         return s
#
#     fs = []
#     for i in range(1,4):
#         fs.append(add(i))
#     return  fs
#
#
# list = count()
# print(list)
# print(f1())
# print(f2())

import requests
import json
import openpyxl

Get_China=r"https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5"
class item:
    def __init__(self):
        self.country=list()#国家
        self.province = list()#省份
        self.area=list()#地区
        self.confirm=list()#确诊
        self.suspect=list()#疑似
        self.heal=list()#治愈
        self.dead=list()#死亡
Data_Box=item()#数据盒子
def GetHtmlText(url):
    try:
        res = requests.get(url,timeout = 30)
        res.raise_for_status()
        res.encoding = res.apparent_encoding
        return res.text
    except:
        return "Error"
#获取Json
China = GetHtmlText(Get_China)
City_Count_json = json.loads(China)
City_Count_json = City_Count_json["data"]#将json数据中的data字段的数据提取处理
City_Count_json = json.loads(City_Count_json)
print(type(City_Count_json))
print(City_Count_json)
print(City_Count_json['areaTree'])
reaTree_json = City_Count_json['areaTree']
# print(len(reaTree_json))
for i in range(0, len(reaTree_json)):
    # print(reaTree_json[i]['name'])
    if reaTree_json[i]['name'] == '中国':
        print(len(reaTree_json[i]['children']))
        for j in range(0,len(reaTree_json[i]['children'])):
            print(reaTree_json[i]['children'][j]['name'])