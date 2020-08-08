import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name='api_tests',
    platforms='win10',
    version='0.0.1',
    author='Ars',
    author_email='master.visput@gmail.com',
    description='api_tests',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/MasterVisput/docker_proj',
    packages=['api_tests.api', 'api_tests.tests'],
    keywords='sample api tests',
    classifiers=[
        'Programming Language :: Python :: 3'
    ],
    zip_safe=False,
    python_requires='>3.5',
    install_requires=[
        'Cerberus==1.3.2',
        'requests==2.22.0',
        'selenium==3.141.0'

    ]
)
