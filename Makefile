docs_html:
	sphinx-build -M html docs/source docs/build

show_built_docs:
	xdg-open docs/build/html/index.html