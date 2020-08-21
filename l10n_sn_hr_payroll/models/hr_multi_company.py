# -*- coding: utf-8 -*-
from odoo import fields, models, _


class HrSalaryCategoryMultiCompany(models.Model):
    """inherit model for removing required=True for company field """
    _inherit = 'hr.salary.rule.category'

    company_id = fields.Many2one('res.company', 'Compagnie', copy=False,
                                 default=lambda self: self.env.company)


class OptesisConventionInherit(models.Model):
    """inherit model for adding company_id field"""
    _inherit = "optesis.convention"

    company_id = fields.Many2one('res.company', 'Compagnie', copy=False, readonly=True,
                                 default=lambda self: self.env.company)


class OptesisLineConvention(models.Model):
    """inherit model for adding company_id field"""
    _inherit = "line.optesis.convention"

    company_id = fields.Many2one('res.company', 'Compagnie', copy=False, readonly=True,
                                 default=lambda self: self.env.company)


class HRPayrollStructureMulticompany(models.Model):
    """inherit model for removing required=True for company field """
    _inherit = "hr.payroll.structure"

    company_id = fields.Many2one('res.company', 'Compagnie', required=False)


class HRAccountJournal(models.Model):
    """inherit model for removing required=True for company field """
    _inherit = "account.journal"

    company_id = fields.Many2one('res.company', 'Compagnie',  required=False)
    
    
    
class HRSalaryRuleInherit(models.Model):
    """inherit model to add company_id"""
    _inherit = "hr.salary.rule"

    company_id = fields.Many2one('res.company', 'Compagnie', required=False)
    
    
class HRSalaryRuleTypeInherit(models.Model):
    """inherit model to add company_id"""
    _inherit = "hr.payroll.structure.type"

    company_id = fields.Many2one('res.company', 'Compagnie',  required=False)
    
    
class HRSalaryRuleTypeInherit(models.Model):
    """inherit model to add company_id"""
    _inherit = "hr.payslip.input.type"

    company_id = fields.Many2one('res.company', 'Compagnie',  required=False)
