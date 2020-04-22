from setuptools import setup, find_packages
import about

with open("README.rst", "r") as fh:
    long_description = fh.read()

setup_args = dict(
    name="hpcsapb",
    version=about.__version__,
    author=about.__author__,
    author_email=about.__email__,
    description=about.__summary__,
    long_description=long_description,
    url=about.__uri__,
    platforms=about.__platform__,
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
    py_modules=['hpcsap', 'job', 'about']
)

if __name__ == '__main__':
    setup(**setup_args)
