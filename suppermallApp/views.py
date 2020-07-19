#utf-8
from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
import json

from .models import HomeGoods,Banner,Recommend
# 可以将model对象转换为字典
from django.forms.models import  model_to_dict

# Create your views here.

def addGoods(request):
    return HttpResponse('正在添加')

def getGoods(request):
    def fengzhuang(qryObj):
        data_list = []
        for i in qryObj:
            data_dict = {}
            data_dict['id']=i.id
            data_dict['GoodsName'] = i.GoodsName
            data_dict['GoodsPhoto'] = i.GoodsPhoto
            data_dict['GoodsPrice'] = i.GoodsPrice
            data_dict['Page'] = i.Page
            data_dict['CollectionCount'] = i.CollectionCount
            data_list.append(data_dict)
        return  data_list

    if request.method == "GET":
        page = request.GET["Page"]
        qryObj = HomeGoods.objects.filter(Page=page)
        data_list = fengzhuang(qryObj)
        data_dict = {}
        data_dict['data']=data_list
        data_json = json.dumps(data_dict,ensure_ascii=False)
        response = HttpResponse(data_json)
        response["Access-Control-Allow-Origin"] = "*"
        response["Content-Type"] = "application/json"
        return response

def getBanner(request):
    def fengzhuang(qryObj):
        data_list = []
        for i in qryObj:
            data_dict = model_to_dict(i)
            data_list.append(data_dict)
        return data_list

    if request.method == "GET":
        qryObject1 =  Banner.objects.all()
        qryObject2 = Recommend.objects.all()
        banner_list = fengzhuang(qryObject1)
        recommend_list = fengzhuang(qryObject2)
        data ={}
        data['banner'] = banner_list
        data['recommend'] = recommend_list
        data_json = json.dumps(data, ensure_ascii=False)
        response = HttpResponse(data_json)
        response["Access-Control-Allow-Origin"] = "*"
        response["Content-Type"] = "application/json"
        return response






