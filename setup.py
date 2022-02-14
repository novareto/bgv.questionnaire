import os
from setuptools import setup, find_packages


version = "0.1"


install_requires = [
]

test_requires = [
]

setup(
    name='bgv.questionnaire',
    version=version,
    author='Novareto GmbH',
    author_email='ck@novareto.de',
    description='Fixme.',
    long_description=(
        open("README.rst").read() + "\n" +
        open(os.path.join("docs", "HISTORY.rst")).read()
    ),
    license='ZPL',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
    ],
    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=['bgv',],
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    extras_require={
        'test': test_requires,
    },
)
