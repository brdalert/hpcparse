import csv
from collections import defaultdict

from accounts import Accounts


class AccountsParser:
    def __init__(self):
        self.__fileName = ''
        self.__acct_list = []

    def par_slurm_acct(self, filename):
        self.__fileName = filename
        try:
            with open(self.__fileName, 'r', newline='') as inputFile:
                records = csv.DictReader(inputFile, delimiter='|')
                for row in records:
                    row = defaultdict(lambda: None, row)
                    try:
                        new_account = Accounts()

                        new_account.account = row['Account']
                        new_account.descr = row['Descr']
                        new_account.org = row['Org']

                        self.__acct_list.append(new_account)
                    except Exception as ex:
                        print(ex)
                        print('error')
        except Exception as ex:
            print(ex)
            print('error')
        return self.__acct_list
