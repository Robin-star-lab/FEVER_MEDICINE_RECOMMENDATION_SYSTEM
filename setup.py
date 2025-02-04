from setuptools import setup, find_packages
from typing import List
def get_requirements(filepath)->List[str]:
    requirements = []
    with open(filepath, 'r') as f:
        requirements = f.readlines()
        requirements = [req.replace('/n','') for req in requirements]
        if '-e .' in requirements:
            requirements.remove('-e .')
            
            return requirements


setup(
    name = "Fever Medicine Recommendation",
    version = "0.0.1",
    author = "Robin Aluma",
    author_email = "alumarobin@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)