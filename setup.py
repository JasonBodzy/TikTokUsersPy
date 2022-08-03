from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.3'
DESCRIPTION = 'A WebScraper that provides tiktok user data.'
LONG_DESCRIPTION = 'Data includes followers, total likes, and statistics on the accounts last 30 videos including views, likes, comments, date, and description.'

# Setting up
setup(
    name="TikTokUsersPy",
    version=VERSION,
    author="Jason Bodzy",
    author_email="<jasonbodzy@gmail.com.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['selenium'],
    keywords=['python', 'tiktok', 'analytics', 'video', 'media', 'social'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
