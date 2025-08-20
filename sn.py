import ipaddress
import sys

def ParseIP_Range(network_address):
	try:
		IP = ipaddress.ip_interface(network_address)
		return IP
	except Exception:
		return None

def ParseIP(address):
	try:
		IP = ipaddress.ip_address(address)
		return IP
	except Exception:
		return None

def GetNetworkInfo(network_address):
	net = network_address.network
	prefix = network_address.with_prefixlen
	subnet_mask = network_address.with_netmask
	wildcard_address = network_address.hostmask
	broadcast_address = net.broadcast_address

	first_address = list(net.hosts())[0]
	last_address = list(net.hosts())[-1]

	print('Network address   : ', str(net).split('/')[0])
	print('CIDR              : ', prefix.split('/')[1])
	print('Broadcast address : ', broadcast_address)
	print('Subnet Mask       : ', subnet_mask.split('/')[1])
	print('Wildcard address  : ', wildcard_address)
	print('First address     : ', first_address)
	print('Last address      : ', last_address)
    
	return first_address,last_address

def Print_Usage():
    print('Simple Subnet Calculator')
    print('\tUsage: subnet.py [IP/CIDR] [IP]')
    print('\nParameters')
    print('\t[IP/CIDR]:\t Enter the Network address in CIDR notation.')
    print('\t[IP]:\t\t Enter the IP you wish to check for in range of the network address')
    print('\nOptions')
    print('\t-h\t\t Display this usage statement.')

def main():
    IP_Range = None
    IP = None
    if (len(sys.argv) == 1):
        IP_Range = ParseIP_Range(input("Enter IP/CIDR: "))
        IP = ParseIP(input("Enter IP to check: "))
    elif (len(sys.argv) == 2):
        if (sys.argv[1] == '-h'):
            Print_Usage()
            exit()
        IP_Range = ParseIP_Range(sys.argv[1])
        IP = ParseIP(input("Enter IP to check: "))
    else:
        IP_Range = ParseIP_Range(sys.argv[1])
        IP = ParseIP(sys.argv[2])

    if (IP_Range == None):
        print(f'Not at valid IP address range!')
        Print_Usage();
        exit()
        
    first,last = GetNetworkInfo(IP_Range)
    if (IP is not None):
        if IP in IP_Range.network:
            print(f'\n({IP}) in network: TRUE')
        else:
            print(f'\n({IP}) in network: FALSE')

if (__name__ == '__main__'):
    main()