#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""The setup script."""
import sys

from setuptools import setup, find_packages


def get_version(filename):
    """Extract the package version"""
    with open(filename, encoding='utf8') as in_fh:
        for line in in_fh:
            if line.startswith('__version__'):
                return line.split('=')[1].strip()[1:-1]
    raise ValueError("Cannot extract version from %s" % filename)


with open('README.rst', encoding='utf8') as readme_file:
    readme = readme_file.read()

try:
    with open('HISTORY.rst', encoding='utf8') as history_file:
        history = history_file.read()
except OSError:
    history = ''

# requirements for use
requirements = ['glom', 'numpy', 'scipy', 'qutip', 'uniseg']

# requirements for development (testing, generating docs)
dev_requirements = [
    'click',
    'coverage',
    'flake8',
    'gitpython',
    'isort',
    'jupyter',
    'matplotlib',
    'nbsphinx',
    'nbval',
    'pep8',
    'pylint',
    'pytest',
    'pytest-cov',
    'pytest-xdist',
    'sphinx',
    'sphinx-autobuild',
    'sphinx_rtd_theme',
    'sphinxcontrib-bibtex',
    'twine',
    'watermark',
    'weylchamber>=0.3.1',
    'wheel',
]
dev_requirements.append('better-apidoc==0.3.1')
if sys.version_info >= (3, 6):
    dev_requirements.append('black')

# some recommended packages that make development nicer
dev_extras = ['jupyterlab', 'pdbpp']

version = get_version('./src/krotov/__init__.py')

setup(
    author="Michael Goerz",
    author_email='mail@michaelgoerz.net',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Framework :: Jupyter',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Physics',
    ],
    description=(
        "Python implementation of Krotov's method for quantum optimal control"
    ),
    python_requires='~=3.5',
    install_requires=requirements,
    extras_require={'dev': dev_requirements, 'extras': dev_extras},
    license="BSD license",
    long_description=readme + '\n\n' + history,
    long_description_content_type='text/x-rst',
    include_package_data=True,
    keywords='krotov',
    name='krotov',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    url='https://github.com/qucontrol/krotov',
    version=version,
    zip_safe=False,
)
