# -*- coding: utf-8 -*-
from odoo import fields, models, _, api
import logging

_logger = logging.getLogger(__name__)


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

    
    @api.model
    def _get_default_rule_ids(self):
        _logger.info('IN THE FUNCTION GET DEFAULT RULE')
        return [
            (0, 0, {
                'name': 'Salaire de base',
                'sequence': 1000,
                'code': 'C1000',
                'category_id': self.env.ref('hr_payroll.BASIC').id,
                'condition_select': 'none',
                'amount_select': 'code',
                'amount_python_compute': 'result = contract.wage*(worked_days.WORK100.number_of_days)/30',
                'note': 'La règle du salaire de base',
            }),
            (0, 0, {
                'name': 'Allocation Congés',
                'sequence': 1060,
                'code': 'C1060',
                'category_id': self.env.ref('hr_payroll.ALW').id,
                'condition_select': 'python',
                'condition_python': """if contract.alloc_conges != 0:
                    result = True""",
                'amount_select': 'code',
                'amount_python_compute': 'result = round(contract.alloc_conges)',
            }),
            (0, 0, {
                'name': 'Prime de transport',
                'sequence': 1125,
                'code': 'C1125',
                'category_id': self.env.ref('l10n_sn_hr_payroll.non_imposable').id,
                'condition_select': 'none',
                'amount_select': 'code',
                'amount_python_compute': 'result = worked_days.WORK100.number_of_days*20800/30',
                'note': 'Prime de transport',
            }),
            (0, 0, {
                'name': 'Indemnité KM',
                'sequence': 1140,
                'code': 'C1100',
                'category_id': self.env.ref('l10n_sn_hr_payroll.non_imposable').id,
                'condition_select': 'none',
                'amount_select': 'code',
                'amount_python_compute': 'result = worked_days.WORK100.number_of_days*50000/30',
                'note': 'Indemnité KM',
            }),
            (0, 0, {
                'name': 'Salaire Brut',
                'sequence': 1148,
                'code': 'C1148',
                'category_id': self.env.ref('hr_payroll.GROSS').id,
                'condition_select': 'none',
                'amount_select': 'code',
                'amount_python_compute': 'result = round(categories.BASE + categories.INDM + categories.NOIMP + categories.HS)',
                'note': 'la valeur du salaire Brut se base sur la somme du salaire de base et les indemnités tout en faisant la soustraction des déductions.',
                'appears_on_payslip': True
            }),
            (0, 0, {
                'name': 'Ipres RG',
                'sequence': 2030,
                'code': 'C2030',
                'category_id': self.env.ref('l10n_sn_hr_payroll.SALC').id,
                'condition_select': 'none',
                'amount_select': 'percentage',
                'amount_percentage_base': 'min((categories.BRUT - categories.NOIMP),360000)',
                'quantity': 1,
                'amount_percentage': 5.6,
                'note': 'Ipres RG',
                'partner_id': self.env.ref('l10n_sn_hr_payroll.hr_prevoyance_register').id
            }),
            (0, 0, {
                'name': 'Ipres RG Pat',
                'sequence': 2031,
                'code': 'C2031',
                'category_id': self.env.ref('hr_payroll.COMP').id,
                'condition_select': 'none',
                'amount_select': 'percentage',
                'amount_percentage_base': 'min((categories.BRUT - categories.NOIMP),360000)',
                'quantity': 1,
                'amount_percentage': 5.6,
                'note': 'Ipres RG',
                'partner_id': self.env.ref('l10n_sn_hr_payroll.hr_prevoyance_register').id
            }),
            (0, 0, {
                'name': 'Ipres RC',
                'sequence': 2040,
                'code': 'C2040',
                'category_id': self.env.ref('l10n_sn_hr_payroll.SALC').id,
                'condition_select': 'none',
                'amount_select': 'percentage',
                'amount_percentage_base': 'min(categories.BRUT - categories.NOIMP,1080000)',
                'quantity': 1,
                'amount_percentage': 2.4,
                'note': 'Ipres RC',
                'partner_id': self.env.ref('l10n_sn_hr_payroll.hr_prevoyance_register').id
            }),
            (0, 0, {
                'name': 'Ipres RC Pat',
                'sequence': 2041,
                'code': 'C2041',
                'category_id': self.env.ref('hr_payroll.COMP').id,
                'condition_select': 'none',
                'amount_select': 'percentage',
                'amount_percentage_base': 'min(categories.BRUT - categories.NOIMP,1080000)',
                'quantity': 1,
                'amount_percentage': 3.6,
                'note': 'Ipres RC Patronale',
                'partner_id': self.env.ref('l10n_sn_hr_payroll.hr_prevoyance_register').id
            }),
            (0, 0, {
                'name': 'Prestations Familiale',
                'sequence': 2010,
                'code': 'C2010',
                'category_id': self.env.ref('hr_payroll.COMP').id,
                'condition_select': 'none',
                'amount_select': 'percentage',
                'amount_percentage_base': 'min(63000,categories.BRUT)',
                'quantity': 1,
                'amount_percentage': 7,
            }),
            (0, 0, {
                'name': 'Accident de travail',
                'sequence': 2020,
                'code': 'C2020',
                'category_id': self.env.ref('hr_payroll.COMP').id,
                'condition_select': 'none',
                'amount_select': 'percentage',
                'amount_percentage_base': 'min(63000,categories.BRUT)',
                'quantity': 1,
                'amount_percentage': 7,
                'note': """C'est la valeur d'accident de travail qui se base sur la valeur de salaire "Brut". Elle doit être réglée chaque trimestre .Cette valeur appartient à la rubrique "Cotisations Patronales"""
            }),
            (0, 0, {
                'name': 'CFCE',
                'sequence': 2000,
                'code': 'C2000',
                'category_id': self.env.ref('hr_payroll.COMP').id,
                'condition_select': 'none',
                'amount_select': 'percentage',
                'amount_percentage_base': 'categories.BRUT - categories.NOIMP',
                'quantity': 1,
                'amount_percentage': 3,
                'partner_id': self.env.ref('l10n_sn_hr_payroll.hr_VRS_register').id
            }),
            (0, 0, {
                'name': 'Total Charges Patronales',
                'sequence': 3010,
                'code': 'C3010',
                'category_id': self.env.ref('l10n_sn_hr_payroll.TOTALCOMP').id,
                'condition_select': 'none',
                'amount_select': 'code',
                'amount_python_compute': 'result = round(categories.COMP)',
                'note': """la somme des charges patronales."""
            }),
            (0, 0, {
                'name': """Cout total pour l'entreprise""",
                'sequence': 3020,
                'code': 'C3020',
                'category_id': self.env.ref('l10n_sn_hr_payroll.TOTAL').id,
                'appears_on_payslip': True,
                'condition_select': 'none',
                'amount_select': 'code',
                'amount_python_compute': 'result = round(categories.BRUT + categories.COMP)',
                'note': """le coût total de l'entreprise qui est la somme du salaire brut et les cotistaions patronales."""
            }),
            (0, 0, {
                'name': '2eme Tranche',
                'sequence': 2100,
                'code': 'C2100',
                'category_id': self.env.ref('l10n_sn_hr_payroll.tranche_impot_sur_revenu').id,
                'appears_on_payslip': False,
                'condition_select': 'none',
                'amount_select': 'code',
                'amount_python_compute': """if categories.BFISC < 125000 and categories.BFISC > 52500:
  result=round((categories.BFISC - 52500)*0.2)
else:
  if categories.BFISC &gt; 125000:
    result=14500
  else:
    result=0"""
            }),
            (0, 0, {
                'name': """3eme Tranche""",
                'sequence': 2101,
                'code': 'C2101',
                'category_id': self.env.ref('l10n_sn_hr_payroll.tranche_impot_sur_revenu').id,
                'appears_on_payslip': True,
                'condition_select': 'none',
                'amount_select': 'code',
                'amount_python_compute': """if categories.BFISC < 333333 and categories.BFISC > 125000:
    result=round((categories.BFISC - 125000)*0.3)
else:
  if categories.BFISC &gt; 333333:
    result=62500
  else:
    result=0""",
            }),
            (0, 0, {
                'name': '4eme Tranche',
                'sequence': 2102,
                'code': 'C2102',
                'category_id': self.env.ref('l10n_sn_hr_payroll.tranche_impot_sur_revenu').id,
                'appears_on_payslip': False,
                'condition_select': 'none',
                'amount_select': 'code',
                'amount_python_compute': """if categories.BFISC < 666667 and categories.BFISC > 333333:
    result=round((categories.BFISC - 333333)*0.35)
else:
    if categories.BFISC > 666667 :
      result=116667
    else:
      result=0""",
            }),
        ]
    
    rule_ids = fields.One2many(
        'hr.salary.rule', 'struct_id',
        string='Salary Rules', default=_get_default_rule_ids)


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
