from setuptools import find_packages
from setuptools import setup

import os


long_description = (
    open(os.path.join("Products", "PloneGazette", "docs", "README.rst")).read() + "\n" +
    open(os.path.join("Products", "PloneGazette", "docs", "HISTORY.rst")).read() + "\n" +
    open(os.path.join("Products", "PloneGazette", "docs", "CONTRIBUTORS.rst")).read())


setup(
    name='Products.PloneGazette',
    version='3.2.0.1',
    author='Pilot Systems, Nidelven IT LTD and others',
    author_email='',
    maintainer='Morten W. Petersen',
    maintainer_email='info@nidelven-it.no',
    classifiers=[
        "Framework :: Plone",
        "Framework :: Plone :: 4.2",
        "Framework :: Plone :: 4.3",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7"],
    keywords='Zope plone newsletter communication',
    url='http://plone.org/products/plonegazette',
    description='A complete Newsletter product for Plone.',
    long_description=long_description,
    packages=find_packages(exclude=['ez_setup']),
    include_package_data=True,
    zip_safe=False,
    namespace_packages=['Products'],
    install_requires=[
        'Plone>=4.2',
        'Products.OrderableReferenceField',
        'hexagonit.testing',
        'plone.directives.form',
        'setuptools',
        'zope.i18nmessageid'],
    entry_points="""
    # -*- Entry points: -*-

    [z3c.autoinclude.plugin]
    target = plone
    """)
