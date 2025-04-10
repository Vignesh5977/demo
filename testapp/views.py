from itertools import groupby
from operator import itemgetter
from django.shortcuts import render
from django.http import HttpResponse
from .form import datafrom
from rest_framework.views import APIView
from rest_framework.response import Response
from .serial import *
# Create your views here.

# class demo(APIView):
#     def post(request):
#         serials=dataserial(data=request.data)
#         if serials.is_valid():
#             serials.save()
#         return Response(serials.data)
def demo(request):
    if request.method =='POST':
        form=datafrom(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("save")
        else:
             print(form.errors)
             return render(request,"index.html",{'form':form})     
    else:         
        form= datafrom()
        return render(request,"index.html",{'form':form})  

class orderview(APIView):
    def post(self,request):
        #  name = request.data.get("name")
        #  orderQty = request.data.get("orderQty")
        #  sellQty=request.data.get("sellQty")
        #  dataStore = order(name=name,orderQty=orderQty,sellQty=sellQty)
        #  dataStore.save()
        #  return Response("save order")
         serial=orderserial(data=request.data)
         if serial.is_valid():
             serial.save()
             return Response("save order")
         else:
             return Response(serial.errors)
         
    def get(self,request):
        data=order.objects.order_by('name')
        datalist=orderserial(data,many=True).data
        # groupdata = groupby(datalist, key=itemgetter('name'))
        output=[]    
        a,b=0,0
        for x in range(len(datalist)):
            if x < len(datalist)-1:
                if datalist[x]['name'] == datalist[x+1]['name']:
                    output.append(datalist[x])
                    a+=datalist[x]['orderQty']
                    b+=datalist[x]['sellQty']
                else:
                     output.append(datalist[x])
                     a+=datalist[x]['orderQty']
                     b+=datalist[x]['sellQty']   
                     output.append({
                            'total order qty':a ,
                            'total sell qty ': b
                        })
                     a,b=0,0
            elif x == len(datalist)-1:
                 output.append(datalist[x])
                 a+=datalist[x]['orderQty']
                 b+=datalist[x]['sellQty']   
                 output.append({
                    'total order qty':a ,
                    'total sell qty ':b
                })   
                
        return Response(output)    
          
              