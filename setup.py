from setuptools import find_packages, setup
from typing import List


def get_requirements(file_path:str)->list:
    '''
    This function reads the requirements.txt file and returns the list of requirements
    '''
    requirements = []
    hyphen_e_dot = '-e .'
    with open(file_path) as file_obj:
        requirements = file_obj.read().splitlines()
        requirements=[req.replace("\n", " ") for req in requirements]

        if hyphen_e_dot in requirements:
            requirements.remove(hyphen_e_dot)
    return requirements

setup(
    name='my_package',
    version='0.1',
    packages=find_packages(),
    author='Ragu',
    author_email= 'ragu.james20@gmail.com',
    install_requires=get_requirements('requirements.txt'),

    
)
