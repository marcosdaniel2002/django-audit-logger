from setuptools import setup, find_packages

setup(
    name='django-audit-logger',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'Django>=3.0',
        'confluent_kafka>=1.7.0',  # Add confluent_kafka as a dependency
    ],
    description='A reusable Django app for auditing models automatically',
    long_description=open('README.md').read(),
    author='Marcos Daniel',
    author_email='mteranc@unemi.edu.ec',
    url='https://github.com/marcosdaniel2002/django-audit-logger',  # Replace with your GitHub repo
    classifiers=[
        'Framework :: Django',
        'Programming Language :: Python',
    ],
)
