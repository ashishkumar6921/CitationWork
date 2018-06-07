ip = input('Enter the file name: ')

txt=[]
print ('Reading', ip, '...')
with open(ip, encoding="utf8") as f:
    for line in f:
        txt.append(line)
    
    #txt=f.read().split('#')
    


dict={}
for item in txt:
    if item.startswith('#index'):
        dict.update({item[6:14]:-1})
#print(dict)
for item in dict.keys():
    for a in txt:
        if item in a:
            dict[item]=dict[item]+1
#print(dict)
f.close()            
'''fout=open("Citation_Output",'w')'''
file=input("Name the output file:")
fout=open("{}.csv".format(file),'w')
for item in dict.keys():
    fout.write("{} : {}\r\n".format(item,dict[item]))

fout.close()
