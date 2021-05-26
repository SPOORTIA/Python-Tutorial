

# message is a variable ,  variable's start with lower case and if variable has two words it's usually indicated with underscore 
message = 'hello world' 
my_message = 'hi'
print (message)
print (my_message)

# count the length of a particular variable using len

message = 'hello'
# index    0 1 2 3 4
#index    -4 -3 -2 -1 0
print (len(message)) # variables can be repated as it is always overridden

print(message)
print(message[0])# index 0 is printed
print(message[3]) # index 3 is printed
print(message[0:3])
print(message[:3])
print(message[::-3])
print(message[::-2])
print(message[:-4])
print(message[-5:-2])
print(message[0:-2])
print(message[:])
print(message[0:-1:2])
print(message[-1:1:-1])
print(message[-1:0:-2])
print(message[::-1])


message = 'SPoOrtI'
          
print(message.lower())
print(message.upper())
print(message.count('o'))
print(message.find('r'))
message = message.replace('SPoOrtI','Ambekar')
print(message)

message_new = 'hello'
message_again = 'spoorti'
message = message_new + ' '+message_again
print(message)



