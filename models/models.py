# -*- coding: utf-8 -*-

from odoo import models, fields, api
from dateutil.relativedelta import *
from datetime import date 

class coche(models.Model):
	_name = 'concesionario.coche'
	_description = 'Coches'

	matricula = fields.Char('Matricula',required=True)
	marca = fields.Char(string='Marca',required=True)
	modelo = fields.Char(string='Modelo',required=True)
	color = fields.Char(string='Color',required=True)
	fecha_fabricacion = fields.Date(string='Fecha',required=True)
	anios = fields.Integer(string='Años',compute="_get_annos")
	precio = fields.Integer(string='Precio',required=True)
	

	@api.depends('fecha_fabricacion')
	def _get_annos(self):
		for coche in self:
			hoy=date.today()
			coche.anios = relativedelta(hoy, coche.fecha_fabricacion).years

	# relaciones
	cochesVendidos_id = fields.Many2one('concesionario.ventas',string='Coche Vendido')


class vendedor(models.Model):
	_name = 'concesionario.vendedor'
	_description = 'Vendedor'

	dni = fields.Char('DNI',required=True)
	nombre = fields.Char(string='Nombre',required=True)
	apellidos = fields.Char(string='Apellidos',required=True)
	cargo = fields.Char(string='Cargo',required=True)

	# relaciones
	vendedorVenta_ids = fields.One2many('concesionario.ventas','vendedorVenta_id',string='Vendedor')

class cliente(models.Model):
	_name = 'concesionario.cliente'
	_description = 'Cliente'

	dni = fields.Char('DNI',required=True)
	nombre = fields.Char(string='Nombre',required=True)
	apellidos = fields.Char(string='Apellidos',required=True)
	
	# concesionario
	compradorVenta_ids = fields.One2many('concesionario.ventas','compradorVenta_id',string='Comprador')

class ventas(models.Model):
	_name = 'concesionario.ventas'
	_description = 'Ventas'

	idVenta = fields.Char('Identificador Venta',required=True)
	fecha_venta = fields.Char(string='Fecha Venta',required=True)

	# relaciones
	cochesVendidos_ids = fields.One2many('concesionario.coche','cochesVendidos_id', string='Coche/s vendidos')
	vendedorVenta_id = fields.Many2one('concesionario.vendedor',string='Vendedor')
	compradorVenta_id = fields.Many2one('concesionario.cliente',string='Comprador')





















	

# from odoo import models, fields, api


# class concesionario(models.Model):
#     _name = 'concesionario.concesionario'
#     _description = 'concesionario.concesionario'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
