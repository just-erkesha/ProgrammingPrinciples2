n=int(input())#number of matrix
arr=[[0]*n]*n#create two dimen. array with "0" values and with n rows and columns
for i in range(n):
    for j in range(n):
        if(i==j):#if number of rows and columns are equal// if it is diagonal
            arr[i][j]=i*j#write multiplication of row and column
        elif(i==0 or j==0):#if it is the first row(top) OR first column(left) 
            arr[i][j]=i+j#fill out the borders of multiplication table
for i in range(n):
    for j in range(n):
        print(arr[i][j],end=' ')# output each element with space at tyhe end
    print()#next row should be started with the new line