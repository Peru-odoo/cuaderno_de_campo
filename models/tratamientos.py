from odoo import models, fields, api

class tratamientos(models.Model):
    _name='cc.tratamientos'
    
    name = fields.Char(
        string='Código',
        required=True,
        help='Escribe el código del tratamiento'
    )
    
    fecha = fields.Date(
        string='Fecha',
        required=True,
        help='Fecha del tratamiento'
    )
    
    producto = fields.Many2one(
        comodel_name='cc.fitosanitario',
        string='Producto',
        required=True
    )
    
    dosis = fields.Float(
        string='Dosis',
        required=True,
        help='Dosis del producto en Kg/Ha'
    )
    
    superficie_tratada = fields.Float(
        string='Superficie tratada',
        required=True,
        help='Superficie tratada en Ha'
    )
    
    total_producto = fields.Float(
        string='Total producto',
        required=False,
        help='Total de producto utilizado en Kg',
        compute='_total_producto',)
    
    @api.depends('total_producto')
    def _total_producto(self):
        for record in self:
            record.total_producto = record.dosis * record.superficie_tratada
    
    maquinaria_1 = fields.Many2one(
        comodel_name='cc.maquinaria',
        string='Maquinaria 1',
        required=False,
        help='Tractor utilizado en el tratamiento'
    )
    
    maquinaria_2 = fields.Many2one(
        comodel_name='cc.maquinaria',
        string='Maquinaria',
        required=False,
        help='Maquinaria utilizada en la aplicación del tratamiento'
    )
    
    cultivo = fields.Many2one(
        comodel_name='cc.cultivos',
        string='Cultivo',
        required=True
    )
    
    parcela = fields.Many2one(
        comodel_name='cc.parcelas',
        string='Parcela',
        required=True
    )
    
    aplicador = fields.Many2one(
        comodel_name='cc.aplicadores',
        string='Aplicador',
        required=False,
        ondelete='cascade'
        
    )
    
    asesor = fields.Many2one(
        comodel_name='cc.aplicadores',
        string='Asesor',
        required=False,
        ondelete='cascade',
    )
    
    
    observaciones = fields.Text(
        string='Observaciones',
        required=False,
        help='Observaciones del tratamiento'
    )
