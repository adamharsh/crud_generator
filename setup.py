from setuptools import setup
with open("README.md","r") as fh:
    long_description = fh.read()
setup(
    name='crud_generator',
    version='1.0.1',
    description='This will generate a crud operations (crud.py) for your Database tables.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    py_modules=["crud_generator"],
)
