import io
import os
from setuptools import setup, find_packages


def local_file(*name):
    return os.path.join(
        os.path.dirname(__file__),
        *name)


def read(*names, **kwargs):
    with io.open(
        os.path.join(os.path.dirname(__file__), *names),
        encoding=kwargs.get("encoding", "utf8")
    ) as fp:
        return fp.read()


def read_version():
    """Read the `(version-string, version-info)` from
    `src/{{cookiecutter.project_name}}/version.py`.
    """

    version_file = local_file(
        'src', '{{cookiecutter.project_name}}', 'version.py')
    local_vars = {}
    with open(version_file) as handle:
        exec(handle.read(), {}, local_vars)  # pylint: disable=exec-used
    return (local_vars['__version__'], local_vars['__version_info__'])


long_description = read(local_file('README.rst'), mode='rt')

setup(
    name='{{cookiecutter.project_name}}',
    version=read_version()[0],
    packages=find_packages('src'),

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
    package_dir={'': 'src'},
    # package_data={'{{cookiecutter.project_name}}': . . .},
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
