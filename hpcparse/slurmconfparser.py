"""
This Class implements a pasrser for teh SLURM scheduler's slurm.conf file.

GPL licensing
"""
# Libs

# Own Modules
from hpcparse.partitiontype import PartitionType
from hpcparse.nodetype import NodeType
from hpcparse.configoptions import ConfigOptions


class SlurmConfParser:
    def __init__(self):
        self.__nodes = []
        self.__partitions = []
        self.__options = None
        self.__temp = []
        self.__filename = None

    def Parse(self, filename):
        linecount = 0
        self.__filename = filename
        print(self.__filename)
        try:
            with open(self.__filename, 'r', newline='') as inputFile:
                self.__options = ConfigOptions()

                for line in inputFile:
                    linecount += 1
                    line = line.strip('\r')
                    if '#' in line:
                        continue

                    elif 'NodeName' in line:
                        node = NodeType()
                        x = line.split(' ')
                        for column in x:
                            y = x.split('=')
                            if 'AllowGrpups' in y:
                                node.allow_groups = y[1]
                            elif 'AllowUsers' in y:
                                node.allow_users = y[1]
                            elif 'BcastADDR' in y:
                                node.bcast_addr = y[1]
                            elif 'Boards' in y:
                                node.boards = y[1]
                            elif 'CoresSpecCount' in y:
                                node.cores_spec_count = y[1]
                            elif 'CoresPerSocket' in y:
                                node.cores_per_socket = y[1]
                            elif 'CPUBind' in y:
                                node.cpu_bind = y[1]
                            elif 'CPUs' in y:
                                node.cpus = y[1]
                            elif 'CPUsSpecList' in y:
                                node.cpus_spec_list = y[1]
                            elif 'DenyGroups' in y:
                                node.deny_groups = y[1]
                            elif 'DenyUsers' in y:
                                node.deny_users = y[1]
                            elif 'Feature' in y:
                                node.features = y[1]
                            elif 'FrontendName' in y:
                                node.frontend_name = y[1]
                            elif 'FrontEndADDR' in y:
                                node.frontend_addr = y[1]
                            elif 'GRES' in y:
                                node.gres = y[1]
                            elif 'MemSpecLimit' in y:
                                node.mem_spec_limit = y[1]
                            elif 'NodeADDR' in y:
                                node.node_addr = y[1]
                            elif 'NodeHostname' in y:
                                node.node_hostname = y[1]
                            elif 'NodeName' in y:
                                node.node_name = y[1]
                            elif 'Port' in y:
                                node.port = y[1]
                            elif 'Procs' in y:
                                node.procs = y[1]
                            elif 'RealMemory' in y:
                                node.real_Memory = y[1]
                            elif 'Reason' in y:
                                node.reason = y[1]
                            elif 'Sockets' in y:
                                node.sockets = y[1]
                            elif 'SocketsPerBoard' in y:
                                node.sockets_per_board = y[1]
                            elif 'State' in y:
                                node.state = y[1]
                            elif 'THreadsPerCore' in y:
                                node.threads_per_core = y[1]
                            elif 'TmpDisk' in y:
                                node.tmp_disk = y[1]
                            elif 'TRESWeight' in y:
                                node.tres_weights = y[1]
                            elif 'Weight' in y:
                                node.weight = y[1]
                            else:
                                print('Error parsing node information from\
                                    config file on line: {}', linecount)

                    elif 'PartitionName' in line:
                        partition = PartitionType()
                        x = line.split(' ')
                        for column in x:
                            y = x.split('=')
                            if 'ALLOCNode' in y:
                                partition.alloc_nodes = y[1]
                            elif 'AllowAccounts' in y:
                                partition.allow_accounts = y[1]
                            elif 'AllowGroup' in y:
                                partition.allow_groups = y[1]
                            elif 'AllowQOS' in y:
                                partition.allow_qos = y[1]
                                partition.alternate = y[1]
                                partition.cpubind = y[1]
                                partition.default = y[1]
                                partition.def_cpu_per_gpu = y[1]
                                partition.def_mem_per_cpu = y[1]
                                partition.def_mem_per_gpu = y[1]
                                partition.def_mem_per_node = y[1]
                                partition.deny_accounts = y[1]
                                partition.deny_qos = y[1]
                                partition.default_time = y[1]
                                partition.disable_root_jobs = y[1]
                                partition.exclusive_user = y[1]
                                partition.grace_time = y[1]
                                partition.hidden = y[1]
                                partition.lnn = y[1]
                                partition.max_cpus_per_node = y[1]
                                partition.max_mem_per_cpu = y[1]
                                partition.max_mem_per_node = y[1]
                                partition.max_Nodes = y[1]
                                partition.over_subscribe = y[1]
                                partition.max_time = y[1]
                                partition.nodes = y[1]
                                partition.partition_name = y[1]
                                partition.preempt_mode = y[1]
                                partition.priority_job_factor = y[1]
                                partition.priority_tier = y[1]
                                partition.qos = y[1]
                                partition.req_resv = y[1]
                                partition.root_only = y[1]
                                partition.select_type_parameters = y[1]
                                partition.state = y[1]
                                partition.tres_billing_weights = y[1]

                    else:
                        x = line.split('=')
                        if 'ClusterName' in x:
                            self.__options.cluster_name = x[1]
                        if 'SlurmctldHost' in x:
                            self.__options.slurmctld_host(x[1])
                        if 'SlurmUser' in x:
                            self.__options.slurm_user(x[1])
                        if 'SlurmctldPort' in x:
                            self.__options.slurmctld_port(x[1])
                        if 'SlurmctldSyslogDebug' in x:
                            self.__options.slurmctld_syslog_debug(x[1])
                        if 'SlurmdPort' in x:
                            self.__options.slurmd_port(x[1])
                        if 'SlurmdSyslogDebug' in x:
                            self.__options.slurmd_syslog_dbug(x[1])
                        if 'AuthType' in x:
                            self.__options.auth_type(x[1])
                        if 'StateSaveLocation' in x:
                            self.__options.state_save_location(x[1])
                        if 'SlurmdSpoolDir' in x:
                            self.__options.slurmd_spool_dir(x[1])
                        if 'SwitchType' in x:
                            self.__options.switch_type(x[1])
                        if 'MpiDefault' in x:
                            self.__options.mpi_default(x[1])
                        if 'SlurmctldPidFile' in x:
                            self.__options.slurmctld_pid_file(x[1])
                        if 'SlurmdPidFile' in x:
                            self.__options.slurmd_pid_file(x[1])
                        if 'ReturnToService' in x:
                            self.__options.return_to_service(x[1])
                        if 'DebugFlags' in x:
                            self.__options.debug_flags(x[1])
                        if 'HealthCheckInterval' in x:
                            self.__options.health_check_interval(x[1])
                        if 'HealthCheckProgram' in x:
                            self.__options.health_check_program(x[1])
                        if 'SlurmctldTimeout' in x:
                            self.__options.slurmctld_timeout(x[1])
                        if 'SlurmdTimeout' in x:
                            self.__options.slurmd_timeout(x[1])
                        if 'InactiveLimit' in x:
                            self.__options.inactive_limit(x[1])
                        if 'MinJobAge' in x:
                            self.__options.min_job_age(x[1])
                        if 'KillWait' in x:
                            self.__options.kill_wait(x[1])
                        if 'Waittime' in x:
                            self.__options.wait_time(x[1])
                        if 'GroupUpdateTime' in x:
                            self.__options.group_update_time
                        if 'GroupUpdateForce' in x:
                            self.__options.group_update_force(x[1])
                        if 'SchedulerType' in x:
                            self.__options.scheduler_type(x[1])
                        if 'SchedulerParameters' in x:
                            self.__options.scheduler_parameters(x[1])
                        if 'SelectType' in x:
                            self.__options.select_type(x[1])
                        if 'SelectTypeParameters' in x:
                            self.__options.select_type_parameters(x[1])
                        if 'TaskPlugin' in x:
                            self.__options.task_plugin(x[1])
                        if 'ProctrackType' in x:
                            self.__options.proctrack_type(x[1])
                        if 'FastSchedule' in x:
                            self.__options.fast_schedule(x[1])
                        if 'GresTypes' in x:
                            self.__options.gres_types(x[1])
                        if 'MaxArraySize' in x:
                            self.__options.max_array_size(x[1])
                        if 'MaxJobCount' in x:
                            self.__options.max_job_count(x[1])
                        if 'PreemptMode' in x:
                            self.__options.preempt_mode(x[1])
                        if 'PreemptType' in x:
                            self.__options.preempt_type(x[1])
                        if 'PrologFlags' in x:
                            self.__options.prolog_flags(x[1])
                        if 'JobCompType' in x:
                            self.__options.job_comp_type(x[1])
                        if 'JobSubmitPlugins' in x:
                            self.__options.job_submit_plugins(x[1])
                        if 'PriorityFlags' in x:
                            self.__options.priority_flags(x[1])
                        if 'PriorityType' in x:
                            self.__options.priority_type(x[1])
                        if 'PriorityDecayHalfLife' in x:
                            self.__options.priority_decay_half_life(x[1])
                        if 'PriorityCalcPeriod' in x:
                            self.__options.priority_calc_period(x[1])
                        if 'PriorityMaxAge' in x:
                            self.__options.priority_max_age(x[1])
                        if 'PriorityWeightAge' in x:
                            self.__options.priority_weight_age(x[1])
                        if 'PriorityWeightFairShare' in x:
                            self.__options.priority_weight_fair_share(x[1])
                        if 'PriorityWeightJobSize' in x:
                            self.__options.priority_weight_job_size(x[1])
                        if 'PriorityWeightPartition' in x:
                            self.__options.priority_weight_partition(x[1])
                        if 'PriorityWeightQOS' in x:
                            self.__options.priority_weight_qos(x[1])
                        if 'PriorityWeightTRES' in x:
                            self.__options.priority_weight_tres(x[1])
                        if 'FairShareDampeningFactor' in x:
                            self.__options.fair_share_dampening_factor(x[1])
                        if 'SlurmctldDebug' in x:
                            self.__options.slurmctld_debug(x[1])
                        if 'SlurmctldLogFile' in x:
                            self.__options.slurmctld_log_file(x[1])
                        if 'SlurmdDebug' in x:
                            self.__options.slurmd_debug(x[1])
                        if 'SlurmdLogFile' in x:
                            self.__options.slurmd_log_file(x[1])
                        if 'JobAcctGatherType' in x:
                            self.__options.job_acct_gather_type(x[1])
                        if 'JobAcctGatherFrequency' in x:
                            self.__options.job_acct_gather_frequency(x[1])
                        if 'AcctGatherNodeFreq=' in x:
                            self.__options.acct_gather_node_freq(x[1])
                        if 'JobAcctGatherParams' in x:
                            self.__options.job_acct_gather_params(x[1])
                        if 'MemLimitEnforce' in x:
                            self.__options.mem_limit_enforce(x[1])
                        if 'AccountingStorageEnforce' in x:
                            self.__options.accounting_storage_enforce(x[1])
                        if 'AccountingStorageHost' in x:
                            self.__options.accounting_storage_host(x[1])
                        if 'AccountingStorageType' in x:
                            self.__options.accounting_storage_type(x[1])
                        if 'AccountingStorageTRES' in x:
                            self.__options.accounting_storage_tres(x[1])
                        if 'TopologyPlugin' in x:
                            self.__options.topology_plugin(x[1])
                        if 'ResumeTimeout' in x:
                            self.__options.resume_timeout(x[1])
                        if 'RebootProgram' in x:
                            self.__options.reboot_program(x[1])

            return self.__optionss, self.__nodes, self.__partitions

        except Exception as ex:
            print(ex)
            print('There was a parsing error at line: ' + str(linecount))
            print(line)
