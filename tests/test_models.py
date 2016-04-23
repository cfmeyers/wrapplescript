from wrapplescript.models import Person, Name, Address, email_from_name, build_person
from pyrsistent import InvariantException
import pytest


JVN_NAME = Name(
    first='John',
    last='von Neumann',
)

JVN_PERSON = Person(
    name=JVN_NAME,
    email=None,
)

CALIFORNIA_ADDRESS = Address(
    street_address="1526 H St",
    city="Sacramento",
    state="CA",
    zip_code="95814",
    phone_number="703-818-7223",
)

EMAIL = 'John.von.Neumann@example.com'


class TestName(object):
    
    def test_full_name(self):
        assert JVN_NAME.first == 'John'
        assert JVN_NAME.last == 'von Neumann'
        assert JVN_NAME.full == 'John von Neumann'


class TestEmail(object):

    def test_fails_on_invalid_emails(self):
        with pytest.raises(InvariantException):
            Person(email='no@tld')

    def test_build_email_from_name(self):
        email = email_from_name(JVN_NAME, domain='example.com')
        assert email ==  'John.von.Neumann@example.com'

    def test_build_email_from_name_with_modifier(self):
        email = email_from_name(JVN_NAME,
                                modifier='functional',
                                domain='gmail.com')
        assert email == 'functional.John.von.Neumann@gmail.com'


class TestPerson(object):

    def test_build_person(self):
        person = build_person(JVN_NAME, email=EMAIL)
        assert person.email == EMAIL

    def test_build_person_no_email(self):
        person = build_person(JVN_NAME)
        assert person == JVN_PERSON
        assert person.email is None

    def test_build_person_from_name(self):
        person = Person.from_name(JVN_NAME, email_from_name)
        assert person == build_person(JVN_NAME, email=EMAIL)

    def test_build_person_from_name_with_args(self):
        person = Person.from_name(JVN_NAME, email_from_name, domain='gmail.com')
        email = 'John.von.Neumann@gmail.com'
        assert person == build_person(JVN_NAME, email=email)
