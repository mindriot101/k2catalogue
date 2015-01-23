from setuptools import setup, find_packages

setup(
    name='k2catalogue',
    version='0.0.1',
    author='Simon Walker',
    packages=find_packages(exclude=['venv']),
    entry_points={
        'console_scripts': [
            'k2cat-search = k2catalogue.cli:main',
        ],
    }
)