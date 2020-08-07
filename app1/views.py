import json

from django.contrib import messages
from django.shortcuts import render,redirect

# Create your views here.
from yashIMDB.settings import IMDB_FILE


def adminloginpage(request):
    return render(request,"admin_L_page.html")


def adminhomep(request):
    user_name=request.POST.get("y1")
    passwd=request.POST.get("y2")
    if user_name == "yash" and passwd == "kumar2280":
        return render(request,"adminwelcom.html",{"data":user_name})
    else:
        messages.error("invalid user JAI MATA DI")
        return redirect('main')


def adminwelcomepage(request):
    dict_data = json.loads(open(IMDB_FILE).read())
    print(dict_data)
    # id = [x for x in dict_data]
    return render(request, "adminwelcom.html", {'data': dict_data})


def openmovie(request):
    movid = request.GET.get("id")
    dict_data = json.loads(open(IMDB_FILE).read())
    return render(request, "actor.html", {"idi": movid, "result": dict_data[movid]})


def test(request):
    dict_data = json.loads(open(IMDB_FILE).read())
    print(dict_data)

    return render(request, "test.html", {'data': dict_data})
