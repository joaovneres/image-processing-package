from setuptools import setup, find_packages

with open("README.md", "r") as file:
    page_description = file.read()
    
with open("requirements.txt", "r") as file:
    requirements = file.read().splitlines()

setup(
    name = "image-processing-package",
    version = "0.0.1",
    author = "João Neres",
    author_email = "joaovneres@outlook.com"
    description = 'A package to process images',
    long_description = page_description,
    long_description_content_type = "text/markdown",
    packages = find_packages(),
    install_requires = requirements,
    python_requires = '>=3.6'
)