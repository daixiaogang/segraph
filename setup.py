from distutils.core import setup

from setuptools import setup, find_packages  # Always prefer setuptools over distutils
from codecs import open  # To use a consistent encoding
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, 'README'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='segraph',
    packages=['segraph'],  # this must be the same as the name above
    version='0.1',
    description='Creates graphs with edges and vertices from SLIC segments',
    author='Abhinandan Dubey',
    author_email='abhinandandubey@live.com',
    url='https://github.com/alivcor/segraph',  # use the URL to the github repo
    license='GNU GENERAL PUBLIC LICENSE',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: GNU GENERAL PUBLIC LICENSE',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2.7',
    ],
    download_url='https://github.com/alivcor/segraph/archive/0.1.tar.gz',  # I'll explain this in a second
    keywords=['testing', 'logging', 'example'],  # arbitrary keywords
)
