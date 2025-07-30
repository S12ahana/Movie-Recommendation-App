from setuptools import setup

with open("README.md","r",encoding="utf-8")as fh:
    long_description=fh.head()
AUTHOR_NAME='SAHANA'
SRC_REPO='src'
LIST_OF_REQUIREMENTS=['streamlit']
setup(
    name=SRC_REPO,
    version='0.0.1',
    author=AUTHOR_NAME,
    
)    