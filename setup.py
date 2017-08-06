from distutils.core import setup


with open('README.md') as file:
    long_description = file.read()

setup(
    name='Seventime Python3 library',
    version='0.1',
    description='Python API wrapper library for CRM system Seventime.',
    author='Andreas Klintberg',
    author_email='ankl@kth.se',
    long_description=long_description,
    py_modules=['seventime']
)