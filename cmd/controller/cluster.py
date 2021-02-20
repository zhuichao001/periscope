import cmd.controller.agent as agent
import common.consul as consul
import common.const as const

class cluster:
    def __init__(self, kind):
        name = const.AGENT_NEAR if kind=='near' else const.AGENT_REMOTE
        self.consul = consul.consul()
        addrs = self.consul.discovery(name)
        print("AGENT_NEAR:", name, addrs)
        self.agents = [agent.agent(addr) for addr in addrs]

    def prepare(self):
        for agent in self.agents:
            agent.prepare()

    def restore(self):
        for agent in self.agents:
            agent.restore()

    def drive(self):
        for agent in self.agents:
            agent.drive()
