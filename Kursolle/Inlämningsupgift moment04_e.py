def omkrets(s1, s2):
    o = s1 + s2 + s1 +s2
    return o

def area(s1, s2):
    a = s1 * s2
    return a

def volym(s1, s2, s3):
    v = s1 * s2 * s3
    return v

s1 = int(input("Vad är värdet på sida 1?"))
s2 = int(input("Vad är värdet på sida 2?"))
s3 = int(input("Vad är värdet på sida 3?"))

print(omkrets(s1, s2))
print(area(s1, s2))
print(volym(s1, s2, s3))
