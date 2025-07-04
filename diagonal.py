def diagonalDifference(arr):
    filasColumnas=len(arr)
    diagonal1=[]
    diagonal2=[]
    reversa=1
    total=0
    for i in range(0,filasColumnas):
        diagonal1.append(arr[i][i])
        diagonal2.append(arr[i][-reversa])
        reversa+=1
    diagonal1=sum(diagonal1)
    diagonal2=sum(diagonal2)
    total= abs(diagonal1-diagonal2)
    return(total)