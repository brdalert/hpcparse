import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="HPC-scheduler-accounting-parser",
    version="0.0.5",
    author="Brandon Dunn",
    author_email="brdunn@ksu.edu",
    description="Package for parsing HPC scheduler account data.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.cs.ksu.edu/brdunn/hpc-scheduler-accounting-parser",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
