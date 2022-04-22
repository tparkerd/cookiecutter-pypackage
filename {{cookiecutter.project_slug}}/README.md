# {{ cookiecutter.project_name }}
{% set is_open_source = cookiecutter.open_source_license != 'Not
open source' -%}

{% if is_open_source %} .. image:: <https://img.shields.io/pypi/v/>{{
cookiecutter.project_slug }}.svg :target:
<https://pypi.python.org/pypi/>{{ cookiecutter.project_slug }}

[![image](https://img.shields.io/travis/%7B%7B%20cookiecutter.github_username%20%7D%7D/%7B%7B%20cookiecutter.project_slug%20%7D%7D.svg)](https://travis-ci.com/%7B%7B%20cookiecutter.github_username%20%7D%7D/%7B%7B%20cookiecutter.project_slug%20%7D%7D)

[![Documentation Status](https://readthedocs.org/projects/%7B%7B%20cookiecutter.project_slug%20%7C%20replace(%22_%22,%20%22-%22)%20%7D%7D/badge/?version=latest)](https://%7B%7B%20cookiecutter.project_slug%20%7C%20replace(%22_%22,%20%22-%22)%20%7D%7D.readthedocs.io/en/latest/?version=latest)

{%- endif %}

{% if cookiecutter.add_pyup_badge == 'y' %} .. image::
<https://pyup.io/repos/github/>{{ cookiecutter.github_username }}/{{
cookiecutter.project_slug }}/shield.svg :target:
<https://pyup.io/repos/github/>{{ cookiecutter.github_username }}/{{
cookiecutter.project_slug }}/ :alt: Updates {% endif %}

{{ cookiecutter.project_short_description }}

{% if is_open_source %} \* Free software: {{
cookiecutter.open_source_license }} \* Documentation: <https://>{{
cookiecutter.project_slug | replace("_", "-") }}.readthedocs.io. {%
endif %}

## Features

- TODO

## Credits

This package was created with
[Cookiecutter](https://github.com/audreyr/cookiecutter) and the
[tparkerd/cookiecutter-pypackage]() project template.
