import os
import sys
import config.consul as consul


def jarmain(taskid, addr, opt):
    for url in opt.targets:
        if url.startswith('drc-consumer'):
            src = url
        else:
            dest = url
    if src and dest:
        consul_addr = consul.option().consul
        logfile = './output/jar-executor-%s.log' % (str(taskid))
        #cmd = 'java -jar ./cmd/executor/jarexecutor/jar/periscope-executor.jar --taskid %s --src %s --dest %s --listen %s --consul %s > %s' % (taskid, src, dest, addr, consul_addr, logfile)
        cmd = 'echo "hello periscope" > %s' % (logfile)
        os.system(cmd)
    else:
        print('Error: java-drc target invalid:', opt.targets)

if __name__ == '__main__':
    if len(sys.argv)<2:
        print('usage:\n  python main.py ip:port')
        sys.exit()

    host = sys.argv[1]
    ip,port = host.split(':')
    port = int(port)

    import config.executor as config
    jarmain('unknown', (ip,port), config.option())
