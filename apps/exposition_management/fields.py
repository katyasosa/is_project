# coding=utf-8
from __future__ import absolute_import, unicode_literals

from django import forms


class ImageChoiceField(forms.ModelChoiceField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("empty_label", None)
        super(ImageChoiceField, self).__init__(*args, **kwargs)

    def label_from_instance(self, obj):
        return obj

class ImageMultipleChoiceField(forms.ModelMultipleChoiceField):
    def __init__(self, *args, **kwargs):
        super(ImageMultipleChoiceField, self).__init__(*args, **kwargs)

    def label_from_instance(self, obj):
        return obj
