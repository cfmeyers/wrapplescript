from pyrsistent import PClass, field
from re import compile, IGNORECASE

EMAIL_RE = compile(r'^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}$', IGNORECASE)

string = (str, unicode)


def maybe(*some_types):
    return some_types + (type(None),)


def validate_email(email):
    if email is None or EMAIL_RE.match(email):
        return True, ''
    return False, 'not a valid email address'


class Name(PClass):
    first = field(string, mandatory=True)
    last = field(string, mandatory=True)

    @property
    def full(self):
        return ' '.join((self.first, self.last))


class Address(PClass):
    street_address = field(string, mandatory=True)
    city = field(string, mandatory=True)
    state = field(string, mandatory=True)
    zip_code = field(string, mandatory=True)
    phone_number = field(string)


class Person(PClass):
    name = field(Name)
    email = field(maybe(str, unicode), invariant=validate_email)
    address = field(maybe(Address))

    @classmethod
    def from_name(cls, name, email_constructor, **kwargs):
        email = email_constructor(name, **kwargs)
        return cls(name=name, email=email)


def build_person(name, email=None):
    return Person(
        name=name,
        email=email,
    )


def email_from_name(name, domain='example.com', modifier=''):
    if modifier:
        modifier = modifier + '.'
    local_part = modifier + name.full.replace(' ', '.')
    return local_part + '@' + domain
