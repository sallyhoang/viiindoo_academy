from odoo import models, fields, api


class ResEthnic(models.Model):
    _name = 'res.ethnic'
    _description = 'Ethnic'
    
    name = fields.Char(
        string='Name',
        required=True)
    code = fields.Char(
        string='Code',
        required=True,
        groups='base.group_user,base.group_portal'
        )
    other_name = fields.Char(
        string='Other Name',
        required=True)
    
    country_ids = fields.Many2many(
        comodel_name="res.country",
        relation="ethnicity_rel",
        column1="ethnic_id",
        column2="country_id",
        )
    description = fields.Text(
        string='Description',
        )
    student_ids = fields.One2many(
        comodel_name="education.student",
        inverse_name='ethnic_id',
        string='Students')
    

