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
sys.path.insert(0, os.path.abspath('..'))


# -- Project information -----------------------------------------------------

project = 'Test'
copyright = '2020, BeeFi.io'
author = 'BeeFi'

# The full version, including alpha/beta/rc tags
release = '0.0.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc',
'sphinx.ext.doctest',
'sphinx.ext.intersphinx',
'sphinx.ext.todo',
'sphinx.ext.coverage',
'sphinx.ext.mathjax',
'sphinx.ext.ifconfig',
'sphinx.ext.viewcode',
'sphinx.ext.githubpages']


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
rst_prolog = """
.. include:: <s5defs.txt>
.. default-role::

"""
html_theme = 'sphinx_rtd_theme'

html_logo = 'BeeFi_Logo.png'
html_favicon = 'BeeFi_Logo.png'
master_doc = 'index'
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

latex_engine = 'pdflatex'

latex_elements = {

    # Logo on cover
    'maketitle': r'''
     \small BeeFi Technology
     \vspace{0mm}
     \begin{figure}[!h]
     \centering
     \includegraphics[scale=1.0]{BeeFi_Logo.png}
     \end{figure}
     ''',
  
    #footer
    #\usepackage{eso-pic}
    #\AddToShipoutPictureBG{%
    #\AtPageLowerLeft{\hspace{1cm}\includegraphics[scale=0.7]{BeeFi_Logo.png}}}
    
    # background image
    # footer logo and header logo, haven't been able to take them out of the cover page
  
    'preamble': r'''
    \usepackage{eso-pic,graphicx,transparent}
    \AddToShipoutPictureBG*{%
    \AtPageLowerLeft{%
    \transparent{0.4}\includegraphics[width=\paperwidth,height=\paperheight]{BeeFi_Logo.png}%
    }%
    }
   \usepackage{eso-pic}
   \usepackage{graphicx}
   \AddToShipoutPictureBG{%
   \AtPageUpperLeft{\hspace{1cm}\raisebox{-\height}{\includegraphics[scale=0.7]{BeeFi_Logo.png}}}%
}
    ''',
}

latex_logo = 'BeeFi_Logo.png'

latex_documents = [
    (master_doc, 'test.tex', 'Test',
     'Trieu Nguyen', 'manual' )
]

