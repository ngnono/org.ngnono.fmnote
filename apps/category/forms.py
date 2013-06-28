# -*- coding:utf-8 -*-
from django import forms
from apps.bill.models import CategoryEntity
from apps.common.utils import isNoneOrEmpty

__author__ = 'ngnono'


class CategoryForm(forms.ModelForm):
    class Meta:
        model = CategoryEntity
        fields = ['Name', 'Description']

    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)

    def clean_Name(self):
        Name = str(self.cleaned_data["name"])

        if Name.startswith('a'):
            raise forms.ValidationError(" baohan ale ")

        if isNoneOrEmpty(Name):
            raise forms.ValidationError("名称不能为空（大写）")

        return Name

    def clean(self):


