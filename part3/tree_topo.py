from mininet.topo import Topo
from mininet.net import Mininet
from mininet.cli import CLI

class MyTreeTopo(Topo):
    def build(self):
        rootSwitch = self.addSwitch('s1')
        leftSwitch = self.addSwitch('s2')
        rightSwitch = self.addSwitch('s3')
        self.addLink(rootSwitch, leftSwitch)
        self.addLink(rootSwitch, rightSwitch)
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')
        self.addLink(h1, leftSwitch)
        self.addLink(h2, leftSwitch)
        self.addLink(h3, rightSwitch)
        self.addLink(h4, rightSwitch)

topo = MyTreeTopo()
net = Mininet(topo=topo)
net.start()
CLI(net)
net.stop()

