from pylfsr import LFSR
import numpy as np
elements = input("please insert the factorials in your polynomial excluding the constant:  ")
constant = input("please insert the constant:  ")
polynom = ""
real_polynom =  []
real_constant = int(constant)

for i in elements:
    if i != " ":
        polynom = polynom + "x^{} +".format(i)
        real_polynom.append(int(i))

if constant == "1":
    polynom = polynom + "{}".format(constant)
    real_polynom.append(int(constant))
else:
    constant = input("please insert the constant:  ")

real_polynom.sort(reverse=True)
period = pow(2, real_polynom[0])-1
number_of_ones = (pow(2, real_polynom[0])/2)
number_of_zeros = number_of_ones - 1

seq_input = input("please insert the starting sequence containing {} binary digits:  ".format(real_polynom[0]))
seq = [int(i) for i in seq_input]

modulo_exp = real_polynom[1:]
temp = []
i = 0
while i < period:
    temp.append(seq[modulo_exp[0]]%seq[modulo_exp[1]])
    for j in range(1, modulo_exp[0]):
        temp.append(seq[j])
    period = period - 1


print(temp)

"""
print("your polynominal is: {} ".format(polynom))

print("the period is {}".format(period))

print("there are {} ones and {} zeros in your sequences".format(number_of_ones, number_of_zeros))

print("Output: ")

converted = []

for i in range(0, period):
    converted.append(register.next())
    if converted[i] == 0:
        converted[i] = -1
    else:
        converted[i] = 1

"""





