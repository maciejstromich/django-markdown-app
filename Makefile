MODULE=django_markdown
VIRTUALENV=$(shell echo "$${VDIR:-'.env'}")


all: $(VIRTUALENV)

.PHONY: help
# target: help - Display callable targets
help:
	@egrep "^# target:" [Mm]akefile

.PHONY: clean
# target: clean - Clean repo
clean:
	@rm -rf build dist docs/_build django_markdown_app.egg-info
	find $(CURDIR) -name "*.pyc" -delete
	find $(CURDIR) -name "*.orig" -delete
	find $(CURDIR) -name "__pycache__" | xargs rm -rf
	find $(CURDIR) -name "django_markdown_app-?.?.?.dist-info" | xargs rm -rf

# ==============
#  Bump version
# ==============

.PHONY: release
VERSION?=minor
# target: release - Bump version
release:
	@pip install bumpversion
	@bumpversion $(VERSION)
	@git checkout master
	@git merge develop
	@git checkout develop
	@git push --all
	@git push --tags

.PHONY: minor
minor: release

.PHONY: patch
patch:
	make release VERSION=patch

.PHONY: major
major:
	make release VERSION=major


# ===============
#  Build package
# ===============

.PHONY: register
# target: register - Register module on PyPi
register:
	@python setup.py register

.PHONY: upload
# target: upload - Upload module on PyPi
upload: clean docs
	@pip install twine wheel
	@python setup.py sdist bdist_wheel
	@twine upload dist/*

.PHONY: docs
# target: docs - Compile and upload docs
docs:
	@pip install sphinx sphinx-pypi-upload
	@python setup.py build_sphinx --source-dir=docs/ --build-dir=docs/_build --all-files


# =============
#  Development
# =============

.PHONY: build
# target: build - Build the Docker image
build:
	docker compose build

.PHONY: shell
# target: shell - Open a bash shell in the container
shell:
	docker compose run --rm dev

.PHONY: test
# target: test - Run tox tests in Docker
test:
	docker compose run --rm dev tox

.PHONY: lint
# target: lint - Run ruff linter in Docker
lint:
	docker compose run --rm dev ruff check $(MODULE)

.PHONY: format
# target: format - Run ruff formatter in Docker
format:
	docker compose run --rm dev ruff format $(MODULE)
