class Accounts:
    def __init__(self):
        self.account = None
        self.description = None
        self.org = None
        self.num_acct = None

    def __str__(self):
        return """Slurm User(account name: {}, account description: {},
                  orginization account belongs to: {}, number of accounts: {}"""\
                  .format(self.account, self.description, self.org,
                          self.num_acct)
