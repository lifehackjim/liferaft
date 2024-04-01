# TODO

## Development Tools and Libraries

- **Packages to Use Eventually**
  - `Rich`: For pretty printing.
  - `Pendulum`: For datetime manipulation.
  - `httpx`: For async requests.
  - `mkdocs`: For documentation (requires hatch environment setup).
  - `logging.QueueHandler`: For advanced logging solutions.
  - `icecream`: For debugging in the development environment.
  - `hunter`: Useful for viewing Python workflows as code runs. [Hunter on GitHub](https://github.com/ionelmc/python-hunter?tab=readme-ov-file)
  - `pytest`: Control logging in CLI with logging options. A good example is provided in their documentation.

- **Debugging and Code Quality**
  - `Commitizen`: Research its purpose and usefulness.
  - `loguru`/`structlog`: Evaluate for logging.
  - `codecov`: Clean up old projects and understand the upload process. [Codecov](https://app.codecov.io/gh/lifehackjim)
  - `pre-commit`: Consider setup implications for enforcing code quality without burdening the user. Debate on enforcing pre-commit setup on users.
  - `ruff.toml`: Do we need to add `pydantic.field_validator` to `[lint.pep8-naming].classmethod-decorators`?
  - disable pylance in user settings, only enable it in workspace settings

## Documentation and Versioning

- **Documentation**
  - `mike`: Assess for documentation utility.
  - `mkdocs-material`: Experiment with for enhancing documentation.
  - Document tests: Consider a decorator for including tests in documentation.
  - `STYLE.md`: Develop or find a comprehensive style guide for consistency. Explore other examples like [STYLE.md](https://github.com/bentoml/OpenLLM/blob/fbab26ddc412d79efbae12f6c58c7b8c0a9fbca8/STYLE.md) for inspiration.
  - `hatch fancy pypi readme`: Investigate for attractive READMEs. [Hatch Fancy PyPI README](https://github.com/hynek/hatch-fancy-pypi-readme?tab=readme-ov-file)
  - Explore various documentation practices from repositories like [scientific-python/cookie](https://github.com/scientific-python/cookie?tab=readme-ov-file).

## Automation and CI/CD

- **GitHub Actions**
  - `act`: For GitHub Actions testing.
  - Set up CI/CD pipeline using GitHub actions. Explore various CI/CD practices, including GPG for PyPI test publishing ([Example](https://github.com/Erotemic/xdoctest/blob/main/.github/workflows/tests.yml#L479)) and GitHub Actions environmental variables usage for coverage reports.

## pyproject.toml Examples and Insights

- Examine the use of `hatch` and other tools within `pyproject.toml` across various projects for best practices in Python package development.
  - **Noteworthy `pyproject.toml` Examples:**
    - OpenLLM use of hatch and namespace files. [OpenLLM](https://github.com/bentoml/OpenLLM/blob/fbab26ddc412d79efbae12f6c58c7b8c0a9fbca8/pyproject.toml)
    - complex coverage and dependency setup. [example 1](https://github.com/scikit-hep/hist/blob/main/pyproject.toml), [example 2](https://fuchsia.googlesource.com/third_party/github.com/platformdirs/platformdirs/+)
    - advanced pytest and coverage configurations. [example 1](https://github.com/ansible/ansible-lint/blob/main/pyproject.toml#L13-L24), [example 2](https://github.com/tiangolo/fastapi/blob/cb0ab4322456c52a3b8463d217f3445a82cbbf9c/pyproject.toml#L136)
    - [Towncrier usage](https://github.com/RasaHQ/rasa/blob/7807b19ad5fffab73ca1a04dc710f812115a9288/pyproject.toml#L28)
    - Innovative hatch.toml configurations in various projects for managing dependencies and versioning.
