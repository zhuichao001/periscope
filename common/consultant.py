import httpio
import json
import localip


#curl -X PUT -d '{"id": "jetty","name": "jetty","address": "192.168.1.200","port": 8080,"tags": ["dev"],"checks": [{"http": "http://192.168.1.104:9020/health","interval": "1s"}]}' http://192.168.1.100:8500/v1/agent/service/register

class consultant:
    def __init__(self):
        self.host = '11.3.90.194:8500'
        #self.host = '127.0.0.1:8500'

    def register(self, name, svrhost):
        ip, port = svrhost.split(':')
        id = name+'-'+localip.hostip().replace('.','_')
        body = {
                'Id': id,
                'Name': name,
                'Address': ip,
                'Port': int(port),
                'Tags': [name],
                'Check': {}
                #'Check': {'Id':id, 'Name':'executor', 'Tcp':svrhost, 'Interval':'1s', 'Timeout':'1s'}
        }

        uri = 'v1/agent/service/register?replace-existing-checks=true'
        data = json.dumps(body)
        print(data)
        resp = httpio.httpio(self.host).put(uri, data)
        print("after register:::", resp)

    def discovery(self, name):
        uri = 'v1/health/service/%s?passing=false' % (name)
        resp = httpio.httpio(self.host).get(uri)
        data = json.loads(resp)
        hosts = [obj['Service']['Address']+':'+str(obj['Service']['Port']) for obj in data]
        print(':::', hosts)


if __name__ == '__main__':
    consul = consultant()
    consul.register('aes', '127.0.0.2:9001')
    consul.register('aes', '127.0.0.2:9001')
    consul.discovery('aes')
