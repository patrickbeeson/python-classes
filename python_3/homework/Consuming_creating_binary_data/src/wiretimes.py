"""
wiretimes.py: reads the wiretimes.bin file and prints the timestamp for each packet
in seconds and microseconds.
"""
import struct
import os


def parse_packet(wsbinfilepath):
    """
    Parses packets in a given wireshark binary file
    and prints the timestamp for each packet in seconds and microseconds.
    """
    # Set initial header offset
    offset = 24
    with open(wsbinfilepath, 'rb') as f:
        while True:
            # Skip initial headers
            f.seek(offset)
            # Skip to the first packet
            data = f.read(16)
            if not data:
                break
            # Grab our entry headers
            ts_sec, ts_usec, incl_len, orig_len = struct.unpack('=4L', data)
            # Advance our offset to get the next timestamp
            offset = f.tell() + incl_len
            print('Timestamp: {} seconds, {} microseconds'.format(ts_sec, ts_usec))

if __name__ == "__main__":
    wsbinfile = 'wireshark.bin'
    wsbinfilepath = os.path.join(os.getcwd(), wsbinfile)
    parse_packet(wsbinfilepath)
