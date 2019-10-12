class SGEJob:
    def __init__(self):
        self.__qname              = None
        self.__hostname           = None
        self.__group              = None
        self.__owner              = None
        self.__job_name           = None
        self.__job_id             = None
        self.__account            = None
        self.__priority           = None
        self.__submission_time    = None
        self.__start_time         = None
        self.__end_time           = None
        self.__failed             = None
        self.__exit_status        = None
        self.__ru_wallclock       = None
        self.__ru_utime           = None
        self.__ru_stime           = None
        self.__ru_maxrss          = None
        self.__ru_ixrss           = None
        self.__ruismrss           = None
        self.__ru_idrss           = None
        self.__ru_isrss           = None
        self.__ruminflt           = None
        self.__ru_majflt          = None
        self.__ru_nswap           = None
        self.__ru_inblock         = None
        self.__ru_outblock        = None
        self.__ru_msgsnd          = None
        self.__ru_msgrcv          = None
        self.__ru_nsignals        = None
        self.__ru_nvcsw           = None
        self.__ru_nivcsw          = None
        self.__project            = None
        self.__department         = None
        self.__granted_pe         = None
        self.__slots              = None
        self.__task_number        = None
        self.__cpu                = None
        self.__mem                = None
        self.__io                 = None
        self.__catagory           = None
        self.__iow                = None       
        self.__pe_taskid          = None
        self.__maxvmem            = None
        self.__arid               = None
        self.__ar_submission_time = None

    def set_qname(self, x):
        self.__qname = x

    def set_hostname(self, x):
        self.__hostname = x

    def set_group(self, x):
        self.__group = x

    def set_owner(self, x):
        self.__owner = x

    def set_job_name(self, x):
        self.__job_name = x

    def set_job_id(self, x):
        self.__job_id = x

    def set_account(self, x):
        self.__account = x

    def set_priority(self, x):
        self.__priority = x

    def set_submission_time(self, x):
        self.__submission_time = x

    def set_start_time(self, x):
        self.__start_time = x

    def set_end_time(self, x):
        self.__end_time = x

    def set_failed(self, x):
        self.__failed = x

    def set_exit_status(self, x):
        self.__exit_status = x

    def set_ru_wallclock(self, x):
        self.__ru_wallclock = x

    def set_ru_utime(self, x):
        self.__ru_utime = x

    def set_ru_stime(self, x):
        self.__ru_stime = x

    def set_ru_maxrss(self, x):
        self.__ru_maxrss = x

    def set_ru_ixrss(self, x):
        self.__ru_ixrss = x

    def set_ruismrss(self, x):
        self.__ruismrss = x

    def set_ru_idrss(self, x):
        self.__ru_idrss = x

    def set_ru_isrss(self, x):
        self.__ru_isrss = x

    def set_ruminflt(self, x):
        self.__ruminflt = x

    def set_ru_majflt(self, x):
        self.__ru_majflt = x

    def set_ru_nswap(self, x):
        self.__ru_nswap = x

    def set_ru_inblock(self, x):
        self.__ru_inblock = x

    def set_ru_outblock(self, x):
        self.__ru_outblock = x

    def set_ru_msgsnd(self, x):
        self.__ru_msgsnd = x

    def set_ru_msgrcv(self, x):
        self.__ru_msgrcv = x

    def set_ru_nsignals(self, x):
        self.__ru_nsignals = x

    def set_ru_nvcsw(self, x):
        self.__ru_nvcsw = x

    def set_ru_nivcsw(self, x):
        self.__ru_nivcsw = x

    def set_project(self, x):
        self.__project = x

    def set_department(self, x):
        self.__department = x

    def set_granted_pe(self, x):
        self.__granted_pe = x

    def set_slots(self, x):
        self.__slots = x

    def set_task_number(self, x):
        self.__task_number = x

    def set_cpu(self, x):
        self.__cpu = x

    def set_mem(self, x):
        self.__mem = x

    def set_io(self, x):
        self.__io = x

    def set_catagory(self, x):
        self.__catagory = x

    def set_iow(self, x):
        self.__iow = x

    def set_pe_taskid(self, x):
        self.__pe_taskid = x

    def set_maxvmem(self, x):
        self.__maxvmem = x

    def set_arid(self, x):
        self.__arid = x

    def set_ar_submission_time(self, x):
        self.__ar_submission_time = x