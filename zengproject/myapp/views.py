from plistlib import UID
from django.shortcuts import render

# Create your views here.

from myapp.models import student
from datetime import datetime
from django.http import HttpResponse
# Create your views here.

def basic(request):
    return render(request, "space.html")

def callusername(request, username):
    return HttpResponse("Hello, "+  username)

def welcome(request, username):
    if len(username) >= 10:
        if len(username) >= 10:
            Uname_ID = username[-9:]
            Uname = username[:-9]
            Uname_IDL = int(username[-2:])
            if Uname_IDL == 10:
                Uname_IDL = int(10)
            else:
                Uname_IDL = int(username[-1:])
        #109021071曾俊杰
        now = datetime.now()
        food1 = { 'name':'蝦仁滑蛋', 'type':'4.png', 'price':180, 'comment':'好吃', 'is_spicy':False }
        food2 = { 'name':'蒜泥白肉', 'type':'3.png', 'price':160, 'comment':'人氣推薦', 'is_spicy':True }
        food3 = { 'name':'貴妃醉雞', 'type':'1.png', 'price':260, 'comment':'主廚推薦', 'is_spicy':False }
        food4 = { 'name':'客家小炒', 'type':'3.png', 'price':120, 'comment':'主廚推薦', 'is_spicy':False }
        food5 = { 'name':'玫瑰油雞', 'type':'1.png', 'price':180, 'comment':'主廚推薦', 'is_spicy':False }
        food6 = { 'name':'三杯中捲', 'type':'2.png', 'price':260, 'comment':'主廚推薦', 'is_spicy':False }
        food7 = { 'name':'烏骨雞湯', 'type':'1.png', 'price':360, 'comment':'主廚推薦', 'is_spicy':False }
        food8 = { 'name':'麻婆豆腐', 'type':'3.png', 'price':120, 'comment':'主廚推薦', 'is_spicy':True }
        food9 = { 'name':'五更腸旺', 'type':'3.png', 'price':160, 'comment':'主廚推薦', 'is_spicy':True}
        food10 = { 'name':'四喜丸子', 'type':'3.png', 'price':160, 'comment':'主廚推薦', 'is_spicy':False }
        menu = [food1,food2,food3,food4,food5,food6,food7,food8,food9,food10]

        return render(request, "welcome.html", locals())
    else:
        return render(request, "space.html", locals())

def form(request):  
    if request.method == "POST":  
        Cname = request.POST['Uname']
        Cuid =  request.POST['UID']
        Cpassword = request.POST['Password']
        CSex = request.POST['Sex']
        Cagree = request.POST['agree']
        Ccode = request.POST['code']

    else:
        message = '請輸入資料(資料不作驗證)'
    return render(request, "fill.html", locals())

'''
含有以下Form元件：

1. text (姓名/ID)v

2. radio (性別) v

3. checkbox (興趣)

4. submit v

5. Reset v

6. password (10碼)v

'''
