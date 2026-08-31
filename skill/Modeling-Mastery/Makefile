.PHONY: install install-all test smoke demo-vault clean

install:
	python -m pip install -e ".[pdf]"

install-all:
	python -m pip install -e ".[all]"

test:
	python -m pytest

smoke:
	python -m compileall -q modeling_mastery scripts
	python -m modeling_mastery --help >/dev/null
	python scripts/validate_ir.py examples/demo_paper/paper_ir.json

demo-vault:
	python -m modeling_mastery pipeline examples/demo_paper/normalized_paper.md --workspace workspaces/demo --vault examples/generated_vault --provider none --backend markdown

clean:
	find . -type d -name '__pycache__' -prune -exec rm -rf {} +
	find . -type d -name '.pytest_cache' -prune -exec rm -rf {} +
	rm -rf build dist .coverage htmlcov
