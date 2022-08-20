import setuptools
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(os.path.dirname(dir_path), "README.rst"), "r") as fh:
    long_description = fh.read()

import contact_sam

setuptools.setup(
    name="contact_sam",
    version=contact_sam.version,
    author="Samuel Mehalko",
    author_email="samuel.mehalko@ngc.com",
    description="A semi-creative excuse to make a both a python package and business cards",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    license="GPLv3",
    url="https://contact-sam.github.io/contact_sam",
    download_url="https://github.com/contact-sam/contact_sam/tags",
    project_urls={
        'Source': 'https://github.com/contact-sam/contact_sam',
    },
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Topic :: Documentation :: Sphinx",
        "Topic :: Office/Business",
    ],
)