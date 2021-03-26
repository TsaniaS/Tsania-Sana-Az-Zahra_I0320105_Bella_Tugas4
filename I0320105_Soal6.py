# SOAL 6

a = 4
b = 11
print('nilai :', a,' , binary :', format(a,'08b'))
print('nilai :', b,' , binary :', format(b,'08b'))

# a. 4 | 11 (bitwise OR)
c = a | b
print('Keluaran dari operator bitwise 4 | 11 ')
print('nilai :',c,' ,binary :', format(c,'08b'))

# b. 4 >> 11 (bitwise shift right)
c = a >> b
print('Keluaran dari operator bitwise 4 >> 11 ')
print('nilai :',c,' ,binary :', format(c,'08b'))

# c. 4 ^ 11 (bitwise XOR)
c = a ^ b
print('Keluaran dari operator bitwise 4 ^ 11 ')
print('nilai :',c,' ,binary :', format(c,'08b'))

# d. ~4 (bitwise NOT)
c = ~a
print('Keluaran dari operator bitwise ~4 ')
print('nilai :',c,' ,binary :', format(c,'08b'))

# e. 11 & 4 (bitwise AND)
c = b & a
print('Keluaran dari operator bitwise 11 & 4 ')
print('nilai :',c,' ,binary :', format(c,'08b'))