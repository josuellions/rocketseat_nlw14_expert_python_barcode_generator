### OmniStack - NLW 14 - Experts

#### Data: 05/02/2024 a 07/02/2024

#### RocketSeat

##### Educator: Rafael Ferreira

##### Developer: Josuel A. Lopes

#### About

Desenvolvimento de uma aplicação back-end em Python, utilizando Flask como framework, preparação de ambiente e boas práticas de projeto com Virtualenv, Pylint e versionamento de código usando pre-commit, criação do código de barras com python-barcode e testes com Pytest.
Aplicação que gera código barras e automação para utilização em logística com Python.

- Python
- Flask

##### Inicio projeto

- Referencia ambiente virtual python:
  https://pypi.org/project/virtualenv/
  https://packaging.python.org/pt-br/latest/guides/installing-using-pip-and-virtual-environments/

- Teste e Requestes API: Hoppscotch Browser Extension

```
git init
sudo apt-get install python3-pip
pip install virtualenv
python3 -m venv .venv
. .venv/bin/activate

```

##### Instalando e configurando bibliotecas

- Ferramentas padronização código
  ref: https://pre-commit.com/

```
pip install pylint
pylint --generate-rcfile > .pylintrc
pip install pre-commit
```

- Salvando config do python vm

```
.venv/bin/pip3 freeze > requirements.txt
```

- Instalando e configurando Flask
  ref:
  https://pypi.org/project/Flask/
  https://pypi.org/project/python-barcode/

```
pip install Flask
```

- Instalando e configurando Gerador Barras
  ref:
  https://pypi.org/project/python-barcode/
  https://pypi.org/project/pillow/

```
pip install pillow
pip install python-barcode
```

ou

```
python -m pip install barcode
```

- Subir servido python

```
python3 run_raw.py
```

- verificar se esta no ambiente virtual

```
which python
```

##### Instalando e configurando Cerberus

- Tratativa de Error
- - Ref:
    https://docs.python-cerberus.org/
    https://pypi.org/project/Cerberus/

    ```
    pip3 install Cerberus
    ```

##### Instalando e configurando PyTest

- Teste unitário
- - Ref:
    https://docs.pytest.org/en/8.0.x/
    https://pypi.org/project/pytest/

    ```
    pip install pytest
    pytest -s -v
    pytest
    ```
