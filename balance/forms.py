from flask_wtf import FlaskForm
from wtforms import DateField, HiddenField
from wtforms.fields.core import FloatField, RadioField, StringField
from wtforms.fields.simple import SubmitField
from wtforms.validators import DataRequired, Length, NumberRange, ValidationError

import datetime

def validar_fecha(formilario, campo):
    hoy = datetime.date.today()
    if campo.data > hoy:
        raise ValidationError("La fecha no puede ser posterior a hoy - soy externo")


class MovimientoFormulario(FlaskForm):

    id = HiddenField()

    fecha = DateField("Fecha", validators=[DataRequired(message="Debe informar la fecha")])
    concepto = StringField("Concepto", validators=[DataRequired(message="Debe informar el concepto"), Length(min=10)])
    cantidad = FloatField("Cantidad", validators=[DataRequired("Debe informar el monto del movimiento"), 
                                                  NumberRange(message="Debe informar un importe positivo", min=0.01)])
    ingreso_gasto = RadioField(validators=[DataRequired(message="Debe informar el tipo de movimiento")], 
                                            choices=[("G", "Gasto"), ("I", "Ingreso")])
    submit = SubmitField("Aceptar")

    def validate_fecha(self, campo):
        hoy = datetime.date.today()
        if campo.data > hoy:
            raise ValidationError("La fecha no puede ser posterior a hoy - interno")        