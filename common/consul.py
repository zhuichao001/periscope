import json
import random
import common.httpio as httpio
import common.localip as localip


class consultant:
    def __init__(self):
        self.consulhost = '127.0.0.1:8500'

    def deregister(self, id):
        uri = 'v1/agent/service/deregister/%s' % (id)
        resp = httpio.httpio(self.consulhost).put(uri, '')
        print("after deregister:::", resp)

    def deregall(self, name):
        ids = consul.discovery(name)
        print("after discovery all:::", ids)
        for id in ids:
            consul.deregister(id)

    def register(self, name, svrhost):
        ip, port = svrhost.split(':')
        id = name+'-'+localip.hostip()
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

    def discovery(self, name):
        uri = 'v1/health/service/%s?passing=false' % (name)
        resp = httpio.httpio(self.consulhost).get(uri)
        data = json.loads(resp)
        print("|||", data)
        hosts = [obj['Service']['Address']+':'+str(obj['Service']['Port']) for obj in data]
        ids = [obj['Service']['ID'] for obj in data]
        print("ids:::", ids)
        print('hosts:::', hosts)
        return ids


if __name__ == '__main__':
    consul = consultant()
    consul.deregister('aes')
    consul.register('aes', '127.0.0.1:9001')
    consul.discovery('aes')
