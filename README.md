# P4SmartSwitch

```python3 IpToJsonCreator.py``` -> Run this command to update s1-runtime.json file.

copy s1-runtime.json file to pod-topo folder.

```make run``` -> start the mininet

``` mininet > pingall``` -> ping all the network and control the if the packets is dropped

```simple_switch_CLI --thrift-port 9090``` -> open p4 shell

```table_dump MyIngress.ipv4_lpm``` -> to show all the action table.
