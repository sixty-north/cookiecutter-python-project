from pathlib import Path
from setuptools import setup, find_packages


setup(
    name='{{cookiecutter.project_name}}',
    version="{{cookiecutter.version}}",
    packages=find_packages('source'),

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
    package_dir={'': 'source'},
    # package_data={'{{cookiecutter.project_name}}': . . .},
    install_requires=[],
    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax, for
    # example: $ pip install -e .[dev,test]
    extras_require={
        'dev': ['black', 'bump2version'],
        # 'doc': ['sphinx', 'cartouche'],
        'test': ['hypothesis', 'pytest'],
    },
    entry_points={
        # 'console_scripts': [
        #    '{{cookiecutter.project_name}} = {{cookiecutter.project_name}}.cli:main',
        # ],
    },
    long_description=Path('README.rst').read_text(encoding='utf-8'),
)
