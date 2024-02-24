likelist = ['Alex']
zapyataya = str(',')
if len(likelist) == 0:
    print ('No one likes this.')
elif len(likelist) == 1:
    print (likelist[0], 'likes this.')
elif len(likelist) == 2:
    print (likelist[0].rstrip(),'and', likelist[1].strip(), 'likes this')
elif len(likelist) == 3:
    print (likelist[0].rstrip()+zapyataya.lstrip(), likelist[1].rstrip(), 'and', likelist[2].rstrip(),'likes this')
else:
    print (likelist[0].rstrip()+zapyataya.lstrip(), likelist[1].rstrip().lstrip(), 'and', (len(likelist)-2), 'many others likes this')