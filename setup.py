from setuptools import setup, find_packages

setup(name='ArtC',
    version='1.0',
    description='Art Classifier using CNNs',
    author='Daan Meijers, Wouter de Bruijn',
    author_email='daanmeijers@live.nl',
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    install_requires=[
        "tensorflow>=2.1.0"
    ]
)