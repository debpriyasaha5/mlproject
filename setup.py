from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path:str) -> List[str]:
    requirements = []
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [req.replace('\n', '') for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
name='mlproject',
version='0.0.1',
author='Debpriya',
author_email='debpriyasaha5@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txts')#['pandas', 'numpy', 'seaborn', 'matplotlib', 'scikit-learn', 'xgboost', 'lightgbm', 'catboost', 'joblib']

)