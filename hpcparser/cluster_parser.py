import csv
from collections import defaultdict

# own modules
from cluster import Cluster


class ClusterParser:
    def __init__(self, filename):
        self.__fileName = filename
        self.__cluster_list = []

    @classmethod
    def par_slurm_acct(self):
        try:
            with open(self.__fileName, 'r', newline='') as inputFile:
                records = csv.DictReader(inputFile, delimiter='|')
                for row in records:
                    row = defaultdict(lambda: None, row)
                    try:
                        new_cluster = Cluster()

                        new_cluster.clustername = row['Cluster']
                        new_cluster.control_host = row['ControlHost']
                        new_cluster.control_port = row['ControlPort']
                        new_cluster.rpc = row['RPC']
                        new_cluster.share = row['Share']
                        new_cluster.group_jobs = row['GrpJobs']
                        new_cluster.group_tres = row['GrpTRES']
                        new_cluster.group_submit = ['GrpSubmit']
                        new_cluster.max_jobs = row['MaxJopbs']
                        new_cluster.max_tres = row['MaxTRES']
                        new_cluster.max_submit = row['MaxSubmit']
                        new_cluster.max_wall = row['MaxWall']
                        new_cluster.qos = row['QOS']
                        new_cluster.def_qos = row['Def QOS']
                        self.__cluster_list.append(new_cluster)
                    except Exception as ex:
                        print(ex)
                        print('error')
        except Exception as ex:
            print(ex)
            print('error')
        return self.__cluster_list
