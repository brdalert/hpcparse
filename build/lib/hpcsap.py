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
__version__ = '0.0.8'
__maintainer__ = 'Brandon Dunn'
__email__ = 'brdunn@ksu.edu'
__status__ = 'in development'


# Accounting Parser Class Definition
class AccountingParser:
    def __init__(self):
        self.__count = 0

    # SGE parser Method Definition
    def SGE_Parser(self, file_path, line_count=0, start=0):

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
                        if line_count and self.__count == line_count:
                            break
                        if self.__count < start:
                            continue
                        self.__count += 1
                        job.account = row['account']
                        job.alloc_CPUS = row['AllocCPUS']
                        job.alloc_GRES = row['AllocGRES']
                        job.alloc_Nodes = row['AllocNodes']
                        job.alloc_TRES = row['AllocTRES']
                        job.assoc_ID = row['AssocID']
                        job.ave_CPU = row['AveCPU']
                        job.ave_CPU_freq = row['AveCPUFreq']
                        job.ave_disk_read = row['AveDiskRead']
                        job.ave_disk_write = row['AveDiskWrite']
                        job.ave_pages = row['AvePages']
                        job.ave_RSS = row['AveRSS']
                        job.ave_VM_size = row['AveVMSize']
                        job.block_ID = row['BlockID']
                        job.cluster = row['Cluster']
                        job.comment = row['Comment']
                        job.consumed_energy = row['ConsumedEnergy']
                        job.consumed_energy_raw = row['ConsumedEnergyRaw']
                        job.CPU_time = row['CPUTime']
                        job.CPU_time_raw = row['cpu']
                        job.derived_exit_code = row['exit_status']
                        job.elapsed = row['ru_wallclock']
                        job.elapsed_raw = row['ElapsedRaw']
                        job.eligible = row['Eligible']
                        job.end = row['End']
                        job.exit_code = row['ExitCode']
                        job.GID = row['GID']
                        job.group = row['Group']
                        job.job_ID = row['JobID']
                        job.job_ID_raw = row['JobIDRaw']
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
                        job.mwmory = row['MaxRSS']
                        job.mwmory_node = row['MaxRSSNode']
                        job.mwmory_task = row['MaxRSSTask']
                        job.max_VM_size = row['MaxVMSize']
                        job.max_VM_size_node = row['MaxVMSizeNode']
                        job.max_VM_size_task = row['MaxVMSizeTask']
                        job.mcs_label = row['McsLabel']
                        job.min_CPU = row['MinCPU']
                        job.min_CPU_node = row['MinCPUNode']
                        job.min_CPU_task = row['MinCPUTask']
                        job.NCPUS = row['NCPUS']
                        job.NNodes = row['NNodes']
                        job.node_list = row['NodeList']
                        job.NTasks = row['NTasks']
                        job.priority = row['priority']
                        job.partition = row['Partition']
                        job.QOS = row['QOS']
                        job.QOS_raw = row['QOSRAW']
                        job.req_CPU_freq = row['ReqCPUFreq']
                        job.req_CPU_freq_min = job.account = row['Account']
                        job.admin_comment = row['AdminComment']
                        job.alloc_CPUS = row['AllocCPUS']
                        job.alloc_GRES = row['AllocGRES']
                        job.alloc_Nodes = row['AllocNodes']
                        job.alloc_TRES = row['AllocTRES']
                        job.assoc_ID = row['AssocID']
                        job.ave_CPU = row['AveCPU']
                        job.ave_CPU_freq = row['AveCPUFreq']
                        job.ave_disk_read = row['AveDiskRead']
                        job.ave_disk_write = row['AveDiskWrite']
                        job.ave_pages = row['AvePages']
                        job.ave_RSS = row['AveRSS']
                        job.ave_VM_size = row['AveVMSize']
                        job.block_ID = row['BlockID']
                        job.cluster = row['qname']
                        job.comment = row['Comment']
                        job.consumed_energy = row['ConsumedEnergy']
                        job.consumed_energy_raw = row['ConsumedEnergyRaw']
                        job.CPU_time = row['CPUTime']
                        job.CPU_time_raw = row['CPUTimeRAW']
                        job.derived_exit_code = row['DerivedExitCode']
                        job.elapsed = row['Elapsed']
                        job.elapsed_raw = row['ElapsedRaw']
                        job.eligible = row['Eligible']
                        job.end = row['end_time']
                        job.exit_code = row['ExitCode']
                        job.GID = row['GID']
                        job.group = row['group']
                        job.job_ID = row['job_number']
                        job.job_ID_raw = row['JobIDRaw']
                        job.job_name = row['job_name']
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
                        job.mwmory = row['MaxRSS']
                        job.mwmory_node = row['MaxRSSNode']
                        job.mwmory_task = row['MaxRSSTask']
                        job.max_VM_size = row['MaxVMSize']
                        job.max_VM_size_node = row['MaxVMSizeNode']
                        job.max_VM_size_task = row['MaxVMSizeTask']
                        job.mcs_label = row['McsLabel']
                        job.min_CPU = row['MinCPU']
                        job.min_CPU_node = row['MinCPUNode']
                        job.min_CPU_task = row['MinCPUTask']
                        job.NCPUS = row['NCPUS']
                        job.NNodes = row['ReqCPUFreqGov']
                        job.req_CPUS = row['ReqCPUS']
                        job.req_GRES = row['ReqGRES']
                        job.req_mem = row['ReqMem']
                        job.req_nodes = row['ReqNodes']
                        job.req_TRES = row['ReqTRES']
                        job.reservation = row['Reservation']
                        job.reservation_Id = row['ReservationId']
                        job.reserved = row['Reserved']
                        job.resvCPU = row['ResvCPU']
                        job.resvCPURAW = row['ResvCPURAW']
                        job.start = row['start_time']
                        job.state = row['State']
                        job.submit = row['submission_time']
                        job.suspended = row['Suspended']
                        job.system_CPU = row['SystemCPU']
                        job.system_comment = row['SystemComment']
                        job.time_limit = row['Timelimit']
                        job.time_limit_raw = row['TimelimitRaw']
                        job.total_CPU = row['TotalCPU']
                        job.TRES_usage_in_ave = row['TRESUsageInAve']
                        job.TRES_usage_in_max = row['TRESUsageInMax']
                        job.TRES_usage_in_max_node = row['TRESUsageInMaxNode']
                        job.TRES_usage_in_max_task = row['TRESUsageInMaxTask']
                        job.TRES_usage_in_min = row['TRESUsageInMin']
                        job.TRES_usage_in_min_node = row['TRESUsageInMinNode']
                        job.TRES_usage_in_min_task = row['TRESUsageInMinTask']
                        job.TRES_usage_in_tot = row['TRESUsageInTot']
                        job.TRES_usage_out_ave = row['TRESUsageOutAve']
                        job.TRES_usage_out_max = row['TRESUsageOutMax']
                        job.TRES_usage_out_max_node = \
                            row['TRESUsageOutMaxNode']
                        job.TRES_usage_out_max_task = \
                            row['TRESUsageOutMaxTask']
                        job.TRES_usage_out_min = row['TRESUsageOutMin']
                        job.TRES_usage_out_min_node = \
                            row['TRESUsageOutMinNode']
                        job.TRES_usage_out_min_task = \
                            row['TRESUsageOutMinTask']
                        job.TRES_usage_out_tot = row['TRESUsageOutTot']
                        job.UID = row['UID']
                        job.user = row['owner']
                        job.user_CPU = row['UserCPU']
                        job.WC_key = row['WCKey']
                        job.WC_key_ID = row['WCKeyID']
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

    def SLURM_Parser(self, file_path, line_count=0, start=0):

        joblist = []
        # Parse SLURM File
        try:
            with open(file_path, 'r', newline='') as inputFile:
                records = csv.DictReader(inputFile, delimiter='|')
                for row in records:
                    row = defaultdict(lambda: None, row)
                    try:
                        job = Job()
                        if line_count and self.__count == line_count:
                            print('count issues')
                            break
                        if self.__count < start:
                            continue
                        self.__count += 1

                        job.account = row['Account']
                        job.admin_comment = row['AdminComment']
                        job.alloc_CPUS = row['AllocCPUS']
                        job.alloc_GRES = row['AllocGRES']
                        job.alloc_Nodes = row['AllocNodes']
                        job.alloc_TRES = row['AllocTRES']
                        job.assoc_ID = row['AssocID']
                        job.ave_CPU = row['AveCPU']
                        job.ave_CPU_freq = row['AveCPUFreq']
                        job.ave_disk_read = row['AveDiskRead']
                        job.ave_disk_write = row['AveDiskWrite']
                        job.ave_pages = row['AvePages']
                        job.ave_RSS = row['AveRSS']
                        job.ave_VM_size = row['AveVMSize']
                        job.block_ID = row['BlockID']
                        job.cluster = row['Cluster']
                        job.comment = row['Comment']
                        job.consumed_energy = row['ConsumedEnergy']
                        job.consumed_energy_raw = row['ConsumedEnergyRaw']
                        job.CPU_time = row['CPUTime']
                        job.CPU_time_raw = row['CPUTimeRAW']
                        job.derived_exit_code = row['DerivedExitCode']
                        job.elapsed = row['Elapsed']
                        job.elapsed_raw = row['ElapsedRaw']
                        job.eligible = row['Eligible']
                        job.end = row['End']
                        job.exit_code = row['ExitCode']
                        job.GID = row['GID']
                        job.group = row['Group']
                        job.job_ID = row['JobID']
                        job.job_ID_raw = row['JobIDRaw']
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
                        job.mwmory = row['MaxRSS']
                        job.mwmory_node = row['MaxRSSNode']
                        job.mwmory_task = row['MaxRSSTask']
                        job.max_VM_size = row['MaxVMSize']
                        job.max_VM_size_node = row['MaxVMSizeNode']
                        job.max_VM_size_task = row['MaxVMSizeTask']
                        job.mcs_label = row['McsLabel']
                        job.min_CPU = row['MinCPU']
                        job.min_CPU_node = row['MinCPUNode']
                        job.min_CPU_task = row['MinCPUTask']
                        job.NCPUS = row['NCPUS']
                        job.NNodes = row['NNodes']
                        job.node_list = row['NodeList']
                        job.NTasks = row['NTasks']
                        job.priority = row['Priority']
                        job.partition = row['Partition']
                        job.QOS = row['QOS']
                        job.QOS_raw = row['QOSRAW']
                        job.req_CPU_freq = row['ReqCPUFreq']
                        job.req_CPU_freq_min = job.account = row['Account']
                        job.admin_comment = row['AdminComment']
                        job.alloc_CPUS = row['AllocCPUS']
                        job.alloc_GRES = row['AllocGRES']
                        job.alloc_Nodes = row['AllocNodes']
                        job.alloc_TRES = row['AllocTRES']
                        job.assoc_ID = row['AssocID']
                        job.ave_CPU = row['AveCPU']
                        job.ave_CPU_freq = row['AveCPUFreq']
                        job.ave_disk_read = row['AveDiskRead']
                        job.ave_disk_write = row['AveDiskWrite']
                        job.ave_pages = row['AvePages']
                        job.ave_RSS = row['AveRSS']
                        job.ave_VM_size = row['AveVMSize']
                        job.block_ID = row['BlockID']
                        job.cluster = row['Cluster']
                        job.comment = row['Comment']
                        job.consumed_energy = row['ConsumedEnergy']
                        job.consumed_energy_raw = row['ConsumedEnergyRaw']
                        job.CPU_time = row['CPUTime']
                        job.CPU_time_raw = row['CPUTimeRAW']
                        job.derived_exit_code = row['DerivedExitCode']
                        job.elapsed = row['Elapsed']
                        job.elapsed_raw = row['ElapsedRaw']
                        job.eligible = row['Eligible']
                        job.end = row['End']
                        job.exit_code = row['ExitCode']
                        job.GID = row['GID']
                        job.group = row['Group']
                        job.job_ID = row['JobID']
                        job.job_ID_raw = row['JobIDRaw']
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
                        job.mwmory = row['MaxRSS']
                        job.mwmory_node = row['MaxRSSNode']
                        job.mwmory_task = row['MaxRSSTask']
                        job.max_VM_size = row['MaxVMSize']
                        job.max_VM_size_node = row['MaxVMSizeNode']
                        job.max_VM_size_task = row['MaxVMSizeTask']
                        job.mcs_label = row['McsLabel']
                        job.min_CPU = row['MinCPU']
                        job.min_CPU_node = row['MinCPUNode']
                        job.min_CPU_task = row['MinCPUTask']
                        job.NCPUS = row['NCPUS']
                        job.NNodes = row['ReqCPUFreqGov']
                        job.req_CPUS = row['ReqCPUS']
                        job.req_GRES = row['ReqGRES']
                        job.req_mem = row['ReqMem']
                        job.req_nodes = row['ReqNodes']
                        job.req_TRES = row['ReqTRES']
                        job.reservation = row['Reservation']
                        job.reservation_Id = row['ReservationId']
                        job.reserved = row['Reserved']
                        job.resvCPU = row['ResvCPU']
                        job.resvCPURAW = row['ResvCPURAW']
                        job.start = row['Start']
                        job.state = row['State']
                        job.submit = row['Submit']
                        job.suspended = row['Suspended']
                        job.system_CPU = row['SystemCPU']
                        job.system_comment = row['SystemComment']
                        job.time_limit = row['Timelimit']
                        job.time_limit_raw = row['TimelimitRaw']
                        job.total_CPU = row['TotalCPU']
                        job.TRES_usage_in_ave = row['TRESUsageInAve']
                        job.TRES_usage_in_max = row['TRESUsageInMax']
                        job.TRES_usage_in_max_node = row['TRESUsageInMaxNode']
                        job.TRES_usage_in_max_task = row['TRESUsageInMaxTask']
                        job.TRES_usage_in_min = row['TRESUsageInMin']
                        job.TRES_usage_in_min_node = row['TRESUsageInMinNode']
                        job.TRES_usage_in_min_task = row['TRESUsageInMinTask']
                        job.TRES_usage_in_tot = row['TRESUsageInTot']
                        job.TRES_usage_out_ave = row['TRESUsageOutAve']
                        job.TRES_usage_out_max = row['TRESUsageOutMax']
                        job.TRES_usage_out_max_node = \
                            row['TRESUsageOutMaxNode']
                        job.TRES_usage_out_max_task = \
                            row['TRESUsageOutMaxTask']
                        job.TRES_usage_out_min = row['TRESUsageOutMin']
                        job.TRES_usage_out_min_node = \
                            row['TRESUsageOutMinNode']
                        job.TRES_usage_out_min_task = \
                            row['TRESUsageOutMinTask']
                        job.TRES_usage_out_tot = row['TRESUsageOutTot']
                        job.UID = row['UID']
                        job.user = row['User']
                        job.user_CPU = row['UserCPU']
                        job.WC_key = row['WCKey']
                        job.WC_key_ID = row['WCKeyID']
                        job.working_dir = row['WorkDir']
                        job.granted_pe = row['granted_pe']
                        job.catagotries = row['catagories']

                        joblist.append(job)
                        self.__count += 1
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
