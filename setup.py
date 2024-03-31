import setuptools

with open("README.md",encoding="utf-8") as f:
    long_description=f.read()

__version__="0.0.0"
REPO_NAME="cnnClassifer"
AUTHOR_USER_NAME='fardin79'
SRC_REPO='cnnClassifier'
AUTHOR_EMAIL="fardeenrangrezz4@gmail.com"




setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for cnn app",
    long_description=long_description,
    url=f"https://github.com/{AUTHOR_USER_NAME}/{AUTHOR_EMAIL}",
    package_dir={"":"src"},
    packages=setuptools.find_packages(where='src')
)