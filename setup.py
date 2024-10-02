import setuptools 

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name="image-processing-package", 
    version="0.0.1",
    author="Gustavo de Assis Cavalheiro",
    author_email="gustavocavalheiro2015@gmail.com",
    description="A small package for image processing",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Kavas07/image-processing-package",
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
    install_requires=requirements,
)
