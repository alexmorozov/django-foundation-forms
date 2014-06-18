django-foundation-forms
=======================
Django templates for Zurb Foundation forms.

Requirements:
* `HamlPy <https://github.com/jessemiller/HamlPy>`_

Example
-------

::
    {% load foundation_forms %}
    ...
    {% form your_form %}

or, to customize field output:

::
    {% load foundation_forms %}
    ...
    {% form_header your_form %}
    {% form_field your_form.some_field %}
    ...
    {% form_field_label your_form.other_field %}
    {% form_field_widget your_form.other_field %}
    ...
    {% form_footer your_form %}

feel free to override default templates for further customization.
