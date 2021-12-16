from functools import reduce

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

def eval(packet):
    if "literal" in packet:
        return packet["literal"]
    values = [eval(subpacket) for subpacket in packet["subpackets"]]
    match packet["type"]:
        case 0:
            return sum(values)
        case 1:
            return reduce(lambda a, b: a*b, values)
        case 2:
            return min(values)
        case 3:
            return max(values)
        case 4:
            return packet["literal"]
        case 5:
            return values[0] > values[1] if 1 else 0
        case 6:
            return values[0] < values[1] if 1 else 0
        case 7:
            return values[0] == values[1] if 1 else 0

def process(content):
    bits = hex_to_bin(content)
    (bits, packet) = parse_packet(bits)
    return eval(packet)

assert process("C200B40A82") == 3
assert process("04005AC33890") == 54
assert process("880086C3E88112") == 7
assert process("CE00C43D881120") == 9
assert process("D8005AC2A8F0") == 1
assert process("F600BC2D8F") == 0
assert process("9C005AC2F8F0") == 0
assert process("9C0141080250320F1802104A08") == 1

assert process(content) == 912901337844

print(process(content))
