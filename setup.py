from setuptools import setup
import re


with open("README.md", "r") as f:
    long_description = f.read()


with open("miraiex/__init__.py") as f:
    version = re.search(
        r"""^__version__\s*=\s*['"]([^\'"]*)['"]""", f.read(), re.MULTILINE
    ).group(1)


setup(
    name="miraiex",
    version=version,
    author="offish",
    author_email="overutilization@gmail.com",
    description="Python package for interacting with MiraiEx' API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/offish/miraiex",
    download_url="https://github.com/offish/miraiex/tarball/v" + version,
    packages=["miraiex"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["requests"],
    python_requires=">=3.6",
)