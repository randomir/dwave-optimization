# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import subprocess

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    # extensions provided by sphinx
    'sphinx.ext.autosummary',
    'sphinx.ext.autodoc',
    'sphinx.ext.coverage',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.mathjax',
    'sphinx.ext.napoleon',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
    'sphinx.ext.ifconfig',

    # other extensions
    'reno.sphinxext',
    'sphinx_design',
    'breathe',
]

autosummary_generate = True

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
source_suffix = ['.rst']

# The master toctree document.
master_doc = 'index'

# General information about the project.
# from dwave.optimization import package_info
# project = package_info.__title__
# copyright = package_info.__copyright__
# author = package_info.__author__
# version = package_info.__version__
# release = package_info.__version__

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'en'

add_module_names = False
# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['build', 'Thumbs.db', '.DS_Store', 'sdk_index.rst']

linkcheck_retries = 2
linkcheck_anchors = False
linkcheck_ignore = [r'https://cloud.dwavesys.com/leap',  # redirects, many checks
                    r'.clang-format',
                    r'setup.cfg',
                    ]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

modindex_common_prefix = ['dwave.optimization.']

doctest_global_setup = """

import dwave.optimization

"""

autodoc_type_aliases = {
    'numpy.typing.ArrayLike': 'numpy.typing.ArrayLike',
}

# -- Breathe --------------------------------------------------------------

breathe_projects = {
  'dwave-optimization': os.path.join(os.path.dirname(os.path.abspath(__file__)), 'build', 'doxygen', 'xml'),
}

# see https://breathe.readthedocs.io/en/latest/readthedocs.html
if os.environ.get('READTHEDOCS', False):
    subprocess.call('make cpp', shell=True, cwd=os.path.dirname(os.path.abspath(__file__)))

# -- Options for HTML output ----------------------------------------------

html_theme = "pydata_sphinx_theme"

html_theme_options = {
    "collapse_navigation": True,
    "show_prev_next": False,
}
html_sidebars = {"**": ["search-field", "sidebar-nav-bs"]}  # remove ads

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']

def setup(app):
   app.add_css_file('cookie_notice.css')
   app.add_js_file('cookie_notice.js')
   app.add_config_value('target', 'repo', 'env')

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {'python': ('https://docs.python.org/3', None),
                       'numpy': ('https://numpy.org/doc/stable/', None),
                       'networkx': ('https://networkx.org/documentation/stable/', None),
                       'oceandocs': ('https://docs.ocean.dwavesys.com/en/stable/', None),
                       'sysdocs_gettingstarted': ('https://docs.dwavesys.com/docs/latest/', None),
                       }

rst_epilog = """
.. |array-like| replace:: array-like
.. _array-like: https://numpy.org/devdocs/glossary.html#term-array_like
"""
