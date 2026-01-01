def ftTom(feet):
    metre = feet / 3.281
    return metre
feet = int(input("Convert ft to m"))
metre = ftTom(feet)
print(feet,"ft is",round(metre,3),"m")