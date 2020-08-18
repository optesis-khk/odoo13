# -*- coding: utf-8 -*-
from odoo import fields, models, _


class HrLeaveMultiCompany(models.Model):
    """inherit model for removing required=True for company field """
    _inherit = 'hr.leave'

    company_id = fields.Many2one('res.company', 'Company', copy=False,
                                 default=lambda self: self.env.user.company_id)


class HrSalaryCategoryMultiCompany(models.Model):
    """inherit model for removing required=True for company field """
    _inherit = 'hr.salary.rule.category'

    company_id = fields.Many2one('res.company', 'Company', copy=False,
                                 default=lambda self: self.env.user.company_id)


class OptesisConventionInherit(models.Model):
    """inherit model for adding company_id field"""
    _inherit = "optesis.convention"

    company_id = fields.Many2one('res.company', 'Company', copy=False, readonly=True,
                                 default=lambda self: self.env.user.company_id)


class OptesisLineConvention(models.Model):
    """inherit model for adding company_id field"""
    _inherit = "line.optesis.convention"

    company_id = fields.Many2one('res.company', 'Company', copy=False, readonly=True,
                                 default=lambda self: self.env.user.company_id)


class HRPayrollStructureMulticompany(models.Model):
    """inherit model for removing required=True for company field """
    _inherit = "hr.payroll.structure"

    company_id = fields.Many2one('res.company', required=False)


class HRAccountJournal(models.Model):
    """inherit model for removing required=True for company field """
    _inherit = "account.journal"

    company_id = fields.Many2one('res.company', required=False)
    
    
    
class HRSalaryRuleInherit(models.Model):
    """inherit model to add company_id"""
    _inherit = "hr.salary.rule"

    company_id = fields.Many2one('res.company', required=False)
