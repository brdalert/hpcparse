#Description: Parser for reading in 

import csv
from sge_job import SGEJob
from slurm_job import SlurmJob
import re
from datetime import datetime


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
    

    

    def SGE_Parser(self, fileName, lineCount, start):
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
                        job.set_qname = row['qname']
                        job.set_hostname = row['hostname']
                        job.set_group = row['group']
                        job.set_owner = row['owner']
                        job.set_job_name = row['job_name']
                        job.set_job_id = row['job_id']
                        job.set_account = row['account']
                        job.set_priority = row['priority']
                        job.set_submission_time = row['submission_time']
                        job.set_start_time = row['start_time']
                        job.set_end_time = row['end_time']
                        job.set_failed = row['failed']
                        job.set_exit_status = row['exit_status']
                        job.set_ru_wallclock = row['ru_wallclock']
                        job.set_ru_utime = row['ru_utime']
                        job.set_ru_stime = row['ru_stime']
                        job.set_ru_maxrss = row['ru_maxrss']
                        job.set_ru_ixrss = row['ru_ixrss']
                        job.set_ruismrss = row['ruismrss']
                        job.set_ru_idrss = row['ru_idrss']
                        job.set_ru_isrss = row['ru_isrss']
                        job.set_ruminflt = row['ruminflt']
                        job.set_ru_majflt = row['ru_majflt']
                        job.set_ru_nswap = row['ru_nswap']
                        job.set_ru_inblock = row['ru_inblock']
                        job.set_ru_outblock = row['ru_outblock']
                        job.set_ru_msgsnd = row['ru_msgsnd']
                        job.set_ru_msgrcv = row['ru_msgrcv']
                        job.set_ru_nsignals = row['ru_nsignals']
                        job.set_ru_nvcsw = row['ru_nvcsw']
                        job.set_ru_nivcsw = row['ru_nivcsw']
                        job.set_project = row['project']
                        job.set_department = row['department']
                        job.set_granted_pe = row['granted_pe']
                        job.set_slots = row['slots']
                        job.set_task_number = row['task_number']
                        job.set_cpu = row['cpu']
                        job.set_mem = row['mem']
                        job.set_io = row['io']
                        job.set_catagory = row['catagory']
                        job.set_iow = row['iow']
                        job.set_pe_taskid = row['pe_task']
                        job.set_maxvmem = row['maxvmem']
                        job.set_arid = row['arid']
                        job.set_ar_submission_time = row['ar_submission_time']

                        self.__joblist.append(job)

                    except:
                        print('There was a parsing error on line: ' + str(self.__count) + '\n skipping line and continuing:')
        except:
            print("error opening File please check filename and file path")
            return
        return self.__joblist
    
    def SLURM_Parser(self, fileName, lineCount, start):
        #Parse SLURM File
        self.__fileName = fileName
        self.__lineCount = lineCount
        self.__start = start
        try:
            with open(self.__fileName, 'r', newline='') as inputFile:
                records = csv.DictReader(inputFile, delimiter='|')
                for row in records:
                    try:
                        if self.__lineCount != None and self.__count == int(self.__lineCount):
                                break
                        if self.__count <= self.__start:
                                continue
                        self.__count += 1
                        if row['User']:
                            username = row['User']
                        if row['JobID']:
                            jobID = row['JobID']
                        if not jobID.isdigit():
                            continue
                        date = row['Submit']
                        mem_used = row['MaxRSS']
                        tasks = row['NTasks']
                        wclimit = row['TimelimitRaw']
                        duration_actual = str(100)
                        if row['ReqMem'][-1] == 'c':
                            req_mem_per_cpu = mem_parse(row['ReqMem'][:-1])
                            self.__joblist.append(Job(username, jobID, date, duration_actual, mem_used, tasks, wclimit, req_mem_per_cpu))
                        else:
                            req_mem = mem_parse(row['ReqMem'][:-1])
                            self.__joblist.append(Job(username, jobID, date, duration_actual, mem_used, tasks, wclimit, req_mem))
                    except:
                        print('There was a parsing error on line: ' + str(self.__count) + '\n skipping line and continuing:')
        except:
            print("error opening File please check filename")
            return
        return self.__joblist