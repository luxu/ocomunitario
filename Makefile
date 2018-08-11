.PHONY: test
test:
	py.test --cov tests/

.PHONY: unsed
unsed:
	autoflake --in-place --remove-unused-variables tests/*.py app/controllers/*/*.py app/*.py

.PHONY: format
format:
	autopep8 --in-place --aggressive --aggressive test/*.py app/controllers/*/*.py app/*.py