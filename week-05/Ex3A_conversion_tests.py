# Description: This script tests various numeric
#              conversion techniques
# Author: Netsanet Aweke

a = " 101.1 "
b = '55'
c = "402 Stevens"
d = 'Number 5 '

print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))

#int_a = int(a)
# int_a = int(a) # ValuesError: a decimalstring cannot convert directly to int

float_a = float(a)
print(float_a, type(float_a))
# float() can convert the decimal text in a to a float.

int_b = int(b)
print(int_b, type(int_b))

# int_c = int(c) # ValueError: c contains text, so it cannot convert to int
# print(int_c, type(int_c))

# int_d = int(d) # ValueError: dcontains text so cannot convert to int
# print(int_d, type(int_d))

#float_d = float(d) # ValueError: d contains text, so it cannot convert to float
#print(float_d, type(float_d))

float_b = float(b) 
print(float_b, type(float_b))

# float_c = float(c) # ValueError: c contains text, so it cannot convert to float
# print(float_c, type(float_c))

int_float_a = int(float(a))
print(int_float_a, type(int_float_a))

a_number_text = a[1:6]
print(a_number_text, type(a_number_text))

a_number = float(a_number_text)
print(a_number, type(a_number))

b_number_text = b[0:2]
print(b_number_text, type(b_number_text))

b_number = int(b_number_text)
print(b_number,  type(b_number))

c_number_text = c[0:3]
print(c_number_text, type(c_number_text))

c_number = int(c_number_text)
print(c_number, type(c_number))

d_number_text =d[7]
print(d_number_text, type(d_number_text))

d_number = int(d_number_text)
print(d_number, type(d_number))

print(a.strip())
print(b.strip())
print(d.strip())

















