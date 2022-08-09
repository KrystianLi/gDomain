# -*- coding: utf-8 -*-
# @Author : KrystianLi
# @Github : https://github.com/KrystianLi

import csv
from time import time
import requests
import urllib3,urllib
import time
from module.argParse import parseArgs
import json
import os
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

result_list = []

url = 'https://zfwzzc.www.gov.cn/check_web/databaseInfo_mainSearch.action?sEcho=1&iColumns=6&sColumns=%2C%2C%2C%2C%2C&iDisplayStart=0&iDisplayLength=10&mDataProp_0=dataNumber&bSortable_0=false&mDataProp_1=sitecode&bSortable_1=false&mDataProp_2=wzzgdw&bSortable_2=false&mDataProp_3=wzmc&bSortable_3=false&mDataProp_4=url&bSortable_4=false&mDataProp_5=caozuo&bSortable_5=false&iSortCol_0=0&sSortDir_0=asc&iSortingCols=1&type=2&term={}&searchType=wzmc&isSearch=true&tt=Tue+Aug+09+2022+10%3A13%3A27+GMT%2B0800+(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)&is_exp=0%2C1%2C3&size=10&pos=1&pageNo=1&_t=1660011207890'
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.47"
}


def outputResult(argsFile, argsOutput, resultList):
    fileName = list(os.path.splitext(os.path.basename(argsFile)))[0]
    outputFile = f"./output/{fileName}_{argsOutput}.csv"
    if not os.path.isdir(r"./output"):
        os.mkdir(r"./output")
    with open(outputFile, "a", encoding="utf-8", newline="") as f:
        csvWrite = csv.writer(f)
        csvWrite.writerow(["网站组织单位", "网站名称", "首页网址"])
        for result in resultList:
            csvWrite.writerow(result)


def findDomain(keyword):
    tmp_keyword  = urllib.parse.quote(keyword)
    tmp_keyword  = urllib.parse.quote(tmp_keyword)
    temp_url = url.format(tmp_keyword)
    res = requests.get(url=temp_url,headers=header,verify=False)
    result = res.text
    a = json.loads(result)
    if a['iTotalDisplayRecords'] > 0 :
        wzmc = a['body'][0]['wzmc']
        wzzgdw = a['body'][0]['wzzgdw']
        wzurl = a['body'][0]['url']
        print(wzzgdw,"--------------",wzmc,"--------------",wzurl)
        result_list.append([wzzgdw,wzmc,wzurl])
    else:
        print(keyword,"--------------")

def batchFindDomain(file):
    list = set()
    count = 0
    with open(file,encoding='utf-8') as lines:
        for line in lines:
            list.add(line.replace('\n',''))
    for keyword in list:
        count += 1
        findDomain(keyword)
        if count == 5:
            time.sleep(60)
            count = 0
           

if __name__ == '__main__':
    parseClass = parseArgs()
    args = parseClass.parse_args()
    batchFindDomain(args.file)
    outputResult(args.file, args.output, result_list)
