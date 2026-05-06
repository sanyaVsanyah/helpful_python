int(123.45)
int('123')
int('   -12_345\n')
int('FACE', 16)
int('0xface', 0)
int('01110011', base=2)

#пустышки
x = 1
x.__int__()
x.__index__()

bin(x)
x.bit_length() #Return the number of bits necessary to represent an integer in binary, excluding the sign and leading zeros

x.is_integer() #???

