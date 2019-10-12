class SlurmJob:
    def __init__(self=None, job_id=None, user=None, cpu_time=None, run_time=None, start=None, end=None, exit_code=None, max_rss=None, max_vm=None,
                    n_cpu=None, num_tasks=None, queue=None, req_mem=None, account=None, AdminComment=None, AllocCPUS=None, AllocGRES=None,
                    AllocNodes=None, AllocTRES=None, AssocID=None, AveCPU=None, AveCPUFreq=None, AveDiskRead=None, AveDiskWrite=None,
                    AvePages=None, AveRSS=None, AveVMSize=None, BlockID=None, Cluster=None, Comment=None, ConsumedEnergy=None, ConsumedEnergyRaw=None,
                    CPUTime=None, CPUTimeRAW=None, DerivedExitCode=None, Elapsed=None, ElapsedRaw=None, Eligible=None, End=None, ExitCode=None,
                    GID=None, Group=None, JobID=None, JobIDRaw=None, JobName=None, Layout=None, MaxDiskRead=None, MaxDiskReadNode=None,
                    MaxDiskReadTask=None, MaxDiskWrite=None, MaxDiskWriteNode=None, MaxDiskWriteTask=None, MaxPages=None, MaxPagesNode=None,
                    MaxPagesTask=None, MaxRSS=None, MaxRSSNode=None, MaxRSSTask=None, MaxVMSize=None, MaxVMSizeNode=None, MaxVMSizeTask=None,
                    McsLabel=None, MinCPU=None, MinCPUNode=None, MinCPUTask=None, NCPUS=None, NNodes=None, NodeList=None, NTasks=None,
                    Priority=None, Partition=None, QOS=None, QOSRAW=None, ReqCPUFreq=None, ReqCPUFreqMin=None, ReqCPUFreqMax=None,
                    ReqCPUFreqGov=None, ReqCPUS=None, ReqGRES=None, ReqMem=None, ReqNodes=None, ReqTRES=None, Reservation=None,
                    ReservationId=None, Reserved=None, ResvCPU=None, ResvCPURAW=None, Start=None, State=None, Submit=None, Suspended=None,
                    SystemCPU=None, SystemComment=None, Timelimit=None, TimelimitRaw=None, TotalCPU=None, TRESUsageInAve=None,
                    TRESUsageInMax=None, TRESUsageInMaxNode=None, TRESUsageInMaxTask=None, TRESUsageInMin=None, TRESUsageInMinNode=None,
                    TRESUsageInMinTask=None, TRESUsageInTot=None, TRESUsageOutAve=None, TRESUsageOutMax=None, TRESUsageOutMaxNode=None,
                    TRESUsageOutMaxTask=None, TRESUsageOutMin=None, TRESUsageOutMinNode=None, TRESUsageOutMinTask=None, TRESUsageOutTot=None,
                    UID=None, User=None, UserCPU=None, WCKey=None, WCKeyID=None, WorkDir=None):
        self.Account = account
        self.AdminComment = AdminComment
        self.AllocCPUS = AllocCPUS
        self.AllocGRES = AllocGRES
        self.AllocNodes = AllocNodes
        self.AllocTRES = AllocTRES
        self.AssocID = AssocID
        self.AveCPU = AveCPU
        self.AveCPUFreq = AveCPUFreq
        self.AveDiskRead = AveDiskRead
        self.AveDiskWrite = AveDiskWrite
        self.AvePages = AvePages
        self.AveRSS = AveRSS
        self.AveVMSize = AveVMSize
        self.BlockID = BlockID
        self.Cluster = Cluster
        self.Comment = Comment
        self.ConsumedEnergy = ConsumedEnergy
        self.ConsumedEnergyRaw = ConsumedEnergyRaw
        self.CPUTime = CPUTime
        self.CPUTimeRAW = CPUTimeRAW
        self.DerivedExitCode = DerivedExitCode
        self.Elapsed = Elapsed
        self.ElapsedRaw = ElapsedRaw
        self.Eligible = Eligible
        self.End = End
        self.ExitCode = ExitCode
        self.GID = GID
        self.Group = Group
        self.JobID = JobID
        self.JobIDRaw = JobIDRaw
        self.JobName = JobName
        self.Layout = Layout
        self.MaxDiskRead = MaxDiskRead
        self.MaxDiskReadNode = MaxDiskReadNode
        self.MaxDiskReadTask = MaxDiskReadTask
        self.MaxDiskWrite = MaxDiskWrite
        self.MaxDiskWriteNode = MaxDiskWriteNode
        self.MaxDiskWriteTask = MaxDiskWriteTask
        self.MaxPages = MaxPages 
        self.MaxPagesNode = MaxPagesNode
        self.MaxPagesTask = MaxPagesTask
        self.MaxRSS = MaxRSS
        self.MaxRSSNode = MaxRSSNode
        self.MaxRSSTask = MaxRSSTask
        self.MaxVMSize = MaxVMSize
        self.MaxVMSizeNode = MaxVMSizeNode
        self.MaxVMSizeTask = MaxVMSizeTask
        self.McsLabel = McsLabel
        self.MinCPU = MinCPU
        self.MinCPUNode = MinCPUNode
        self.MinCPUTask = MinCPUTask
        self.NCPUS = NCPUS
        self.NNodes = NNodes
        self.NodeList = NodeList
        self.NTasks = NTasks
        self.Priority = Priority
        self.Partition = Partition
        self.QOS = QOS
        self.QOSRAW = QOSRAW
        self.ReqCPUFreq = ReqCPUFreq
        self.ReqCPUFreqMin = ReqCPUFreqMin
        self.ReqCPUFreqMax = ReqCPUFreqMax
        self.ReqCPUFreqGov = ReqCPUFreqGov
        self.ReqCPUS = ReqCPUS
        self.ReqGRES = ReqGRES
        self.ReqMem = ReqMem
        self.ReqNodes = ReqNodes
        self.ReqTRES = ReqTRES
        self.Reservation = Reservation
        self.ReservationId = ReservationId
        self.Reserved = Reserved
        self.ResvCPU = ResvCPU
        self.ResvCPURAW = ResvCPURAW
        self.Start = Start
        self.State = State
        self.Submit = Submit
        self.Suspended = Suspended
        self.SystemCPU = SystemCPU
        self.SystemComment = SystemComment
        self.Timelimit = Timelimit
        self.TimelimitRaw = TimelimitRaw
        self.TotalCPU = TotalCPU
        self.TRESUsageInAve = TRESUsageInAve
        self.TRESUsageInMax = TRESUsageInMax
        self.TRESUsageInMaxNode = TRESUsageInMaxNode
        self.TRESUsageInMaxTask = TRESUsageInMaxTask
        self.TRESUsageInMin = TRESUsageInMin
        self.TRESUsageInMinNode = TRESUsageInMinNode
        self.TRESUsageInMinTask = TRESUsageInMinTask
        self.TRESUsageInTot = TRESUsageInTot
        self.TRESUsageOutAve = TRESUsageOutAve
        self.TRESUsageOutMax = TRESUsageOutMax
        self.TRESUsageOutMaxNode = TRESUsageOutMaxNode
        self.TRESUsageOutMaxTask = TRESUsageOutMaxTask
        self.TRESUsageOutMin = TRESUsageOutMin
        self.TRESUsageOutMinNode = TRESUsageOutMinNode
        self.TRESUsageOutMinTask = TRESUsageOutMinTask
        self.TRESUsageOutTot = TRESUsageOutTot
        self.UID = UID
        self.User = User
        self.UserCPU = UserCPU
        self.WCKey = WCKey
        self.WCKeyID = WCKeyID
        self.WorkDir = WorkDir

    def set_Account(self, x):
        self.Account = x

    def set_AdminComment(self, x):
        self.AdminComment = x

    def set_AllocCPUS(self, x):
        self.AllocCPUS = x

    def set_AllocGRES(self, x):
        self.AllocGRES = x

    def set_AllocNodes(self, x):
        self.AllocNodes = x

    def set_AllocTRES(self, x):
        self.AllocTRES = x

    def set_AssocID(self, x):
        self.AssocID = x

    def set_AveCPU(self, x):
        self.AveCPU = x

    def set_AveCPUFreq(self, x):
        self.AveCPUFreq = x

    def set_AveDiskRead(self, x):
        self.AveDiskRead = x

    def set_AveDiskWrite(self, x):
        self.AveDiskWrite = x

    def set_AvePages(self, x):
        self.AvePages = x

    def set_AveRSS(self, x):
        self.AveRSS = x

    def set_AveVMSize(self, x):
        self.AveVMSize = x

    def set_BlockID(self, x):
        self.BlockID = x

    def set_Cluster(self, x):
        self.Cluster = x

    def set_Comment(self, x):
        self.Comment = x

    def set_ConsumedEnergy(self, x):
        self.ConsumedEnergy = x

    def set_ConsumedEnergyRaw(self, x):
        self.ConsumedEnergyRaw = x

    def set_CPUTime(self, x):
        self.CPUTime = x

    def set_CPUTimeRAW(self, x):
        self.CPUTimeRAW = x

    def set_DerivedExitCode(self, x):
        self.DerivedExitCode = x

    def set_Elapsed(self, x):
        self.Elapsed = x

    def set_ElapsedRaw(self, x):
        self.ElapsedRaw = x

    def set_Eligible(self, x):
        self.Eligible = x

    def set_End(self, x):
        self.End = x

    def set_ExitCode(self, x):
        self.ExitCode = x

    def set_GID(self, x):
        self.GID = x

    def set_Group(self, x):
        self.Group = x

    def set_JobID(self, x):
        self.JobID = x

    def set_JobIDRaw(self, x):
        self.JobIDRaw = x

    def set_JobName(self, x):
        self.JobName = x

    def set_Layout(self, x):
        self.Layout = x

    def set_MaxDiskRead(self, x):
        self.MaxDiskRead = x

    def set_MaxDiskReadNode(self, x):
        self.MaxDiskReadNode = x

    def set_MaxDiskReadTask(self, x):
        self.MaxDiskReadTask = x

    def set_MaxDiskWrite(self, x):
        self.MaxDiskWrite = x

    def set_MaxDiskWriteNode(self, x):
        self.MaxDiskWriteNode = x

    def set_MaxDiskWriteTask(self, x):
        self.MaxDiskWriteTask = x

    def set_MaxPages(self, x):
        self.MaxPages = x

    def set_MaxPagesNode(self, x):
        self.MaxPagesNode = x

    def set_MaxPagesTask(self, x):
        self.MaxPagesTask = x

    def set_MaxRSS(self, x):
        self.MaxRSS = x

    def set_MaxRSSNode(self, x):
        self.MaxRSSNode = x

    def set_MaxRSSTask(self, x):
        self.MaxRSSTask = x

    def set_MaxVMSize(self, x):
        self.MaxVMSize = x

    def set_MaxVMSizeNode(self, x):
        self.MaxVMSizeNode = x

    def set_MaxVMSizeTask(self, x):
        self.MaxVMSizeTask = x

    def set_McsLabel(self, x):
        self.McsLabel = x

    def set_MinCPU(self, x):
        self.MinCPU = x

    def set_MinCPUNode(self, x):
        self.MinCPUNode = x

    def set_MinCPUTask(self, x):
        self.MinCPUTask = x

    def set_NCPUS(self, x):
        self.NCPUS = x

    def set_NNodes(self, x):
        self.NNodes = x

    def set_NodeList(self, x):
        self.NodeList = x

    def set_NTasks(self, x):
        self.NTasks = x

    def set_Priority(self, x):
        self.Priority = x

    def set_Partition(self, x):
        self.Partition = x

    def set_QOS(self, x):
        self.QOS = x

    def set_QOSRAW(self, x):
        self.QOSRAW = x

    def set_ReqCPUFreq(self, x):
        self.ReqCPUFreq = x

    def set_ReqCPUFreqMin(self, x):
        self.ReqCPUFreqMin = x

    def set_ReqCPUFreqMax(self, x):
        self.ReqCPUFreqMax = x

    def set_ReqCPUFreqGov(self, x):
        self.ReqCPUFreqGov = x

    def set_ReqCPUS(self, x):
        self.ReqCPUS = x

    def set_ReqGRES(self, x):
        self.ReqGRES = x

    def set_ReqMem(self, x):
        self.ReqMem = x

    def set_ReqNodes(self, x):
        self.ReqNodes = x

    def set_ReqTRES(self, x):
        self.ReqTRES = x

    def set_Reservation(self, x):
        self.Reservation = x

    def set_ReservationId(self, x):
        self.ReservationId = x

    def set_Reserved(self, x):
        self.Reserved = x

    def set_ResvCPU(self, x):
        self.ResvCPU = x

    def set_ResvCPURAW(self, x):
        self.ResvCPURAW = x

    def set_Start(self, x):
        self.Start = x

    def set_State(self, x):
        self.State = x

    def set_Submit(self, x):
        self.Submit = x

    def set_Suspended(self, x):
        self.Suspended = x

    def set_SystemCPU(self, x):
        self.SystemCPU = x

    def set_SystemComment(self, x):
        self.SystemComment = x

    def set_Timelimit(self, x):
        self.Timelimit = x

    def set_TimelimitRaw(self, x):
        self.TimelimitRaw = x

    def set_TotalCPU(self, x):
        self.TotalCPU = x

    def set_TRESUsageInAve(self, x):
        self.TRESUsageInAve = x

    def set_TRESUsageInMax(self, x):
        self.TRESUsageInMax = x

    def set_TRESUsageInMaxNode(self, x):
        self.TRESUsageInMaxNode = x

    def set_TRESUsageInMaxTask(self, x):
        self.TRESUsageInMaxTask = x

    def set_TRESUsageInMin(self, x):
        self.TRESUsageInMin = x

    def set_TRESUsageInMinNode(self, x):
        self.TRESUsageInMinNode = x

    def set_TRESUsageInMinTask(self, x):
        self.TRESUsageInMinTask = x

    def set_TRESUsageInTot(self, x):
        self.TRESUsageInTot = x

    def set_TRESUsageOutAve(self, x):
        self.TRESUsageOutAve = x

    def set_TRESUsageOutMax(self, x):
        self.TRESUsageOutMax = x

    def set_TRESUsageOutMaxNode(self, x):
        self.TRESUsageOutMaxNode = x

    def set_TRESUsageOutMaxTask(self, x):
        self.TRESUsageOutMaxTask = x

    def set_TRESUsageOutMin(self, x):
        self.TRESUsageOutMin = x

    def set_TRESUsageOutMinNode(self, x):
        self.TRESUsageOutMinNode = x

    def set_TRESUsageOutMinTask(self, x):
        self.TRESUsageOutMinTask = x

    def set_TRESUsageOutTot(self, x):
        self.TRESUsageOutTot = x

    def set_UID(self, x):
        self.UID = x

    def set_User(self, x):
        self.User = x

    def set_UserCPU(self, x):
        self.UserCPU = x

    def set_WCKey(self, x):
        self.WCKey = x

    def set_WCKeyID(self, x):
        self.WCKeyID = x

    def set_WorkDir(self, x):
        self.WorkDir = x