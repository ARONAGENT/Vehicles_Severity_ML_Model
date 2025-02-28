from django.shortcuts import render
import joblib

def home(request):
    return render(request,"index.html")

def modelformrequest(request):
    if request.method=="POST":
        dic={}
        speed=int(request.POST.get('speed'))
        weather=int(request.POST.get('weather'))
        rtype=int(request.POST.get('road_type'))
        day_time=int(request.POST.get('time_of_day'))
        vtype=int(request.POST.get('vehicle_type'))
        tdensity=int(request.POST.get('traffic_density'))

        model=joblib.load('accident_ready.joblib')

        result=model.predict([[speed,weather,rtype,day_time,vtype,tdensity]])
        dic['result']=result[0]
    return render(request,"modelresponse.html",dic)

