import os

from setuptools import find_packages, setup

from immunity_ipam import get_version

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()


def get_install_requires():
    """
    parse requirements.txt, ignore links, exclude comments
    """
    requirements = []
    for line in open('requirements.txt').readlines():
        if line.startswith('#') or line == '' or line.startswith('git'):
            continue
        requirements.append(line)
    return requirements


setup(
    name='immunity-ipam',
    version=get_version(),
    license='BSD-3-Clause',
    author='Immunity',
    author_email='support@immunity.io',
    description='IP address space administration module of Immunity.',
    long_description_content_type='text/markdown',
    long_description=README,
    url='https://github.com/edge-servers/immunity-ipam',
    download_url='https://github.com/edge-servers/immunity-ipam/releases',
    platforms=['Platform Independent'],
    keywords=['django', 'freeradius', 'networking', 'immunity'],
    packages=find_packages(exclude=['tests*', 'docs*']),
    include_package_data=True,
    zip_safe=False,
    install_requires=get_install_requires(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: System :: Networking',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Framework :: Django',
        'Programming Language :: Python :: 3',
    ],
)
