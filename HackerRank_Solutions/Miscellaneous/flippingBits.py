def flippingBits(n):
    BITS = 32

    effective_bits = n.bit_length()
    binary_representation = bin(n)
    string_equivalent = ''

    for i in range(BITS - effective_bits) :
        string_equivalent += '0'
    string_equivalent += str(binary_representation[2:])
    
    flipped = 0
    for i in range(BITS) :
        if string_equivalent[i] == '0' :
            flipped += pow(2, BITS - i - 1)
    return flipped