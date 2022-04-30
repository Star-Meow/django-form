from django.shortcuts import render,redirect
from myapp.forms import PostForm
from email import message


from myapp.models import student2
from datetime import datetime
from django.http import HttpResponse
# Create your views here.

def is_valid(self):
    """Return True if the form has no errors, or False otherwise."""
    return self.is_bound and not self.errors

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

def delete2(request,name=None):  #刪除資料
	if name !=None:
		if request.method == "POST":  #如果是以POST方式才處理
			name =request.POST['cName'] #取得表單輸入的編號
		try:
			unit = student2.objects.get(cName = name)
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
        postform = PostForm(request.POST) 
        if postform.is_valid():	
            cName = postform.cleaned_data['cName'] 
            cSex =  postform.cleaned_data['cSex']
            cUID = postform.cleaned_data['cUID']
            cBirthday =  postform.cleaned_data['cBirthday']
            cEmail = postform.cleaned_data['cEmail']
            cPhone =  postform.cleaned_data['cPhone']
            cAddr =  postform.cleaned_data['cAddr']
            #新增一筆記錄
            unit = student2.objects.create(cName=cName, cSex=cSex,cUID=cUID, cBirthday=cBirthday, cEmail=cEmail,cPhone=cPhone, cAddr=cAddr) 
            unit.save()  #寫入資料庫
            return redirect('/index/')
    else:
        message = 'stop'
        postform = PostForm()
    return render(request, "dtform.html", locals())	

def edit(request,id=None,mode=None):
    if mode == "load":  
        unit = student2.objects.get(id=id)  
        strdate=str(unit.cBirthday)
        strdate2=strdate.replace("年","-")
        strdate2=strdate.replace("月","-")
        strdate2=strdate.replace("日","-")
        unit.cBirthday = strdate2		
        return render(request, "edit.html", locals())
    elif mode == "edit":			
        unit = student2.objects.get(id=id)  	
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
    return render(request, "postform.html", locals())
'''
def set_cookie(request,key=None,value=None):
    response = HttpResponse('Cookie儲存完畢')
    response.set_cookie(key,value)
    return response

def set_cookie2(request,key=None,value=None):
	response = HttpResponse('Cookie 有效時間1小時!')
	response.set_cookie(key,value,max_age=3600)
	return response	

def get_cookie(request,key=None):
	if key in request.COOKIES:
		return HttpResponse('%s : %s' %(key,request.COOKIES[key]))
	else:
		return HttpResponse('Cookie 不存在!')	

def get_allcookie(request):
    if request.COOKIES!= None:
        strcookie = ''
        for key1 , value1 in request.COOKIES.items():
            strcookie = strcookie + key1 + ":" + value1 + "<br>"
        return HttpResponse('%s' %(strcookie))
    else:
        return HttpResponse('cookie 不存在')
    
def delete_cookie(request,key=None):
	if key in request.COOKIES:
		response = HttpResponse('Delete Cookie: '+key)	
		response.delete_cookie(key)
		return response

def time_cookie(request):
	if "counter" in request.COOKIES:
		counter=int(request.COOKIES["counter"])
		counter+=1
	else:		
		counter=1
	response = HttpResponse('今日瀏覽次數：' + str(counter))		
	tomorrow = datetime.now() + datetime.timedelta(days = 1)
	tomorrow = datetime.replace(tomorrow, hour=0, minute=0, second=0)
	expires = datetime.strftime(tomorrow, "%a, %d-%b-%Y %H:%M:%S GMT") 
	response.set_cookie("counter",counter,expires=expires)
	return response	

def set_session(request,key=None,value=None):
	response = HttpResponse('Session 儲存完畢!')
	request.session[key]=value
	return response

def set_session2(request,key=None,value=None):
	response = HttpResponse('Session 儲存完畢!')
	request.session[key]=value
	request.session.set_expiry(30) # 設持續的時間為30秒
	return response

def get_session(request,key=None):
	if key in request.session:
		return HttpResponse('%s : %s' %(key,request.session[key]))
	else:
		return HttpResponse('Session 不存在!')

def get_allsession(request):
	if request.session!=None:
		strsessions=""
		for key1,value1 in request.session.items():
			strsessions= strsessions + key1 + ":" + str(value1) + "<br>"
		return HttpResponse(strsessions)
	else:
		return 	

def delete_session(request,key=None):
	if key in request.session:
		response = HttpResponse('Delete Session: '+key)	
		del request.session[key]#刪除某一 Session
		return response
	else:
		return HttpResponse('No Session:' + key)

def kill_allsession(request):
    request.session.clear()
    return HttpResponse('Session 已清空')

def login(request):
	#預設帳號密碼
    username = "star"
    password = "109021071"
    if request.method == 'POST':
        if not 'username' in request.session:
            if request.POST['username']==username and request.POST['password']==password:
                request.session['username']=username #儲存Session
                message=username + " 您好，登入成功！"
                status="login"
    else:
        if 'username' in request.session:
            if request.session['username']==username:
                message=request.session['username'] + " 您已登入過了！"
                status="login"			
    return render(request, 'login.html',locals())
	
def logout(request):
	if 'username' in request.session:
		message=request.session['username'] + ' 您已登出!'
		del request.session['username']	#刪除Session	
	return render(request, 'login.html',locals())

def register(request,key=None,value=None):
    if request.method == "POST":
        request.session[key] = request.POST['password'] 
        password = request.POST['username']  
    return render(request, 'register.html',locals())
'''