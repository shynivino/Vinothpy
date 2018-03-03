import random
def main():
    a=[[0 for i in range(3)] for j in range(3)]
    for i in range(3):
        for j in range(3):
            a[i][j]=random.randrange(1,10)

    b=[[0 for i in range(3)] for j in range(3)]
    for i in range(3):
        for j in range(3):
            b[i][j]=random.randrange(1,6)
    print "Matrix A"
    for i in a:
        print i,"\n"

    print "Matrix B"
    for i in b:
        print i,"\n"

    c=[[0 for i in range(3)] for j in range(3)]
    print "sum of Matrix"
    for i in range(3):
        for j in range(3):
            c[i][j]=a[i][j]+b[i][j]

    for i in c:
        print i,"\n"

    print "Transpose of A:"
    d=[[0 for i in range(3)] for j in range(3)]
    for i in range(3):
        for j in range(3):
            d[i][j]=a[j][i]
    for i in d:
        print i,"\n"
    e=[[0 for i in range(3)] for j in range(3)]
    print "Matrix A * Matrix B:"
    for i in range(3):
        for j in range(3):
            for k in range(3):
                e[i][j]+=a[i][k]*b[k][j]


    for i in e:
        print i,"\n"   
if __name__=='__main__':
    main()
