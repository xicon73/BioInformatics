def readFasta(file):
    id = ""
    Seq = ""
    f=open(file,"r")
    for line in f:
        if line.startswith(">"):
            id=line[1:]
        else: Seq+=line
    f.close()
    return(id,Seq)


def generateRandonSeq2():
    
