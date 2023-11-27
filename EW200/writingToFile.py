# Write your code here :-)

#write to a file


print('running writingToFile.py')
#open the file

f = open('no_name.txt','w')


#create txt to write to file

txt = 'line 1'
f.write(txt + '\n')

#write it to the file
#f.write(txt)

txt = 'line 2'

f.write(txt)

#close the file
f.close()
print('------------------------------------------------------')
#read the file
#open the file for reading
g = open('no_name.txt','r')

#read one line
#rx_txt = g.readline()
#print(rx_txt)

#rx_txt = g.readline()
#print(rx_txt)

rx_txt_list = g.readlines()
print(rx_txt_list)


g.close()


print('End of line.')
