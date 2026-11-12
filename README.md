[![CI](https://github.com/de-it-krachten/ansible-role-portscan/workflows/CI/badge.svg?event=push)](https://github.com/de-it-krachten/ansible-role-portscan/actions?query=workflow%3ACI)


# ansible-role-portscan

Performs portscan



## Dependencies

#### Roles
None

#### Collections
- ansible.windows

## Platforms

Supported platforms

- Red Hat Enterprise Linux 8<sup>1</sup>
- Red Hat Enterprise Linux 9<sup>1</sup>
- Red Hat Enterprise Linux 10<sup>1</sup>
- RockyLinux 8
- RockyLinux 9
- RockyLinux 10
- OracleLinux 8
- OracleLinux 9
- OracleLinux 10
- AlmaLinux 8
- AlmaLinux 9
- AlmaLinux 10
- Debian 12 (Bookworm)
- Debian 13 (Trixie)
- Ubuntu 22.04 LTS
- Ubuntu 24.04 LTS
- Ubuntu 26.04 LTS
- Fedora 43
- Fedora 44<sup>1</sup>
- Windows Server 2012 R2<sup>1</sup>
- Windows Server 2016<sup>1</sup>
- Windows Server 2019<sup>1</sup>
- Windows Server 2022<sup>1</sup>
- Windows Server 2025<sup>1</sup>

Note:
<sup>1</sup> : no automated testing is performed on these platforms


## Role Variables
### defaults/main.yml
<pre><code>
portscan_target: ""                      # required: IP, hostname, CIDR (192.168.1.0/24), or comma-separated mix
portscan_ports: "22,53,80,443"           # override with -e portscan_ports=1-65535
portscan_timing: "T4"                    # T3 is gentler on busy networks
portscan_version: true                   # -sV: detect service and version (Linux)
portscan_os: false                       # -O: OS detection (Linux, needs root)
portscan_udp: false                      # -sU: top 100 UDP ports (Linux, needs root)
portscan_timeout_s: 1                    # per-connection timeout (Windows)
portscan_max_addresses: 4096             # safety cap on portscan_expanded addresses (Windows expansion)

portscan_report_server: localhost
portscan_report_dir: /tmp/reports
</pre></code>




## Example Playbook
### molecule/default/converge.yml
<pre><code>
- name: sample playbook for role 'portscan'
  hosts: all
  become: 'yes'
  tasks:
    - name: Include role 'portscan'
      ansible.builtin.include_role:
        name: portscan
</pre></code>
