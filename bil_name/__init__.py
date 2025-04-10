import os
import struct
import argparse

def gen_device_name(device_id):
        path = os.path.dirname(os.path.abspath(__file__))
        with open(path + "/adjs.txt", 'r') as file:
            adjs = file.read().splitlines()
        with open(path + "/nouns.txt", 'r') as file:
            nouns = file.read().splitlines()

        device_id_bytes = bytes.fromhex(device_id)
        id_h, id_l = struct.unpack('>LL', device_id_bytes)
        device_name = adjs[id_h % len(adjs)] + '_' + nouns[id_l % len(nouns)]

        return device_name

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
            prog='human readable name generator',
            description='Converts a 64-bit hex string to a human-readable "adj_name" name'
    )
    parser.add_argument('hex_id')

    args = parser.parse_args()

    if (len(args.hex_id) != 16):
        print('invalid hex string')
        exit(1)
    for i, b in enumerate(args.hex_id):
        if b.lower() not in '0123456789abcdef':
            print('invalid hex character at', i)
            exit(1)

    print(get_device_name(args.hex_id))
