from setuptools import findall
from setuptools import setup, find_packages

mod1_pkgs = [pkg for pkg in find_packages('.') if pkg.startswith('mod1')]

setup(
    name="mod1",
    packages=mod1_pkgs
)

