# -*- coding: utf-8 -*-
from odoo import models, fields


class OptesisPayrollInputs(models.Model):
    _name = "optesis.payslip.input"
    _description = "Model to create inputs for employee"

    name = fields.Char()
    input_id = fields.Many2one('hr.payslip.input.type', 'Entrée')
    employee_id = fields.Many2one('hr.employee', 'Employé')
    date_from = fields.Date(string='From', readonly=True, required=True,
        default=lambda self: fields.Date.to_string(date.today().replace(day=1)), states={'draft': [('readonly', False)], 'verify': [('readonly', False)]})
    date_to = fields.Date(string='To', readonly=True, required=True,
        default=lambda self: fields.Date.to_string((datetime.now() + relativedelta(months=+1, day=1, days=-1)).date()),
        states={'draft': [('readonly', False)], 'verify': [('readonly', False)]})
    state = fields.Selection([
        ('draft', 'Draft'),
        ('verify', 'Waiting'),
        ('done', 'Done'),
        ('cancel', 'Rejected'),
    ], string='Status', index=True, readonly=True, copy=False, default='draft')
