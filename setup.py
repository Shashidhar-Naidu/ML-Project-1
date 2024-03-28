from setuptools import setup, find_packages
from typing import List


HYPEN_E_DOT = '-e .'
def get_requirements(filename) -> List[str]:
    '''
    Read requirements from requirements.txt
    '''
    with open(filename) as f:
        requirements = f.read().splitlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
    name='ML Project 1',
    author='Shashidhar Naidu Boya',
    version='0.0.1',
    packages=find_packages(),
    author_email='shashidharnaiduboya@gmail.com',
    install_requires=get_requirements('requirements.txt')
)


