import setuptools

with open("README.md","r",encoding='utf-8') as f:
    long_description = f.read()

__version__= "0.0.0"

REPO_NAME="text"

AUTHOR_USER_NAME="jyotsana700"
SRC_REPO="text Summarizer"

AUTHOR_EMAIL="jenikunwar17@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="package for cnn app",
    url=f"https:github.com/{AUTHOR_USER_NAME}/{REPO_NAME}"
)