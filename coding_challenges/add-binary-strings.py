"""
hackerrank challenge #67 Add Binary Strings
"""
def addBinary(a: str, b: str) -> str:
    carry=0
    a=a[len(a)::-1]
    b=b[len(b)::-1]
    res,end = (list(a),len(b)) if len(a)>len(b) else (list(b),len(a))
    i=0
    while i < end:
        sum=int(a[i])+int(b[i])+carry
        carry= 1 if sum>1 else 0
        res[i]=str(sum % 2)
        i+=1
    while i < len(res) and carry==1:
        sum=int(res[i])+carry
        res[i]=str(sum % 2)
        carry= 1 if sum>1 else 0
        i+=1
    if carry==1:
        res.append('1')
    return ''.join(res[len(res)::-1])
