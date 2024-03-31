from odoo import models, api, fields


class cc_aplicadores(models.Model):
    _name = 'cc.aplicadores'
    
    
    nombre = fields.Char(
        string='Nombre',
        required=True,
        help='Escriba el nombre de la persona inscrita en el ROPO'
    )
    
    
    name = fields.Char(
        string='Apellidos',
        required=True,
        help='Escriba los apellidos de la persona inscrita en el ROPO'
        
    )
    
    numero_inscripcion = fields.Char(
        string='Nº inscripción ROPO',
        help="Escriba el número de inscripción en el ROPO")

    dni_nif = fields.Char(
        string='DNI/NIF',
        size=9,
        required=True,
        help="Escriba el número de DNI o NIF"
    )

    carnet = fields.Selection(
        string='Carnet',
        selection=[
            ('1', 'Básico'),
            ('2', 'Cualificado'),
            ('3', 'Fumigador'),
            ('4', 'Piloto')
        ]
    )
    
    asesor = fields.Boolean(
        string='Asesor',
        help='Indica si la persona que realiza el tratamiento también tiene puede realizar las labores de asesoria'
    )
    
    tratamiento = fields.One2many(
        comodel_name='cc.tratamientos',
        inverse_name='aplicador',
        string='Tratamientos'
    )
    
    asesoria = fields.One2many(
        comodel_name='cc.tratamientos',
        inverse_name='asesor'
    )
    
