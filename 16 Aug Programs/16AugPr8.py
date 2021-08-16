#Write program to generate equated monthly instalments (EMI)(intrest 5%/Month) of 3 year and 5 year of amount 161258/-
emi=161258
emi3=emi/(12*3)
emi5=emi/(12*5)
#print("\n Emi after 3 year without interest",emi3)
#print("\n Emi after 5 years",emi5)
emin3=emi3+((5/100)*emi3)
emin5=emi5+((5/100)*emi5)
print("\n Emi after 3 year with interest",emin3)
print("\n Emi after 5 years with interest",emin5)