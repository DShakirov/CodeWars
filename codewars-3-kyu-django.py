from datetime import datetime
from typing import Any
import re

class ValidationError(Exception):
    pass

class ValidationField():
    def __init__(self, blank=False, default=None, **kwargs):
        self.default = default
        self.blank = blank
        self.__dict__.update(kwargs)

    def validate(self, value):
        if value is None and self.blank == False:
            raise ValidationError
        

class CharField(ValidationField):

    def __init__(self, min_length=0, max_length=None, **kwargs):
        super().__init__(**kwargs)
        self.min_length = min_length
        self.max_length = max_length

    def validate(self, value):
        super().validate(value)

        if not value:
            return None
        if not isinstance(value, str):
            raise ValidationError
        if self.min_length and len(value) < self.min_length:
            raise ValidationError
        if self.max_length and len(value) > self.max_length:
            raise ValidationError


class IntegerField(ValidationField):
    def __init__(self, min_value, max_value, **kwargs):
        super().__init__(**kwargs)
        self.min_value = min_value
        self.max_value = max_value

    def validate(self, value):
        super().validate(value)
        if value is None:
            return
        if not isinstance(value, int):
            raise ValidationError
        if self.min_value and value < self.min_value:
            raise ValidationError
        if self.max_value and value > self.max_value:
            raise ValidationError
        

class BooleanField(ValidationField):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def validate(self, value):
        super().validate(value)

        if value is None:
            return
        if not isinstance(value, bool):
            raise ValidationError
        

class DateTimeField(ValidationField):
    def __init__(self, default=None, auto_now=False, **kwargs):
        super().__init__(**kwargs)
        self.default = default
        self.auto_now = auto_now

    def __getattribute__(self, name: str) -> Any:
        if name == 'default':
            if not self.default and self.auto_now:
                return datetime.datetime.now()
            return self.default
        return super().__getattribute__(name)

    def validate(self, value):
        super().validate(value)
        if value is None:
            return
        if not isinstance(value, datetime.datetime):
            raise ValidationError
        

class EmailField(ValidationField):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def validate(self, value):
        super().validate(value)
        if value is None:
            return
        if not isinstance(value, str):
            raise ValidationError
        if not re.match(r"[^@]+@[^@]+\.[^@]+", value):
            raise ValidationError
        

class Model:
    def __init__(self, **kwargs):
        for d in [d for d in dir(self.__class__) if d.startswith('_f_')]:
            attr = getattr(self.__class__, d)
            setattr(self, d[3:], attr.default)

        for k, value in kwargs.items():
            setattr(self, k, value)

    def __init_subclass__(cls) -> None:
        for d in [d for d in dir(cls) if not d.startswith('_')]:
            attr = getattr(cls, d)
            if isinstance(attr, (CharField, EmailField,
                                 IntegerField, BooleanField, DateTimeField)):
                delattr(cls, d)
                setattr(cls, '_f_' + d, attr)
        super().__init_subclass__()

    def validate(self):
        for d in [d for d in dir(self.__class__) if d.startswith('_f_') and hasattr(self, d[3:])]:
            class_attr = getattr(self.__class__, d)
            instance_attr = getattr(self, d[3:])
            class_attr.validate(instance_attr)






# Example usage
class User(Model):
    first_name = CharField(max_length=30)
    last_name = CharField(max_length=50)
    email = EmailField()
    is_verified = BooleanField(default=False)
    date_joined = DateTimeField(auto_now=True)
    age = IntegerField(min_value=5, max_value=120, blank=True)

user1 = User(first_name='Liam', last_name='Smith', email='liam@example.com')
user1.validate()