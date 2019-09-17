ospf_route = "O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
list1 = (ospf_route.split())
print("%-20s %-15s" % ('Protocol:',((list1[0])+'SPF') ))
print("%-20s %-15s" % ('Prefix:',(list1[1])))
print("%-20s %-15s" % ('AD/Metric:',(list1[2]).strip('[]')))
print("%-20s %-15s" % ('Next-Hop:',(list1[4]).strip(',')))
print("%-20s %-15s" % ('Last update:',(list1[5]).strip(',')))
print("%-20s %-15s" % ('Outbound Interface:',(list1[6])))