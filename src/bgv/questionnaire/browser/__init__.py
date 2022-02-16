from reiter.ui import TemplateLoader


import wtforms

from wtforms import widgets, SelectMultipleField


TEMPLATES = TemplateLoader("./templates")


class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()


class FormMeta(wtforms.meta.DefaultMeta):

    locales = ["de_DE", "de"]

    def render_field(inst, field, render_kw):
        if isinstance(field, MultiCheckboxField):
            class_ = "form-check"
        elif isinstance(field, wtforms.fields.BooleanField):
            class_ = "form-check"
        elif isinstance(field, wtforms.fields.SelectFieldBase._Option):
            class_ = "form-check-input"
        elif isinstance(field, wtforms.fields.RadioField):
            class_ = "form-check"
        else:
            class_ = "form-control"
        if field.errors:
            class_ += " is-invalid"
        render_kw.update({"class_": class_})
        if hasattr(field, "render_kw"):
            if field.render_kw:
                render_kw.update(field.render_kw)
        return field.widget(field, **render_kw)


class Form(wtforms.Form):
    Meta = FormMeta
