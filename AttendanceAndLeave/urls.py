"""AttendanceAndLeave URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import AdminView
from . import StateCityView
from . import EmployeeVew
from . import Attendance

urlpatterns = [
    #ForAdmin
    path('admin/', admin.site.urls),
    path('adminlogin/',AdminView.AdminLogin),
    path('checkadminlogin',AdminView.CheckAdminLogin),
    path('admindashboard/',EmployeeVew.DisplayAll),
    path('adminlogout/',AdminView.AdminLogut),

    #ForEmployee
    path('employeelogin/',EmployeeVew.EmployeeLogin),
    path('checkemployeelogin',EmployeeVew.CheckEmployeeLogin),
    path('employeeregister/',EmployeeVew.EmployeeRegister),
    path('employeedashboard/',EmployeeVew.EmployeeDashboard),
    path('employeesubmit',EmployeeVew.EmployeeSubmit),
    path('employeelogout/',EmployeeVew.EmployeeLogout),

    #ForAttendance
    path('attendance/',Attendance.Attendance),
    path('markattendance',Attendance.MarkAttendance),
    path('viewattendance/',Attendance.DisplayAttendance),

    path('fetchallstates/',StateCityView.FetchAllStates),
    path('fetchallcities/',StateCityView.FetchAllCities)
]
