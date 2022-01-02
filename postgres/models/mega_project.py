import re
from enum import Enum

from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator
from tortoise.validators import ValidationError, RegexValidator


PHONE_REGEX = re.compile("[0-9]{10}", re.I)
EMAIL_REGEX = re.compile(r"[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+", re.I)


def verify_email(value: str) -> None:
    if not EMAIL_REGEX.match(str(value)):
        raise ValidationError("Email is invalid.")


def verify_phone(value: int) -> None:
    if not PHONE_REGEX.match(str(value)):
        raise ValidationError("Phone number is invalid.")


class Departments(str, Enum):
    CS = "CS"
    EC = "EC"
    ME = "ME"
    EE = "EE"
    BT = "BT"
    CE = "CE"


class MegaProjects(models.Model):
    """
    MegaProjects model.
    """
    name = fields.CharField(max_length=256)
    email = fields.CharField(max_length=256, validators=[verify_email])
    srn = fields.CharField(max_length=14)
    phone = fields.CharField(max_length=10, validators=[verify_phone])
    department = fields.CharEnumField(Departments)

    project_title = fields.CharField(max_length=128)
    project_description = fields.TextField()
    components = fields.TextField()

    approved = fields.BooleanField(default=False)


MegaProjectsPydantic = pydantic_model_creator(MegaProjects)
MegaProjectsPydanticIn = pydantic_model_creator(
    MegaProjects,
    name="MegaProjectIn",
    exclude_readonly=True,
    exclude=("approved",)
)
