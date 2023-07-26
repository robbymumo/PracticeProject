'''this program will show how to open files and read them'''
#there are different parameters to pass to the open() function to read, write, read+write and append information to the
#file.
#always make sure you have closed the file after opening.
# read_mode = open('friends.txt', 'r+') # to read and write
read_mode = open('friends.txt', 'r') # to only read from the file
# read_mode = open('friends.txt', 'a') # to append information to the file
# read_mode = open('friends.txt', 'w') #Just to write to the file
# read_mode.write('Evans - Ule msee')
# print (read_mode.writable())
# read_mode.write("Ando - Kasarani\n")
# read_mode.write("Robbie - Msanii")
print(read_mode.read())
# read_mode = open('friends.txt', 'a')

#read_mode.close()