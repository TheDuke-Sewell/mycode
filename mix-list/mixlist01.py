#!/user/bin/env python3

my_list = ["192.168.0.5", 5060, "UP"]

#print the first item in the list
print("The first item in the list (IP): " + my_list[0])

#print the 2nd item in the list
print("The second item in the list (port): " + str(my_list[1]) )


#print the 3rd item in the list
print("The last item in the list (state): " + my_list[2] )

iplist = [5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh"]

#need to add more notes
print("IP address " + iplist[3] + " and " + iplist[4])
#add notes here also like what is f doing
print(f"IP address: {iplist[3]} and {iplist[4]}")
