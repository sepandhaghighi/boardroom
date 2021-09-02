# -*- coding: utf-8 -*-
"""Setup module."""
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='boardroom',
    packages=['boardroom'],
    version='0.1',
    description='Boardroom in Python',
    long_description="",
    long_description_content_type='text/markdown',
    author='Sepand Haghighi & Farzad Ramezani',
    author_email='sepand@4r7.ir',
    url='https://github.com/sepandhaghighi/boardroom',
    keywords="boardroom",
    project_urls={
        'Source': 'https://github.com/sepandhaghighi/boardroom',
        'Tracker': 'https://github.com/sepandhaghighi/boardroom/issues',
    },
    install_requires=[],
    python_requires='>=3.5',
    classifiers=[
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    license='MIT',
    include_package_data=True
)
