from __future__ import unicode_literals

from django import forms
from django.utils.html import conditional_escape, mark_safe


class ImageChoiceField(forms.ModelChoiceField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("empty_label", None)
        kwargs.setdefault("widget", forms.RadioSelect)
        super(ImageChoiceField, self).__init__(*args, **kwargs)

    def label_from_instance(self, obj):
        if obj.image:
            image = conditional_escape(obj.image.url_200x200)
        else:
            image = "http://placekitten.com/200/200"

        title = conditional_escape(obj)
        return mark_safe(
            """<span class="thumbnail">
                 <img src="{0}" alt="{1}" />
                 <span class="caption">{1}</span>
               </span>""".format(image, title))
