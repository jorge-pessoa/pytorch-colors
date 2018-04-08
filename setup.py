# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pytorch_colors',
    packages=['pytorch_colors'],
    version='0.1.0',
    description='Utility to convert between color spaces for PyTorch Tensors and Variables',
    url='https://github.com/jorge-pessoa/pytorch-colors',
    author='Jorge Pessoa',
    author_email='jpessoa.on@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers'
    ],
    keywords='pytorch color space conversion tensor variable',
    project_urls={
        'Source': 'https://github.com/jorge-pessoa/pytorch-colors/',
    },
)
