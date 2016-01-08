from setuptools import setup, find_packages
import os
import time
import sys

CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: GNU General Public License (GPL)',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development',
    'Topic :: Software Development :: Libraries :: Application Frameworks',
]

setup(
    author="JGabrielFreitas",
    author_email="jgabrielafreitas@gmail.com",
    name='First Django App',
    version='0.1',
    description='Simple hello world using Django framework',
    url='https://github.com/jgabrielfreitas/first_django_app',
    license='GPL',
    platforms=['OS Independent'],
    classifiers=CLASSIFIERS,
    install_requires=[
        'Django==1.6.5',
    ],
    packages=find_packages(exclude=["project","project.*"]),
    include_package_data=True,
    zip_safe = False
)

def time():
    for i in range(100):
        print i,
        sys.stdout.flush()
        time.sleep(1)
        print "\r",
