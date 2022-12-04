from setuptools import setup, find_packages

setup(
    name="cbp-translate",
    version="0.0.1",
    url="https://github.com/elanmart/cbp-translate.git",
    author="Marcin Elantkowski",
    author_email="marcin.elantkowski@gmail.com",
    packages=find_packages(
        include=["cbp_translate", "cbp_translate.*"], exclude=["playground"]
    ),
)
