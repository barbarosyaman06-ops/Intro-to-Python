x=5
x&=3
print(x) # Output: 1
# Bitwise AND assignment multiplies the bit level 5 and 3 and returns the result of bitwise result.

y=7
y |=12
print(y) # Output: 15
# Bitwise OR assignment combines the bit level 7 and 12 and returns the result of bitwise result.

k=10
k ^= 3
print(k) # Output: 9
# Bitwise XOR assignment compares the bit level 10 and 3 and returns the result of bitwise result.

L=16
L >>= 2
print(L) # Output: 4
# Bitwise right shift assignment shifts the bits of 16 to the right by 2 positions and returns the result.
# actually divides the number by 2 raised to the power of 2 (2^2 = 4), so 16 / 4 = 4.


M=16
M <<=4
print(M) # Output: 256
# Bitwise left shift assignment shifts the bits of 16 to the left by 4 positions
# actually multiplies the number by 2 raised to the power of 4 (2^4 = 16), so 16 * 16 = 256.

S=5
print(S:=3) # Output: 3
#The walrus operator reassigns a value to corresponding variable.