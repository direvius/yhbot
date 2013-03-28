from setuptools import setup, find_packages

version = '0.1.0'

setup(
    name='yhbot',
    version=version,
    description="A jabber bot for YaHome",
    long_description="""A jabber bot for YaHome""",
    classifiers=[],  # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='Alexey Lavrenuke',
    author_email='direvius@yandex-team.ru',
    url='',
    license='LGPLv3',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'jabberbot',
        'xmpppy',
    ],
    entry_points={
        'console_scripts': [
            'yhbot = yhbot.bot:main',
        ]
    },
)
