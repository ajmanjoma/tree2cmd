# ============================================================
#  Makefile for tree2cmd — Developer Workflow
# ============================================================

PACKAGE=tree2cmd
VENV=.venv
PYTHON=$(VENV)/bin/python
PIP=$(VENV)/bin/pip

# -------------------------------
# Help
# -------------------------------
.PHONY: help
help:
	@echo ""
	@echo "Developer Makefile for $(PACKAGE)"
	@echo ""
	@echo "Commands:"
	@echo "  make venv              - Create virtual environment"
	@echo "  make activate          - Show activate command"
	@echo "  make install           - Install package in editable mode with dev tools"
	@echo "  make build             - Build wheel + sdist"
	@echo "  make test              - Run unittest suite"
	@echo "  make lint              - Run flake8 + black checks"
	@echo "  make format            - Auto-format code using black"
	@echo "  make typecheck         - Run mypy static type analysis"
	@echo "  make preview FILE=xxx  - Preview generated commands"
	@echo "  make install-local     - Install built wheel locally"
	@echo "  make uninstall         - Uninstall package"
	@echo "  make clean             - Remove build artifacts"
	@echo ""

# -------------------------------
# Virtual Environment
# -------------------------------
.PHONY: venv activate
venv:
	python3 -m venv $(VENV)
	@echo "✔ Virtual environment created."

activate:
	@echo "source $(VENV)/bin/activate"

# -------------------------------
# Install (Dev Mode)
# -------------------------------
.PHONY: install
install: venv
	$(PIP) install --upgrade pip build wheel setuptools
	$(PIP) install -e .
	$(PIP) install black flake8 mypy
	@if [ -f requirements.txt ]; then $(PIP) install -r requirements.txt; fi
	@echo "✔ Development environment ready."

# -------------------------------
# Build Package
# -------------------------------
.PHONY: build
build:
	$(PYTHON) -m build
	@echo "✔ Build complete (dist/*)"

# -------------------------------
# Local Install From Wheel
# -------------------------------
.PHONY: install-local
install-local:
	$(PIP) install dist/$(PACKAGE)-*.whl
	@echo "✔ Installed local wheel"

# -------------------------------
# Run Tests
# -------------------------------
.PHONY: test
test:
	$(PYTHON) -m unittest discover -s tests -p "test*.py" -v


# -------------------------------
# Linting
# -------------------------------
.PHONY: lint
lint:
	flake8 $(PACKAGE)
	black --check $(PACKAGE)

# -------------------------------
# Auto-Format Code
# -------------------------------
.PHONY: format
format:
	black $(PACKAGE) tests

# -------------------------------
# Type Checking
# -------------------------------
.PHONY: typecheck
typecheck:
	mypy $(PACKAGE)

# -------------------------------
# Preview Output
# -------------------------------
.PHONY: preview
preview:
	@if [ -z "$(FILE)" ]; then \
		echo "Usage: make preview FILE=struct.txt"; \
		exit 1; \
	fi
	$(VENV)/bin/tree2cmd $(FILE)

# -------------------------------
# Uninstall Package
# -------------------------------
.PHONY: uninstall
uninstall:
	-$(PIP) uninstall -y $(PACKAGE) || true

# -------------------------------
# Clean Build Artifacts
# -------------------------------
.PHONY: clean
clean:
	rm -rf build dist *.egg-info .pytest_cache
	@echo "✔ Cleaned build artifacts."
