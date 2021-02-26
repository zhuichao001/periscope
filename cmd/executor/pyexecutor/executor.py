import redis
import time
import cmd.executor.pyexecutor.handler as handler


class RedisExecuter:
    def __init__(self, ip, port, password=None):
        self.addr = (ip, port)
        #self.pool = redis.ConnectionPool(host=ip, port=port, password=password, max_connections=8)
        self.red = redis.Redis(host=ip, port=port, password=password)
        self.host = '%s:%d' % (ip, port)

    def execute(self, cmd):
        cmd = cmd[2:] if cmd.startswith(b'::') else cmd
        return handler.call(self.red, cmd)


class JimkvExecuter:
    def __init__(self, ip, port, password=None):
        self.addr = (ip,port)
        if password:
            self.red = redis.Redis(host=ip, port=port, password=password, retry_on_timeout=True)
        else:
            self.red = redis.Redis(host=ip, port=port, retry_on_timeout=True)
        self.host = '%s:%d' % (ip, port)

    def _patch(self, cmd):
        if cmd.find(b'SCAN') >= 0:
            cmd = cmd.replace(b' 0 ', b' "" ')
            print(":::", cmd)
        return cmd

    def execute(self, cmd):
        cmd = self._patch(cmd)
        cmd = cmd[2:] if cmd.startswith(b'::') else cmd
        return handler.call(self.red, cmd)


class JimdbDrcExecuter:
    def __init__(self, whost, wport, wpassword, rhost, rport, rpassword):
        self.addr = (host,port)
        self.wred = redis.Redis(host=whost, port=wport, password=wpassword)
        self.rred = redis.Redis(host=rhost, port=rport, password=rpassword)

    def _patch(self, cmd):
        if cmd.find(b'SCAN') >= 0:
            cmd = cmd.replace(b' 0 ', b' "" ')
            print(":::", cmd)
        return cmd

    def execute(self, cmd):
        cmd = self._patch(cmd)
        if cmd.startswith('::'):
            wres = handler.call(self.wred, cmd[2:])
            rres = handler.call(self.rred, cmd[2:])
            if wres==rres:
                return wres
            else:
                return None
        else:
            return handler.call(self.wred, cmd)


if __name__ == '__main__':
    #exe = JimkvExecuter('11.3.85.38', 5363, password='jimdb://2913114965120297581/2')
    exe = RedisExecuter('127.0.0.1', 6379)
    #exe = JimkvExecuter('11.3.90.194', 6378, password='jimdb://2911032239959041295/11')
    print(exe.execute(b'SETEX hVLoBIFJ3k 237 QJmfyLNG2OV61RhvxeXgr5iI3s90Ek'))
    print(exe.execute(b"SET a b"))
