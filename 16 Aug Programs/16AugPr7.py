#Write programm to calculate monthly simple intrest and compound intrest(5%/Month) on amount - 161258/-

#Simple INterest
p=161258
r=5
t=1

si=p*r*t*0.01

print("Simple Interest : ",si)

#Compound Interest

Amount = p * (pow((1 + r / 100), t))
ci = Amount - p 
print("Compound interest is", ci)