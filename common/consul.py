import json
import random
import common.httpio as httpio
import common.localip as localip
import common.const as const
import config.consul as config


class consul:
    def __init__(self):
        self.enable = True
        self.consulhost = config.option().consul

    def deregister(self, id):
        uri = 'v1/agent/service/deregister/%s' % (id)
        resp = httpio.httpio(self.consulhost).put(uri, '')

    def deregall(self, name):
        ids = self.ids(name)
        for id in ids:
            self.deregister(id)

    def register(self, id, name, svrhost):
        ip, port = svrhost.split(':')
        body = {
                'Id': id,
                'Name': name,
                'Address': ip,
                'Port': int(port),
                'Tags': [name],
                'Check': {}
                #'Check': {'id':id, 'name':'executor', 'tcp':svrhost, 'interval':'1s', 'timeout':'1s'}
        }

        uri = 'v1/agent/service/register?replace-existing-checks=true'
        data = json.dumps(body)
        print(data)
        resp = httpio.httpio(self.consulhost).put(uri, data)
        print("after register:::", resp)

    def ids(self, name):
        uri = 'v1/health/service/%s?passing=false' % (name)
        resp = httpio.httpio(self.consulhost).get(uri)
        data = json.loads(resp)
        print("discovery:::", name, data)
        hosts = [obj['Service']['Address']+':'+str(obj['Service']['Port']) for obj in data]
        ids = [obj['Service']['ID'] for obj in data]
        return ids

    def discovery(self, name):
        uri = 'v1/health/service/%s?passing=false' % (name)
        resp = httpio.httpio(self.consulhost).get(uri)
        data = json.loads(resp)
        hosts = [obj['Service']['Address']+':'+str(obj['Service']['Port']) for obj in data]
        return hosts


if __name__ == '__main__':
    consultant = consul()
    print("AGENT_NEAR:::", consultant.discovery(const.AGENT_NEAR))
    print("GENERATOR:::", consultant.discovery(const.GENERATOR))
    print("EXECUTOR:::", consultant.discovery(const.EXECUTOR))
    print("DIFFER:::", consultant.discovery(const.DIFFER))

    consultant.deregall(const.AGENT_NEAR)
    consultant.deregall(const.GENERATOR)
    consultant.deregall(const.EXECUTOR)
    consultant.deregall(const.DIFFER)

    print('=================================')

    print("AGENT_NEAR:::", consultant.discovery(const.AGENT_NEAR))
    print("GENERATOR:::", consultant.discovery(const.GENERATOR))
    print("EXECUTOR:::", consultant.discovery(const.EXECUTOR))
    print("DIFFER:::", consultant.discovery(const.DIFFER))
