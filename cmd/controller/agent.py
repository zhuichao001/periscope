import cmd.controller.hardware as hardware
import cmd.controller.deploy as deployer
import config.agent as config


class agent:
    def __init__(self, addr, opt):
        self.opt = config.option()
        print(">>>", addr)
        addr = addr.split(':')
        self.addr = (addr[0], int(addr[1]))
        self.device = hardware.hardware(self.addr)
        self.deploy = deployer.deploy(self.addr, opt)

    def prepare(self):
        if self.opt.net_enable:
            self.device.net_delay(self.opt.net_delay)
            self.device.net_loss(self.opt.net_loss)
        elif self.opt.mem_enable:
            self.device.mem_occupy(self.opt.mem_occupy)
        elif self.opt.disk_enable:
            self.device.disk_write(self.opt.disk_write)
            self.device.disk_occupy(self.opt.disk_occupy)
        elif self.opt.split_enable:
            pass #TODO
        elif self.opt.failover_enable:
            pass #TODO
        elif self.opt.transform_enable:
            pass #TODO

    def restore(self):
        if self.opt.net_enable:
            self.device.net_clear()
        elif self.opt.mem_enable:
            self.device.mem_clear()
        elif self.opt.disk_enable:
            self.device.disk_clear()

    def drive(self, act):
        if act == 'start':
            self.deploy.differ()
            self.deploy.executor(act)
            self.deploy.generator(act)
        elif act == 'stop':
            self.deploy.differ(act)
            self.deploy.executor(act)
            self.deploy.generator(act)

