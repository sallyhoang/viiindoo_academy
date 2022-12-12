from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class EducationClass(models.Model):
    _name = 'education.class'
    _description = 'Education Class'
    
    name = fields.Char(
        string='Name',
        help="The name of the class for identification",
        required=True)
    state = fields.Selection(
        [
            ('draft', 'Draft'),
            ('confirmed', 'Confirmed'),
            ('done', 'Done'),
            ('cancelled', 'Cancelled'),
            ],
        string='Status',
        default='draft',
        help="Status of the class",
        )
    description = fields.Text(
        string='Description',
        help="The description for identification.")
    active = fields.Boolean(default=True)
    
    start_date = fields.Date(
        string='Start Date',
        help="The start date from of class",
                            )

    end_date = fields.Date(
        string='End Date',
        help="The end date of class",
                            )    
    student_ids = fields.One2many(
        comodel_name='education.student',
        inverse_name='class_id',
        string='Students',
        help="The students that belong to the class.")
    
    historical_student_ids = fields.Many2many(
        comodel_name='education.student',
        relation='class_education_rel',
        column1='class_id',
        column2='student_id',
        string="Historical Students")
    
    student_count = fields.Integer(
        string='Student Count',
        compute='_compute_student_count',
        )
    historical_students_count = fields.Integer(
        string='Historical Student Count',
        compute='_compute_historical_student_count',
        )
    company_id = fields.Many2one(
        comodel_name='res.company',
        string='Company',
        default=lambda self: self.env.company,
        )
    responsible_id = fields.Many2one(
    comodel_name='res.users',
    string='User',
    default=lambda self: self.env.user,
        )
    _sql_constraints = [('class_name_unique', 'unique(name)', "The name of class must be unique!")]
    @api.depends('student_ids')
    def _compute_student_count(self):
        for r in self:
            r.student_count = len(r.student_ids)

    @api.depends('historical_student_ids')            
    def _compute_historical_student_count(self):
        for r in self:
            r.historical_students_count = len(r.historical_student_ids)

    @api.constrains('start_date', 'end_date')
    def _check_date(self):
        for r in self:
            if r.start_date and r.end_date and r.start_date > r.end_date:
                raise ValidationError(_("The class start date must be earlier than or equal to end date."))
    
