# -*- coding:utf-8 -*-
from django import forms

from apps.bill.models import BillEntity
from apps.common.utils import isNoneOrEmpty

__author__ = 'ngnono'


class BillForm(forms.ModelForm):
    class Meta:
        model = BillEntity

    def __init__(self, *args, **kwargs):
        super(BillForm, self).__init__(*args, **kwargs)

    def clean_price(self):
        price = self.cleaned_data["price"]
        if price < 0:
            raise forms.ValidationError("价格必须大于零")
        return price

    def clean_title(self):
        title = str(self.cleaned_data["title"])
        if isNoneOrEmpty(title):
            raise forms.ValidationError("标题不能为空")

        return title