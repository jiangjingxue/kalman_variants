from setuptools import setup, find_packages  # Always prefer setuptools over distutils
from codecs import open  # To use a consistent encoding
from os import path
import kalman_variants

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='kalman_variants',
    description='Kalman filter variants implementation',
    long_description=long_description,

        # The project's main homepage.
    url='https://github.com/jiangjingxue/kalman_filter_variants',

    # Author details
    author='Jingxue Jiang',
    author_email='jingxue07@gmail.com',

    # Choose your license
    license='MIT',

    install_requires=['numpy', 'scipy', 'matplotlib'],

)



