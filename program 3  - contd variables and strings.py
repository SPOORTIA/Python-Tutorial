# concatination of strings

message_1 = 'hello'
message_2 = 'hi'

message = message_1 + ' ' + message_2 + 'monkey'
print(message)

# f - formating

message = f'{message_1} {message_2}'
print(message)


message = f'{message_1} {message_2.upper()}'
print(message)

# dir - displays all the fuctions / attributes that are avaliable 

print(dir(message))

# help fuction for string
print(help(str))

print(help(str.lower))

# integers and numbers

num = 3

print(type(num)) # prints the data type of num

mum = 3.12
print(type(num))
print(3+2)
print(3-2)
print(3*2)
print(3/2)
print(3//2)# drops decimal
print(3**2) # exponent
print(3%2) # modules
print(3+2*1)
print(3+(2+1))# order of operations


# incrementation
num = 2
num = num + 1
print(num)

num =  4
num += 2
num *= 10
num -= 2
print(num)

# build in numeric funtiions
num = -3
print(abs(-3))
num =  3.97
print(round(num))
print(round(num,1))


# numeric comparisons

num_1 = 3
num_2 = 4
print(num_1==num_2)
print(num_1!=num_2)
print(num_1>num_2)
print(num_1>=num_2)
print(num_1<num_2)
print(num_1<=num_2)

# type casting
num_1 = '5'
num_2 = '2'
print(num_1+num_2)


num_1 = int(num_1)
num_2 = int(num_2)
print(num_1+num_2)

num_1 = 5
num_2 = 2
print(num_1+num_2)

num_1 = str(num_1)
num_2 = str(num_2)
print(num_1+num_2)







