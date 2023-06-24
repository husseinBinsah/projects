# -*- coding: utf-8 -*-
import sys
print(sys.path)
from odoo import models, fields
class CarStore(models.Model):
   _name ="car.store"
   name = fields.Char()

   m_year = fields.Date(string="Date of car")
   comany_id=fields.Many2one()
   count=fields.Integer()
class Companies(models.Model):
   _name ="companies"
   name = fields.Char()
   icon = fields.Binary()