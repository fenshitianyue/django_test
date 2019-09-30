# -*- coding:UTF-8 -*-

from django.http import HttpResponse
from TestModel.models import Test

def insertdb(request):
    test1 = Test(name='firsr data')
    test1.save()
    return HttpResponse("<p>数据添加成功！</p>")

def getdb(request):
    response = ""
    response1 = ""
    # 通过 objects 这个模型管理器的all()来获得所有的数据行
    # 相当于SQL：select * from
    List = Test.objects.all()
    # filter 相当于SQL：where。可以用来设置条件过滤
    response2 = Test.objects.filter(id=1)
    # 获取单个对象
    response3 = Test.objects.get(id=1)
    # 限制返回的数据，相当于SQL：offset 0 limit 2;
    Test.objects.order_by('name')[0:2]
    # 数据排序
    Test.objects.order_by("id")
    # 上面的方法可以连锁使用
    Test.objects.filter(name="hello").order_by("id")
    # 输出所有数据
    for var in List:
        response1 += var.name + " "
    response = response1
    return HttpResponse("<p>" + response + "</p>")



