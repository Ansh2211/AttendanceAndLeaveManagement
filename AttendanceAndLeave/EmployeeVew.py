from django.shortcuts import render
from . import Pool
from . import PoolDict
import uuid
import random


def EmployeeLogin(request):
    try:
        result = request.session['EMPLOYEE']
        return render(request, 'EmployeeDashboard.html', {'result': result})
    except Exception as e:
        return render(request, 'EmployeeLogin.html')


def CheckEmployeeLogin(request):
    try:
        email = request.POST['email']
        password = request.POST['password']
        db, cmd = PoolDict.ConnectionPool()
        q = "select * from employeepbl where email='{}' and password='{}'".format(email, password)
        cmd.execute(q)
        result = cmd.fetchone()
        print(result)
        if(result):
            request.session['EMPLOYEE']=result
            return render(request, 'EmployeeDashboard.html', {'result': result})
        else:
            return render(request, 'EmployeeLogin.html', {'result': result,'msg':'Invalid Email/Password'})
        db.close()
        return render(request, 'EmployeeDashboard.html', {'result': result})
    except Exception as e:
        print(e)
        return render(request, 'EmployeeLogin.html', {'result': {},'msg':'Server Error '})


def EmployeeLogout(request):
    del request.session['EMPLOYEE']
    return render(request,'EmployeeLogin.html')


def EmployeeDashboard(request):
    result=request.session['EMPLOYEE']
    return render(request,"EmployeeDashboard.html",{'result':result})


def EmployeeRegister(request):
    try:
        result=request.session['ADMIN']
        return render(request,'EmployeeRegister.html')

    except Exception as e:
        return render(request, 'AdminLogin.html')


def EmployeeSubmit(request):
    try:
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        gender=request.POST['gender']
        birthdate=request.POST['birthdate']
        paddress=request.POST['paddress']
        states=request.POST['states']
        city=request.POST['city']
        caddress=request.POST['caddress']
        emailaddress=request.POST['emailaddress']
        mobilenumber=request.POST['mobilenumber']
        designation=request.POST['designation']

        picture=request.FILES['picture']
        filename=str(uuid.uuid4())+picture.name[picture.name.rfind('.'):]
        password="".join(random.sample(['1','5','a','x','@','#','66','r'],k=6))
        q="insert into employeepbl(firstname, lastname, gender, dob, paddress, stateid, cityid, caddress, email, mobileno, designation, picture, password)values('{}','{}','{}','{}','{}',{},{},'{}','{}','{}','{}','{}','{}')".format(firstname,lastname,gender,birthdate,paddress,states,city,caddress,emailaddress,mobilenumber,designation,filename,password)
        db,cmd=Pool.ConnectionPool()
        cmd.execute(q)
        db.commit()
        F=open("D:/AttendanceAndLeave/assets/"+filename,"wb")
        for chunk in picture.chunks():
            F.write(chunk)
        F.close()
        db.close()
        return render(request, 'EmployeeRegister.html',{'msg':'Record Submitted Successfully'})


    except Exception as e:
        print("Error:",e)
        return render(request, 'EmployeeRegister.html',{'msg':'Failed To Submit Record'})

def DisplayAll(request):
    try:
        db, cmd = Pool.ConnectionPool()
        q="select E.*,(select C.cityname from cities C where C.cityid=E.cityid),(select S.statename from states S where S.stateid=E.stateid) from employeepbl E"
        cmd.execute(q)
        rows=cmd.fetchall()
        db.close()
        result = request.session['ADMIN']
        return render(request, 'AdminDashboard.html', {'rows':rows})

    except Exception as e:
        return render(request, 'AdminLogin.html', {'rows': []})

def DisplayByID(request):
    empid=request.GET['empid']
    try:
        db, cmd = Pool.ConnectionPool()
        q="select E.*,(select C.cityname from cities C where C.cityid=E.cityid),(select S.statename from states S where S.stateid=E.stateid) from employeepbl E where employeeid={}".format(empid)
        cmd.execute(q)
        row=cmd.fetchone()
        db.close()
        return render(request, 'EmployeeDashboard.html', {'row': row})

    except Exception as e:
        return render(request, 'EmployeeDashboard.html', {'rows': []})
