# Write your code here :-)
#this method automatically closes the file for you
with open('no_name_02.txt','w') as f:
    txt = 'Line 1\n'
    f.write(txt)
    txt = 'Line 2\n'
    f.write(txt)

with open('no_name_02.txt','r') as g:
    rx_txt_list = g.readlines()
print(rx_txt_list)

print('End of line. \n')
