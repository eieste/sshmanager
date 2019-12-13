import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sshock",
    version="0.0.1",
    license='MIT',
    author="Stefan Eiermann",
    author_email="python-org@ultraapp.de",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/eieste/sshmanager",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.7',
    include_package_data=True,
)

