"""
This Class implements a pareser for SLURM and SGE output files.

GNU GPL3 licensing
"""
# Libs
import csv
from collections import defaultdict

# Own Modules
from job import Job

__author__ = 'Brandon Dunn'
__copyright__ = 'Copyright 2019'
__credits__ = []
__license__ = 'GPL'
__version__ = '0.0.10'
__maintainer__ = 'Brandon Dunn'
__email__ = 'brdunn@ksu.edu'
__status__ = 'in development'


# Accounting Parser Class Definition
class AccountingParser:
    def __init__(self):
        self.__count = 0

    # SGE parser Method Definition
    def SGE_Parser(self, file_path, num_lines=None, start=0):

        joblist = []
        # Parse SGE File
        dictValues = ['qname', 'hostname', 'group', 'owner', 'job_name',
                      'job_id', 'account', 'priority', 'submission_time',
                      'start_time', 'end_time', 'failed', 'exit_status',
                      'ru_wallclock', 'ru_utime', 'ru_stime', 'ru_maxrss',
                      'ru_ixrss', 'ruismrss', 'ru_idrss', 'ru_isrss',
                      'ruminflt', 'ru_majflt', 'ru_nswap', 'ru_inblock',
                      'ru_outblock', 'ru_msgsnd', 'ru_msgrcv', 'ru_nsignals',
                      'ru_nvcsw', 'ru_nivcsw', 'project', 'department',
                      'granted_pe', 'slots', 'task_number', 'cpu', 'mem', 'io',
                      'catagory', 'iow', 'pe_taskid', 'maxvmem', 'arid',
                      'ar_submission_time']
        try:
            with open(file_path, 'r', newline='') as inputFile:
                records = csv.DictReader(inputFile, fieldnames=dictValues,
                                         delimiter=':')
                for row in records:
                    row = defaultdict(lambda: None, row)
                    try:
                        job = Job()
                        if num_lines is not None and num_lines > 0 and \
                           self.__count == num_lines:
                            break

                        if start >= 0 and self.__count < start:
                            start -= 1
                            continue

                        self.__count += 1
                        job.account = row['Account']
                        job.admin_comment = row['AdminComment']
                        job.alloc_cpus = row['AllocCPUS']
                        job.alloc_gres = row['AllocGRES']
                        job.alloc_nodes = row['AllocNodes']
                        job.alloc_tres = row['AllocTRES']
                        job.assoc_id = row['AssocID']
                        job.ave_cpu = row['AveCPU']
                        job.ave_cpu_freq = row['AveCPUFreq']
                        job.ave_disk_read = row['AveDiskRead']
                        job.ave_disk_write = row['AveDiskWrite']
                        job.ave_pages = row['AvePages']
                        job.ave_rss = row['AveRSS']
                        job.ave_vm_size = row['AveVMSize']
                        job.block_ID = row['BlockID']
                        job.cluster = row['Cluster']
                        job.comment = row['Comment']
                        job.consumed_energy = row['ConsumedEnergy']
                        job.consumed_energy_raw = row['ConsumedEnergyRaw']
                        job.cpu_time = row['CPUTime']
                        job.cpu_time_raw = row['cpu']
                        job.derived_exit_code = row['exit_status']
                        job.elapsed = row['ru_wallclock']
                        job.elapsed_raw = row['ElapsedRaw']
                        job.eligible = row['Eligible']
                        job.end = row['End']
                        job.exit_code = row['ExitCode']
                        job.gid = row['GID']
                        job.group = row['Group']
                        job.job_id = row['JobID']
                        job.job_id_raw = row['JobIDRaw']
                        job.job_name = row['JobName']
                        job.layout = row['Layout']
                        job.max_disk_read = row['MaxDiskRead']
                        job.max_disk_read_node = row['MaxDiskReadNode']
                        job.max_disk_read_task = row['MaxDiskReadTask']
                        job.max_disk_write = row['MaxDiskWrite']
                        job.max_disk_write_node = row['MaxDiskWriteNode']
                        job.max_disk_write_task = row['MaxDiskWriteTask']
                        job.max_pages = row['MaxPages']
                        job.max_pages_node = row['MaxPagesNode']
                        job.max_pages_task = row['MaxPagesTask']
                        job.memory = row['MaxRSS']
                        job.memory_node = row['MaxRSSNode']
                        job.memory_task = row['MaxRSSTask']
                        job.max_vm_size = row['MaxVMSize']
                        job.max_vm_size_node = row['MaxVMSizeNode']
                        job.max_vm_size_task = row['MaxVMSizeTask']
                        job.mcs_label = row['McsLabel']
                        job.min_cpu = row['MinCPU']
                        job.min_cpu_node = row['MinCPUNode']
                        job.min_cpu_task = row['MinCPUTask']
                        job.num_cpus = row['NCPUS']
                        job.num_nodes = row['NNodes']
                        job.node_list = row['NodeList']
                        job.num_tasks = row['NTasks']
                        job.priority = row['Priority']
                        job.partition = row['Partition']
                        job.qos = row['QOS']
                        job.qos_raw = row['QOSRAW']
                        job.req_cpu_freq = row['ReqCPUFreq']
                        job.req_cpu_freq_min = row['ReqCPUFreqMin']
                        job.req_cpu_freq_max = row['ReqCPUFreqMax']
                        job.req_cpu_freq_gov = row['ReqCPUFreqGov']
                        job.req_cpuS = row['ReqCPUS']
                        job.req_gres = row['ReqGRES']
                        job.req_mem = row['ReqMem']
                        job.req_nodes = row['ReqNodes']
                        job.req_tres = row['ReqTRES']
                        job.reservation = row['Reservation']
                        job.reservation_Id = row['ReservationId']
                        job.reserved = row['Reserved']
                        job.resv_cpu = row['ResvCPU']
                        job.resv_cpu_raw = row['ResvCPURAW']
                        job.start = row['start_time']
                        job.state = row['State']
                        job.submit = row['submission_time']
                        job.suspended = row['Suspended']
                        job.system_cpu = row['SystemCPU']
                        job.system_comment = row['SystemComment']
                        job.time_limit = row['Timelimit']
                        job.time_limit_raw = row['TimelimitRaw']
                        job.total_cpu = row['TotalCPU']
                        job.tres_usage_in_ave = row['TRESUsageInAve']
                        job.tres_usage_in_max = row['TRESUsageInMax']
                        job.tres_usage_in_max_node = row['TRESUsageInMaxNode']
                        job.tres_usage_in_max_task = row['TRESUsageInMaxTask']
                        job.tres_usage_in_min = row['TRESUsageInMin']
                        job.tres_usage_in_min_node = row['TRESUsageInMinNode']
                        job.tres_usage_in_min_task = row['TRESUsageInMinTask']
                        job.tres_usage_in_tot = row['TRESUsageInTot']
                        job.tres_usage_out_ave = row['TRESUsageOutAve']
                        job.tres_usage_out_max = row['TRESUsageOutMax']
                        job.tres_usage_out_max_node = \
                            row['TRESUsageOutMaxNode']
                        job.tres_usage_out_max_task = \
                            row['TRESUsageOutMaxTask']
                        job.tres_usage_out_min = row['TRESUsageOutMin']
                        job.tres_usage_out_min_node = \
                            row['TRESUsageOutMinNode']
                        job.tres_usage_out_min_task = \
                            row['TRESUsageOutMinTask']
                        job.tres_usage_out_tot = row['TRESUsageOutTot']
                        job.uid = row['UID']
                        job.user = row['owner']
                        job.user_cpu = row['UserCPU']
                        job.wc_key = row['WCKey']
                        job.wc_key_id = row['WCKeyID']
                        job.working_dir = row['WorkDir']
                        job.granted_pe = row['granted_pe']
                        job.catagotries = row['catagories']

                        joblist.append(job)
                    except Exception as ex:
                        print(ex)
                        print('There was a parsing error on line: ' + str(
                               self.__count) + '\n skipping line and \
                               continuing:')
        except Exception as ex:
            print('error opening File path:' + str(file_path) + ', please check\
                filename and file path: the Exact error \
                follows this message: \n')
            print(ex)
            return
        return joblist

    def SLURM_Parser(self, file_path, num_lines=None, start=0):
        joblist = []
        # Parse SLURM File
        try:
            with open(file_path, 'r', newline='') as inputFile:
                records = csv.DictReader(inputFile, delimiter='|')
                for row in records:
                    row = defaultdict(lambda: None, row)
                    try:
                        if num_lines is not None and num_lines >= 0 and \
                           self.__count == num_lines:
                            break

                        if self.__count < start:
                            start -= 1
                            continue

                        self.__count += 1
                        job = Job()
                        job.account = row['Account']
                        job.admin_comment = row['AdminComment']
                        job.alloc_cpus = row['AllocCPUS']
                        job.alloc_gres = row['AllocGRES']
                        job.alloc_nodes = row['AllocNodes']
                        job.alloc_tres = row['AllocTRES']
                        job.assoc_id = row['AssocID']
                        job.ave_cpu = row['AveCPU']
                        job.ave_cpu_freq = row['AveCPUFreq']
                        job.ave_disk_read = row['AveDiskRead']
                        job.ave_disk_write = row['AveDiskWrite']
                        job.ave_pages = row['AvePages']
                        job.ave_rss = row['AveRSS']
                        job.ave_vm_size = row['AveVMSize']
                        job.block_ID = row['BlockID']
                        job.cluster = row['Cluster']
                        job.comment = row['Comment']
                        job.consumed_energy = row['ConsumedEnergy']
                        job.consumed_energy_raw = row['ConsumedEnergyRaw']
                        job.cpu_time = row['CPUTime']
                        job.cpu_time_raw = row['CPUTimeRaw']
                        job.derived_exit_code = row['DerivedExitCode']
                        job.elapsed = row['Elapsed']
                        job.elapsed_raw = row['ElapsedRaw']
                        job.eligible = row['Eligible']
                        job.end = row['End']
                        job.exit_code = row['ExitCode']
                        job.gid = row['GID']
                        job.group = row['Group']
                        job.job_id = row['JobID']
                        job.job_id_raw = row['JobIDRaw']
                        job.job_name = row['JobName']
                        job.layout = row['Layout']
                        job.max_disk_read = row['MaxDiskRead']
                        job.max_disk_read_node = row['MaxDiskReadNode']
                        job.max_disk_read_task = row['MaxDiskReadTask']
                        job.max_disk_write = row['MaxDiskWrite']
                        job.max_disk_write_node = row['MaxDiskWriteNode']
                        job.max_disk_write_task = row['MaxDiskWriteTask']
                        job.max_pages = row['MaxPages']
                        job.max_pages_node = row['MaxPagesNode']
                        job.max_pages_task = row['MaxPagesTask']
                        job.memory = row['MaxRSS']
                        job.memory_node = row['MaxRSSNode']
                        job.memory_task = row['MaxRSSTask']
                        job.max_vm_size = row['MaxVMSize']
                        job.max_vm_size_node = row['MaxVMSizeNode']
                        job.max_vm_size_task = row['MaxVMSizeTask']
                        job.mcs_label = row['McsLabel']
                        job.min_cpu = row['MinCPU']
                        job.min_cpu_node = row['MinCPUNode']
                        job.min_cpu_task = row['MinCPUTask']
                        job.num_cpus = row['NCPUS']
                        job.num_nodes = row['NNodes']
                        job.node_list = row['NodeList']
                        job.num_tasks = row['NTasks']
                        job.priority = row['Priority']
                        job.partition = row['Partition']
                        job.qos = row['QOS']
                        job.qos_raw = row['QOSRAW']
                        job.req_cpu_freq = row['ReqCPUFreq']
                        job.req_cpu_freq_min = row['ReqCPUFreqMin']
                        job.req_cpu_freq_max = row['ReqCPUFreqMax']
                        job.req_cpu_freq_gov = row['ReqCPUFreqGov']
                        job.req_cpuS = row['ReqCPUS']
                        job.req_gres = row['ReqGRES']
                        job.req_mem = row['ReqMem']
                        job.req_nodes = row['ReqNodes']
                        job.req_tres = row['ReqTRES']
                        job.reservation = row['Reservation']
                        job.reservation_Id = row['ReservationId']
                        job.reserved = row['Reserved']
                        job.resv_cpu = row['ResvCPU']
                        job.resv_cpu_raw = row['ResvCPURAW']
                        job.start = row['Start']
                        job.state = row['State']
                        job.submit = row['Submit']
                        job.suspended = row['Suspended']
                        job.system_cpu = row['SystemCPU']
                        job.system_comment = row['SystemComment']
                        job.time_limit = row['Timelimit']
                        job.time_limit_raw = row['TimelimitRaw']
                        job.total_cpu = row['TotalCPU']
                        job.tres_usage_in_ave = row['TRESUsageInAve']
                        job.tres_usage_in_max = row['TRESUsageInMax']
                        job.tres_usage_in_max_node = row['TRESUsageInMaxNode']
                        job.tres_usage_in_max_task = row['TRESUsageInMaxTask']
                        job.tres_usage_in_min = row['TRESUsageInMin']
                        job.tres_usage_in_min_node = row['TRESUsageInMinNode']
                        job.tres_usage_in_min_task = row['TRESUsageInMinTask']
                        job.tres_usage_in_tot = row['TRESUsageInTot']
                        job.tres_usage_out_ave = row['TRESUsageOutAve']
                        job.tres_usage_out_max = row['TRESUsageOutMax']
                        job.tres_usage_out_max_node = \
                            row['TRESUsageOutMaxNode']
                        job.tres_usage_out_max_task = \
                            row['TRESUsageOutMaxTask']
                        job.tres_usage_out_min = row['TRESUsageOutMin']
                        job.tres_usage_out_min_node = \
                            row['TRESUsageOutMinNode']
                        job.tres_usage_out_min_task = \
                            row['TRESUsageOutMinTask']
                        job.tres_usage_out_tot = row['TRESUsageOutTot']
                        job.uid = row['UID']
                        job.user = row['User']
                        job.user_cpu = row['UserCPU']
                        job.wc_key = row['WCKey']
                        job.wc_key_id = row['WCKeyID']
                        job.working_dir = row['WorkDir']
                        job.granted_pe = row['granted_pe']
                        job.catagotries = row['catagories']

                        joblist.append(job)
                    except Exception as ex:
                        print('There was a parsing error on line: ' +
                              str(self.__count) + '\n skipping line and \
                              continuing. the Exact error follows this \
                              message: \n')
                        print(ex)
        except Exception as ex:
            print('error opening File path:' + str(file_path) + ', please check\
                filename and file path: the Exact error \
                follows this message: \n')
            print(ex)
            return
        return joblist
