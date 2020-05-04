# Libs
import csv
from collections import defaultdict

# Own modules
from qos import QOS


class QOSParser:
    def __init__(self, filename):
        self.__fileName = filename
        self.__qos_list = []

    @classmethod
    def parse_qos(self):
        try:
            with open(self.__fileName, 'r', newline='') as inputFile:
                records = csv.DictReader(inputFile, delimiter='|')
                for row in records:
                    row = defaultdict(lambda: None, row)
                    try:
                        new_qos = QOS()

                        new_qos.name = row['']
                        new_qos.priority = row['']
                        new_qos.grace_time = row['']
                        new_qos.preempt = row['']
                        new_qos.preempt_mode = row['']
                        new_qos.flags = row['']
                        new_qos.usage_thres = row['']
                        new_qos.usage_factor = row['']
                        new_qos.group_tres = row['']
                        new_qos.group_tres_mins = row['']
                        new_qos.group_tres_run_mins = row['']
                        new_qos.group_jobs = row['']
                        new_qos.group_submit = row['']
                        new_qos.group_wall = row['']
                        new_qos.max_tres = row['']
                        new_qos.max_tres_per_node = row['']
                        new_qos.max_tres_mins = row['']
                        new_qos.max_wall = row['']
                        new_qos.max_tres_pu = row['']
                        new_qos.max_jobs_pu = row['']
                        new_qos.max_submit_pu = row['']
                        new_qos.max_tres_pa = row['']
                        new_qos.max_jobs_pa = row['']
                        new_qos.max_sub = row['']
                        new_qos.min_tres = row['']
                        self.__qos_list.append(new_qos)
                    except Exception as ex:
                        print(ex)
                        print('error')
        except Exception as ex:
            print(ex)
            print('error')
        return self.__qos_list
