from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import Http404

# Create your views here.
from celery.result import AsyncResult

from tools.tasks import add
from .models import Add
# from tools.db import Db
import datetime


def add_1(request):
    first = int(request.POST.get('add1'))
    second = int(request.POST.get('add2'))
    result = add.delay(first, second)
    dd = Add(task_id=result.id, first=first, second=second,
             log_date=datetime.datetime.now())
    dd.save()
    return HttpResponseRedirect("/")


# 任务结果
def result(request):
    # 查询所有的任务信息
    # db = Db()
    # rows = db.get_tasksinfo()
    # return render_to_response('result.html', {'rows': rows})
    raise Http404("Not Support for now")
