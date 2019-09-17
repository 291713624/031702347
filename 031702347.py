import re
import os
import json
import string
# -*- coding:utf8 -*-
    
with open('pcas.json','r',encoding='UTF-8') as f:
    load_dict=json.load(f)

s=input();
def Get_name(a):
    name=a[2:a.find(',')]
    return name

def Get_number(a):
    now=re.search(r'\d{11}',a)
    if now==None:
        print("手机号码信息异常，请重新输入")
        return None
    number=now.group()
    return number

name=Get_name(s)
i=s.find(',')
if s[0]=='1':
    level=1
    s=s[i+1:len(s)-1]
else:
    level=2
    s=s[i+1:len(s)-1]

number=Get_number(s)
s=re.sub(r'\d{11}','',s)
i=-1
for now in load_dict:
    if now[0:2]==s[0:2]:
        i=1
        if(i+1==len(now)):
                break
        while now[i+1]==s[i+1]:
            i=i+1
            if(i+1==len(now)):
                break
        break
    else:
        now=""
province=now
s=s[i+1:]
i=-1
for now in load_dict[province]:
    if now[0:2]==s[0:2]:
        i=1
        if(i+1==len(now)):
                break
        while now[i+1]==s[i+1]:
            i=i+1
            if(i+1==len(now)):
                break
        break
    else:
        now=""
if province=="北京" or province=="天津" or province=="上海" or province=="重庆":
    city=province+"市"
    if s[0]=="市":
        s=s[1:]
else:
    city=now
s=s[i+1:]
if city=="":
    i=s.find("县")
    area=s[:i+1]
    s=s[i+1:]
    for now in nows in load_dict[province]:
        if now==area:
            citys=now
            break
else:
    citys=city
    i=0
    for now in load_dict[province][citys]:
        j=len(now)
        if now==s[0:j]:
            i=j
            break
        else:
            now=""
    area=now
    s=s[i:]
i=0
if area=="" and load_dict[province][citys].get(citys)!=None:
    for now in load_dict[province][citys][citys]:
        j=len(now)
        if now==s[0:j]:
            i=j
            break
        else:
            now=""
elif area=="" and load_dict[province][citys].get(citys)==None:
    for now in nows in load_dict[province][citys]:
        j=len(now)
        if now==s[0:j]:
            i=j
            break
        else:
            now=""
else:
    for now in load_dict[province][citys][area]:
        j=len(now)
        if now==s[0:j]:
            i=j
            break
        else:
            now=""
street=now
s=s[i:]
if level==1:
    detail=s
    addressbook={
        "姓名":name,
        "手机":number,
        "地址":[
            province,
            city,
            area,
            street,
            detail
            ]
        }
    print(json.dumps(addressbook,ensure_ascii=False))
else:
    if s.find("路")!=-1:
        j=s.find("路")
        road=s[0:j+1]
        s=s[j+1:]
    elif s.find("街")!=-1:
        j=s.find("街")
        road=s[0:j+1]
        s=s[j+1:]
    elif s.find("巷")!=-1:
        j=s.find("巷")
        road=s[0:j+1]
        s=s[j+1:]
    elif s.find("道")!=-1:
        j=s.find("道")
        road=s[0:j+1]
        s=s[j+1:]
    elif s.find("区")!=-1:
        j=s.find("区")
        road=s[0:j+1]
        s=s[j+1:]
    elif s.find("岛")!=-1:
        j=s.find("岛")
        road=s[0:j+1]
        s=s[j+1:]
    elif s.find("线")!=-1:
        j=s.find("线")
        road=s[0:j+1]
        s=s[j+1:]
    elif s.find("桥")!=-1:
        j=s.find("桥")
        road=s[0:j+1]
        s=s[j+1:]
    elif s.find("梁")!=-1:
        j=s.find("梁")
        if s[j-1]=="桥":
            road=s[0:j+1]
            s=s[j+1:]
        else:
            road=""
    else:
        road=""
    if s.find("号")!=-1:
        j=s.find("号")
        door=s[0:j+1]
        if j+1==len(s):
            s=""
        else:
            s=s[j+1:]
    else:
        door=""
    detail=s
    addressbook={
        "姓名":name,
        "手机":number,
        "地址":[
            province,
            city,
            area,
            street,
            road,
            door,
            detail
            ]
        }
    print(json.dumps(addressbook,ensure_ascii=False))