#!/usr/bin/python3
"""
0-validate_utf8.py
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    :param data: List of integers representing bytes
    :return: True if data is a valid UTF-8 encoding, else False
    """
    num_bytes = 0

    for num in data:
        byte = num & 0xFF  # Only examine the least significant 8 bits

        if num_bytes == 0:
            if byte >> 5 == 0b110:  # 110xxxxx
                num_bytes = 1
            elif byte >> 4 == 0b1110:  # 1110xxxx
                num_bytes = 2
            elif byte >> 3 == 0b11110:  # 11110xxx
                num_bytes = 3
            elif byte >> 7:  # 1xxxxxxx (must be 0xxxxxxx)
                return False
        else:
            if byte >> 6 != 0b10:  # 10xxxxxx
                return False
            num_bytes -= 1

    return num_bytes == 0
