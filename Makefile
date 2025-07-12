# Makefile for tree2cmd CLI Tool

PACKAGE_NAME=tree2cmd
VENV_PATH=venv
PYTHON=$(VENV_PATH)/bin/python
PIP=$(VENV_PATH)/bin/pip

.PHONY: help venv install build install-local test clean uninstall preview

help:
	@echo "Usage:"
	@echo "  make venv             # Create virtual environment"
	@echo "  make install          # Install dev dependencies"
	@echo "  make build            # Build package (sdist and wheel)"
	@echo "  make install-local    # Install built wheel locally"
	@echo "  make test             # Run unit tests"
	@echo "  make preview FILE=sample.txt  # Preview shell commands from tree text"
	@echo "  make uninstall        # Uninstall the tree2cmd package"
	@echo "  make clean            # Remove build artifacts"

venv:
	python3 -m venv $(VENV_PATH)
	@echo "Run 'source venv/bin/activate' to activate virtual environment."

install: venv
	$(PIP) install --upgrade pip setuptools wheel
	$(PIP) install -r requirements.txt || true  # Optional

build:
	$(PYTHON) setup.py sdist bdist_wheel

install-local:
	$(PIP) install dist/$(PACKAGE_NAME)-*.whl

test:
	$(PYTHON) -m unittest discover tests

preview:
	$(VENV_PATH)/bin/tree2cmd $(FILE)

uninstall:
	-$(PIP) uninstall -y $(PACKAGE_NAME)

clean:
	rm -rf build dist *.egg-info

