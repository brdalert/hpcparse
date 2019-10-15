class SGEJob:
    def __init__(self):
        self.qname              = None
        self.hostname           = None
        self.group              = None
        self.owner              = None
        self.job_name           = None
        self.job_id             = None
        self.account            = None
        self.priority           = None
        self.submission_time    = None
        self.start_time         = None
        self.end_time           = None
        self.failed             = None
        self.exit_status        = None
        self.ru_wallclock       = None
        self.ru_utime           = None
        self.ru_stime           = None
        self.ru_maxrss          = None
        self.ru_ixrss           = None
        self.ruismrss           = None
        self.ru_idrss           = None
        self.ru_isrss           = None
        self.ruminflt           = None
        self.ru_majflt          = None
        self.ru_nswap           = None
        self.ru_inblock         = None
        self.ru_outblock        = None
        self.ru_msgsnd          = None
        self.ru_msgrcv          = None
        self.ru_nsignals        = None
        self.ru_nvcsw           = None
        self.ru_nivcsw          = None
        self.project            = None
        self.department         = None
        self.granted_pe         = None
        self.slots              = None
        self.task_number        = None
        self.cpu                = None
        self.mem                = None
        self.io                 = None
        self.catagory           = None
        self.iow                = None       
        self.pe_taskid          = None
        self.maxvmem            = None
        self.arid               = None
        self.ar_submission_time = None
    
    def __str__(self):
        return """owner:{}, job_name:{}, job_id:{}, qname:{}, hostname:{}, group:{}, \
            account:{}, priority:{}, submission_time:{}, start_time:{}, end_time:{}, \
            failed:{}, exit_status:{}, ru_wallclock:{}, ru_utime:{}, ru_stime:{}, \
            ru_maxrss:{}, ru_ixrss:{}, ruismrss:{}, ru_idrss:{}, ru_isrss:{}, \
            ruminflt:{}, ru_majflt:{}, ru_nswap:{}, ru_inblock:{}, ru_outblock:{}, \
            ru_msgsnd:{}, ru_msgrcv:{}, ru_nsignals:{}, ru_nvcsw:{}, ru_nivcsw:{}, \
            project:{}, department:{}, granted_pe :{}, slots:{}, task_number:{}, \
            cpu:{}, mem:{}, io:{}, catagory:{}, iow:{}, pe_taskid:{}, maxvmem:{}, \
            arid:{}, ar_submission_time:{}""".format(self.owner, self.job_name, self.qname, self.hostname, self.group, self.job_id,
            self.account, self.priority, self.submission_time, self.start_time, self.end_time,
            self.failed, self.exit_status, self.ru_wallclock, self.ru_utime, self.ru_stime,
            self.ru_maxrss, self.ru_ixrss, self.ruismrss, self.ru_idrss, self.ru_isrss,
            self.ruminflt, self.ru_majflt, self.ru_nswap, self.ru_inblock, self.ru_outblock,
            self.ru_msgsnd, self.ru_msgrcv, self.ru_nsignals, self.ru_nvcsw, self.ru_nivcsw,
            self.project, self.department, self.granted_pe , self.slots, self.task_number,
            self.cpu, self.mem, self.io, self.catagory, self.iow, self.pe_taskid, self.maxvmem,
            self.arid, self.ar_submission_time)

    def __repr__(self):
        return { 'owner':self.owner, 'job_name':self.job_name, 'job_id':self.job_id, 'qname':self.qname,
            'hostname':self.hostname, 'group':self.group, 'account':self.account, 'priority':self.priority,
            'submission_time':self.submission_time, 'start_time':self.start_time, 'end_time':self.end_time,
            'failed':self.failed, 'exit_status':self.exit_status, 'ru_wallclock':self.ru_wallclock, 
            'ru_utime':self.ru_utime, 'ru_stime':self.ru_stime, 'ru_maxrss':self.ru_maxrss, 'ru_ixrss':self.ru_ixrss,
            'ruismrss':self.ruismrss, 'ru_idrss':self.ru_idrss, 'ru_isrss':self.ru_isrss, 'ruminflt':self.ruminflt,
            'ru_majflt':self.ru_majflt, 'ru_nswap':self.ru_nswap, 'ru_inblock':self.ru_inblock,
            'ru_outblock':self.ru_outblock, 'ru_msgsnd':self.ru_msgsnd, 'ru_msgrcv':self.ru_msgrcv,
            'ru_nsignals':self.ru_nsignals, 'ru_nvcsw':self.ru_nvcsw, 'ru_nivcsw':self.ru_nivcsw,
            'project':self.project, 'department':self.department, 'granted_pe':self.granted_pe, 
            'slots':self.slots, 'task_number':self.task_number, 'cpu':self.cpu, 'mem':self.mem,
            'io':self.io, 'catagory':self.catagory, 'iow':self.iow, 'pe_taskid':self.pe_taskid,
            'maxvmem':self.maxvmem, 'arid':self.arid, 'ar_submission_time':self.ar_submission_time}