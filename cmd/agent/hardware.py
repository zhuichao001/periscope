import cmd.agent.net as net
import cmd.agent.memory as memory
import cmd.agent.disk as disk
import cmd.agent.cpu as cpu

class Hardware:
    def __init__(self):
        self.netdev = net.NetDevice()
        self.mem = memory.Memory()
        self.disk = disk.Disk()
        self.cpu = cpu.Cpucore()

    def exec(self, cmd):
        prefix, val = cmd.split(":")
        if prefix == 'net.delay':
            self.netdev.delay(int(val))
        elif prefix == 'net.loss':
            self.netdev.loss(int(val))
        elif prefix == 'net.clear':
            self.netdev.clear()
        elif prefix == 'mem.occupy':
            self.memory.occupy(int(val))
        elif prefix == 'mem.clear':
            self.memory.clear()
        elif prefix == 'disk.write':
            self.disk.write(int(val))
        elif prefix == 'disk.occupy':
            self.disk.occupy(int(val))
        elif prefix == 'disk.clear':
            self.disk.clear()
        else:
            pass
