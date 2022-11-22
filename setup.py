from setuptools import setup


with open("README.md", 'r', encoding="utf-8") as f:
    long_decsription = f.read()

REPO_NAME = "RegressionProject"
SRC_REPO = 'src'
AUTHOR = "ShashiDivs"
LIST_OF_REQUIREMENTS = []

setup(
    
    name = SRC_REPO,
    version = "0.0.1",
    author=AUTHOR,
    author_email='shashipolity@gmail.com'
    description='This is our first release',
    long_description= long_decsription,
    url = f"https://github.com/{ShashiDivs}/{REPO_NAME }",
    packages=[SRC_REPO ],
    python_requires = ">=3.6",
    install_requires = LIST_OF_REQUIREMENTS
)