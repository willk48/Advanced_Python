def to_power(n):
    def power_n(m):
        return n**m
    return power_n

#this framework allows me to set up a variety of functions in this form that are distinct
power2=to_power(2)
power4=to_power(4)
power10=to_power(10)

print("expected: 4, actual: "+str(power2(2)))
print("expected: 8, actual: "+str(power2(3)))
print("expected: 16, actual: "+str(power2(4)))
print("expected: 16, actual: "+str(power4(2)))
print("expected: 64, actual: "+str(power4(3)))
print("expected: 256, actual: "+str(power4(4)))
print("expected: 100, actual: "+str(power10(2)))