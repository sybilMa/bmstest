from django.shortcuts import render

# Create your views here.
from app01 import models
#第一种：我们一直写的
#路由的第二种写法：
#只要继承了ViewSetMixin  路由的写法
# url(r'^publish/$', views.PublishView.as_view({'get':'list','post':'create'})),
# url(r'^publish/(?P<pk>\d+)$', views.PublishView.as_view({'get':'retrieve','delete':'destroy','put':'update'})),

# 第三种写法（自动生成路由）

from rest_framework.views import  APIView
from rest_framework.response import  Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.status import HTTP_404_NOT_FOUND
from app01 import serializer
from rest_framework.renderers import JSONRenderer,BrowsableAPIRenderer
# class PublishView(ModelViewSet):
#     renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
#     queryset=models.Publish.objects.all()
#     serializer_class=serializer.PublishSerializers

from rest_framework.parsers import JSONParser,FormParser,MultiPartParser
from rest_framework.request import  Request


from rest_framework.versioning import URLPathVersioning


# class Test(APIView):
#     #默认可以解析三种格式
#     versioning_class = URLPathVersioning
#     parser_classes=[JSONParser,]
#
#     def get(self,request,*args,**kwargs):
#         print(request.version)
#         # rest_framework.versioning.URLPathVersioning
#         print(type(request.versioning_scheme))
#         return Response()
#     def post(self,request):
#         print(request.data)
#         print(type(request.data))
#         return Response()

from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination,CursorPagination
class PublishView(APIView):
    versioning_class = URLPathVersioning
    parser_classes=[JSONParser,]
    # def get(self,request,*args,**kwargs):
    #     #批量添加
    #     # ll=[]
    #     # for i in range(100):
    #     #     ll.append(models.Publish(name='%s出版社'%i,city='%s城市'%i))
    #     #
    #     # models.Publish.objects.bulk_create(ll)
    #     #第一种方法，普通分页
    #     #查询出所有数据
    #     ret=models.Publish.objects.all()
    #     #实例化产生一个普通分页对象
    #     page=PageNumberPagination()
    #     #每页显示多少条
    #     page.page_size=3
    #     #查询指定查询哪一页的key值
    #     page.page_query_param='xxx'
    #
    #     #前端控制每页显示多少条的查询key值比如size=9，表示一页显示9条
    #     page.page_size_query_param='size'
    #     #控制每页最大显示多少，size如果传100，最多也是显示10
    #     page.max_page_size=10
    #     ret_page=page.paginate_queryset(ret,request,self)
    #     #序列化
    #     pub_ser=serializer.PublishSerializers(ret_page,many=True)
    #     #去setting中配置每页显示多少条
    #
    #     return Response(pub_ser.data)

    # def get(self, request, *args, **kwargs):
    #     ret = models.Publish.objects.all()
    #     # 实例化产生一个偏移分页对象
    #     page = LimitOffsetPagination()
    #     #四个参数：
    #     #从标杆位置往后取几个，默认取3个，我可以指定
    #     page.default_limit=3
    #     #每次取得条数
    #     page.limit_query_param='limit'
    #     #标杆值，现在偏移到哪个位置，如果offset=6 表示当前在第6条位置上，往后取
    #     page.offset_query_param='offset'
    #     #最大取10条
    #     page.max_limit=10
    #
    #     ret_page = page.paginate_queryset(ret, request, self)
    #     # 序列化
    #     pub_ser = serializer.PublishSerializers(ret_page, many=True)
    #     # 去setting中配置每页显示多少条
    #     return page.get_paginated_response(pub_ser.data)
    #     # return Response(pub_ser.data)

    def get(self, request, *args, **kwargs):
        ret = models.Publish.objects.all()
        # 实例化产生一个偏移分页对象
        page = CursorPagination()
        #三个参数：
        #每页显示的大小
        page.page_size=3
        #查询的key值
        page.cursor_query_param='cursor'
        # 按什么排序
        page.ordering='id'

        ret_page = page.paginate_queryset(ret, request, self)
        # 序列化
        pub_ser = serializer.PublishSerializers(ret_page, many=True)
        # 去setting中配置每页显示多少条
        return page.get_paginated_response(pub_ser.data)
        # return Response(pub_ser.data)

