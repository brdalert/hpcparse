import os.path

__all__ = [
    "__title__",
    "__summary__",
    "__uri__",
    "__version__",
    "__commit__",
    "__author__",
    "__email__",
    "__license__",
    "__copyright__",
    "__platform__",
]


try:
    base_dir = os.path.dirname(os.path.abspath(__file__))
except NameError:
    base_dir = None


__title__ = "hpcsap"
__summary__ = "Package for parsing HPC scheduler account data"
__uri__ = "https://gitlab.cs.ksu.edu/brdunn/hpc-scheduler-accounting-parser"

__version__ = "0.1.15"

if base_dir is not None and os.path.exists(os.path.join(base_dir, ".commit")):
    with open(os.path.join(base_dir, ".commit")) as fp:
        __commit__ = fp.read().strip()
else:
    __commit__ = None

__author__ = 'Brandon Dunn'
__email__ = 'brdunn@ksu.edu'

__license__ = 'GNU General Public License v3 (GPLv3)'
__copyright__ = "2019 %s" % __author__
__platform__ = 'Linux'
