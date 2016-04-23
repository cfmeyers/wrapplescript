from wrapplescript.template import get_raw_template, make_template


SIMPLE = """This is
a simple file
"""

COMPLEX = """inputEmail = function () {
    document.forms.signup_email.email.value = 'x@example.com';
}
"""

PATH_TO_SIMPLE = 'tests/fixtures/simple.applescript'
PATH_TO_COMPLEX = 'tests/fixtures/complex.applescript'

class TestTemplates(object):

    def test_get_raw_template_reads_in_template_from_path(self):
        raw_template = get_raw_template(PATH_TO_SIMPLE)
        assert raw_template == SIMPLE

    def test_passing_path_and_params_returns_rendered_template(self):
        template = make_template(PATH_TO_SIMPLE, {})
        assert template == SIMPLE

    def test_make_template_renders_complex_template(self):
        template = make_template(PATH_TO_COMPLEX, {'email': 'x@example.com'})
        assert template == COMPLEX
