#Q5. Write Program - A train 340 m long is running at a speed of 45 km/hr. what time will it take to cross a 160 m long tunnel?

#a 160 m long tunnel
tunnel_length=160
# A train 340 m long
train_length=340
#at a speed of 45 km/hr
s=45

#Now we have to calculate speed distance and time
speed=45000/3600
distance=340+160
time=distance/speed
print("Time required to cross a tunnel is ",time)
