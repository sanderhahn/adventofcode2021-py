with open("day16.txt") as f:
    content = f.read()

def debug(val):
    print(val)
    return val

def parse_literal(version, type, bits):
    literal = 0
    while True:
        indicator, bits = int(bits[0], 2), bits[1:]
        value, bits = int(bits[:4], 2), bits[4:]
        literal <<= 4
        literal += value
        if indicator == 0:
            break
    return (bits, {
        "type": type,
        "version": version,
        "literal": literal,
    })

def parse_operator_bits(bits, number_of_bits):
    subpackets = []
    while number_of_bits > 0:
        (new_bits, data) = parse_packet(bits)
        number_of_bits -= len(bits) - len(new_bits)
        subpackets.append(data)
        bits = new_bits
    return (bits, subpackets)

def parse_operator_packets(bits, number_of_packets):
    subpackets = []
    for _ in range(number_of_packets):
        (bits, data) = parse_packet(bits)
        subpackets.append(data)
    return (bits, subpackets)

def parse_operator(version, type, bits):
    length_type_id, bits = int(bits[0], 2), bits[1:]
    if length_type_id == 0:
        number_of_bits, bits = int(bits[:15], 2), bits[15:]
        (bits, subpackets) = parse_operator_bits(bits, number_of_bits)
        data = {
            "version": version,
            "type": type,
            "subpackets": subpackets,
        }
    else:
        number_of_packets, bits = int(bits[:11], 2), bits[11:]
        (bits, subpackets) = parse_operator_packets(bits, number_of_packets)
        data = {
            "version": version,
            "type": type,
            "subpackets": subpackets,
        }
    return (bits, data)

def parse_packet(bits):
    version, bits = int(bits[:3], 2), bits[3:]
    type, bits = int(bits[:3], 2), bits[3:]
    if type == 4:
        (bits, data) = parse_literal(version, type, bits)
    else:
        (bits, data) = parse_operator(version, type, bits)
    return (bits, data)

def hex_to_bin(hex):
    bits = ""
    for digit in hex:
        match digit:
            case "0":
                bits += "0000"
            case "1":
                bits += "0001"
            case "2":
                bits += "0010"
            case "3":
                bits += "0011"
            case "4":
                bits += "0100"
            case "5":
                bits += "0101"
            case "6":
                bits += "0110"
            case "7":
                bits += "0111"
            case "8":
                bits += "1000"
            case "9":
                bits += "1001"
            case "A":
                bits += "1010"
            case "B":
                bits += "1011"
            case "C":
                bits += "1100"
            case "D":
                bits += "1101"
            case "E":
                bits += "1110"
            case "F":
                bits += "1111"
    return bits

def process(content):
    bits = hex_to_bin(content)
    (bits, packet) = parse_packet(bits)
    return sum_versions(packet)

def sum_versions(packet):
    version = packet["version"]
    if "subpackets" in packet:
        for packet in packet["subpackets"]:
            version += sum_versions(packet)
    return version

# literal
assert parse_packet("110100101111111000101000") == ('000', {
    "version": 6,
    "type": 4,
    "literal": 2021,
})

# operator with bits
assert parse_packet("00111000000000000110111101000101001010010001001000000000") == ('0000000', {
    'version': 1,
    'type': 6, 'subpackets': [
        {'version': 6, 'type': 4, 'literal': 10},
        {'version': 2, 'type': 4, 'literal': 20},
    ],
})

assert parse_packet("11101110000000001101010000001100100000100011000001100000") == ('00000', {
    'version': 7,
    'type': 3,
    'subpackets': [
        {'type': 4, 'version': 2, 'literal': 1},
        {'type': 4, 'version': 4, 'literal': 2},
        {'type': 4, 'version': 1, 'literal': 3},
    ],
})

assert process("8A004A801A8002F478") == 16
assert process("620080001611562C8802118E34") == 12
assert process("A0016C880162017C3686B18A3D4780") == 31
assert process("C0015000016115A2E0802F182340") == 23

assert process(content) == 934

print(process(content))
