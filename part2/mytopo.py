from mininet.topo import Topo
from mininet.net import Mininet
from mininet.cli import CLI

class MyTopo(Topo):
    def build(self):
        switch = self.addSwitch("s1")
        for i in range(3):
            host = self.addHost(f"h{i+1}")
            self.addLink(host, switch)

topo = MyTopo()
net = Mininet(topo=topo)
net.start()
CLI(net)
net.stop()

