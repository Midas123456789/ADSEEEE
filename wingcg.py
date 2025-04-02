
b = 10
cR = 2
cT = 1
AR = 0.09685*cR**2
AT = 0.09685*cT*2
cgR = 0.4066*cR
cgT = 0.4066*cT + 0.25*cR - 0.25*cT
a1 = AR
a2 = (AT-AR)/(b/2)
c1 = cgR
c2 = (cgT-cgR)/(b/2)
y = b/2
cg = (a1*c1*y+a1*c2*y**2/2+a2*c1*y**2/2+a2*c2*y**3/3)/(a1*y+a2*y**2/2)
print(cg)