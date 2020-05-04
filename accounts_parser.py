import csv
from collections import defaultdict

from user import SlurmUser


class AccountsParser:
    def __init__(self):
        self.__fileName = ''
        self.__acct_list = []
        self.__count = 0

    def par_slurm_acct(self, filename):
        self.__fileName = filename
        try:
            with open(self.__fileName, 'r', newline='') as inputFile:
                records = csv.DictReader(inputFile, delimiter='|')
                for row in records:
                    row = defaultdict(lambda: None, row)
                    try:
                        user = SlurmUser()

                        user.username = row['Account']
                        user.def_account = row['Descr']
                        user.admin = row['Org']

                        self.__userslist.append(user)
                        self.__count += 1
                    except Exception as ex:
                        print(ex)
                        print('error')
        except Exception as ex:
            print(ex)
            print('error')
        return self.__userslist, self.__count