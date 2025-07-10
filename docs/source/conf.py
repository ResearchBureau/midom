# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import os

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "midom"
copyright = "2025, sjoerdk"
author = "sjoerdk"
release = "0.1"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# -- PDF output options ------------------------------------------------------
extensions = ["sphinxcontrib.plantuml"]

# For ReadTheDocs environment
if os.environ.get("READTHEDOCS", False):
    plantuml = "plantuml"
else:
    # Local development path (adjust as needed)
    plantuml = "java -jar /usr/share/java/plantuml.jar"


templates_path = ["_templates"]
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]

from sphinx.builders.html import StandaloneHTMLBuilder  # noqa: E402


StandaloneHTMLBuilder.supported_image_types = [
    "image/gif",
    "image/png",
    "image/svg+xml",
    "image/jpeg",
]
