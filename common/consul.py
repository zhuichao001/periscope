import json
import random
import common.httpio as httpio
import common.localip as localip
import common.const as const


class consul:
    def __init__(self):
        self.consulhost = '127.0.0.1:8500'

    def deregister(self, name):
        for id in self.ids(name):
            print("deregister id:::", id)
            uri = 'v1/agent/service/deregister/%s' % (id)
            resp = httpio.httpio(self.consulhost).put(uri, '')
            print("after deregister:::", resp)

    def deregall(self, name):
        ids = consul.discovery(name)
        print("after discovery all:::", ids)
        for id in ids:
            consul.deregister(id)

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
        print("ids:::", ids)
        return ids

    def discovery(self, name):
        uri = 'v1/health/service/%s?passing=false' % (name)
        resp = httpio.httpio(self.consulhost).get(uri)
        data = json.loads(resp)
        #print("discovery:::", name, data)
        hosts = [obj['Service']['Address']+':'+str(obj['Service']['Port']) for obj in data]
        ids = [obj['Service']['ID'] for obj in data]
        #print("ids:::", ids)
        #print('hosts:::', hosts)
        return hosts


if __name__ == '__main__':
    consultant = consul()
    consultant.deregister(const.AGENT_NEAR)
    #consultant.register('aes', '127.0.0.1:9001')
    #consultant.discovery('aes')
