from __future__ import absolute_import, unicode_literals

from django import forms

from .widgets import ImagePicker


class ImageChoiceField(forms.ModelChoiceField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("empty_label", None)
        kwargs.setdefault("widget", ImagePicker)
        super(ImageChoiceField, self).__init__(*args, **kwargs)

    def label_from_instance(self, obj):
        return obj