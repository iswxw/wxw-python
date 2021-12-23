#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/19 01:53
# @Author  : wxw
# @Site    : 
# @File    : buildjson.py

"""
一、第一部分为: Json格式与python对象的相互转换
"""

import json

# 普通的json单列表
jsondata = '''
{
    "Uin":0,
    "UserName":"@c482d142bc698bc3971d9f8c26335c5c",
    "NickName":"CSDNzoutao",
    "HeadImgUrl":"https://blog.csdn.net/ITBigGod",
    "DisplayName":"ZouTao",
    "ChatRoomId":0,
    "KeyWord":"che",
    "EncryChatRoomId":"",
    "IsOwner":0
}
'''

myfriend = json.loads(jsondata)  # json转化字典对象
print(myfriend)
# 转为字典以后，就可以根据key来获取各种字段数值了
name = myfriend.get('NickName')
print(name)
# json.dumps(name) #将python对象转化为json

# 常见的还有 Json 数组-嵌套型
Json_doc = '''
    {
        "MemberList": [{
                "UserName": "CSDNzoutao",
                "Sex": "男",
                "Age":10
            },
            {
                "UserName": "CSDNzoutao的1号女朋友",
                "Sex": "女",
                "Age":10
            },
            {
                "UserName": "CSDNzoutao的2号女朋友",
                "Sex": "不限",
                "Age":10
            }]
    }
    '''

myfriends = json.loads(Json_doc)
memberList = myfriends.get('MemberList')  # 得到list对象-包含字典数据
print(memberList)

# 　用个 for 循环就能轻而易举的获取数据
for x in memberList:
    print('遍历list数据：', x)
