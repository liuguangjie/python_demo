# -*-coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

from dss.Serializer import serializer
# Create your views here.
from api.models import User

"""
列出 用户
"""
def list_user(request):
    users = User.objects.all()

    lists = []

    for u in users:
        d = {}
        d['username'] = u.username
        d['userId'] = u.user_id
        lists.append(d)
    data = {
        "code": 200,
        "msg": "ok",
        "data": lists,
    }
    jsonString = serializer(data=data, output_type="json", foreign=False)
    print(jsonString)
    response = HttpResponse(
        # json.dumps(dataa, cls=MyEncoder),
        jsonString,
        content_type="application/json;charset=utf-8",
    )
    response["Access-Control-Allow-Origin"] = "*"
    return response


def multi_datasource(request):
    from django.db import connection, transaction
    """
        不用模型 直接 用sql语句 形式
        django.db.connection：代表默认的数据库连接
        django.db.transaction ：代表默认数据库事务（transaction）
        用database connection调用 connection.cursor() 得到一个游标(cursor)对象。
        然后调用 cursor.execute(sql, [params]) 执行SQL
        cursor.fetchone() 或者 cursor.fetchall()： 返回结果行

        如果执行修改操作，则调用 transaction.commit_unless_managed()来保证你的更改提交到数据库。


    """
    cursor = connection.cursor()

    cursor.execute("select menu_id, name, type  from sys_menu limit 2")

    row = cursor.fetchall()
    views_list = []
    fields = ["menuId", "name", "type"]
    for s in row:
        d = {}
        index = 0
        for r in s:
            d[fields[index]] = r
            index += 1
        views_list.append(d)

    cursor.close()
    return render(request, "test.html", {"data": views_list})



