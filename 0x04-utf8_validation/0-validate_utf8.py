#!/usr/bin/python3
"""validUTF8"""


def validUTF8(data):
    """UTF8 validation"""
    num_bytes = 0
    mask_1 = 1 << 7
    mask_2 = 1 << 6

    for num in data:
        mask = 1 << 7
        if num_bytes == 0:
            while mask & num:
                num_bytes += 1
                mask = mask >> 1

            if num_bytes == 0:
                continue

            if num_bytes == 1 or num_bytes > 4:
                return False

        else:
            if not ((num & mask_1) and not (num & mask_2)):
                return False
        num_bytes -= 1
    return num_bytes == 0
