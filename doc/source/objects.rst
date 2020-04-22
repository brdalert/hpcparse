AccountingParser objects
========================


.. class:: hpcsap.AccountingParser()

    Create a new :mod:`AccountingParser` object. we provided a short list here
    as quick list reference:

    * filepath_ - string representation of the filepath.

    * num_lines_ - number of lines to read from the file. (default: ``None``)

    * start_ - line in file to start reading from. (default: ``0``)

The next few section describe in detail what each of the object parameters do and what they are used for.

filepath
^^^^^^^^^^^

All calls to the :class:`AccountingParser` constructor, will require the filepath argument
to be passed. This argument give the file name or absolute path to the file that is to be
parsed. Currently it takes a csv file from either Sun Grid Engine (SGE) or SLURM. 
standard argument::

    >>> parser = AccountingParser(filepath)
    >>> joblist = parser.slurm_Parser()
    usage: repr(joblist)
    

We hope to
add the ability to auto detect the file type later.

num_lines
^^^^^^^^^

In some cases it might be wise to only parse a portion of the a given file. the

start
^^^^^