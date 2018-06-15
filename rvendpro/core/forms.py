from crispy_forms.helper import FormHelper 
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
from crispy_forms.bootstrap import FormActions, InlineField, StrictButton

class TabVendProFormHelper(FormHelper):    
    form_id = 'tabvendpro-search-form'
    form_class = 'form-inline'
    field_template = 'bootstrap3/layout/inline_field.html'
    field_class = 'col-xs-3'
    label_class = 'col-xs-3'
    form_show_errors = True
    help_text_inline = False
    html5_required = True
    layout = Layout(
                Fieldset(
                    '<i class="fa fa-search"></i> Busca Registros RVendPro',       
                    InlineField('cd_almoxarifado'),
                    InlineField('dt_venda'),
                ),
                FormActions(
                    StrictButton(
                        '<i class="fa fa-search"></i> Buscar', 
                        type='submit',
                        css_class='btn-primary',
                        style='margin-top:10px;')
                )
    )

