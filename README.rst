django-foundation-forms
=======================
Django templates for Zurb Foundation forms.

This module provides some template tags to make it easier to deal with forms
markup. In contrast to the (excellent)
`crispy-forms <https://github.com/maraujop/django-crispy-forms>`_ app,
foundation-forms doesn`t move the presentational layer to your Python code -
just plain ol` templates.

You have the following template tags (nesting shows structure):

* {% form %}

  * {% form_header %}

  * {% form_fields %}

    * {% form_field %}

      * {% form_field_label %}
      * {% form_field_widget %}
  * {% form_footer %}

Requirements:

* `HamlPy <https://github.com/jessemiller/HamlPy>`_

Example
-------

If you want to output the whole form, just do:

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
