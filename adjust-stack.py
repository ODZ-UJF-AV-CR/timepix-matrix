#!/opt/local/bin/python
import sys
import struct
import array

# Alters the mode in 256x256 byte matrix of binary pixel configuration file of a Timepix detector 
#
# Assuming the mode in the input file is 0 (Medipix),
# this modifies first two bits of the elements of the matrix to either 01 (ToT mode) or 11 (Timepix) 
# You'll likely need to modify the shift array to suit your application.
#
# Syntax: $0 <source >output
#
# Source: BPC file saved from Pixet Pro - with Medipix mode set for all pixels and threshold values
#         specific for the particular detector.
# 
# Authors: Vaclav Stepan, stepan@ujf.cas.cz, Marek Sommer, sommer@ujf.cas.cz

def load_binary():
    file = sys.stdin.read()
    array = struct.unpack("<131072B", file)
    return array


def print_matrix(array):
	# Print top left 10x10 of elements as binary
	for row in range(0,10):
		for column in range(0,10):
	    		sys.stderr.write('{0:08b}'.format(int(array[256*row+column])))
	    		sys.stderr.write(' ')
		sys.stderr.write('\n')
	sys.stderr.write('...\n')

def shift_array(array):
	# shift first two bits of the array from Medipix (00) to ToT or Timepix modes
	newarray = []
	for row in range(0,512):
		for column in range(0,256):
			# Set first two bits in matrix to set the modes
			# Since they are 00 now, this sets them accordingly
			if ((row % 5) == 0) and ((column % 5) == 0):
				pad = 0
				#pad = 192
			else:
				pad = -192+64
				#pad = 64
			newarray.append(pad+int(array[256*row+column]))
	return newarray

def print_bytes(array):
	# Print the array to stdout
	for row in range(0,512):
		for column in range(0,256):
			sys.stdout.write(chr(int(array[256*row+column])))

data = load_binary()
sys.stderr.write('Original:\n')
print_matrix(data)
data = shift_array(data)
sys.stderr.write('After modification:\n')
print_matrix(data)
print_bytes(data)
