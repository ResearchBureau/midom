docs_html:
	sphinx-build -M html docs/source docs/build

show_built_docs:
	xdg-open docs/build/html/index.html

launch_source_listener:
	(find docs/source/ -type f \( -name "*.rst" -o -name "*.puml" -o -name "*.py" \) | entr -s 'uv run make docs_html' & livereload docs/build/html -t docs/build/html/index.html) | cat

start_editing:
	uv run make launch_source_listener