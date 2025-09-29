from setuptools import find_packages,setup
from typing import List


def get_req(filepath: str)-> List[str]:
    requirements=[]
    with open(filepath)as file_obj:
            requirements=file_obj.readlines()
            requirements = [req.strip() for req in requirements if req.strip() and not req.startswith("-e")]
    return requirements
              


setup (name='Fault_detection',
      version='0.01',
      author='Teja',
      author_email='Tejamtrsms@gmail.com',
      install_requires= get_req('requirements.txt'),
      packages=find_packages()
      )