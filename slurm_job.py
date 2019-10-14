class SlurmJob:
    def __init__(self):
        self.account                    = None
        self.admin_comment              = None
        self.alloc_CPUS                 = None
        self.alloc_GRES                 = None
        self.alloc_nodes                = None
        self.alloc_TRES                 = None
        self.assoc_ID                   = None
        self.ave_CPU                    = None
        self.ave_CPU_freq               = None
        self.ave_disk_read              = None
        self.ave_disk_write             = None
        self.ave_pages                  = None
        self.ave_RSS                    = None
        self.ave_VM_size                = None
        self.block_ID                   = None
        self.cluster                    = None
        self.comment                    = None
        self.consumed_energy            = None
        self.consumed_energy_raw        = None
        self.CPU_time                   = None
        self.CPU_time_raw               = None
        self.derived_exit_code          = None
        self.elapsed                    = None
        self.elapsed_raw                = None
        self.eligible                   = None
        self.end                        = None
        self.exit_code                  = None
        self.GID                        = None
        self.group                      = None
        self.job_ID                     = None
        self.job_ID_raw                 = None
        self.job_name                   = None
        self.layout                     = None
        self.max_disk_read              = None
        self.max_disk_read_node         = None
        self.max_disk_read_task         = None
        self.max_disk_write             = None
        self.max_disk_write_node        = None
        self.max_disk_write_task        = None
        self.max_pages                  = None 
        self.max_pages_node             = None
        self.max_pages_task             = None
        self.max_RSS                    = None
        self.max_RSS_node               = None
        self.max_RSS_task               = None
        self.max_VM_size                = None
        self.max_VM_size_node           = None
        self.max_VM_size_task           = None
        self.mcs_label                  = None
        self.min_CPU                    = None
        self.min_CPU_node               = None
        self.min_CPU_task               = None
        self.NCPUS                      = None
        self.NNodes                     = None
        self.node_list                  = None
        self.NTasks                     = None
        self.priority                   = None
        self.partition                  = None
        self.QOS                        = None
        self.QOS_raw                    = None
        self.req_CPU_freq               = None
        self.req_CPU_freq_min           = None
        self.req_CPU_freq_max           = None
        self.req_CPU_freq_gov           = None
        self.req_CPUS                   = None
        self.req_GRES                   = None
        self.req_mem                    = None
        self.req_nodes                  = None
        self.req_TRES                   = None
        self.reservation                = None
        self.reservation_Id             = None
        self.reserved                   = None
        self.resv_CPU                   = None
        self.resv_CPU_raw               = None
        self.start                      = None
        self.state                      = None
        self.submit                     = None
        self.suspended                  = None
        self.system_CPU                 = None
        self.system_comment             = None
        self.time_limit                 = None
        self.time_limit_raw             = None
        self.total_CPU                  = None
        self.TRES_usage_in_ave          = None
        self.TRES_usage_in_max          = None
        self.TRES_usage_in_max_node     = None
        self.TRES_usage_in_max_task     = None
        self.TRES_usage_in_min          = None
        self.TRES_usage_in_min_node     = None
        self.TRES_usage_in_min_task     = None
        self.TRES_usage_in_tot          = None
        self.TRES_usage_out_ave         = None
        self.TRES_usage_out_max         = None
        self.TRES_usage_out_max_node    = None
        self.TRES_usage_out_max_task    = None
        self.TRES_usage_out_min         = None
        self.TRES_usage_out_min_node    = None
        self.TRES_usage_out_min_task    = None
        self.TRES_usage_out_tot         = None
        self.UID                        = None
        self.user                       = None
        self.user_CPU                   = None
        self.WC_key                     = None
        self.WC_key_ID                  = None
        self.working_dir                = None

    def __str__(self):
        temp = "Job ( account:{}, admin_comment:{}, alloc_CPUS:{}, alloc_GRES:{}, alloc_nodes:{}, alloc_TRES:{}, assoc_ID:{}, ave_CPU:{}, \
                ave_CPU_freq:{}, ave_disk_read:{}, ave_disk_write:{}, ave_pages:{}, ave_RSS:{}, ave_VM_size:{}, block_id:{}, cluster:{}, consumed_energy:{}, \
                consumed_energy_raw:{}, CPU_time{}, CPU_time_raw:{}  , derived_exit_code:{}, elapsed:{}, elapsed_raw:{}, end:{}, exit_code:{}, \
                GID:{}, group:{}, job_ID:{}, job_ID_raw:{}, job_name:{}, layout:{}, max_disk_read:{}, max_disk_read_node:{}, max_disk_read_task:{} \
                max_disk_write:{}, max_disk_write_node:{}, max_disk_write_task:{}, max_pages:{}, max_pages_node:{}, max_pages_task:{}, max_RSS:{}, \
                max_RSS_node:{}, max_RSS_task:{}, max_VM_size:{}, max_VM_size_node:{}, max_VM_size_task:{}, mcs_label:{}, min_CPU:{}, min_CPU_node:{}, \
                min_CPU_task:{}, NCPUS:{}, NNodes:{}, node_list:{}, NTasks:{}, priority:{}, partition:{}, QOS:{}, QOS_raw:{}, req_CPU_freq:{}, \
                req_CPU_freq_min:{}, req_CPU_freq_max:{}, req_CPU_freq_gov:{}, req_CPUS:{}, req_GRES:{}, req_mem:{}, req_nodes:{}, req_TRES:{}, \
                reservation:{}, reservatio_id:{}, reserved:{}, resv_CPU:{}, resv_CPU_raw:{}, start:{}, state:{}, submit:{}, susspended:{}, system_CPU:{}, \
                system_comment:{}, time_limit:{}, time_limit_raw:{}, total_CPU:{}, TRES_usage_in_ave:{}, TRES_usage_in_max:{}, TRES_usage_in_max_node:{}, \
                TRES_usage_in_max_task:{}, TRES_usage_in_min:{}, TRES_usage_in_min_node:{}, TRES_usage_in_min_task:{}, TRES_usage_in_tot:{}, \
                TRES_usage_out_ave:{}, TRES_usage_out_max:{}, TRES_usage_out_max_node:{}, TRES_usage_out_max_task:{}, TRES_usage_out_min:{}, \
                TRES_usage_out_min_node:{}, TRES_usage_out_min_task:{}, TRES_usage_out_tot:{}, UID:{}, user:{}, user_CPU:{}, WC_key:{}, \
                WC_key_ID:{}, working_dir:{} )".format( self.account, self.admin_comment, self.alloc_CPUS, self.alloc_GRES, self.alloc_nodes, self.alloc_TRES, self.assoc_ID,
                self.ave_CPU, self.ave_CPU_freq, self.ave_disk_read, self.ave_disk_write, self.ave_pages, self.ave_RSS, self.ave_VM_size, self.block_ID,
                self.cluster, self.consumed_energy, self.consumed_energy_raw, self.CPU_time, self.CPU_time_raw, self.derived_exit_code, self.elapsed,
                self.elapsed_raw, self.end, self.exit_code, self.GID, self.group, self.job_ID, self.job_ID_raw, self.job_name, self.layout, self.max_disk_read,
                self.max_disk_read_node, self.max_disk_read_task, self.max_disk_write, self.max_disk_write_node, self.max_disk_write_task, self.max_pages,
                self.max_pages_node, self.max_pages_task,  self.max_RSS, self.max_RSS_node, self.max_RSS_task, self.max_VM_size, self.max_VM_size_node,
                self.max_VM_size_task, self.mcs_label, self.min_CPU, self.min_CPU_node, self.min_CPU_task, self.NCPUS, self.NNodes, self.node_list,
                self.NTasks, self.priority, self.partition, self.QOS_raw, self.QOS_raw, self.req_CPU_freq, self.req_CPU_freq_min, self.req_CPU_freq_max,
                self.req_CPU_freq_gov, self.req_CPUS, self.req_GRES, self.req_mem, self.req_nodes, self.req_TRES, self.reservation,  self.reservation_Id,
                self.reserved, self.resv_CPU, self.resv_CPU_raw, self.start, self.state, self.submit, self.suspended, self.system_CPU,  self.system_comment,
                self.time_limit, self.time_limit_raw, self.total_CPU, self.TRES_usage_in_ave, self.TRES_usage_in_max,self.TRES_usage_in_max_node,
                self.TRES_usage_in_max_task, self.TRES_usage_in_min, self.TRES_usage_in_min_node, self.TRES_usage_in_min_task, self.TRES_usage_in_tot,
                self.TRES_usage_out_ave, self.TRES_usage_out_max, self.TRES_usage_out_max_node, self.TRES_usage_out_max_task,self.TRES_usage_out_min,
                self.TRES_usage_out_min_node, self.TRES_usage_out_min_task, self.TRES_usage_out_tot, self.UID, self.user, self.user_CPU, self.WC_key,
                self.WC_key_ID, self.working_dir)
        return temp

    def __repr__(self):
        return {'account':self.account, 'admin_comment':self.admin_comment, 'alloc_CPUS':self.alloc_CPUS,
                'alloc_GRES':self.alloc_GRES, 'alloc_nodes':self.alloc_nodes, 'alloc_TRES':self.alloc_TRES,
                'assoc_ID':self.assoc_ID, 'ave_CPU':self.ave_CPU, 'ave_CPU_freq':self.ave_CPU_freq,
                'ave_disk_read':self.ave_disk_read, 'ave_disk_write':self.ave_disk_write, 'ave_pages':self.ave_pages,
                'ave_RSS':self.ave_RSS, 'ave_VM_size':self.ave_VM_size, 'block_id':self.block_ID, 'cluster':self.cluster,
                'consumed_energy':self.consumed_energy, 'consumed_energy_raw':self.consumed_energy_raw, 'CPU_time':self.CPU_time,
                'CPU_time_raw':self.CPU_time_raw, 'derived_exit_code':self.derived_exit_code, 'elapsed':self.elapsed,
                'elapsed_raw':self.elapsed_raw, 'end':self.end, 'exit_code':self.exit_code, 'GID':self.GID, 'group':self.group,
                'job_ID':self.job_ID, 'job_ID_raw':self.job_ID_raw, 'job_name':self.job_name, 'layout':self.layout,
                'max_disk_read':self.max_disk_read, 'max_disk_read_node':self.max_disk_read_node, 'max_disk_read_task':self.max_disk_read_task,
                'max_disk_write':self.max_disk_write, 'max_disk_write_node':self.max_disk_write_node,
                'max_disk_write_task':self.max_disk_write_task, 'max_pages':self.max_pages, 'max_pages_node':self.max_pages_node,
                'max_pages_task':self.max_pages_task, 'max_RSS':self.max_RSS, 'max_RSS_node':self.max_RSS_node,
                'max_RSS_task':self.max_RSS_task, 'max_VM_size':self.max_VM_size, 'max_VM_size_node':self.max_VM_size_node,
                'max_VM_size_task':self.max_VM_size_task, 'mcs_label':self.mcs_label, 'min_CPU':self.min_CPU,
                'min_CPU_node':self.min_CPU_node, 'min_CPU_task':self.min_CPU_task, 'NCPUS':self.NCPUS, 'NNodes':self.NNodes,
                'node_list':self.node_list, 'NTasks':self.NTasks, 'priority':self.priority, 'partition':self.partition,
                'QOS':self.QOS_raw, 'QOS_raw':self.QOS_raw, 'req_CPU_freq':self.req_CPU_freq, 'req_CPU_freq_min':self.req_CPU_freq_min,
                'req_CPU_freq_max':self.req_CPU_freq_max, 'req_CPU_freq_gov':self.req_CPU_freq_gov, 'req_CPUS':self.req_CPUS,
                'req_GRES':self.req_GRES, 'req_mem':self.req_mem, 'req_nodes':self.req_nodes, 'req_TRES':self.req_TRES,
                'reservation':self.reservation, 'reservatio_id':self.reservation_Id, 'reserved':self.reserved, 'resv_CPU':self.resv_CPU,
                'resv_CPU_raw':self.resv_CPU_raw, 'start':self.start, 'state':self.state, 'submit':self.submit, 'susspended':self.suspended,
                'system_CPU':self.system_CPU, 'system_comment':self.system_comment, 'time_limit':self.time_limit,
                'time_limit_raw':self.time_limit_raw, 'total_CPU':self.total_CPU, 'TRES_usage_in_ave':self.TRES_usage_in_ave,
                'TRES_usage_in_max':self.TRES_usage_in_max, 'TRES_usage_in_max_node':self.TRES_usage_in_max_node,
                'TRES_usage_in_max_task':self.TRES_usage_in_max_task, 'TRES_usage_in_min':self.TRES_usage_in_min,
                'TRES_usage_in_min_node':self.TRES_usage_in_min_node, 'TRES_usage_in_min_task':self.TRES_usage_in_min_task,
                'TRES_usage_in_tot':self.TRES_usage_in_tot, 'TRES_usage_out_ave':self.TRES_usage_out_ave,
                'TRES_usage_out_max':self.TRES_usage_out_max, 'TRES_usage_out_max_node':self.TRES_usage_out_max_node,
                'TRES_usage_out_max_task':self.TRES_usage_out_max_task, 'TRES_usage_out_min':self.TRES_usage_out_min,
                'TRES_usage_out_min_node':self.TRES_usage_out_min_node, 'TRES_usage_out_min_task':self.TRES_usage_out_min_task,
                'TRES_usage_out_tot':self.TRES_usage_out_tot, 'UID':self.UID, 'user':self.user, 'user_CPU':self.user_CPU,
                'WC_key':self.WC_key, 'WC_key_ID':self.WC_key_ID, 'working_dir':self.working_dir}


