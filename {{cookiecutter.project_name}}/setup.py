import io
import os
import re
from setuptools import setup, find_packages


def read(*names, **kwargs):
    with io.open(
        os.path.join(os.path.dirname(__file__), *names),
        encoding=kwargs.get("encoding", "utf8")
    ) as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


long_description = read('README.md', mode='rt')

setup(
    name='{{cookiecutter.project_name}}',
    version=find_version('{{cookiecutter.project_name}}/version.py'),
    packages=find_packages(exclude=['contrib', 'docs', 'test*']),

    author='{{cookiecutter.author}}',
    author_email='{{cookiecutter.email_address}}',
    description='{{cookiecutter.short_description}}',
    license='{{cookiecutter.license}}',
    keywords='',
    url='{{cookiecutter.project_url}}',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
    ],
    platforms='any',
    include_package_data=True,
    install_requires=[],
    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax, for
    # example: $ pip install -e .[dev,test]
    extras_require={
        # 'dev': ['check-manifest', 'wheel'],
        # 'doc': ['sphinx', 'cartouche'],
        'test': ['hypothesis', 'pytest'],
    },
    entry_points={
        # 'console_scripts': [
        #    '{{cookiecutter.project_name}} = {{cookiecutter.project_name}}.cli:main',
        # ],
    },
    long_description=long_description,
)
