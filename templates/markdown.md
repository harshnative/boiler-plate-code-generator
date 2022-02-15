# Index : 
1. gitignore / gi
    1. gi-python
2. html
    1. html-main
3. python / py
    1. py-main
    2. py-pytest_config
4. shellscripts / sh
    1. sh-install_jupyter
    2. sh-install_pytest

<br>
<br>
<br>
<br>
<br>


# 1. gitignore / gi
<br>
<br>

### 1. gi-python

<br>

```gitignore
myvirtual/

apis.txt

apis.py

binFiles/

*.ini

*.bin

tempTest/

temp/

*.txt

testing/

assets/

releases/

tempCodeRunnerFile.py


# Byte-compiled / optimized / DLL files
__pycache__/
*.pyc
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
#  Usually these files are written by a python script from a template
#  before PyInstaller builds the exe, so as to inject date/other infos into it.
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/
cover/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
.pybuilder/
target/

# Jupyter Notebook
.ipynb_checkpoints

# IPython
profile_default/
ipython_config.py

# pyenv
#   For a library or package, you might want to ignore these files since the code is
#   intended to run in multiple environments; otherwise, check them in:
# .python-version

# pipenv
#   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.
#   However, in case of collaboration, if having platform-specific dependencies or dependencies
#   having no cross-platform support, pipenv may install dependencies that don't work, or not
#   install all needed dependencies.
#Pipfile.lock

# PEP 582; used by e.g. github.com/David-OConnor/pyflow
__pypackages__/

# Celery stuff
celerybeat-schedule
celerybeat.pid

# SageMath parsed files
*.sage.py

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# Pyre type checker
.pyre/

# pytype static type analyzer
.pytype/

# Cython debug symbols
cython_debug/
```
<br>
<br>
<br>


<br>
<br>
<br>
<br>
<br>



# 2. html
<br>
<br>

### 1. html-main

<br>

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    
</body>
</html>
```
<br>
<br>
<br>


<br>
<br>
<br>
<br>
<br>



# 3. python / py
<br>
<br>

### 1. py-main

<br>

```python





def main():
    pass





if __name__ == "__main__":
    main()
```
<br>
<br>
<br>

### 2. py-pytest_config

<br>

```python
[pytest]

addopts = --html=pytest_results.html --junitxml="pytest_results.xml" -v --ignore=assets/ --ignore=binFiles/ --ignore=myvirtual/ 


```
<br>
<br>
<br>


<br>
<br>
<br>
<br>
<br>



# 4. shellscripts / sh
<br>
<br>

### 1. sh-install_jupyter

<br>

```shellscripts
# set up virtual env
virtualenv myvirtual

sleep 3

# activate virtual env
. myvirtual/bin/activate


# install jupyter notebook and related packages
pip install ipykernel

pip install numpy

pip install pandas

pip install nbconvert

pip install notebook

# install and activate dark theme
pip install jupyterthemes

jt -t onedork
```
<br>
<br>
<br>

### 2. sh-install_pytest

<br>

```shellscripts
. myvirtual/bin/activate

pip install pytest

pip install pytest-html

pip install pytest-xdist

pip install pytest-benchmark

pip install pytest-repeat
```
<br>
<br>
<br>


<br>
<br>
<br>
<br>
<br>

