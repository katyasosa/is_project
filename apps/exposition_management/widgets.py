from __future__ import unicode_literals

from django.forms import widgets
from django.utils.encoding import force_text
from django.utils.html import mark_safe, format_html


class ImagePicker(widgets.Select):
    def __init__(self, image_field="image", *args, **kwargs):
        self.image_field = image_field
        super(ImagePicker, self).__init__(*args, **kwargs)

    def render_option(self, selected_choices, option_value, option_label):
        option_value = force_text(option_value)
        if option_value in selected_choices:
            selected_html = mark_safe(' selected="selected"')
            if not self.allow_multiple_selected:
                # Only allow for a single selection.
                selected_choices.remove(option_value)
        else:
            selected_html = ''

        # HACK(superbobry): our 'ImageChoiceField' returns a model
        # instance, instead of a "proper" label.
        obj = option_label

        # Make everything ready for 'image-picker.js'.
        image_url = (obj.image.url_200x200 if obj.image else
                     "http://placekitten.com/200/200")
        image_picker_html = mark_safe(' data-img-src="{0}" data-img-label="{1}"'
                                      .format(image_url, obj))
        return format_html('<option value="{0}"{1}{2}>{3}</option>',
                           option_value,
                           selected_html,
                           image_picker_html,
                           force_text(option_label))
