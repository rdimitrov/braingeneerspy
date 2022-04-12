from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='braingeneerspy',
    version='0.1.0',
    python_requires='>=3.6.0',
    description='Braingeneers Python utilities',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/braingeneers/braingeneerspy',
    author='Braingeneers',
    include_package_data=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Braingeneers, collaborators',
        'Programming Language :: Python :: 3',
        'License :: MIT',
    ],
    packages=find_packages(exclude=()),
    # Include only the minimum dependencies for working with data in install_requires
    # Consider the minimum necessary dependencies that would be installed on a RaspberryPI
    install_requires=[
        'matplotlib',
        'requests',
        'numpy',
        'scipy',
        'tenacity',
        'awswrangler',
        'sortedcontainers',
        'powerlaw',
        'boto3==1.17.96',  # depends on awscrt==0.11.22
        'smart_open>=5.1.0',
    ],
    # Include dependencies for specific use cases in extra_requires, additional categories
    # can be added, but 'all' should contain dependencies for all user cases.
    extras_require={
        'all': [
            # iot
            'awsiotsdk==1.6.0',
            'redis',
            # ml
            'torch',
            # hengenlab
            'neuraltoolkit @ git+https://github.com/hengenlab/neuraltoolkit.git',
        ],
        'iot': [
            'awsiotsdk==1.6.0',
            'redis',
        ],
        'ml': [
            'torch'
        ],
        'hengenlab': [
            'neuraltoolkit @ git+https://github.com/hengenlab/neuraltoolkit.git'
        ],
    }
)
