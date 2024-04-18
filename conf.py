# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'DFMEA with LLMs'
copyright = '2024,GIIA,ENSAM-Meknès'
author = 'Graziella'


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['/Documentation/Scripts/_static']
