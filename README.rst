======================
Cookiecutter PyPackage
======================

.. image:: https://pyup.io/repos/github/tparkerd/cookiecutter-pypackage/shield.svg
    :target: https://pyup.io/repos/github/tparkerd/cookiecutter-pypackage/
    :alt: Updates

.. image:: https://travis-ci.org/tparkerd/cookiecutter-pypackage.svg?branch=master
    :target: https://travis-ci.org/github/tparkerd/cookiecutter-pypackage
    :alt: Build Status

.. image:: https://readthedocs.org/projects/cookiecutter-pypackage/badge/?version=latest
    :target: https://cookiecutter-pypackage.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

Cookiecutter_ template for a Python package.

* GitHub repo: https://github.com/tparkerd/cookiecutter-pypackage/
* Documentation: https://cookiecutter-pypackage.readthedocs.io/
* Free software: BSD license

Features
--------

* Testing setup with ``unittest`` and ``python setup.py test`` or ``pytest``
* Travis-CI_: Ready for Travis Continuous Integration testing
* Tox_ testing: Setup to easily test for Python 3.6, 3.7, 3.8
* Sphinx_ docs: Documentation ready for generation with, for example, `Read the Docs`_
* bump2version_: Pre-configured version bumping with a single command
* Auto-release to PyPI_ when you push a new tag to master (optional)
* Command line interface using Click (optional)

.. _Cookiecutter: https://github.com/cookiecutter/cookiecutter

Build Status
-------------

Linux:

.. image:: https://img.shields.io/travis/tparkerd/cookiecutter-pypackage.svg
    :target: https://travis-ci.org/tparkerd/cookiecutter-pypackage
    :alt: Linux build status on Travis CI

Windows:

.. image:: https://ci.appveyor.com/api/projects/status/github/tparkerd/cookiecutter-pypackage?branch=master&svg=true
    :target: https://ci.appveyor.com/project/tparkerd/cookiecutter-pypackage/branch/master
    :alt: Windows build status on Appveyor

Quickstart
----------

Install the latest Cookiecutter if you haven't installed it yet (this requires
Cookiecutter 1.4.0 or higher)::

    pip install -U cookiecutter

Generate a Python package project::

    cookiecutter https://github.com/tparkerd/cookiecutter-pypackage.git

Then:

* Create a repo and put it there.
* Add the repo to your Travis-CI_ account.
* Install the dev requirements into a virtualenv. (``pip install -r requirements_dev.txt``)
* Register_ your project with PyPI.
* Run the Travis CLI command ``travis encrypt --add deploy.password`` to encrypt your PyPI password in Travis config
  and activate automated deployment on PyPI when you push a new tag to master branch.
* Add the repo to your `Read the Docs`_ account + turn on the Read the Docs service hook.
* Release your package by pushing a new tag to master.
* Add a ``requirements.txt`` file that specifies the packages you will need for
  your project and their versions. For more info see the `pip docs for requirements files`_.
* Activate your project on `pyup.io`_.

.. _`pip docs for requirements files`: https://pip.pypa.io/en/stable/user_guide/#requirements-files
.. _Register: https://packaging.python.org/tutorials/packaging-projects/#uploading-the-distribution-archives

For more details, see the `cookiecutter-pypackage tutorial`_.

.. _`cookiecutter-pypackage tutorial`: https://cookiecutter-pypackage.readthedocs.io/en/latest/tutorial.html

Not Exactly What You Want?
--------------------------

Don't worry, you have options:

Similar Cookiecutter Templates
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* `audreyr/cookiecutter-pypackage`_: The original pypackage, uses unittest for testing and other minor changes.

Fork This / Create Your Own
~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you have differences in your preferred setup, I encourage you to fork this
to create your own version. Or create your own; it doesn't strictly have to
be a fork.

* Once you have your own version working, add it to the Similar Cookiecutter
  Templates list above with a brief description.

* It's up to you whether or not to rename your fork/own version. Do whatever
  you think sounds good.

Or Submit a Pull Request
~~~~~~~~~~~~~~~~~~~~~~~~

I also accept pull requests on this, if they're small, atomic, and if they
make my own packaging experience better.


.. _Travis-CI: http://travis-ci.org/
.. _Tox: http://testrun.org/tox/
.. _Sphinx: http://sphinx-doc.org/
.. _Read the Docs: https://readthedocs.io/
.. _`pyup.io`: https://pyup.io/
.. _bump2version: https://github.com/c4urself/bump2version
.. _Punch: https://github.com/lgiordani/punch
.. _Poetry: https://python-poetry.org/
.. _PyPi: https://pypi.python.org/pypi
.. _Mkdocs: https://pypi.org/project/mkdocs/
.. _Pre-commit: https://pre-commit.com/
.. _Black: https://black.readthedocs.io/en/stable/
.. _Mypy: https://mypy.readthedocs.io/en/stable/

.. _`audreyr/cookiecutter-pypackage`: https://github.com/Nekroze/cookiecutter-pypackage