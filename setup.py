import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="word-identifiers",
    version="1.0.0",
    author="Kavi Gupta",
    author_email="word_identifiers@kavigupta.org",
    description="Provides a bijection between numbers and lists of english words.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kavigupta/word-identifiers",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.5",
    install_requires=[],
)
