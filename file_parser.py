#Description: Parser for reading in 

import csv
from sge_job import SGEJob
from slurm_job import SlurmJob

def mem_parse(mem):
    if(mem[-1] == 'G' or mem[-1] == 'g'):
        return str(int(float(mem[:-1]) * 1024))
    elif(mem[-1] == 'M' or mem[-1] == 'm'):
        return str(int(float(mem[:-1])))
    else:
        return "1024"

class FileParser:
    def __init__(self):
        self.__fileName = None
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
                        job.set_qname(row['qname'])
                        job.set_hostname(row['hostname'])
                        job.set_group(row['group'])
                        job.set_owner(row['owner'])
                        job.set_job_name(row['job_name'])
                        job.set_job_id(row['job_id'])
                        job.set_account(row['account'])
                        job.set_priority(row['priority'])
                        job.set_submission_time(row['submission_time'])
                        job.set_start_time(row['start_time'])
                        job.set_end_time(row['end_time'])
                        job.set_failed(row['failed'])
                        job.set_exit_status(row['exit_status'])
                        job.set_ru_wallclock(row['ru_wallclock'])
                        job.set_ru_utime(row['ru_utime'])
                        job.set_ru_stime(row['ru_stime'])
                        job.set_ru_maxrss(row['ru_maxrss'])
                        job.set_ru_ixrss(row['ru_ixrss'])
                        job.set_ruismrss(row['ruismrss'])
                        job.set_ru_idrss(row['ru_idrss'])
                        job.set_ru_isrss(row['ru_isrss'])
                        job.set_ruminflt(row['ruminflt'])
                        job.set_ru_majflt(row['ru_majflt'])
                        job.set_ru_nswap(row['ru_nswap'])
                        job.set_ru_inblock(row['ru_inblock'])
                        job.set_ru_outblock(row['ru_outblock'])
                        job.set_ru_msgsnd(row['ru_msgsnd'])
                        job.set_ru_msgrcv(row['ru_msgrcv'])
                        job.set_ru_nsignals(row['ru_nsignals'])
                        job.set_ru_nvcsw(row['ru_nvcsw'])
                        job.set_ru_nivcsw(row['ru_nivcsw'])
                        job.set_project(row['project'])
                        job.set_department(row['department'])
                        job.set_granted_pe(row['granted_pe'])
                        job.set_slots(row['slots'])
                        job.set_task_number(row['task_number'])
                        job.set_cpu(row['cpu'])
                        job.set_mem(row['mem'])
                        job.set_io(row['io'])
                        job.set_catagory(row['catagory'])
                        job.set_iow(row['iow'])
                        job.set_pe_taskid(row['pe_task'])
                        job.set_maxvmem(row['maxvmem'])
                        job.set_arid(row['arid'])
                        job.set_ar_submission_time(row['ar_submission_time'])

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
                        if self.__count <= self.__start:
                                continue
                        self.__count += 1
                        if row['Account']:
                            job.set_Account(row['Account'])
                        if row['AdminComment']:
                            job.set_AdminComment(row['AdminComment'])
                        if row['AllocCPUS']:
                            job.set_AllocCPUS(row['AllocCPUS'])
                        if row['AllocGRES']:
                            job.set_AllocGRES(row['AllocGRES'])
                        if row['AllocNodes']:
                            job.set_AllocNodes(row['AllocNodes'])
                        if row['AllocTRES']:
                            job.set_AllocTRES(row['AllocTRES'])
                        if row['AssocID']:
                            job.set_AssocID(row['AssocID'])
                        if row['AveCPU']:
                            job.set_AveCPU(row['AveCPU'])
                        if row['AveCPUFreq']:
                            job.set_AveCPUFreq(row['AveCPUFreq'])
                        if row['AveDiskRead']:
                            job.set_AveDiskRead(row['AveDiskRead'])
                        if row['AveDiskWrite']:
                            job.set_AveDiskWrite(row['AveDiskWrite'])
                        if row['AvePages']:
                            job.set_AvePages(row['AvePages'])
                        if row['AveRSS']:
                            job.set_AveRSS(row['AveRSS'])
                        if row['AveVMSize']:
                            job.set_AveVMSize(row['AveVMSize'])
                        if row['BlockID']:
                            job.set_BlockID(row['BlockID'])
                        if row['Cluster']:
                            job.set_Cluster(row['Cluster'])
                        if row['Comment']:
                            job.set_Comment(row['Comment'])
                        if row['ConsumedEnergy']:
                            job.set_ConsumedEnergy(row['ConsumedEnergy'])
                        if row['ConsumedEnergyRaw']:
                            job.set_ConsumedEnergyRaw(row['ConsumedEnergyRaw'])
                        if row['CPUTime']:
                            job.set_CPUTime(row['CPUTime'])
                        if row['CPUTimeRAW']:
                            job.set_CPUTimeRAW(row['CPUTimeRAW'])
                        if row['DerivedExitCode']:
                            job.set_DerivedExitCode(row['DerivedExitCode'])
                        if row['Elapsed']:
                            job.set_Elapsed(row['Elapsed'])
                        if row['ElapsedRaw']:
                            job.set_ElapsedRaw(row['ElapsedRaw'])
                        if row['Eligible']:
                            job.set_Eligible(row['Eligible'])
                        if row['End']:
                            job.set_End(row['End'])
                        if row['ExitCode']:
                            job.set_ExitCode(row['ExitCode'])
                        if row['GID']:
                            job.set_GID(row['GID'])
                        if row['Group']:
                            job.set_Group(row['Group'])
                        if row['JobID']:
                            job.set_JobID(row['JobID'])
                        if row['JobIDRaw']:
                            job.set_JobIDRaw(row['JobIDRaw'])
                        if row['JobName']:
                            job.set_JobName(row['JobName'])
                        if row['Layout']:
                            job.set_Layout(row['Layout'])
                        if row['MaxDiskRead']:
                            job.set_MaxDiskRead(row['MaxDiskRead'])
                        if row['MaxDiskReadNode']:
                            job.set_MaxDiskReadNode(row['MaxDiskReadNode'])
                        if row['MaxDiskReadTask']:
                            job.set_MaxDiskReadTask(row['MaxDiskReadTask'])
                        if row['MaxDiskWrite']:
                            job.set_MaxDiskWrite(row['MaxDiskWrite'])
                        if row['MaxDiskWriteNode']:
                            job.set_MaxDiskWriteNode(row['MaxDiskWriteNode'])
                        if row['MaxDiskWriteTask']:
                            job.set_MaxDiskWriteTask(row['MaxDiskWriteTask'])
                        if row['MaxPages']:
                            job.set_MaxPages(row['MaxPages'])
                        if row['MaxPagesNode']:
                            job.set_MaxPagesNode(row['MaxPagesNode'])
                        if row['MaxPagesTask']:
                            job.set_MaxPagesTask(row['MaxPagesTask'])
                        if row['MaxRSS']:
                            job.set_MaxRSS(row['MaxRSS'])
                        if row['MaxRSSNode']:
                            job.set_MaxRSSNode(row['MaxRSSNode'])
                        if row['MaxRSSTask']:
                            job.set_MaxRSSTask(row['MaxRSSTask'])
                        if row['MaxVMSize']:
                            job.set_MaxVMSize(row['MaxVMSize'])
                        if row['MaxVMSizeNode']:
                            job.set_MaxVMSizeNode(row['MaxVMSizeNode'])
                        if row['MaxVMSizeTask']:
                            job.set_MaxVMSizeTask(row['MaxVMSizeTask'])
                        if row['McsLabel']:
                            job.set_McsLabel(row['McsLabel'])
                        if row['MinCPU']:
                            job.set_MinCPU(row['MinbCPU'])
                        if row['MinCPUNode']:
                            job.set_MinCPUNode(row['MinCPUNode'])
                        if row['MinCPUTask']:
                            job.set_MinCPUTask(row['MinCPUTask'])
                        if row['NCPUS']:
                            job.set_NCPUS(row['NCPUS'])
                        if row['NNodes']:
                            job.set_NNodes(row['NNodes'])
                        if row['NodeList']:
                            job.set_NodeList(row['NodeList'])
                        if row['NTasks']:
                            job.set_NTasks(row['NTasks'])
                        if row['Priority']:
                            job.set_Priority(row['Priority'])
                        if row['Partition']:
                            job.set_Partition(row['Partition'])
                        if row['QOS']:
                            job.set_QOS(row['QOS'])
                        if row['QOSRAW']:
                            job.set(row['QOSRAW'])
                        if row['ReqCPUFreq']:
                            job.set_ReqCPUFreq(row['ReqCPUFreq'])
                        if row['ReqCPUFreqMin']:
                            job.set_ReqCPUFreqMin(row['ReqCPUFreqMin'])
                        if row['ReqCPUFreqMax']:
                            job.set_ReqCPUFreqMax(row['ReqCPUFreqMax'])
                        if row['ReqCPUFreqGov']:
                            job.set_ReqCPUFreqGov(row['ReqCPUFreqGov'])
                        if row['ReqCPUS']:
                            job.set(row['ReqCPUS'])
                        if row['ReqGRES']:
                            job.set_ReqGRES(row['ReqGRES'])
                        if row['ReqMem']:
                            job.set_ReqMem(row['ReqMem'])
                        if row['ReqNodes']:
                            job.set_ReqNodes(row['ReqNodes'])
                        if row['ReqTRES']:
                            job.set_ReqTRES(row['ReqTRES'])
                        if row['Reservation']:
                            job.set_Reservation(row['Reservation'])
                        if row['ReservationId']:
                            job.set_ReservationId(row['ReservationId'])
                        if row['Reserved']:
                            job.set_Reserved(row['Reserved'])
                        if row['ResvCPU']:
                            job.set_ResvCPU(row['ResvCPU'])
                        if row['ResvCPURAW']:
                            job.set_ResvCPURAW(row['ResvCPURAW'])
                        if row['Start']:
                            job.set_Start(row['Start'])
                        if row['State']:
                            job.set_State(row['State'])
                        if row['Submit']:
                            job.set_Submit(row['Submit'])
                        if row['Suspended']:
                            job.set_Suspended(row['Suspended'])
                        if row['SystemCPU']:
                            job.set_SystemCPU(row['SystemCPU'])
                        if row['SystemComment']:
                            job.set_SystemComment(row['SystemComment'])
                        if row['Timelimit']:
                            job.set_Timelimit(row['TimeLimit'])
                        if row['TimelimitRaw']:
                            job.set_TimelimitRaw(row['TimelimitRaw'])
                        if row['TotalCPU']:
                            job.set_TotalCPU(row['TotalCPU'])
                        if row['TRESUsageInAve']:
                            job.set_TRESUsageInAve(row['TRESUsageInAve'])
                        if row['TRESUsageInMax']:
                            job.set_TRESUsageInMax(row['TRESUsageInMax'])
                        if row['TRESUsageInMaxNode']:
                            job.set_TRESUsageInMaxNode(row['TRESUsageInMaxNode'])
                        if row['TRESUsageInMaxTask']:
                            job.set_TRESUsageInMaxTask(row['TRESUsageInMaxTask'])
                        if row['TRESUsageInMin']:
                            job.set_TRESUsageInMin(row['TRESUsageInMin'])
                        if row['TRESUsageInMinNode']:
                            job.set_TRESUsageInMinNode(row['TRESUsageInMinNode'])
                        if row['TRESUsageInMinTask']:
                            job.set_TRESUsageInMinTask(row['TRESUsageInMinTask'])
                        if row['TRESUsageInTot']:
                            job.set_TRESUsageInTot(row['TRESUsageInTot'])
                        if row['TRESUsageOutAve']:
                            job.set_TRESUsageOutAve(row['TRESUsageOutAve'])
                        if row['TRESUsageOutMax']:
                            job.set_TRESUsageOutMax(row['TRESUsageOutMax'])
                        if row['TRESUsageOutMaxNode']:
                            job.set_TRESUsageOutMAxNode(row['TRESUsageOutMaxNode'])
                        if row['TRESUsageOutMaxTask']:
                            job.set_TRESusageOutMaxTask(row['TRESUsageOutMaxTask'])
                        if row['TRESUsageOutMin']:
                            job.set_
                        if row['TRESUsageOutMinNode']:
                            job.set_TRESUsageOutMinNode(row['TRESUsageOutMinNode'])
                        if row['TRESUsageOutMinTask']:
                            job.set_TRESUsageOutMinTask(row['TRESUsageOutMinTask'])
                        if row['TRESUsageOutTot']:
                            job.set_TRESUsageOutTot(row['TRESUsageOutTot'])
                        if row['UID']:
                            job.set_UID(row['UID'])
                        if row['User']:
                            job.set_User(row['User'])
                        if row['UserCPU']:
                            job.set_UserCPU(row['UserCPU'])
                        if row['WCKey']:
                            job.set_WCKey(row['WCKey'])
                        if row['WCKeyID']:
                            job.set_WCKeyID(row['WCKeyID'])
                        if row['WorkDir']:
                            job.set_WorkDir(row['WorkDir'])

                        self.__joblist.append(job)
                    except:
                        print('There was a parsing error on line: ' + str(self.__count) + '\n skipping line and continuing:')
        except:
            print("error opening File please check filename")
            return
        return self.__joblist