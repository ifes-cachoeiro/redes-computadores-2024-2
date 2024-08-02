#!/usr/bin/python
from mininet.log import setLogLevel, info
from mn_wifi.cli import CLI
from mn_wifi.net import Mininet_wifi


# Bandwidth 1Gbps
BW = 1000

def activate_switch(switch):
    cmd = f'ovs-ofctl add-flow {switch.name} "actions=output:NORMAL"'
    switch.cmd(cmd)


def topology():
    "Create a network."
    net = Mininet_wifi()

    info("*** Adding stations/hosts\n")

    h1 = net.addHost("h1", ip="10.0.1.1/24")
    h2 = net.addHost("h2", ip="10.0.1.2/24")

    info("*** Adding Switches\n")

    switch1 = net.addSwitch("switch1")

    info("*** Creating links\n")

    net.addLink(h1, switch1, bw=BW)
    net.addLink(h2, switch1, bw=BW)

    info("*** Starting network\n")
    net.start()

    info("*** Activating switches\n")

    activate_switch(switch1)

    info("*** Running CLI\n")
    CLI(net)

    info("*** Stopping network\n")
    net.stop()


if __name__ == "__main__":
    setLogLevel("info")
    remote_controller = False
