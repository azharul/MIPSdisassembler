"""
This project is done by S M Azharul Karim, student ID: dhf227,
for the course EE 5123-Computer architecture.

this is a MIPS disassembler. It takes one input file called fib_bin.txt
which contains binary MIPS instruction streams, and finds out the instruction
each stream holds and which memory registers it uses. 
"""
#read input file
fo=open('fib_bin.txt','r')
MIPSadd=496
output_arr=[]*1
    
i=0
b=[]
string=[]
#converts string data to binary
for line in fo:
    string.append(line)
    b.append(bin(int(string[i],2))[2:].zfill(32))
    i=i+1
    
L=len(b);
#converts binary files into decimal
def bintodec(bbb):
    num=int(bbb,2)
    return num

#contains ADDI, ADDIU, SLTI instruction
def addimmop(nn):
    op=None
    rs=None
    rt=None
    imm=None
    output=None
    binstr=None
    mipsadd=0
    immadd=0
    opcode=bintodec(nn[0:6])
    if opcode==8:
        op='ADDI'
        rs='R'+str(bintodec(nn[6:11]))
        rt='R'+str(bintodec(nn[11:16]))
        mipsadd=str(MIPSadd)
        immadd='#'+str(bintodec(nn[16:32]))
        output=mipsadd+'  '+op+'  '+rs+','+'  '+rt+','+'  '+immadd
        binstr=str(nn[0:6])+'   '+str(nn[6:11])+'   '+str(nn[11:16])+'   '+str(nn[16:21])+'   '+str(nn[21:26])+'   '+str(nn[26:32])
        output_arr.append(binstr+'   '+output)
    elif opcode==9:
        op='ADDIU'
        rs='R'+str(bintodec(nn[6:11]))
        rt='R'+str(bintodec(nn[11:16]))
        mipsadd=str(MIPSadd)
        immadd='#'+str(bintodec(nn[16:32]))
        output=mipsadd+'  '+op+'  '+rs+','+'  '+rt+','+'  '+immadd
        binstr=str(nn[0:6])+'   '+str(nn[6:11])+'   '+str(nn[11:16])+'   '+str(nn[16:21])+'   '+str(nn[21:26])+'   '+str(nn[26:32])
        output_arr.append(binstr+'   '+output)
    elif opcode==10:
        op='SLTI'
        rs='R'+str(bintodec(nn[6:11]))
        rt='R'+str(bintodec(nn[11:16]))
        mipsadd=str(MIPSadd)
        immadd='#'+str(bintodec(nn[16:32]))
        output=mipsadd+'  '+op+'  '+rs+','+'  '+rt+','+'  '+immadd
        binstr=str(nn[0:6])+'   '+str(nn[6:11])+'   '+str(nn[11:16])+'   '+str(nn[16:21])+'   '+str(nn[21:26])+'   '+str(nn[26:32])
        output_arr.append(binstr+'   '+output)
    return output_arr

#contains ADD, ADDU, SUB, SUBU instructions
def addsubop(nn):
    op=None
    rs=None
    rt=None
    imm=None
    output=None
    binstr=None
    mipsadd=0
    immadd=0
    opcode=bintodec(nn[26:32])
    if opcode==32:
        op='ADD'
        rs='R'+str(bintodec(nn[6:11]))
        rt='R'+str(bintodec(nn[11:16]))
        mipsadd=str(MIPSadd)
        immadd='#'+str(bintodec(nn[16:32]))
        output=mipsadd+'  '+op+'  '+rs+','+'  '+rt
        binstr=str(nn[0:6])+'   '+str(nn[6:11])+'   '+str(nn[11:16])+'   '+str(nn[16:21])+'   '+str(nn[21:26])+'   '+str(nn[26:32])
        output_arr.append(binstr+'   '+output)
    elif opcode==34:
        op='SUB'
        rs='R'+str(bintodec(nn[6:11]))
        rt='R'+str(bintodec(nn[11:16]))
        mipsadd=str(MIPSadd)
        immadd='#'+str(bintodec(nn[16:32]))
        output=mipsadd+'  '+op+'  '+rs+','+'  '+rt
        binstr=str(nn[0:6])+'   '+str(nn[6:11])+'   '+str(nn[11:16])+'   '+str(nn[16:21])+'   '+str(nn[21:26])+'   '+str(nn[26:32])
        output_arr.append(binstr+'   '+output)
    elif opcode==35:
        op='SUBU'
        rs='R'+str(bintodec(nn[6:11]))
        rt='R'+str(bintodec(nn[11:16]))
        mipsadd=str(MIPSadd)
        immadd='#'+str(bintodec(nn[16:32]))
        output=mipsadd+'  '+op+'  '+rs+','+'  '+rt
        binstr=str(nn[0:6])+'   '+str(nn[6:11])+'   '+str(nn[11:16])+'   '+str(nn[16:21])+'   '+str(nn[21:26])+'   '+str(nn[26:32])
        output_arr.append(binstr+'   '+output)
    if opcode==33:
        op='ADDU'
        rs='R'+str(bintodec(nn[6:11]))
        rt='R'+str(bintodec(nn[11:16]))
        mipsadd=str(MIPSadd)
        immadd='#'+str(bintodec(nn[16:32]))
        output=mipsadd+'  '+op+'  '+rs+','+'  '+rt
        binstr=str(nn[0:6])+'   '+str(nn[6:11])+'   '+str(nn[11:16])+'   '+str(nn[16:21])+'   '+str(nn[21:26])+'   '+str(nn[26:32])
        output_arr.append(binstr+'   '+output)
    return output_arr

#defines the branch instructions BEQ, BNE
def branchop(nn):
    op=None
    rs=None
    rt=None
    imm=None
    output=None
    binstr=None
    mipsadd=0
    immadd=0
    opcode=bintodec(nn[0:6])
    if opcode==4:
        op='BEQ'
        rs='R'+str(bintodec(nn[6:11]))
        rt='R'+str(bintodec(nn[11:16]))
        mipsadd=str(MIPSadd)
        immadd='#'+str(bintodec(nn[16:32]))
        output=mipsadd+'  '+op+'  '+rs+','+'  '+rt+','+'  '+immadd
        binstr=str(nn[0:6])+'   '+str(nn[6:11])+'   '+str(nn[11:16])+'   '+str(nn[16:21])+'   '+str(nn[21:26])+'   '+str(nn[26:32])
        output_arr.append(binstr+'   '+output)
    elif opcode==5:
        op='BNE'
        rs='R'+str(bintodec(nn[6:11]))
        rt='R'+str(bintodec(nn[11:16]))
        mipsadd=str(MIPSadd)
        immadd='#'+str(bintodec(nn[16:32]))
        output=mipsadd+'  '+op+'  '+rs+','+'  '+rt+','+'  '+immadd
        binstr=str(nn[0:6])+'   '+str(nn[6:11])+'   '+str(nn[11:16])+'   '+str(nn[16:21])+'   '+str(nn[21:26])+'   '+str(nn[26:32])
        output_arr.append(binstr+'   '+output)
    return output_arr

#defines the branch instructions BLEZ, BGTZ
def branchequalop(nn):
    op=None
    rs=None
    rt=None
    imm=None
    output=None
    binstr=None
    mipsadd=0
    immadd=0
    opcode=bintodec(nn[0:6])
    if opcode==6:
        op='BLEZ'
        rs='R'+str(bintodec(nn[6:11]))
        rt='R'+str(bintodec(nn[11:16]))
        mipsadd=str(MIPSadd)
        immadd='#'+str(bintodec(nn[16:32]))
        output=mipsadd+'  '+op+'  '+rs+','+'  '+rt+','+'  '+immadd
        output_arr.append(str(nn)+'   '+output)
    elif opcode==7:
        op='BGTZ'
        rs='R'+str(bintodec(nn[6:11]))
        rt='R'+str(bintodec(nn[11:16]))
        mipsadd=str(MIPSadd)
        immadd='#'+str(bintodec(nn[16:32]))
        output=mipsadd+'  '+op+'  '+rs+','+'  '+rt+','+'  '+immadd
        binstr=str(nn[0:6])+'   '+str(nn[6:11])+'   '+str(nn[11:16])+'   '+str(nn[16:21])+'   '+str(nn[21:26])+'   '+str(nn[26:32])
        output_arr.append(binstr+'   '+output)
    return output_arr

#defines the branch instructions BLTZ, BGEZ
def branchthanop():
    op=None
    rs=None
    rt=None
    imm=None
    output=None
    binstr=None
    mipsadd=0
    immadd=0
    opcode=bintodec(nn[0:6])
    if opcode==0:
        op='BLTZ'
        rs='R'+str(bintodec(nn[6:11]))
        rt='R'+str(bintodec(nn[11:16]))
        mipsadd=str(MIPSadd)
        immadd='#'+str(bintodec(nn[16:32]))
        output=mipsadd+'  '+op+'  '+rs+','+'  '+rt+','+'  '+immadd
        binstr=str(nn[0:6])+'   '+str(nn[6:11])+'   '+str(nn[11:16])+'   '+str(nn[16:21])+'   '+str(nn[21:26])+'   '+str(nn[26:32])
        output_arr.append(binstr+'   '+output)
    elif opcode==1:
        op='BGEZ'
        rs='R'+str(bintodec(nn[6:11]))
        rt='R'+str(bintodec(nn[11:16]))
        mipsadd=str(MIPSadd)
        immadd='#'+str(bintodec(nn[16:32]))
        output=mipsadd+'  '+op+'  '+rs+','+'  '+rt+','+'  '+immadd
        binstr=str(nn[0:6])+'   '+str(nn[6:11])+'   '+str(nn[11:16])+'   '+str(nn[16:21])+'   '+str(nn[21:26])+'   '+str(nn[26:32])
        output_arr.append(binstr+'   '+output)
    return output_arr

#shift instructions SLL, SRL, SRA
def shiftop(nn):
    op=None
    rs=None
    rt=None
    imm=None
    output=None
    binstr=None
    mipsadd=0
    immadd=0
    opcode=bintodec(nn[26:32])
    if opcode==0:
        op='SLL'
        rs='R'+str(bintodec(nn[6:11]))
        rt='R'+str(bintodec(nn[11:16]))
        mipsadd=str(MIPSadd)
        immadd='#'+str(bintodec(nn[16:32]))
        output=mipsadd+'  '+op+'  '+rs+','+'  '+rt
        binstr=str(nn[0:6])+'   '+str(nn[6:11])+'   '+str(nn[11:16])+'   '+str(nn[16:21])+'   '+str(nn[21:26])+'   '+str(nn[26:32])
        output_arr.append(binstr+'   '+output)
    elif opcode==2:
        op='SRL'
        rs='R'+str(bintodec(nn[6:11]))
        rt='R'+str(bintodec(nn[11:16]))
        mipsadd=str(MIPSadd)
        immadd='#'+str(bintodec(nn[16:32]))
        output=mipsadd+'  '+op+'  '+rs+','+'  '+rt
        binstr=str(nn[0:6])+'   '+str(nn[6:11])+'   '+str(nn[11:16])+'   '+str(nn[16:21])+'   '+str(nn[21:26])+'   '+str(nn[26:32])
        output_arr.append(binstr+'   '+output)
    elif opcode==3:
        op='SRA'
        rs='R'+str(bintodec(nn[6:11]))
        rt='R'+str(bintodec(nn[11:16]))
        mipsadd=str(MIPSadd)
        immadd='#'+str(bintodec(nn[16:32]))
        output=mipsadd+'  '+op+'  '+rs+','+'  '+rt
        binstr=str(nn[0:6])+'   '+str(nn[6:11])+'   '+str(nn[11:16])+'   '+str(nn[16:21])+'   '+str(nn[21:26])+'   '+str(nn[26:32])
        output_arr.append(binstr+'   '+output)
    return output_arr

#LOGIC instructions AND, OR, NOT, XOR
def logicop(nn):
    op=None
    rs=None
    rt=None
    imm=None
    output=None
    binstr=None
    mipsadd=0
    immadd=0
    opcode=bintodec(nn[26:32])
    if opcode==36:
        op='AND'
        rs='R'+str(bintodec(nn[6:11]))
        rt='R'+str(bintodec(nn[11:16]))
        mipsadd=str(MIPSadd)
        immadd='#'+str(bintodec(nn[16:32]))
        output=mipsadd+'  '+op+'  '+rs+','+'  '+rt
        binstr=str(nn[0:6])+'   '+str(nn[6:11])+'   '+str(nn[11:16])+'   '+str(nn[16:21])+'   '+str(nn[21:26])+'   '+str(nn[26:32])
        output_arr.append(binstr+'   '+output)
    elif opcode==37:
        op='OR'
        rs='R'+str(bintodec(nn[6:11]))
        rt='R'+str(bintodec(nn[11:16]))
        mipsadd=str(MIPSadd)
        immadd='#'+str(bintodec(nn[16:32]))
        output=mipsadd+'  '+op+'  '+rs+','+'  '+rt
        binstr=str(nn[0:6])+'   '+str(nn[6:11])+'   '+str(nn[11:16])+'   '+str(nn[16:21])+'   '+str(nn[21:26])+'   '+str(nn[26:32])
        output_arr.append(binstr+'   '+output)
    elif opcode==38:
        op='XOR'
        rs='R'+str(bintodec(nn[6:11]))
        rt='R'+str(bintodec(nn[11:16]))
        mipsadd=str(MIPSadd)
        immadd='#'+str(bintodec(nn[16:32]))
        output=mipsadd+'  '+op+'  '+rs+','+'  '+rt
        binstr=str(nn[0:6])+'   '+str(nn[6:11])+'   '+str(nn[11:16])+'   '+str(nn[16:21])+'   '+str(nn[21:26])+'   '+str(nn[26:32])
        output_arr.append(binstr+'   '+output)
    if opcode==39:
        op='NOR'
        rs='R'+str(bintodec(nn[6:11]))
        rt='R'+str(bintodec(nn[11:16]))
        mipsadd=str(MIPSadd)
        immadd='#'+str(bintodec(nn[16:32]))
        output=mipsadd+'  '+op+'  '+rs+','+'  '+rt
        binstr=str(nn[0:6])+'   '+str(nn[6:11])+'   '+str(nn[11:16])+'   '+str(nn[16:21])+'   '+str(nn[21:26])+'   '+str(nn[26:32])
        output_arr.append(binstr+'   '+output)
    return output_arr

# SLT INSTRUCTION
def setop(nn):
    op=None
    rs=None
    rt=None
    imm=None
    output=None
    binstr=None
    mipsadd=0
    immadd=0
    opcode=bintodec(nn[26:32])
    if opcode==42:
        op='SLT'
        rs='R'+str(bintodec(nn[6:11]))
        rt='R'+str(bintodec(nn[11:16]))
        mipsadd=str(MIPSadd)
        immadd='#'+str(bintodec(nn[16:32]))
        output=mipsadd+'  '+op+'  '+rs+','+'  '+rt
        binstr=str(nn[0:6])+'   '+str(nn[6:11])+'   '+str(nn[11:16])+'   '+str(nn[16:21])+'   '+str(nn[21:26])+'   '+str(nn[26:32])
        output_arr.append(binstr+'   '+output)
    return output_arr
# SW & LW instructions
def ldstop(nn):
    op=None
    rs=None
    rt=None
    imm=None
    output=None
    binstr=None
    mipsadd=0
    immadd=0
    opcode=bintodec(nn[0:6])
    if opcode==35:
        op='LW'
        rs='R'+str(bintodec(nn[6:11]))
        rt='R'+str(bintodec(nn[11:16]))
        mipsadd=str(MIPSadd)
        immadd=str(bintodec(nn[16:32]))
        output=mipsadd+'  '+op+'  '+rt+','+'  '+immadd+'('+rs+')'
        binstr=str(nn[0:6])+'   '+str(nn[6:11])+'   '+str(nn[11:16])+'   '+str(nn[16:21])+'   '+str(nn[21:26])+'   '+str(nn[26:32])
        output_arr.append(binstr+'   '+output)
    elif opcode==43:
        op='SW'
        rs='R'+str(bintodec(nn[6:11]))
        rt='R'+str(bintodec(nn[11:16]))
        mipsadd=str(MIPSadd)
        immadd=str(bintodec(nn[16:32]))
        output=mipsadd+'  '+op+'  '+rt+','+'  '+immadd+'('+rs+')'
        binstr=str(nn[0:6])+'   '+str(nn[6:11])+'   '+str(nn[11:16])+'   '+str(nn[16:21])+'   '+str(nn[21:26])+'   '+str(nn[26:32])
        output_arr.append(binstr+'   '+output)
        print output
    return output_arr
# BREAK & NOP instruction
def exceptionop(nn):
    op=None
    rs=None
    rt=None
    imm=None
    output=None
    binstr=None
    mipsadd=0
    immadd=0
    opcode=bintodec(nn[26:32])
    if opcode==13:
        op='BREAK'
        rs='R'+str(bintodec(nn[6:11]))
        rt='R'+str(bintodec(nn[11:16]))
        mipsadd=str(MIPSadd)
        immadd='#'+str(bintodec(nn[16:32]))
        output=mipsadd+'  '+op
        binstr=str(nn[0:6])+'   '+str(nn[6:11])+'   '+str(nn[11:16])+'   '+str(nn[16:21])+'   '+str(nn[21:26])+'   '+str(nn[26:32])
        output_arr.append(binstr+'   '+output)
    elif opcode==0:
        op='NOP'
        rs='R'+str(bintodec(nn[6:11]))
        rt='R'+str(bintodec(nn[11:16]))
        mipsadd=str(MIPSadd)
        immadd='#'+str(bintodec(nn[16:32]))
        output=mipsadd+'  '+op
        binstr=str(nn[0:6])+'   '+str(nn[6:11])+'   '+str(nn[11:16])+'   '+str(nn[16:21])+'   '+str(nn[21:26])+'   '+str(nn[26:32])
        output_arr.append(binstr+'   '+output)
    return output_arr
#jump instructions J
def jumpop(nn):
    p=None
    rs=None
    rt=None
    imm=None
    output=None
    binstr=None
    mipsadd=0
    immadd=0
    opcode=bintodec(nn[0:6])
    if opcode==2:
        op='J'
        rs='R'+str(bintodec(nn[6:11]))
        rt='R'+str(bintodec(nn[11:16]))
        mipsadd=str(MIPSadd)
        immadd='#'+str(bintodec(nn[16:32]))
        output=mipsadd+'  '+op+'   '+immadd
        binstr=str(nn[0:6])+'   '+str(nn[6:11])+'   '+str(nn[11:16])+'   '+str(nn[16:21])+'   '+str(nn[21:26])+'   '+str(nn[26:32])
        output_arr.append(binstr+'   '+output)
    return output_arr

#jump instructions JR
def jumpregop(nn):
    p=None
    rs=None
    rt=None
    imm=None
    output=None
    binstr=None
    mipsadd=0
    immadd=0
    opcode=bintodec(nn[0:6])
    if opcode==8:
        op='JR'
        rs='R'+str(bintodec(nn[6:11]))
        rt='R'+str(bintodec(nn[11:16]))
        mipsadd=str(MIPSadd)
        immadd='#'+str(bintodec(nn[16:32]))
        output=mipsadd+'  '+op+'   '+immadd
        binstr=str(nn[0:6])+'   '+str(nn[6:11])+'   '+str(nn[11:16])+'   '+str(nn[16:21])+'   '+str(nn[21:26])+'   '+str(nn[26:32])
        output_arr.append(binstr+'   '+output)
    return output_arr


#convert every string to decimal after getting BREAK
def twocomp(n):
    num=0
    if int(n[0],2)==0:
        for i in range(len(n)):
            p=int(n[i],2)
            num+=p*(2**(len(n)-i-1))
    else:
        for i in range(len(n)):
            if int(n[i],2)==1:
                p=0
                num+=p*(2**(len(n)-i-1))
            else:
                p=1
                num+=p*(2**(len(n)-i-1))
        num=-1*(num+1)
    return num

def dec_convop(nn):
    binstr=None
    mipsadd=str(MIPSadd)
    decim=str(twocomp(nn[0:32]))
    output=mipsadd+'  '+decim
    binstr=str(nn)
    output_arr.append(binstr+'   '+output)

#assigning every data stream to their respective instructions
#and creating output, putting it all together
output=open('output.txt','w')
endlist=False
ii=0;

for i in range(L):  
    temp=b[i]
    print temp
    if bintodec(temp[0:6])==(8 or 9 or 10):
        addimmop(temp)    
    elif bintodec(temp[0:6])==(4 or 5):
        branchop(temp)
    elif bintodec(temp[0:6])==(35 or 43):
        ldstop(temp)
    elif bintodec(temp[0:26])==0: 
        exceptionop(temp)
        if bintodec(temp[26:32])==13:
            endlist=True
            ii=i
            break
    elif bintodec(temp[0:6])== 2:
        jumpop(temp)
    elif bintodec(temp[0:6])== 8:
        jumpregop(temp)
    elif bintodec(temp[0:6])==(6 or 7):
        brancheqaulop(temp)
    elif bintodec(temp[0:6])==(0 or 1):
        branchthanop(temp)
    elif bintodec(temp[0:6])==0 and bintodec(temp[26:32])==(0 or 2 or 3):
        shiftop(temp)
    elif bintodec(temp[0:6])==0 and bintodec(temp[26:32])==(36 or 37 or 38 or 39): 
        logicop(temp)
    elif bintodec(temp[0:6])==0 and bintodec(temp[26:32])==42: 
        setop(temp)
    elif bintodec(temp[0:6])==0 and bintodec(temp[26:32])==(32 or 33 or 34 or 35): 
        addsubop(temp)
    
    MIPSadd =MIPSadd+4


if endlist==True:
    for i in range(ii+1, L):
        MIPSadd+=4
        temp=str(b[i])
        print MIPSadd
        dec_convop(temp)
        

output.write('\n'.join(output_arr))
output.close()
