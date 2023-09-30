# playwright-pytest-bug

Reproducing hanging teardown with [playwright-pytest](https://github.com/microsoft/playwright-pytest) fixture.

See: https://github.com/microsoft/playwright-pytest/issues/187

## To reproduce

1. `python3 -m venv .venv`
2. `source .venv/bin/activate`
3. `pip install -r requirements.txt`
4. `pytest --setup-show`

This hangs on tearing down the `playwright` fixture (use CTRL+C to terminate).
