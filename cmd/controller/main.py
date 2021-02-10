import sys


def main():
    opt = Options('./config.yaml')
    agent = Agent()

    for agent in opt.agents:
        agent = Agent(addr)
        if opt.tc_enable:
            agent.tc_delay(opt.tc_delay)
            agent.tc_loss(opt.tc_loss)
        elif opt.mem_enable:
            agent.mem_occupy(opt.mem_occupy)
        elif opt.disk_enable:
            agent.disk_write(opt.disk_write)
            agent.disk_occupy(opt.disk_occupy)
        elif opt.split_enable:
            pass #TODO
        elif opt.failover_enable:
            pass #TODO
        elif opt.transform_enable:
            pass #TODO
            
    time.sleep(opt.duration)

    for agent in opt.agents:
        agent = Agent(addr)
        if opt.tc_enable:
            agent.tc_clear()
        elif opt.mem_enable:
            agent.mem_clear()
        elif opt.disk_enable:
            agent.disk_clear()
