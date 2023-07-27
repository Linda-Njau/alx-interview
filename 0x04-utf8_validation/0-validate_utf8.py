#!/usr/bin/python3
"""validUTF8"""

def validUTF8(data):
    """validates data encoding"""
    num_bytes_to_check = 0

    for byte in data:
        if byte >> 6 == 0b10:
            if num_bytes_to_check == 0:
                return False
            num_bytes_to_check -= 1
        else:
            if byte >> 7 == 0b0:
                num_bytes_to_check = 0
            elif byte >> 5 == 0b110:
                num_bytes_to_check = 1
            elif byte >> 4 == 0b1110:
                num_bytes_to_check = 2
            elif byte >> 3 == 0b11110:
                num_bytes_to_check = 3
            else:
                return False
    return num_bytes_to_check == 0
