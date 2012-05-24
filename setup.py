from setuptools import find_packages
from setuptools import setup

import os


readme_file= os.path.join('Products', 'PloneGazette', 'README.txt')
desc = open(readme_file).read().strip()
changes_file = os.path.join('Products', 'PloneGazette', 'HISTORY.txt')
changes = open(changes_file).read().strip()

long_description = desc + '\n\nCHANGES\n=======\n\n' +  changes 

setup(
    name='Products.PloneGazette',
    version='3.2-d81540690',
    author='Pilot Systems, Nidelven IT LTD and others',
    author_email='',
    maintainer='Morten W. Petersen',
    maintainer_email='info@nidelven-it.no',
    classifiers=[
        "Framework :: Plone",
        "Framework :: Plone :: 4.1",
        "Framework :: Plone :: 4.2",
        "Framework :: Plone :: 4.3",
        "Programming Language :: Python",
    ],
    keywords='Zope plone newsletter communication',
    url='http://plone.org/products/plonegazette',
    description='A complete Newsletter product for Plone.',
    long_description=long_description,
    packages=['Products', 'Products.PloneGazette'],
    include_package_data = True,
    zip_safe=False,
    namespace_packages=['Products'],
    install_requires=[
        'hexagonit.testing',
        'html2text',
        'setuptools',
        'zope.i18nmessageid',
    ],
    entry_points="""
    # -*- Entry points: -*-

    [z3c.autoinclude.plugin]
    target = plone
    """,
    )
