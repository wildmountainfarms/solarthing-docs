# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'SolarThing'
copyright = '2021, Joshua Shannon'
author = 'Joshua Shannon'

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
    #'sphinxcontrib.globalsubs',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'


extlinks = {
    'issue-page': ('https://github.com/wildmountainfarms/solarthing/issues', 'issues'),
    'issue': ('https://github.com/wildmountainfarms/solarthing/issues/%s', '#%s'),
    'blob': ('https://github.com/wildmountainfarms/solarthing/blob/%s', 'solarthing/blob/%s'),
    'tree': ('https://github.com/wildmountainfarms/solarthing/tree/%s', 'solarthing/tree/%s'),
}

# We aren't using global substitutions now, so keep this commented
#global_substitutions = {
#    'issues': 'https://github.com/wildmountainfarms/solarthing/issues'
#}
