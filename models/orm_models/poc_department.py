
from tortoise import Model, fields


class PoCDepartment(Model):

    class Meta:
        table  = "DEPARTMENT"
        schema = "poc"

    DEPTCODE   = fields.CharField(pk=True,max_length=10)
    DeptName   = fields.CharField(max_length=30, null=True)
    LOCATION   = fields.CharField(max_length=33, null=True)