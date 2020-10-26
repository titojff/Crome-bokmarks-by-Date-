#!/usr/bin/env python3

from datetime import datetime




#open files
path="/home/titojff/Desktop/"
bokmarks_file = open(path+"b",'r')
end_file = open(path+"end.csv",'a')
bt=bokmarks_file.read()

lenBT=len(bt)
lenIndex=0

while True:
    
    #read url
    index=bt.find("HREF",lenIndex)+6
    if index==-1:
        break
    indexE=bt.find("ADD_DATE", index)-2
    url=(bt[index:indexE])
    #read unix timestamp
    indax=bt.find("ADD_DATE", indexE)+10
    indaxE=bt.find('"', indax)
    Udata=bt[indax:indaxE]
    timestamp=str(datetime.fromtimestamp(int(Udata)))
    #to DO >>  icon
    #
    #
    #
    
    print(url ,timestamp)
    #write to file one bookmarm+data + icon...
    oneline=url+"ç"+timestamp+"\n"
    end_file.write(oneline)
    lenIndex=indaxE
    
    
end_file.close()    
