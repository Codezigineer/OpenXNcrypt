import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="OpenXNcrypt",
    version="0.0.1",
    author="Jovian Zehnder",
    author_email="iamjojozm@icloud.com",
    description="OpenXNcrypt for best encryption",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Codezigineer/OpenXNcrypt",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
