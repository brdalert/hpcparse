import csv
from collections import defaultdict

from user import User


class UserParser:
    def __init__(self):
        self.__fileName = ''
        self.__userslist = []

    def parse_users(self, filename):
        self.__fileName = filename
        try:
            with open(self.__fileName, 'r', newline='') as inputFile:
                records = csv.DictReader(inputFile, delimiter='|')
                for row in records:
                    row = defaultdict(lambda: None, row)
                    try:
                        new_user = User()
                        new_user.username = row['User']
                        new_user.def_account = row['Def Acct']
                        new_user.admin = row['Admin']
                        new_user.cluster = row['Cluster']
                        new_user.account = row['Account']
                        new_user.partition = row['Partition']
                        new_user.share = row['Share']
                        new_user.max_jobs = row['MaxJobs']
                        new_user.max_nodes = row['MaxNodes']
                        new_user.Max_cpus = row['MaxCPUs']
                        new_user.max_submit = row['MaxSubmit']
                        new_user.max_wall = row['MaxWall']
                        new_user.max_cpu_mins = row['MaxCPUMins']
                        new_user.qos = row['QOS']
                        new_user.def_qos = row['Def QOS']
                        self.__userslist.append(new_user)
                    except Exception as ex:
                        print(ex)
                        print('error')
        except Exception as ex:
            print(ex)
            print('error')
        return self.__userslist
