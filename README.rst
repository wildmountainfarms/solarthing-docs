SolarThing Documentation Repository
=======================================

This repository contains documentation for SolarThing that can be viewed on https://solarthing.readthedocs.io

Main repository at https://github.com/wildmountainfarms/solarthing

If you are unfamiliar with RST, this is a good reference: https://thomas-cokelaer.info/tutorials/sphinx/rest_syntax.html


Building
----------

To build this yourself, run these commands:

.. code-block:: shell

    cd docs/
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r source/requirements.txt
    make html
    xdg-open "file://$(pwd)/build/html/index.html"
    make latexpdf  # requires latexmk command
    make epub

Dependencies
-------------

Depending on what you want to build yourself from the Building section, you can run these commands to install some or all of the dependencies.

.. code-block:: shell
    apt install python3 python3-pip latexmk


Stuff we might use in the future:
* https://www.sphinx-doc.org/en/master/usage/extensions/linkcode.html

Testing
----------

Running the docker container is optional.

.. code-block:: console

  docs/preview.sh && docker compose restart

Accessing content via the webserver has some benefits rather than just viewing the html file in your browser:

* Cookies are stored across the entire site, so...

  * Tab selection across pages is kept

TODO
---------

* Find a way to get GraphQL syntax highlighting into pygments

  * Waiting on a release. As this issue is merged: https://github.com/pygments/pygments/pull/2428

* Find a way to get JSON5 syntax highlighting into pygments. Or, alternatively, just regular JSON highlighting with the ability to ignore stuff that's not JSON syntax
* Page about common errors including permission issues
* Page about using socat and about configuring timeouts

About These Docs
-------------------

July 27, 2023
^^^^^^^^^^^^^^

We stopped using `sphinx_rtd_theme <https://github.com/readthedocs/sphinx_rtd_theme/issues/1463>`_ because of this: https://github.com/readthedocs/sphinx_rtd_theme/issues/1463.
We want Sphinx 7 support!
That issue referred me to `furo <https://github.com/pradyunsg/furo>`_, a theme that impressed me when I first looked at it.
After trying it out, I couldn't be happier. Dark/light mode support out of the box, and just a better user experience.
