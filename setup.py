from setuptools import setup

long_description = """
# Implementation of Kalman Filter Variants

This package contains the Python implementation of several Kalman filter variants including Extended Kalman Filter,
Unscented Kalman Filter, Error State EKF, Square Root EKF, Invariant EKF, and more. 

The primary purpose of the provided software is to be easy to read and educational. The code is optimized neither for efficiency nor robustness.

"""

setup(
    name = "kalman variants",
    version = "1.0.0",
    author = "Jingxue Jiang",
    author_email = "jingxue07@gmail.com",
    description = ("A collection of Kalman Filter Nonlinear Variants"),
    license = "MIT",
    long_description = long_description,
    long_description_content_type='text/markdown',
    keywords = "robotics kalman filter state estimation",
    url = "",
    packages=['kalman_variants'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        'Intended Audience :: Developers',
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        "Topic :: Education",
        "Topic :: Scientific/Engineering",
        'Topic :: Scientific/Engineering :: Mathematics',

    ],
    install_requires=[
        'numpy','scipy', 'matplotlib'
    ],
    platforms='Linux, Mac, Windows',
)



