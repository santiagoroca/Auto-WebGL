from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name='autowebgl',

    version='0.2.0',

    description='Automation Tool for WebGL based Projects',

    url='https://github.com/santiiiii/autowebgl',

    author='Santiago Nicolas Roca',
    author_email='snroca@hotmail.com',

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    keywords='webgl automation devop image comparison',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    install_requires=['selenium', 'scipy'],

    entry_points={
        'console_scripts': [
            'sample=sample:main',
        ],
    },
)
