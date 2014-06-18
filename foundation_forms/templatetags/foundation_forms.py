#--coding: utf8--

from django import forms
from django import template
from django.utils.translation import ugettext as _

register = template.Library()


@register.filter
def is_checkbox(field):
    return isinstance(field.field.widget, forms.CheckboxInput)


@register.inclusion_tag('foundation_forms/form.html')
def form(form, **kwargs):
    defaults = {'form': form,
                'submit_title': _('Save')}
    defaults.update(kwargs)
    return defaults


@register.inclusion_tag('foundation_forms/form_header.html')
def form_header(form, **kwargs):
    kwargs.update({'form': form})
    return kwargs


@register.inclusion_tag('foundation_forms/form_fields.html')
def form_fields(form, **kwargs):
    kwargs.update({'form': form})
    return kwargs


@register.inclusion_tag('foundation_forms/form_footer.html')
def form_footer(form, **kwargs):
    defaults = {'form': form,
                'submit_title': _('Save')}
    defaults.update(kwargs)
    return defaults


@register.inclusion_tag('foundation_forms/form_field.html')
def form_field(field, **kwargs):
    kwargs.update({'field': field})
    return kwargs


@register.inclusion_tag('foundation_forms/form_field_label.html')
def form_field_label(field, **kwargs):
    kwargs.update({'field': field})
    return kwargs


@register.inclusion_tag('foundation_forms/form_field_widget.html')
def form_field_widget(field, **kwargs):
    kwargs.update({'field': field})
    return kwargs
