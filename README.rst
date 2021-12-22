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


Stuff we might use in the future:
* https://www.sphinx-doc.org/en/master/usage/extensions/linkcode.html

TODO:
* Find a way to get GraphQL syntax highlighting into pygments
* Find a way to get JSON5 syntax highlighting into pygments. Or, alternatively, just regular JSON highlighting with the ability to ignore stuff that's not JSON syntax 
