.PHONY: test
test:
	python -m unittest discover tests

.PHONY: unsed
unsed:
	autoflake --in-place --remove-unused-variables tests/*.py app/controllers/*/*.py app/*.py

.PHONY: format
format: unsed
	autopep8 --in-place --aggressive --aggressive test/*.py app/controllers/*/*.py app/*.py

.PHONY: clean-pyc clean-build clean
clean: clean-build clean-pyc

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr *.egg-info
	rm -fr *.egg

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +