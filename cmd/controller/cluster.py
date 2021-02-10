import cmd.controller.const as const
import cmd.controller.agent as agent
import cmd.controller.option as option
import common.consul as consul

class cluster:
    def __init__(self, kind):
        name = const.AGENT_NEAR if kind=='near' else const.AGENT_REMOTE
        self.consul = consul.consul()
        addrs = self.consul.discovery(name)
        print("AGENT_NEAR:", name, addrs)
        self.opt = option.option('./cmd/controller/config.yaml')
        self.agents = [agent.agent(addr, self.opt) for addr in addrs]

    def prepare(self):
        for agent in self.agents:
            agent.prepare()

    def restore(self):
        for agent in self.agents:
            agent.restore()

    def drive(self):
        for agent in self.agents:
            agent.drive()
