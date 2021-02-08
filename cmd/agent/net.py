
class NetDevice:
    def __init__(self):
        self.delay_tmpl = "sudo tc qdisc add dev eth0 root netem delay %dms"
        self.clear_tmpl = "sudo tc qdisc del dev eth0 root"
        self.loss_tmpl = "sudo tc qdisc add dev eth0 root netem loss %d%"

    def delay(self, val):
        return self.delay_tmpl % (val)

    def loss(self):
        return self.loss_tmpl % (val)

    def clear(self):
        return self.clear_tmpl % (val)
