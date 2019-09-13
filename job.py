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
    def __init__(self, job_id='', user='', cpu_time='', run_time='', start='', end='', exit_code='', max_rss='', max_vm='',
                    n_cpu='', num_tasks='', queue='', req_mem=''):
        super.__init__(job_id, user, cpu_time, run_time, start, end, exit_code, max_rss, max_vm, n_cpu, num_tasks, queue, req_mem)
self.Account
self.AdminComment
self.AllocCPUS
self.AllocGRES
self.AllocNodes
self.AllocTRES
self.AssocID
self.AveCPU
self.AveCPUFreq
self.AveDiskRead
self.AveDiskWrite
self.AvePages
self.AveRSS
self.AveVMSize
self.BlockID
self.Cluster
self.Comment
self.ConsumedEnergy
self.ConsumedEnergyRaw
self.CPUTime
self.CPUTimeRAW
self.DerivedExitCode
self.Elapsed
self.ElapsedRaw
self.Eligible
self.End
self.ExitCode
self.GID
self.Group
self.JobID
self.JobIDRaw
self.JobName
self.Layout
self.MaxDiskRead
self.MaxDiskReadNode
self.MaxDiskReadTask
self.MaxDiskWrite
self.MaxDiskWriteNode
self.MaxDiskWriteTask
self.MaxPages
self.MaxPagesNode
self.MaxPagesTask
self.MaxRSS
self.MaxRSSNode
self.MaxRSSTask
self.MaxVMSize
self.MaxVMSizeNode
self.MaxVMSizeTask
self.McsLabel
self.MinCPU
self.MinCPUNode
self.MinCPUTask
self.NCPUS
self.NNodes
self.NodeList
self.NTasks
self.Priority
self.Partition
self.QOS
self.QOSRAW
self.ReqCPUFreq
self.ReqCPUFreqMin
self.ReqCPUFreqMax
self.ReqCPUFreqGov
self.ReqCPUS
self.ReqGRES
self.ReqMem
self.ReqNodes
self.ReqTRES
self.Reservation
self.ReservationId
self.Reserved
self.ResvCPU
self.ResvCPURAW
self.Start
self.State
self.Submit
self.Suspended
self.SystemCPU
self.SystemComment
self.Timelimit
self.TimelimitRaw
self.TotalCPU
self.TRESUsageInAve
self.TRESUsageInMax
self.TRESUsageInMaxNode
self.TRESUsageInMaxTask
self.TRESUsageInMin
self.TRESUsageInMinNode
self.TRESUsageInMinTask
self.TRESUsageInTot
self.TRESUsageOutAve
self.TRESUsageOutMax
self.TRESUsageOutMaxNode
self.TRESUsageOutMaxTask
self.TRESUsageOutMin
self.TRESUsageOutMinNode
self.TRESUsageOutMinTask
self.TRESUsageOutTot
self.UID
self.User
self.UserCPU
self.WCKey
self.WCKeyID
self.WorkDir
self.