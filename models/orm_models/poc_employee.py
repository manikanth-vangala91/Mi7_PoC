
from tortoise import Model, fields

class PoCEmployee(Model):

    class Meta:
        table = "EMPLOYEE"
        schema = "poc"

    EmpCode      = fields.IntField(pk=True)
    EmpFName     = fields.CharField(max_length=15, null=True)
    EmpLName     = fields.CharField(max_length=15, null=True)
    Job          = fields.CharField(max_length=45, null=True)
    Manager      = fields.CharField(max_length=4, null=True)
    HireDate     = fields.DateField(null=True)
    Salary       = fields.IntField(null=True)
    Commission   = fields.IntField(null=True)
    DEPTCODE     = fields.IntField(null=True)