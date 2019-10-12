class Job:
    def __init__(self, job_id, user, cpu_time, run_time, start, end, exit_code, max_rss, max_vm, n_cpu, num_tasks, queue, req_mem):
       self.job_id      = job_id
       self.user        = user
       self.cpu_time    = cpu_time
       self.run_time    = run_time
       self.start       = start
       self.end         = end
       self.exit_code   = exit_code
       self.max_rss     = max_rss
       self.max_vm      = max_vm
       self.num_tasks   = num_tasks
       self.queue       = queue
       self.req_mem     = req_mem

class SlurmJob(Job):
    def __init__(self, job_id=None, user=None, cpu_time=None, run_time=None, start=None, end=None, exit_code=None, max_rss=None, max_vm=None,
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
        super.__init__(job_id, user, cpu_time, run_time, start, end, exit_code, max_rss, max_vm, n_cpu, num_tasks, queue, req_mem)
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