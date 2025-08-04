# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Path setup --------------------------------------------------------------
# Point Sphinx to the root of your project so it can find the Python modules.
sys.path.insert(0, os.path.abspath('../../'))


# -- Project information -----------------------------------------------------
project = 'PyTransport'
copyright = '2025, Andrea Costantini, David Mulryne, John W. Ronayne'
author = 'Andrea Costantini, David Mulryne, John W. Ronayne'
release = '3.0.0'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',   # Automatically generate docs from docstrings
    'sphinx.ext.napoleon',  # Support for NumPy and Google style docstrings
    'breathe',              # Bridge between Sphinx and Doxygen
]

templates_path = ['_templates']
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']


# -- Breathe Configuration -------------------------------------------------
# This tells Breathe where to find the Doxygen XML output.
breathe_projects = {
    "PyTransport3.0": "../build/doxygen/xml/"
}
breathe_default_project = "PyTransport3.0"
