import pystache


def get_raw_template(path):
    with open(path) as f:
        return f.read()


def make_template(path, params):
    raw_template = get_raw_template(path)
    rendered_template = pystache.render(raw_template, params)
    return rendered_template
