from unittest import TestCase
from models import Person, Name, Address, email_from_name, build_person
from pyrsistent import InvariantException


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


class TestName(TestCase):
    
    def test_full_name(self):
        self.assertEqual(JVN_NAME.first, 'John')
        self.assertEqual(JVN_NAME.last, 'von Neumann')
        self.assertEqual(JVN_NAME.full, 'John von Neumann')


class TestEmail(TestCase):

    def test_fails_on_invalid_emails(self):
        with self.assertRaises(InvariantException):
            Person(email='no@tld')

    def test_build_email_from_name(self):
        email = email_from_name(JVN_NAME, domain='example.com')
        self.assertEqual(email, 'John.von.Neumann@example.com')

    def test_build_email_from_name_with_modifier(self):
        email = email_from_name(JVN_NAME,
                                modifier='functional',
                                domain='gmail.com')
        self.assertEqual(email, 'functional.John.von.Neumann@gmail.com')


class TestPerson(TestCase):

    def test_build_person(self):
        person = build_person(JVN_NAME, email=EMAIL)
        self.assertEqual(person.email, EMAIL)

    def test_build_person_no_email(self):
        person = build_person(JVN_NAME)
        self.assertEqual(person, JVN_PERSON)
        self.assertIsNone(person.email)

    def test_build_person_from_name(self):
        person = Person.from_name(JVN_NAME, email_from_name)
        self.assertEqual(person, build_person(JVN_NAME, email=EMAIL))

    def test_build_person_from_name_with_args(self):
        person = Person.from_name(JVN_NAME, email_from_name, domain='gmail.com')
        email = 'John.von.Neumann@gmail.com'
        self.assertEqual(person, build_person(JVN_NAME, email=email))
