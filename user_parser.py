import csv
from collections import defaultdict

from user import SlurmUser


class SlurmUserParser:
    def __init__(self):
        self.__fileName = ''
        self.__userslist = []
        self.__count = 0

    def parse_users(self, filename):
        self.__fileName = filename
        try:
            with open(self.__fileName, 'r', newline='') as inputFile:
                records = csv.DictReader(inputFile, delimiter='|')
                for row in records:
                    row = defaultdict(lambda: None, row)
                    try:
                        user = SlurmUser()

                        user.username = row['User']
                        user.def_account = row['Def Acct']
                        user.admin = row['Admin']
                        user.cluster = row['Cluster']
                        user.account = row['Account']
                        user.partition = row['Partition']
                        user.share = row['Share']
                        user.max_jobs = row['MaxJobs']
                        user.max_nodes = row['MaxNodes']
                        user.Max_cpus = row['MaxCPUs']
                        user.max_submit = row['MaxSubmit']
                        user.max_wall = row['MaxWall']
                        user.max_cpu_mins = row['MaxCPUMins']
                        user.qos = row['QOS']
                        user.def_qos = row['Def QOS']

                        self.__userslist.append(user)
                        self.__count += 1
                    except Exception as ex:
                        print(ex)
                        print('error')
        except Exception as ex:
            print(ex)
            print('error')
        return self.__userslist, self.__count
