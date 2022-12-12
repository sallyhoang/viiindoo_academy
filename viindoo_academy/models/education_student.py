from odoo import models, fields, api


class EducationStudent(models.Model):
    _name = 'education.student'
    _description = ' Education Student'
    
    name = fields.Char(
        string='Name',
        required=True)
    age = fields.Integer(
        string='Age')
    class_id = fields.Many2one(
        comodel_name='education.class',
        string='Class', help="The Class of student")


    class_ids = fields.Many2many(
        comodel_name='education.class',
        relation='class_education_rel',
        column1='student_id',
        column2='class_id',
        string='Enrolled Classes')
    country_id = fields.Many2one(
        comodel_name='res.country',
        string='Country',
        )
    ethnic_id = fields.Many2one(
        comodel_name='res.ethnic',
        string='Ethnic',
        )
    ethnic_code = fields.Char(related='ethnic_id.code')
    
    user_id = fields.Many2one(
        comodel_name='res.users',
        string='User',
        default=lambda self: self.env.user,
        )
    
    @api.onchange(ethnic_id)
    def _compute_country_id(self):
        if self.ethnic_id:
            self.country_id = self.ethnic_id.country_ids[0]
            
            
    
            
        
    
