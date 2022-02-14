import os
from setuptools import setup, find_packages


version = "0.1"


install_requires = [
    "horseman",
    "reiter.form",
    "reiter.ui",
    "reiter.view",
    "roughrider.application",
    "roughrider.routing",
    "wtforms",
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
    entry_points={
        "fanstatic.libraries": [
            "bgv.questionnaire = bgv.questionnaire.theme:library",
        ],
    }
)
