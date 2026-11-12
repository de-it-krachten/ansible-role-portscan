# Expands IPs, CIDR networks, and hostnames into a JSON list of targets.
# Usage: expand_targets.py "<spec>" <max_addresses>
import ipaddress, json, sys

spec, cap = sys.argv[1], int(sys.argv[2])
out = []
for raw in spec.split(','):
    t = raw.strip()
    if not t:
        continue
    try:
        net = ipaddress.ip_network(t, strict=False)
    except ValueError:
        out.append(t)  # hostname: passed through unchanged
        continue
    if net.num_addresses > cap:
        sys.stderr.write(t + ' expands to ' + str(net.num_addresses) + ' addresses; raise portscan_max_addresses\n')
        sys.exit(1)
    hosts = list(net)  # every address in the range, including network and broadcast (as nmap scans them)
    out.extend(str(h) for h in hosts)
out = list(dict.fromkeys(out))
if len(out) > cap:
    sys.stderr.write('total ' + str(len(out)) + ' targets exceeds portscan_max_addresses\n')
    sys.exit(1)
print(json.dumps(out))
