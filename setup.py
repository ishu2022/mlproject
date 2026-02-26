from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [
            req.strip() for req in requirements
            if req.strip() and req.strip() != HYPEN_E_DOT and not req.startswith("#")
        ]
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Ishika',
    author_email='mohodishika2022@gmail.com',
    description="End-to-End Machine Learning Project",
    
    package_dir={"": "src"},               
    packages=find_packages(where="src"),  
    
    install_requires=get_requirements('requirements.txt'),
    python_requires=">=3.8",
)