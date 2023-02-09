SPHINXBUILD = sphinx-build

default: html

html:
	cd docs && make html

pypi:
	python3 setup.py sdist bdist_wheel;
	twine upload --skip-existing dist/*;

lint:
	flake8 goblet_gcp_client

coverage:
	export G_HTTP_TEST=REPLAY
	coverage run -m pytest goblet_gcp_client/tests;
	coverage report -m --include="goblet_gcp_client/*" --omit="goblet_gcp_client/tests/*";

tests:
	pytest goblet_gcp_client/tests;
