from setuptools import setup, find_packages
import hpcsap

with open("README.md", "r") as fh:
    long_description = fh.read()

setup_args = dict(
    name="hpcsapb",
    version=hpcsap.__version__,
    author="Brandon Dunn",
    author_email="brdunn@ksu.edu",
    description="Package for parsing HPC scheduler account data.",
    long_description=long_description,
    url="https://gitlab.cs.ksu.edu/brdunn/hpc-scheduler-accounting-parser",
    platforms="any",
    classifiers="""\
Development Status :: 4 - Beta
Environment :: Console
Intended Audience :: System Administrators
License :: OSI Approved :: GNU General Public License v3 (GPLv3)
Operating System :: POSIX :: Linux
Programming Language :: Python :: 3
Programming Language :: Python :: 3.0
Programming Language :: Python :: 3.1
Programming Language :: Python :: 3.2
Programming Language :: Python :: 3.3
Programming Language :: Python :: 3.4
    """.splitlines(),
    py_modules=['hpcsap', 'job']
)

if __name__ == '__main__':
    setup(**setup_args)
