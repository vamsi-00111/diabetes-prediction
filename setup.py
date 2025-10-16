from typing import List
from setuptools import setup,find_packages

def find_requires(file:str) -> List[str]:
    with open(file,"r") as file:
        req=file.readlines()
        req=[ packages.replace("\n"," ") for packages in req]
        if "-e ." in req:
            req.remove("-e .")
        return req
setup(
    name="checking diabetes",
    version="0.1",
    author="vamsi",
    author_email="vamsigandavarpu101@gmail.com",
    packages=find_packages(),
    install_requires=find_requires("requirements.txt")
)
    
    
