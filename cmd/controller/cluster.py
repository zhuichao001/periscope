import cmd.controller.agent as agent
import common.consul as consul
import common.const as const
import config.controller as config


class cluster:
    def __init__(self, kind):
        self.opt = config.option()
        name = const.AGENT_NEAR if kind=='near' else const.AGENT_REMOTE
        self.consul = consul.consul()
        self.addrs = self.consul.discovery(name)
        self.__assign()

        print("AGENT_NEAR:", name, self.addrs)
        self.agents = [agent.agent(addr, self.opts[i]) for i,addr in enumerate(self.addrs)]

    def __assign(self):
        n = len(self.addrs)
        self.opts = [config.option() for _ in range(n)]
        for opt in self.opts[1:]:
            opt.generator_count = self.opt.generator_count / n
            opt.executor_count = self.opt.generator_count / n
            opt.differ_count = self.opt.generator_count / n
            opts[0].generator_count -= opt.generator_count
            opts[0].executor_count -= opt.executor_count
            opts[0].differ_count -= opt.differ_count

        for i in range(n):
            print(i, "assign count:::", self.opts[i].generator_count, self.opts[i].executor_count, self.opts[i].differ_count)


    def prepare(self):
        '''
        for agent in self.agents:
            agent.prepare()
        '''

    def restore(self):
        '''
        for agent in self.agents:
            agent.restore()
        '''

    def drive(self, act):
        for agent in self.agents:
            agent.drive(act)
