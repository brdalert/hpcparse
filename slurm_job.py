class SlurmJob:
    def __init__(self):
        self.__Account              = None
        self.__AdminComment         = None
        self.__AllocCPUS            = None
        self.__AllocGRES            = None
        self.__AllocNodes           = None
        self.__AllocTRES            = None
        self.__AssocID              = None
        self.__AveCPU               = None
        self.__AveCPUFreq           = None
        self.__AveDiskRead          = None
        self.__AveDiskWrite         = None
        self.__AvePages             = None
        self.__AveRSS               = None
        self.__AveVMSize            = None
        self.__BlockID              = None
        self.__Cluster              = None
        self.__Comment              = None
        self.__ConsumedEnergy       = None
        self.__ConsumedEnergyRaw    = None
        self.__CPUTime              = None
        self.__CPUTimeRAW           = None
        self.__DerivedExitCode      = None
        self.__Elapsed              = None
        self.__ElapsedRaw           = None
        self.__Eligible             = None
        self.__End                  = None
        self.__ExitCode             = None
        self.__GID                  = None
        self.__Group                = None
        self.__JobID                = None
        self.__JobIDRaw             = None
        self.__JobName              = None
        self.__Layout               = None
        self.__MaxDiskRead          = None
        self.__MaxDiskReadNode      = None
        self.__MaxDiskReadTask      = None
        self.__MaxDiskWrite         = None
        self.__MaxDiskWriteNode     = None
        self.__MaxDiskWriteTask     = None
        self.__MaxPages             = None 
        self.__MaxPagesNode         = None
        self.__MaxPagesTask         = None
        self.__MaxRSS               = None
        self.__MaxRSSNode           = None
        self.__MaxRSSTask           = None
        self.__MaxVMSize            = None
        self.__MaxVMSizeNode        = None
        self.__MaxVMSizeTask        = None
        self.__McsLabel             = None
        self.__MinCPU               = None
        self.__MinCPUNode           = None
        self.__MinCPUTask           = None
        self.__NCPUS                = None
        self.__NNodes               = None
        self.__NodeList             = None
        self.__NTasks               = None
        self.__Priority             = None
        self.__Partition            = None
        self.__QOS                  = None
        self.__QOSRAW               = None
        self.__ReqCPUFreq           = None
        self.__ReqCPUFreqMin        = None
        self.__ReqCPUFreqMax        = None
        self.__ReqCPUFreqGov        = None
        self.__ReqCPUS              = None
        self.__ReqGRES              = None
        self.__ReqMem               = None
        self.__ReqNodes             = None
        self.__ReqTRES              = None
        self.__Reservation          = None
        self.__ReservationId        = None
        self.__Reserved             = None
        self.__ResvCPU              = None
        self.__ResvCPURAW           = None
        self.__Start                = None
        self.__State                = None
        self.__Submit               = None
        self.__Suspended            = None
        self.__SystemCPU            = None
        self.__SystemComment        = None
        self.__Timelimit            = None
        self.__TimelimitRaw         = None
        self.__TotalCPU             = None
        self.__TRESUsageInAve       = None
        self.__TRESUsageInMax       = None
        self.__TRESUsageInMaxNode   = None
        self.__TRESUsageInMaxTask   = None
        self.__TRESUsageInMin       = None
        self.__TRESUsageInMinNode   = None
        self.__TRESUsageInMinTask   = None
        self.__TRESUsageInTot       = None
        self.__TRESUsageOutAve      = None
        self.__TRESUsageOutMax      = None
        self.__TRESUsageOutMaxNode  = None
        self.__TRESUsageOutMaxTask  = None
        self.__TRESUsageOutMin      = None
        self.__TRESUsageOutMinNode  = None
        self.__TRESUsageOutMinTask  = None
        self.__TRESUsageOutTot      = None
        self.__UID                  = None
        self.__User                 = None
        self.__UserCPU              = None
        self.__WCKey                = None
        self.__WCKeyID              = None
        self.__WorkDir              = None

    def set_Account(self, x):
        self.__Account = x

    def set_AdminComment(self, x):
        self.__AdminComment = x

    def set_AllocCPUS(self, x):
        self.__AllocCPUS = x

    def set_AllocGRES(self, x):
        self.__AllocGRES = x

    def set_AllocNodes(self, x):
        self.__AllocNodes = x

    def set_AllocTRES(self, x):
        self.__AllocTRES = x

    def set_AssocID(self, x):
        self.__AssocID = x

    def set_AveCPU(self, x):
        self.__AveCPU = x

    def set_AveCPUFreq(self, x):
        self.__AveCPUFreq = x

    def set_AveDiskRead(self, x):
        self.__AveDiskRead = x

    def set_AveDiskWrite(self, x):
        self.__AveDiskWrite = x

    def set_AvePages(self, x):
        self.__AvePages = x

    def set_AveRSS(self, x):
        self.__AveRSS = x

    def set_AveVMSize(self, x):
        self.__AveVMSize = x

    def set_BlockID(self, x):
        self.__BlockID = x

    def set_Cluster(self, x):
        self.__Cluster = x

    def set_Comment(self, x):
        self.__Comment = x

    def set_ConsumedEnergy(self, x):
        self.__ConsumedEnergy = x

    def set_ConsumedEnergyRaw(self, x):
        self.__ConsumedEnergyRaw = x

    def set_CPUTime(self, x):
        self.__CPUTime = x

    def set_CPUTimeRAW(self, x):
        self.__CPUTimeRAW = x

    def set_DerivedExitCode(self, x):
        self.__DerivedExitCode = x

    def set_Elapsed(self, x):
        self.__Elapsed = x

    def set_ElapsedRaw(self, x):
        self.__ElapsedRaw = x

    def set_Eligible(self, x):
        self.__Eligible = x

    def set_End(self, x):
        self.__End = x

    def set_ExitCode(self, x):
        self.__ExitCode = x

    def set_GID(self, x):
        self.__GID = x

    def set_Group(self, x):
        self.__Group = x

    def set_JobID(self, x):
        self.__JobID = x

    def set_JobIDRaw(self, x):
        self.__JobIDRaw = x

    def set_JobName(self, x):
        self.__JobName = x

    def set_Layout(self, x):
        self.__Layout = x

    def set_MaxDiskRead(self, x):
        self.__MaxDiskRead = x

    def set_MaxDiskReadNode(self, x):
        self.__MaxDiskReadNode = x

    def set_MaxDiskReadTask(self, x):
        self.__MaxDiskReadTask = x

    def set_MaxDiskWrite(self, x):
        self.__MaxDiskWrite = x

    def set_MaxDiskWriteNode(self, x):
        self.__MaxDiskWriteNode = x

    def set_MaxDiskWriteTask(self, x):
        self.__MaxDiskWriteTask = x

    def set_MaxPages(self, x):
        self.__MaxPages = x

    def set_MaxPagesNode(self, x):
        self.__MaxPagesNode = x

    def set_MaxPagesTask(self, x):
        self.__MaxPagesTask = x

    def set_MaxRSS(self, x):
        self.__MaxRSS = x

    def set_MaxRSSNode(self, x):
        self.__MaxRSSNode = x

    def set_MaxRSSTask(self, x):
        self.__MaxRSSTask = x

    def set_MaxVMSize(self, x):
        self.__MaxVMSize = x

    def set_MaxVMSizeNode(self, x):
        self.__MaxVMSizeNode = x

    def set_MaxVMSizeTask(self, x):
        self.__MaxVMSizeTask = x

    def set_McsLabel(self, x):
        self.__McsLabel = x

    def set_MinCPU(self, x):
        self.__MinCPU = x

    def set_MinCPUNode(self, x):
        self.__MinCPUNode = x

    def set_MinCPUTask(self, x):
        self.__MinCPUTask = x

    def set_NCPUS(self, x):
        self.__NCPUS = x

    def set_NNodes(self, x):
        self.__NNodes = x

    def set_NodeList(self, x):
        self.__NodeList = x

    def set_NTasks(self, x):
        self.__NTasks = x

    def set_Priority(self, x):
        self.__Priority = x

    def set_Partition(self, x):
        self.__Partition = x

    def set_QOS(self, x):
        self.__QOS = x

    def set_QOSRAW(self, x):
        self.__QOSRAW = x

    def set_ReqCPUFreq(self, x):
        self.__ReqCPUFreq = x

    def set_ReqCPUFreqMin(self, x):
        self.__ReqCPUFreqMin = x

    def set_ReqCPUFreqMax(self, x):
        self.__ReqCPUFreqMax = x

    def set_ReqCPUFreqGov(self, x):
        self.__ReqCPUFreqGov = x

    def set_ReqCPUS(self, x):
        self.__ReqCPUS = x

    def set_ReqGRES(self, x):
        self.__ReqGRES = x

    def set_ReqMem(self, x):
        self.__ReqMem = x

    def set_ReqNodes(self, x):
        self.__ReqNodes = x

    def set_ReqTRES(self, x):
        self.__ReqTRES = x

    def set_Reservation(self, x):
        self.__Reservation = x

    def set_ReservationId(self, x):
        self.__ReservationId = x

    def set_Reserved(self, x):
        self.__Reserved = x

    def set_ResvCPU(self, x):
        self.__ResvCPU = x

    def set_ResvCPURAW(self, x):
        self.__ResvCPURAW = x

    def set_Start(self, x):
        self.__Start = x

    def set_State(self, x):
        self.__State = x

    def set_Submit(self, x):
        self.__Submit = x

    def set_Suspended(self, x):
        self.__Suspended = x

    def set_SystemCPU(self, x):
        self.__SystemCPU = x

    def set_SystemComment(self, x):
        self.__SystemComment = x

    def set_Timelimit(self, x):
        self.__Timelimit = x

    def set_TimelimitRaw(self, x):
        self.__TimelimitRaw = x

    def set_TotalCPU(self, x):
        self.__TotalCPU = x

    def set_TRESUsageInAve(self, x):
        self.__TRESUsageInAve = x

    def set_TRESUsageInMax(self, x):
        self.__TRESUsageInMax = x

    def set_TRESUsageInMaxNode(self, x):
        self.__TRESUsageInMaxNode = x

    def set_TRESUsageInMaxTask(self, x):
        self.__TRESUsageInMaxTask = x

    def set_TRESUsageInMin(self, x):
        self.__TRESUsageInMin = x

    def set_TRESUsageInMinNode(self, x):
        self.__TRESUsageInMinNode = x

    def set_TRESUsageInMinTask(self, x):
        self.__TRESUsageInMinTask = x

    def set_TRESUsageInTot(self, x):
        self.__TRESUsageInTot = x

    def set_TRESUsageOutAve(self, x):
        self.__TRESUsageOutAve = x

    def set_TRESUsageOutMax(self, x):
        self.__TRESUsageOutMax = x

    def set_TRESUsageOutMaxNode(self, x):
        self.__TRESUsageOutMaxNode = x

    def set_TRESUsageOutMaxTask(self, x):
        self.__TRESUsageOutMaxTask = x

    def set_TRESUsageOutMin(self, x):
        self.__TRESUsageOutMin = x

    def set_TRESUsageOutMinNode(self, x):
        self.__TRESUsageOutMinNode = x

    def set_TRESUsageOutMinTask(self, x):
        self.__TRESUsageOutMinTask = x

    def set_TRESUsageOutTot(self, x):
        self.__TRESUsageOutTot = x

    def set_UID(self, x):
        self.__UID = x

    def set_User(self, x):
        self.__User = x

    def set_UserCPU(self, x):
        self.__UserCPU = x

    def set_WCKey(self, x):
        self.__WCKey = x

    def set_WCKeyID(self, x):
        self.__WCKeyID = x

    def set_WorkDir(self, x):
        self.__WorkDir = x