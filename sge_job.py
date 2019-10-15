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
        return "test"