# Create your views here.
import time

from django.core.paginator import Paginator
from django.shortcuts import render_to_response

from apps.bill.forms import BillForm
from apps.bill.models import BillEntity


def getItem(id):
    item = BillEntity.objects.get(id=id)

    return item


def index(request):
    pass


def create(request):
    # form = BillForm(request.POST or None)
    #
    # if form.is_valid():
    #     form.save()
    #     form = BillForm()

    if request.method == "GET":
        return create_get(request)

    return create_post(request)


def create_get(request):
    entryDate = time.strftime('%m/%d/%Y', time.localtime(time.time()))
    homeHeaderTitle = entryDate
    return render_to_response("web4mobile/bill/create.html", locals())


def create_post(request):
    pass


def list(request):
    uid = 0
    querySet = BillEntity.objects.filter(User_id=uid)
    paginator = Paginator(querySet, 10)
    page = 1

    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        page = 1

    data = paginator.page(page)

    return render_to_response('web4mobile/bill/list.html', locals())


def details(request, id):
    item = getItem(id)

    return render_to_response('web4mobile/bill/details.html', locals())


def deleted(request, id):
    item = getItem(id)
    BillEntity.delete(item)

    return list(request)


def update(request, id):
    item = getItem(id)

    form = BillForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()

    return render_to_response("web4mobile/bill/update.html", locals())


