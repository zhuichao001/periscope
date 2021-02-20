import common.sqlite as sqlite


class fullcheck:
    def __init__(self, taskid):
        taskname = 'task-%s.db' % (taskid)
        self.db = sqlite.sqlitedb(taskname)

        self.db.execute('''CREATE TABLE IF NOT EXISTS cmds(
            `id`     INTEGER PRIMARY KEY   AUTOINCREMENT,
            `val`    TEXT              NOT NULL
        ) ''')
        self.db.flush()

    def income(self, cmds):
        for cmd in cmds:
            self.db.execute('INSERT INTO cmds(val) VALUES("%s"' % (cmd))
        self.db.flush()

    def outcome(self):
        self.db.query('SELECT val from cmds')
        return self.db


