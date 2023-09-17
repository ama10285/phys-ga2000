from numpy import*
actual_num = 100.98763
float_num = float32(100.98763)
float_int32bits = float_num.view(int32) 
diff = float_num - actual_num
print("32-bit representation:",'{:032b}'.format(float_int32bits))
print("Difference between actual number and 32-bit floating-point representation:", diff)