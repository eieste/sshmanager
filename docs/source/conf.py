# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
import django
import sphinx_theme

sys.path.insert(0, os.path.abspath('../../'))

os.environ['DJANGO_SETTINGS_MODULE'] = 'sshmanager.settings'
django.setup()


# -- Project information -----------------------------------------------------

project = 'sshmanager'
copyright = '2019, Stefan Eiermann'
author = 'Stefan Eiermann'

# The full version, including alpha/beta/rc tags
release = 'development'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinxcontrib.mermaid',
    'sphinx.ext.autodoc',
    'sphinx.ext.coverage',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#

html_theme = 'neo_rtd_theme'
html_theme_path = [sphinx_theme.get_html_theme_path()]

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

intersphinx_mapping = {
    'urllib3': ('http://urllib3.readthedocs.org/en/latest', None),
    'django': ('http://django.readthedocs.org/en/latest/', None),
    'python': ('http://docs.python.org/3', None),
}


master_doc = 'index'

