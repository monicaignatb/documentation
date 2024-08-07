# -- Project information -----------------------------------------------------

repository = 'documentation'
project = 'System Level Documentation'
copyright = '2024, Analog Devices, Inc.'
author = 'Analog Devices, Inc.'

# -- General configuration ---------------------------------------------------

extensions = [
    "adi_doctools", 'sphinx.ext.autodoc'
]

needs_extensions = {
    'adi_doctools': '0.3.17'
}

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
source_suffix = '.rst'

# -- External docs configuration ----------------------------------------------

interref_repos = ['doctools']

# -- Options for HTML output --------------------------------------------------

html_theme = 'cosmic'
