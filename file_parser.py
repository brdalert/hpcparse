#Description: Parser for reading in 

import csv
import sge_job
import slurm_job
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
        regex_h_rt = re.compile('h_rt=*')
        try:
            with open(self.__fileName, 'r', newline='') as inputFile:
                records = csv.DictReader(inputFile, fieldnames=dictValues, delimiter=':')
                for row in records:
                    try:
                        if self.__lineCount != None and self.__count == int(self.__lineCount):
                            break
                        if self.__count < self.__start:
                            continue
                        self.__count += 1
                        username = row['owner']
                        jobID = row['job_id']
                        date = str(datetime.utcfromtimestamp(int(row['submission_time'])))
                        duration_actual = row['ru_wallclock']
                        mem_used = str(int(float(row['ru_maxrss']) / 1024))
                        l = list(filter(regex_h_rt.search, row['catagory'].split(" ")))[0]
                        resources = dict(item.split('=') for item in l.split(','))
                        wclimit = str(int(resources['h_rt']) / 60)
                        req_mem = mem_parse(resources['memory'])
                        req_mem_per_cpu = '1'
                        if row['granted_pe'] == "NONE":
                            tasks = '1'
                            cpus_per_task = '1'
                            self.__joblist.append(Job(username, jobID, date, duration_actual, mem_used, tasks, wclimit, req_mem_per_cpu=req_mem_per_cpu, req_mem=req_mem, cpus_per_task=cpus_per_task))
                        elif row['granted_pe'] == "single":
                            tasks = '1'
                            cpus_per_task = row['slots']
                            self.__joblist.append(Job(username, jobID, date, duration_actual, mem_used, tasks, wclimit, req_mem_per_cpu=req_mem_per_cpu, req_mem=req_mem, cpus_per_task=cpus_per_task))
                        else:
                            temp = row['granted_pe'].split("-")
                            if temp[1] == 'spread' or temp[1] == 'fill':
                                continue
                            else:
                                tasks = temp[1]
                                cpus_per_task = str(int(int(row['slots'])/int(tasks)))
                                self.__joblist.append(Job(username, jobID, date, duration_actual, mem_used, tasks, wclimit, req_mem_per_cpu=req_mem_per_cpu, req_mem=req_mem, cpus_per_task=cpus_per_task))
                    except:
                        print('There was a parsing error on line: ' + str(self.__count) + '\n skipping line and continuing:')
        except:
            print("error opening File please check filename")
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