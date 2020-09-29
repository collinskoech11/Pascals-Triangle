def printPascal(n):
    for line in range(1, n + 1):
        C = 1; #represents first line 
        for i in range(1, line+1):
            print(C, end = " ");
            C = int(C * (line-1)/i);
        print("");

n = 5;
printPascal(n);