# {{ cookiecutter.project_name }}

{% set is_open_source = cookiecutter.open_source_license != 'Not
open source' -%}
{% if is_open_source %}
[![image](https://img.shields.io/travis/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug  }}.svg)](https://travis-ci.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }})
[![Documentation Status](https://readthedocs.org/projects/{{ cookiecutter.project_slug | replace("_", "-") }}/badge/?version=latest)](https://{{ cookiecutter.project_slug | replace("_", "-") }}.readthedocs.io/en/latest/?version=latest)
{%- endif %}
{% if cookiecutter.add_pyup_badge == 'y' %}
[[!image](https://pyup.io/repos/github/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/shield.svg)](<https://pyup.io/repos/github/>{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/)
{% endif %}
{{ cookiecutter.project_short_description }}
{% if is_open_source %}
* Free software: {{
cookiecutter.open_source_license }}
* Documentation: https://{{ cookiecutter.project_slug | replace("_", "-") }}.readthedocs.io.
{% endif %}
## Features

* TODO

## Credits

This package was created with[Cookiecutter](https://github.com/audreyr/cookiecutter) and the
[tparkerd/cookiecutter-pypackage]() project template.
