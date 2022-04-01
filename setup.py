from platform import python_revision
from pkg_resources import Requirement
from setuptools import setup, find_packages

with open("readme.md","r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="gerador_de_senhas",
    #version="0.0.1",
    author="Diego_Jaques",
    author_email="diegojaques2016@gmail.com",
    description=" Pacote de gerador de senhas",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/diegoJaques/gerador-de-senhas-Complexas--Python",
    packages=find_packages(),
    #install_requires=Requirement,
    python_requires=">=3.8",
)
