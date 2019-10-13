#Description: Parser for reading in Slurm and SGE Output files

import csv
from sge_job import SGEJob
from slurm_job import SlurmJob

def mem_parse(mem):
    if(mem[-1] == 'G' or mem[-1] == 'g'):
        return str(int(float(mem[:-1] * 1024)))
    elif(mem[-1] == 'M' or mem[-1] == 'm'):
        return str(int(float(mem[:-1])))
    else:
        return "1024"

class FileParser:
    def __init__(self):
        self.__fileName = ''
        self.__joblist = []
        self.__lineCount = None
        self.__count = 0
    

    

    def SGE_Parser(self, fileName, lineCount=None, start=0):
        #Parse SGE File
        dictValues = ['qname', 'hostname', 'group', 'owner', 'job_name', 'job_id', 'account', 'priority', 'submission_time', \
        'start_time', 'end_time', 'failed', 'exit_status', 'ru_wallclock', 'ru_utime', 'ru_stime', 'ru_maxrss', 'ru_ixrss', 'ruismrss', \
        'ru_idrss', 'ru_isrss', 'ruminflt', 'ru_majflt', 'ru_nswap', 'ru_inblock', 'ru_outblock', 'ru_msgsnd', 'ru_msgrcv', 'ru_nsignals', \
        'ru_nvcsw', 'ru_nivcsw', 'project', 'department', 'granted_pe', 'slots', 'task_number', 'cpu', 'mem', 'io', 'catagory', 'iow', \
        'pe_taskid', 'maxvmem', 'arid', 'ar_submission_time']
        self.__fileName = fileName
        self.__lineCount = lineCount
        self.__start = start
        try:
            with open(self.__fileName, 'r', newline='') as inputFile:
                records = csv.DictReader(inputFile, fieldnames=dictValues, delimiter=':')
                for row in records:
                    try:
                        job = SGEJob()
                        if self.__lineCount != None and self.__count == int(self.__lineCount):
                            break
                        if self.__count < self.__start:
                            continue
                        self.__count += 1
                        job.qname = row['qname']
                        job.hostname = row['hostname']
                        job.group = row['group']
                        job.owner = row['owner']
                        job.job_name = row['job_name']
                        job.job_id = row['job_id']
                        job.account = row['account']
                        job.priority = row['priority']
                        job.submission_time = row['submission_time']
                        job.start_time = row['start_time']
                        job.end_time = row['end_time']
                        job.failed = row['failed']
                        job.exit_status = row['exit_status']
                        job.ru_wallclock = row['ru_wallclock']
                        job.ru_utime = row['ru_utime']
                        job.ru_stime = row['ru_stime']
                        job.ru_maxrss = row['ru_maxrss']
                        job.ru_ixrss = row['ru_ixrss']
                        job.ruismrss = row['ruismrss']
                        job.ru_idrss = row['ru_idrss']
                        job.ru_isrss = row['ru_isrss']
                        job.ruminflt = row['ruminflt']
                        job.ru_majflt = row['ru_majflt']
                        job.ru_nswap = row['ru_nswap']
                        job.ru_inblock = row['ru_inblock']
                        job.ru_outblock = row['ru_outblock']
                        job.ru_msgsnd = row['ru_msgsnd']
                        job.ru_msgrcv = row['ru_msgrcv']
                        job.ru_nsignals = row['ru_nsignals']
                        job.ru_nvcsw = row['ru_nvcsw']
                        job.ru_nivcsw = row['ru_nivcsw']
                        job.project = row['project']
                        job.department = row['department']
                        job.granted_pe = row['granted_pe']
                        job.slots = row['slots']
                        job.task_number = row['task_number']
                        job.cpu = row['cpu']
                        job.mem = row['mem']
                        job.io = row['io']
                        job.catagory = row['catagory']
                        job.iow = row['iow']
                        job.pe_taskid = row['pe_task']
                        job.maxvmem = row['maxvmem']
                        job.arid = row['arid']
                        job.ar_submission_time = row['ar_submission_time']

                        self.__joblist.append(job)

                    except:
                        print('There was a parsing error on line: ' + str(self.__count) + '\n skipping line and continuing:')
        except:
            print("error opening File please check filename and file path")
            return
        return self.__joblist
    
    def SLURM_Parser(self, fileName, lineCount=None, start=0):
        #Parse SLURM File
        self.__fileName = fileName
        self.__lineCount = lineCount
        self.__start = start
        try:
            with open(self.__fileName, 'r', newline='') as inputFile:
                records = csv.DictReader(inputFile, delimiter='|')
                for row in records:
                    try:
                        job = SlurmJob()
                        if self.__lineCount != None and self.__count == int(self.__lineCount):
                                break
                        if self.__count < self.__start:
                                continue
                        self.__count += 1
                        if 'Account' in row:
                            job.Account = row['Account']
                        if 'AdminComment' in row:
                            job.AdminComment = row['AdminComment']

                        if 'AllocCPUS' in row:
                            job.AllocCPUS = row['AllocCPUS']

                        if 'AllocGRES' in row:
                            job.AllocGRES = row['AllocGRES']

                        if 'AllocNodes' in row:
                            job.AllocNodes = row['AllocNodes']

                        if 'AllocTRES' in row:
                            job.AllocTRES = row['AllocTRES']

                        if 'AssocID' in row:
                            job.AssocID = row['AssocID']

                        if 'AveCPU' in row:
                            job.AveCPU = row['AveCPU']

                        if 'AveCPUFreq' in row:
                            job.AveCPUFreq = row['AveCPUFreq']

                        if 'AveDiskRead' in row:
                            job.AveDiskRead = row['AveDiskRead']

                        if 'AveDiskWrite' in row:
                            job.AveDiskWrite = row['AveDiskWrite']

                        if 'AvePages' in row:
                            job.AvePages = row['AvePages']

                        if 'AveRSS' in row:
                            job.AveRSS = row['AveRSS']

                        if 'AveVMSize' in row:
                            job.AveVMSize = row['AveVMSize']

                        if 'BlockID' in row:
                            job.BlockID = row['BlockID']

                        if 'Cluster' in row:
                            job.Cluster = row['Cluster']

                        if 'Comment' in row:
                            job.Comment = row['Comment']

                        if 'ConsumedEnergy' in row:
                            job.ConsumedEnergy = row['ConsumedEnergy']

                        if 'ConsumedEnergyRaw' in row:
                            job.ConsumedEnergyRaw = row['ConsumedEnergyRaw']

                        if 'CPUTime' in row:
                            job.CPUTime = row['CPUTime']

                        if 'CPUTimeRAW' in row:
                            job.CPUTimeRAW = row['CPUTimeRAW']

                        if 'DerivedExitCode' in row:
                            job.DerivedExitCode = row['DerivedExitCode']

                        if 'Elapsed' in row:
                            job.Elapsed = row['Elapsed']

                        if 'ElapsedRaw' in row:
                            job.ElapsedRaw = row['ElapsedRaw']
                            
                        if 'Eligible' in row:
                            job.Eligible = row['Eligible']

                        if 'End' in row:
                            job.End = row['End']

                        if 'ExitCode' in row:
                            job.ExitCode = row['ExitCode']

                        if 'GID' in row:
                            job.GID = row['GID']

                        if 'Group' in row:
                            job.Group = row['Group']

                        if 'JobID' in row:
                            job.JobID = row['JobID']

                        if 'JobIDRaw' in row:
                            job.JobIDRaw = row['JobIDRaw']

                        if 'JobName' in row:
                            job.JobName = row['JobName']

                        if 'Layout' in row:
                            job.Layout = row['Layout']

                        if 'MaxDiskRead' in row:
                            job.MaxDiskRead = row['MaxDiskRead']

                        if 'MaxDiskReadNode' in row:
                            job.MaxDiskReadNode = row['MaxDiskReadNode']

                        if 'MaxDiskReadTask' in row:
                            job.MaxDiskReadTask = row['MaxDiskReadTask']

                        if 'MaxDiskWrite' in row:
                            job.MaxDiskWrite = row['MaxDiskWrite']

                        if 'MaxDiskWriteNode' in row:
                            job.MaxDiskWriteNode = row['MaxDiskWriteNode']

                        if 'MaxDiskWriteTask' in row:
                            job.MaxDiskWriteTask = row['MaxDiskWriteTask']

                        if 'MaxPages' in row:
                            job.MaxPages = row['MaxPages']

                        if 'MaxPagesNode' in row:
                            job.MaxPagesNode = row['MaxPagesNode']

                        if 'MaxPagesTask' in row:
                            job.MaxPagesTask = row['MaxPagesTask']

                        if 'MaxRSS' in row:
                            job.MaxRSS = row['MaxRSS']

                        if 'MaxRSSNode' in row:
                            job.MaxRSSNode = row['MaxRSSNode']

                        if 'MaxRSSTask' in row:
                            job.MaxRSSTask = row['MaxRSSTask']

                        if 'MaxVMSize' in row:
                            job.MaxVMSize = row['MaxVMSize']

                        if 'MaxVMSizeNode' in row:
                            job.MaxVMSizeNode = row['MaxVMSizeNode']

                        if 'MaxVMSizeTask' in row:
                            job.MaxVMSizeTask = row['MaxVMSizeTask']

                        if 'McsLabel' in row:
                            job.McsLabel = row['McsLabel']

                        if 'MinCPU' in row:
                            job.MinCPU = row['MinCPU']

                        if 'MinCPUNode' in row:
                            job.MinCPUNode = row['MinCPUNode']

                        if 'MinCPUTask' in row:
                            job.MinCPUTask = row['MinCPUTask']

                        if 'NCPUS' in row:
                            job.NCPUS = row['NCPUS']

                        if 'NNodes' in row:
                            job.NNodes = row['NNodes']

                        if 'NodeList' in row:
                            job.NodeList = row['NodeList']

                        if 'NTasks' in row:
                            job.NTasks = row['NTasks']

                        if 'Priority' in row:
                            job.Priority = row['Priority']

                        if 'Partition' in row:
                            job.Partition = row['Partition']

                        if 'QOS' in row:
                            job.QOS = row['QOS']

                        if 'QOSRAW' in row:
                            job.QOSRAW = row['QOSRAW']

                        if 'ReqCPUFreq' in row:
                            job.ReqCPUFreq = row['ReqCPUFreq']

                        if 'ReqCPUFreqMin' in row:
                            job.ReqCPUFreqMin = row['ReqCPUFreqMin']

                        if 'ReqCPUFreqMax' in row:
                            job.ReqCPUFreqMax = row['ReqCPUFreqMax']

                        if 'ReqCPUFreqGov' in row:
                            job.ReqCPUFreqGov = row['ReqCPUFreqGov']

                        if 'ReqCPUS' in row:
                            job.ReqCPUS = row['ReqCPUS']

                        if 'ReqGRES' in row:
                            job.ReqGRES = row['ReqGRES']

                        if 'ReqMem' in row:
                            job.ReqMem = row['ReqMem']

                        if 'ReqNodes' in row:
                            job.ReqNodes = row['ReqNodes']

                        if 'ReqTRES' in row:
                            job.ReqTRES = row['ReqTRES']

                        if 'Reservation' in row:
                            job.Reservation = row['Reservation']

                        if 'ReservationId' in row:
                            job.ReservationId = row['ReservationId']

                        if 'Reserved' in row:
                            job.Reserved = row['Reserved']

                        if 'ResvCPU' in row:
                            job.ResvCPU = row['ResvCPU']

                        if 'ResvCPURAW' in row:
                            job.ResvCPURAW = row['ResvCPURAW']

                        if 'Start' in row:
                            job.Start = row['Start']

                        if 'State' in row:
                            job.State = row['State']

                        if 'Submit' in row:
                            job.Submit = row['Submit']

                        if 'Suspended' in row:
                            job.Suspended = row['Suspended']

                        if 'SystemCPU' in row:
                            job.SystemCPU = row['SystemCPU']

                        if 'SystemComment' in row:
                            job.SystemComment = row['SystemComment']

                        if 'Timelimit' in row:
                            job.Timelimit = row['Timelimit']

                        if 'TimelimitRaw' in row:
                            job.TimelimitRaw = row['TimelimitRaw']

                        if 'TotalCPU' in row:
                            job.TotalCPU = row['TotalCPU']

                        if 'TRESUsageInAve' in row:
                            job.TRESUsageInAve = row['TRESUsageInAve']

                        if 'TRESUsageInMax' in row:
                            job.TRESUsageInMax = row['TRESUsageInMax']

                        if 'TRESUsageInMaxNode' in row:
                            job.TRESUsageInMaxNode = row['TRESUsageInMaxNode']

                        if 'TRESUsageInMaxTask' in row:
                            job.TRESUsageInMaxTask = row['TRESUsageInMaxTask']

                        if 'TRESUsageInMin' in row:
                            job.TRESUsageInMin = row['TRESUsageInMin']

                        if 'TRESUsageInMinNode' in row:
                            job.TRESUsageInMinNode = row['TRESUsageInMinNode']

                        if 'TRESUsageInMinTask' in row:
                            job.TRESUsageInMinTask = row['TRESUsageInMinTask']

                        if 'TRESUsageInTot' in row:
                            job.TRESUsageInTot = row['TRESUsageInTot']

                        if 'TRESUsageOutAve' in row:
                            job.TRESUsageOutAve = row['TRESUsageOutAve']

                        if 'TRESUsageOutMax' in row:
                            job.TRESUsageOutMax = row['TRESUsageOutMax']

                        if 'TRESUsageOutMaxNode' in row:
                            job.TRESUsageOutMaxNode = row['TRESUsageOutMaxNode']

                        if 'TRESUsageOutMaxTask' in row:
                            job.TRESUsageOutMaxTask = row['TRESUsageOutMaxTask']

                        if 'TRESUsageOutMin' in row:
                            job.TRESUsageOutMin = row['TRESUsageOutMin']

                        if 'TRESUsageOutMinNode' in row:
                            job.TRESUsageOutMinNode = row['TRESUsageOutMinNode']

                        if 'TRESUsageOutMinTask' in row:
                            job.TRESUsageOutMinTask = row['TRESUsageOutMinTask']

                        if 'TRESUsageOutTot' in row:
                            job.TRESUsageOutTot = row['TRESUsageOutTot']

                        if 'UID' in row:
                            job.UID = row['UID']

                        if 'User' in row:
                            job.User = row['User']

                        if 'UserCPU' in row:
                            job.UserCPU = row['UserCPU']

                        if 'WCKey' in row:
                            job.WCKey = row['WCKey']

                        if 'WCKeyID' in row:
                            job.WCKeyID = row['WCKeyID']

                        if 'WorkDir' in row:
                            job.WorkDir = row['WorkDir']

                        self.__joblist.append(job)
                    except Exception as ex:
                        print('There was a parsing error on line: ' + str(self.__count) + '\n skipping line and continuing. the Exact error follows this message: \n')
                        print(ex)
        except Exception as ex:
            print("error opening File please check filename. the Exact error follows this message: \n")
            print(ex)
            return
        return self.__joblist