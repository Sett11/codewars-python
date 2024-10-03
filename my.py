from base64 import b64encode

def hex_to_base64(s):
	return ''.join(map(chr,b64encode(bytearray.fromhex(s))))

print(hex_to_base64('e1b6a959d88a3701c6a51ccbd0'))
print(hex_to_base64('49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'))