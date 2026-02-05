from wtforms import Form
from wtforms import StringField, IntegerField, PasswordField, RadioField
from wtforms import EmailField
from wtforms import validators
from wtforms import Form, IntegerField, StringField, RadioField
from wtforms.validators import DataRequired, NumberRange


# class UserFormd(Form):
#     x1=IntegerField('x1')


class UserForm(Form):
    matricula=IntegerField('Matricula', [validators.DataRequired(message="El campo es requerido"),
                                        validators.NumberRange(min=100, max=1000, message='Ingrese un valor valido')
                                        ])
    nombre=StringField('Nombre', [validators.DataRequired(message="El campo es requerido"),
                                        validators.length(min=3, max=10, message='Ingrese nombre valido')
                                        ])
    apaterno=StringField('Apaterno',[validators.DataRequired(message="El campo es requerido")
                                        ])
    amaterno=StringField('Amaterno',[validators.DataRequired(message="El campo es requerido")
                                        ])
    correo=EmailField('Correo',[validators.Email(message="Ingrese un correo valido")
                                        ])


# class UserFormc(Form):
#     nombre=StringField('Nombre', [validators.DataRequired(message="El campo es requerido"),
#                                         validators.DataRequired(message='El campo es requerido')
#                                         ])
#     cantidad=IntegerField('Cantidad', [validators.DataRequired(message="El campo es requerido"),
#                                         validators.NumberRange(min=1, max=7, message='Ingrese un número válido')
#                                         ])
#     cineco=RadioField('Cineco',[validators.DataRequired(message="El campo es requerido")
#                                         ],
#                                 choices=[('SI','Si'),('NO','No')],
#                                         default='NO')



class UserFormc(Form):
    nombre = StringField(
        'Nombre',
        validators=[DataRequired(message="El campo es requerido")]
    )

    compradores = IntegerField(
        'Cantidad de compradores',
        validators=[
            DataRequired(message="El campo es requerido"),
            NumberRange(min=1, message="Debe haber al menos 1 comprador")
        ]
    )

    cantidad = IntegerField(
        'Cantidad de boletos',
        validators=[
            DataRequired(message="El campo es requerido"),
            NumberRange(min=1, message="Cantidad inválida")
        ]
    )

    cineco = RadioField(
        'Cineco',
        validators=[DataRequired(message="Seleccione una opción")],
        choices=[('si', 'Sí'), ('no', 'No')],
        default='no'
    )


