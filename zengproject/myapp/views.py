from myapp.forms import PostForm
from email import message
from django.shortcuts import render,redirect

# Create your views here.

from myapp.models import student2
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

def index(request):  
    students = student2.objects.all().order_by('id')  #讀取資料表, 依 id 遞增排序
    return render(request, "index.html", locals())	

def delete(request,id=None):  #刪除資料
	if id!=None:
		if request.method == "POST":  #如果是以POST方式才處理
			id=request.POST['cId'] #取得表單輸入的編號
		try:
			unit = student2.objects.get(id=id)
			unit.delete()
			return redirect('/index/')
		except:
			message = "讀取錯誤!"			
	return render(request, "delete.html", locals())	


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


def dtform(request):  
    if request.method == "POST":	 
        cName = request.POST['cName'] 
        cSex =  request.POST['cSex']
        cUID = request.POST['UID']
        cBirthday =  request.POST['cBirthday']
        cEmail = request.POST['cEmail']
        cPhone =  request.POST['cPhone']
        cAddr =  request.POST['cAddr']
        #新增一筆記錄
        unit = student2.objects.create(cName=cName, cSex=cSex,cUID=cUID, cBirthday=cBirthday, cEmail=cEmail,cPhone=cPhone, cAddr=cAddr) 
        unit.save()  #寫入資料庫
        return redirect('/index/')
    else:
        message = 'stop'
    return render(request, "dtform.html", locals())	


def edit(request,id=None,mode=None):
    if mode == "load":  # 由 index.html 按 編輯二 鈕
        unit = student2.objects.get(id=id)  #取得要修改的資料記
        strdate=str(unit.cBirthday)
        strdate2=strdate.replace("年","-")
        strdate2=strdate.replace("月","-")
        strdate2=strdate.replace("日","-")
        unit.cBirthday = strdate2		
        return render(request, "edit.html", locals())
    elif mode == "edit": # 由 edit2.html 按 submit		
        unit = student2.objects.get(id=id)  #取得要修改的資料記錄	
        unit.cName=request.POST['cName']
        unit.cSex=request.POST['cSex']
        unit.cUID = request.POST['UID']
        unit.cBirthday=request.POST['cBirthday']
        unit.cEmail=request.POST['cEmail']
        unit.cPhone=request.POST['cPhone']
        unit.cAddr=request.POST['cAddr']		
        unit.save()  #寫入資料庫
        message = '已修改...'
    return redirect('/index/')


def postform(request):
    postform = PostForm()
