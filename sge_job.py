class SGEJob:
    def __init__(self, qname=None, hostname=None, group=None, owner=None, job_name=None, job_id=None, account=None, priority=None, submission_time=None, \
                start_time=None, end_time=None, failed=None, exit_status=None, ru_wallclock=None, ru_utime=None, ru_stime=None, ru_maxrss=None, ru_ixrss=None, ruismrss=None, \
                ru_idrss=None, ru_isrss=None, ruminflt=None, ru_majflt=None, ru_nswap=None, ru_inblock=None, ru_outblock=None, ru_msgsnd=None, ru_msgrcv=None, ru_nsignals=None, \
                ru_nvcsw=None, ru_nivcsw=None, project=None, department=None, granted_pe=None, slots=None, task_number=None, cpu=None, mem=None, io=None, catagory=None, iow=None, \
                pe_taskid=None, maxvmem=None, arid=None, ar_submission_time=None)
                
        self.qname              = qname
        self.hostname           = hostname
        self.group              = group
        self.owner              = owner
        self.job_name           = job_name
        self.job_id             = job_id
        self.account            = account
        self.priority           = priority
        self.submission_time    = submission_time
        self.start_time         = start_time
        self.end_time           = end_time
        self.failed             = failed
        self.exit_status        = exit_status
        self.ru_wallclock       = ru_wallclock
        self.ru_utime           = ru_utime
        self.ru_stime           = ru_stime
        self.ru_maxrss          = ru_maxrss
        self.ru_ixrss           = ru_ixrss
        self.ruismrss           = ruismrss
        self.ru_idrss           = ru_idrss
        self.ru_isrss           = ru_isrss
        self.ruminflt           = ruminflt
        self.ru_majflt          = ru_majflt
        self.ru_nswap           = ru_nswap
        self.ru_inblock         = ru_inblock
        self.ru_outblock        = ru_outblock
        self.ru_msgsnd          = ru_msgsnd
        self.ru_msgrcv          = ru_msgrcv
        self.ru_nsignals        = ru_nsignals
        self.ru_nvcsw           = ru_nvcsw
        self.ru_nivcsw          = ru_nivcsw
        self.project            = project
        self.department         = department
        self.granted_pe         = granted_pe
        self.slots              = slots
        self.task_number        = task_number
        self.cpu                = cpu
        self.mem                = mem
        self.io                 = io
        self.catagory           = catagory
        self.iow                = iow       
        self.pe_taskid          = pe_taskid
        self.maxvmem            = maxvmem
        self.arid               = arid
        self.ar_submission_time = ar_submission_time