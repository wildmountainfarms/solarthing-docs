# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'SolarThing'
copyright = '2023, Lavender Shannon'
author = 'Lavender Shannon'

# release = '0.1'
# version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.extlinks',
    'sphinx.ext.todo',
    #'sphinxcontrib.globalsubs',
    'sphinx_reredirects', # https://documatt.gitlab.io/sphinx-reredirects/install.html
    'sphinx_tabs.tabs', # https://pypi.org/project/sphinx-tabs/
    'sphinx_search.extension', # https://pypi.org/project/readthedocs-sphinx-search/
]

todo_include_todos=True

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

# html_theme = 'sphinx_rtd_theme'
html_theme = 'furo'

#html_theme_options = {
#}
html_theme_options = dict()

# -- Options for EPUB output
epub_show_urls = 'footnote'


extlinks = {
    'issue-page': ('https://github.com/wildmountainfarms/solarthing/issues%s', 'issues%s'),
    'issue': ('https://github.com/wildmountainfarms/solarthing/issues/%s', '#%s'),
    'blob': ('https://github.com/wildmountainfarms/solarthing/blob/%s', 'solarthing/blob/%s'),
    'tree': ('https://github.com/wildmountainfarms/solarthing/tree/%s', 'solarthing/tree/%s'),
}

# We aren't using global substitutions now, so keep this commented
#global_substitutions = {
#    'issues': 'https://github.com/wildmountainfarms/solarthing/issues'
#}

html_sourcelink_suffix = ""

latex_elements = {
    "maxlistdepth": 10
}

redirects = {
    "database-and-display": "about/database-and-display.html",
    "faq": "about/faq.html",
    "supported-products": "about/supported-products.html",
    "config/cpu-temperature": "../config/file/base-json/request/cpu-temperature.html",
    "rover/bulk-request": "../config/file/base-json/request/modbus/rover/bulk-request.html",
    "tracer/clock": "../config/file/base-json/request/modbus/tracer/clock.html",
    "config/w1-temperature": "../config/file/base-json/request/w1-temperature.html",
    "config/commands": "../config/commands/index.html",
    "config/rpi-cpu-temp": "../misc/legacy/rpi-cpu-temp.html",
    "logging": "logging/index.html",
    "configuration-continued": "quickstart/config/configuration-continued.html",
    "configuration-databases": "quickstart/config/configuration-databases.html",
    "configuration-edit-base-json": "quickstart/config/configuration-edit-base-json.html",
    "configuration-running": "quickstart/config/configuration-running.html",
    "config/couchdb": "../quickstart/config/database/couchdb.html",
    "config/influxdb1": "../quickstart/config/database/influxdb1.html",
    "config/influxdb2": "../quickstart/config/database/influxdb2.html",
    "config/mqtt": "../quickstart/config/database/mqtt.html",
    "mate/config": "../quickstart/config/device/mate.html",
    "rover/config": "../quickstart/config/device/rover.html",
    "tracer/config": "../quickstart/config/device/tracer.html",
    "configuration": "quickstart/config/index.html",
    "data/graphql-grafana": "../quickstart/data/graphql-grafana.html",
    "view-data": "quickstart/data/index.html",
    "data/influxdb-grafana": "../quickstart/data/influxdb-grafana.html",
    "data/pvoutput": "../quickstart/data/pvoutput.html",
    "installation": "quickstart/install/index.html",
    "mate/rs232-port": "../quickstart/serial-port/hardware/mate/rs232-port.html",
    "rover/rs232-port": "../quickstart/serial-port/hardware/rover/rs232-port.html",
    "rover/rs485-port": "../quickstart/serial-port/hardware/rover/rs485-port.html",
    "tracer/rs485-port": "../quickstart/serial-port/hardware/tracer/rs485-port.html",
    "serial-ports": "quickstart/serial-port/identify.html",
    "solarthing-check": "quickstart/serial-port/solarthing-check.html",
    "other/headless-armbian": "../setup/headless-armbian.html",
    "other/headless-odroid": "../setup/headless-odroid.html",
    "other/headless-rpi": "../setup/headless-rpi.html",
    "other/install-couchdb": "../software/couchdb.html",
    "other/install-influxdb": "../software/influxdb.html",

    "quickstart/installation": "install/index.html",

    "config/commands/index": "../../actions/commands.html",
    "config/base-json/index": "../../config/file/base-json/index.html",
    "config/base-json/request/cpu-temperature": "../../config/file/base-json/request/cpu-temperature.html",
    "logging/index": "../misc/legacy/graylog.html",
    "other/remote-monitor": "../misc/legacy/remote-monitor.html",
    "other/security": "../misc/legacy/security.html",
    "stability": "maintenance/stability.html",
    "legacy/index": "../misc/legacy/index.html",
    "legacy/rpi-cpu-temp": "../misc/legacy/rpi-cpu-temp.html",

    "setup/index": "../misc/legacy/setup/index",
    "setup/headless-rpi": "../misc/legacy/setup/headless-rpi",
    "setup/headless-armbian": "../misc/legacy/setup/headless-armbian",
    "setup/headless-odroid": "../misc/legacy/setup/headless-odroid",

    "maintenance/logging/graylog": "../../misc/legacy/graylog.html",
    "maintenance/remote-monitor": "../misc/legacy/remote-monitor.html",
    "maintenance/security": "../misc/legacy/security.html",
}
