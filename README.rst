High Performance Computing Accounting parser
============================================

hpcparse (HPC Scheduler/resource manager general purpose parser) is a Python library that adds functionality to parse HPC scheduler/Resource manager
infromation like Accounting, users, qos, ..etc. This librarary Fully supports SLURM, partial SGE and more to be added later
Parsers available currently are:

    * AccountingParser_ - Parser that gets a list of jobs based on accounting information
    * AccountsParser_ - Parser that get a list of accounts
    * ClusterParser_ -Parser that get a list of clusters and associated information
    * QOSParser_ - Parser that gets a list of QOS's for the cluster
    * UserPaarser_ - Parser that gets a list of Users for the HPC

Prerequisites
^^^^^^^^^^^^^
python csv package
