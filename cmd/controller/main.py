import sys


def main():
    opt = Options('./config.yaml')
    agent = Agent()

    for agent in opt.agents:
        agent = Agent(addr)
        if opt.tc_on:
            agent.tc_delay(opt.tc_delay)
            agent.tc_loss(opt.tc_loss)
        elif opt.mem_on:
            agent.mem_occupy(opt.mem_occupy)
        elif opt.disk_on:
            agent.disk_write(opt.disk_write)
            agent.disk_occupy(opt.disk_occupy)
        elif opt.split_on:
            pass #TODO
        elif opt.failover_on:
            pass #TODO
        elif opt.transform_on:
            pass #TODO
            
    time.sleep(opt.duration)

    for agent in opt.agents:
        agent = Agent(addr)
        if opt.tc_on:
            agent.tc_clear()
        elif opt.mem_on:
            agent.mem_clear()
        elif opt.disk_on:
            agent.disk_clear()
