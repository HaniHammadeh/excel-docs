import os
import sys
sys.path.insert(0, os.path.abspath('.'))

project = 'Excel Docs'
author = 'Hani'
release = '1.0'

extensions = [
    'myst_parser',
]

source_suffix = {
    '.md': 'markdown',
}

master_doc = 'index'

html_theme = 'furo'

html_static_path = ['_static']
