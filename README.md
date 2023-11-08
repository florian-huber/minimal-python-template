![GitHub](https://img.shields.io/github/license/florian-huber/minimal-python-template)
![GitHub Workflow Status (with event)](https://img.shields.io/github/actions/workflow/status/florian-huber/minimal-python-template/basic_ci.yml)


# Minimal Python template
A minimal cookiecutter template to start your own Python project.

There are many great Python cookiecutter templates, such as one by [Jace Browning](https://github.com/jacebrowning/template-python/tree/main) or one by [Netherlands eScience Center template](https://github.com/NLeSC/python-template) (from which this repository borrowed several pieces, e.g., the initial dummy code parts). The idea of the one in this repository is to provide a strongly reduced template for simpler repositories or beginners.


## How to use this

You need `cookiecutter` installed (e.g. using pip). Then you can create a new repository by running:
```
cookiecutter https://github.com/florian-huber/minimal-python-template.git
```

## What this will do
Running this template as described above will generate a Python project folder that gets your new project started properly. I hope.
You should get a project folder with the following structure in it:

```text
my-python-project/
├── .github
│   └── workflows
│       └── basic_ci.yml
├── .gitignore
├── CODE_OF_CONDUCT.md
├── LICENSE
├── my_python_package
│   ├── __init__.py
│   ├── my_module.py
│   └── __version__.py
├── pyproject.toml
├── README.md
└── tests
    ├── __init__.py
    └── test_my_module.py
```
