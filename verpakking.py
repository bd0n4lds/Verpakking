def sniff_packets(iface=None):
    """
    Sniff 80 port packets with `iface`, if None (default), then the
    scapy's default interface is used
    """
	
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-i", "--iface", help="")
    parser.add_argument("--show-raw", dest="show_raw", action="store_true", help="")

    # parse arguments
    args = parser.parse_args()
	iface = args.iface
	show_raw = args.show_raw

    sniff_packets(iface)