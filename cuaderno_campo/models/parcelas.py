from odoo import models, api, fields


class parcelas(models.Model):
    _name = 'cc.parcelas'

    codigo_provincia = fields.Char(
        string='Código Provincia',
        required=True,
        help='Escriba el código de pronvincia. Ej: 02 para Albacete',
        size=2
    )

    codigo_municipio = fields.Char(
        string='Código Municipio',
        help='Escriba el código del municipio. Ej: 069 para La Roda',
        required=True,
        size=3
    )

    name = fields.Char(
        string='Municipio',
        required=True,
        help='Escriba el nombre del municipio'
    )

    codigo = fields.Char(
        string='Identificación',
        required=False,
        help='Nombre de la finca, paraje, entorno, etc donde se encuentra la parcela'
    )

    agregado = fields.Integer(
        string='Agregado',
        help='Agregado (no obligatorio)'
    )

    zona = fields.Integer(
        string='Zona',
        help='Zona (no obligatorio)'
    )

    poligono = fields.Integer(
        string='Polígono',
        required=True,
        help='Nº polígono'
    )

    parcela = fields.Integer(
        string='Parcela',
        required=True,
        help='Nº de parcela'
    )

    recinto = fields.Integer(
        string='Recinto',
        required=True,
        help='Nº de recinto'
    )

    uso = fields.Char(
        string='Uso SIGPAC',
        required=True,
        help='Familia de cultivos indicada en el SIGPAC para la parcela indicada'
    )

    superficie = fields.Float(
        string='Superficie SIGPAC (ha)',
        required=True,
        help='Superficie en hectáreas indicada en el SIGPAC para la parcela'
    )

    superficie_cultivada = fields.Float(
        string='Superficie cultivada',
        required=True,
        help='Superficie real cultivada en la parcela'
    )

    especie = fields.Char(
        string='Especie',
        required=True,
        help='Especie cultivada. Ejemplo: Arroz'
    )

    variedad = fields.Char(
        string='Variedad',
        required=True,
        help='Variedad relativa a la especie cultivada. Ejemplo: Bomba'
    )

    riego = fields.Selection(
        string='Sistema de cultivo (Secano/Regadío)',
        selection=[
            ('1', 'Secano'),
            ('2', 'Aspersión'),
            ('3', 'Goteo o localizado'),
            ('4', 'Gravedad'),
        ],
        required=True,
        help='Sistema de cultivo respecto al sistema de regadío'
    )

    estructura = fields.Selection(
        string='Aire libre/Protegido',
        selection=[
            ('1', 'Aire libre'),
            ('2', 'Malla'),
            ('3', 'Cubierta bajo plástico'),
            ('4', 'Invernadero'),
        ],
        required=True,
        help='Estructura respecto al sistema de cultivo'
    )

    asesoramiento = fields.Selection(
        string='Sistema de asesoramiento',
        selection=[
            ('1', 'Agricultura ecológica'),
            ('2', 'Producción Integrada'),
            ('3', 'Certificación Privada'),
            ('4', 'Agrupación de Tratamiento Integrado en Agricultura'),
            ('5', 'Asistida de un asesor'),
            ('6', 'Sin obligación de aplicar GIP')
        ],
        required=True,
        help='Sistema de asesoramiento en gestión integrada de plagas'
    )
