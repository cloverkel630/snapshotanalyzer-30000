from setuptools import setup

setup(
    name='SnapshotAlyzer-30000',
    version='0.1',
    author="Kelley",
    author_email="kelleymmaloney@yahoo.com",
    Description="SnapshotAlyzer 30000 is a tool to manange AWS EC2 snapshots",
    license="GPL",
    packages=['shotty'],
    url="https://github.com/cloverkel630/snapshotanalyzer-30000",
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        shotty=shotty.shotty:cli
    '''
)
