High Performance Computing Accounting parser
============================================

hpcparse (HPC Scheduler/resource manager general purpose parser) is a Python library that adds functionality to parse HPC scheduler/Resource manager
infromation like Accounting, users, qos, ..etc. This librarary Fully supports SLURM, partial SGE and more to be added later
Parsers available currently are:

* AccountingParser "*"
    - Parser that gets a list of jobs based on accounting information "-"
* AccountsParser "*"
    - Parser that get a list of accounts "-"
* ClusterParser "*"
    - Parser that get a list of clusters and associated information "-"
* QOSParser "*" 
    - Parser that gets a list of QOS's for the cluster "-"
* UserPaarser "*"
    - Parser that gets a list of Users for the HPC "-"

Prerequisites
^^^^^^^^^^^^^
python csv package
