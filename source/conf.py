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
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Veda Online'
copyright = '2021, KanORS-EMR'
author = 'KanORS-EMR'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
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
html_theme = "furo"

# Logo for branding (appears in sidebar)
html_logo = "pages/images/vo_logo_bg_transparent.png"

# Theme options - hide project name text below logo and apply brand colors
html_theme_options = {
    "sidebar_hide_name": True,
    "light_css_variables": {
        # Primary brand color (dark blue)
        "color-brand-primary": "#1a4d7a",
        "color-brand-content": "#1a4d7a",
        # Secondary colors
        "color-foreground-primary": "#1a4d7a",
        "color-foreground-secondary": "#1a4d7a",
        # Links and accents - use secondary colors more prominently
        "color-link": "#f78e6e",  # Coral as primary link color
        "color-link--hover": "#1a4d7a",  # Dark blue on hover
        "color-link--visited": "#B0B8D8",  # Periwinkle for visited links
        # Sidebar - use secondary colors
        "color-sidebar-background": "#f8f9fa",
        "color-sidebar-background-border": "#B0B8D8",  # Periwinkle border
        "color-sidebar-brand-text": "#1a4d7a",
        "color-sidebar-link-text": "#1a4d7a",
        "color-sidebar-link-text--hover": "#f78e6e",  # Coral on hover
        "color-sidebar-link-text--active": "#f78e6e",  # Coral for active page
        "color-sidebar-link-text--top-level": "#1a4d7a",
        "color-sidebar-item-background--hover": "#B0B8D8",  # Periwinkle hover background
        "color-sidebar-item-background--current": "#B0B8D8",  # Periwinkle current page background
        # Code blocks - use secondary colors
        "color-code-background": "#f1f3f5",
        "color-code-foreground": "#1a4d7a",
        "color-code-background--inline": "#B0B8D8",  # Periwinkle for inline code
        # Admonitions and highlights - use secondary colors
        "color-admonition-title--note": "#1a4d7a",
        "color-admonition-title-background--note": "#B0B8D8",  # Periwinkle background
        "color-admonition-title--tip": "#f78e6e",  # Coral for tips
        "color-admonition-title-background--tip": "#f78e6e",
        "color-admonition-title--important": "#f78e6e",  # Coral for important
        "color-admonition-title-background--important": "#f78e6e",
        # Buttons and interactive elements
        "color-background-primary": "#ffffff",
        "color-background-secondary": "#B0B8D8",  # Periwinkle for secondary backgrounds
        "color-background-hover": "#f78e6e",  # Coral for hover backgrounds
    },
    "dark_css_variables": {
        # Primary brand color (dark blue)
        "color-brand-primary": "#1a4d7a",
        "color-brand-content": "#1a4d7a",
        # Secondary colors
        "color-foreground-primary": "#e0e0e0",
        "color-foreground-secondary": "#b0b0b0",
        # Links and accents - use secondary colors more prominently
        "color-link": "#f78e6e",  # Coral as primary link color
        "color-link--hover": "#6ba3d8",  # Lighter blue on hover
        "color-link--visited": "#B0B8D8",  # Periwinkle for visited links
        # Sidebar - use secondary colors
        "color-sidebar-background": "#1e1e1e",
        "color-sidebar-background-border": "#B0B8D8",  # Periwinkle border
        "color-sidebar-brand-text": "#ffffff",
        "color-sidebar-link-text": "#e0e0e0",
        "color-sidebar-link-text--hover": "#f78e6e",  # Coral on hover
        "color-sidebar-link-text--active": "#f78e6e",  # Coral for active page
        "color-sidebar-link-text--top-level": "#ffffff",
        "color-sidebar-item-background--hover": "#2a3d5a",  # Darker blue hover
        "color-sidebar-item-background--current": "#2a3d5a",  # Darker blue current page
        # Code blocks - use secondary colors
        "color-code-background": "#2d2d2d",
        "color-code-foreground": "#e0e0e0",
        "color-code-background--inline": "#3a4a5a",  # Darker blue for inline code
        # Admonitions and highlights - use secondary colors
        "color-admonition-title--note": "#1a4d7a",
        "color-admonition-title-background--note": "#B0B8D8",  # Periwinkle background
        "color-admonition-title--tip": "#f78e6e",  # Coral for tips
        "color-admonition-title-background--tip": "#f78e6e",
        "color-admonition-title--important": "#f78e6e",  # Coral for important
        "color-admonition-title-background--important": "#f78e6e",
        # Buttons and interactive elements
        "color-background-primary": "#1e1e1e",
        "color-background-secondary": "#2a3d5a",  # Darker blue for secondary backgrounds
        "color-background-hover": "#f78e6e",  # Coral for hover backgrounds
    },
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_css_files = [
    'custom.css',
]

html_js_files = [
    'image-lightbox.js',
]