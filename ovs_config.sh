#!/bin/bash
echo "Configuring Open vSwitch for tenant isolation..."
sudo ovs-vsctl add-br br0
sudo ovs-vsctl add-port br0 eth0
sudo ovs-vsctl set port eth0 tag=100
