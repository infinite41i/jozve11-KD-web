# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'جزوه درس تولید کننده و توسعه دهنده پایگاه های اینترنتی'
copyright = 'توحیدی - 1404'
author = 'علی توحیدی'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'shibuya'
pygments_style = "sphinx"
pygments_dark_style = "native"

# These folders are copied to the documentation's HTML output
html_static_path = ['_static']

# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
html_css_files = [
    'css/fa.css',
]

# -- Options for EPUB output
epub_show_urls = 'footnote'
