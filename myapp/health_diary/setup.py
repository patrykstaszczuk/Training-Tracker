from setuptools import find_packages, setup

setup(
    name="health-diary",
    version="0.0.1",
    packages=find_packages(),
    install_requires=["django-injector"],
)
