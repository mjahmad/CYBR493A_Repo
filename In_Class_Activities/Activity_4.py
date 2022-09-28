"""
MJ Ahmad
In-class activity #4.

"""
# import modules
import os
def activity4():
    """
    This is activity #4. Pinger
    It pings several IP addresses in a pre-definded list.
    :return: N/A
    """
# List of all IP Addresses
IPs = ["127.0.0.1", "8.0.0.1", "192.168.0.10", "192.168.10.10"]

# For loop to iterate through the list.
for ip in IPs:
    # visit each item, and then ping and write output to dev
    ping = f"ping -c 1 -w 2 {ip} > ./dev 2>&1"
    # obtain the exit code
    exit_code = os.system(ping)
    # print the exit code
    print (exit_code)

