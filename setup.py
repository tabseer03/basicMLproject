# helps to build and set up the package for distribution
from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT = "-e ."

def get_requirements(file_path:str)->List[str]:
    """This function will return the list of requirements"""
    requirements = []
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
    name='mlProject',
    version='0.0.1',
    author='Tabseer',
    author_email='tabseer03@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)