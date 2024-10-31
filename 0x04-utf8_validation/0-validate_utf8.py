def validUTF8(data):
    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    # Masks to check the first byte of different UTF-8 characters
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for byte in data:
        # Keep only the last 8 bits of each integer
        byte = byte & 0xFF

        if num_bytes == 0:
            # Determine the number of bytes in the UTF-8 character
            if (byte & mask1) == 0:
                # 1-byte character
                continue
            elif (byte & (mask1 >> 1)) == mask1:
                # Check if the byte starts with 110 for 2-byte characters
                num_bytes = 1
            elif (byte & (mask1 >> 2)) == (mask1 >> 1):
                # Check if the byte starts with 1110 for 3-byte characters
                num_bytes = 2
            elif (byte & (mask1 >> 3)) == (mask1 >> 2):
                # Check if the byte starts with 11110 for 4-byte characters
                num_bytes = 3
            else:
                # Invalid first byte
                return False
        else:
            # Check if this byte starts with 10xxxxxx
            if not (byte & mask1 and not (byte & mask2)):
                return False
            num_bytes -= 1

    # If num_bytes is not zero, we have an incomplete character at the end
    return num_bytes == 0

