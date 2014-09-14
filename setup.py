from setuptools import setup

__author__ = 'Atsushi Odagiri <aodagx@gmail.com>'
__version__ = '0.0'

requires = [
]

setup(
    name="aodag.hello",
    version=__version__,
    description="sample package",
    long_description="""\
aodag.hello
==================

sample package
    """,
    author=__author__,
    author_email="aodagx@gmail.com",
    packages=["aodag.hello"],
    namespace_packages=["aodag"],
    install_requires=requires,
    url="http://example.com/aodag.hello"
)
