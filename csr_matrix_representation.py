#Ben Schreyer 3/7/2021, Write into a csr matrix
def csr_write(row,col,val,csr_col, csr_val, csr_rowC):
  if val == 0:
    return

  

  insert_index = csr_rowC[row + 1]

  for i in range(csr_rowC[row],csr_rowC[row + 1]):
    if csr_col[i] == col:
      csr_val[i] = val
      return
    if csr_col[i] > col:
      insert_index = i
      break
    
  for i in range(row+1,len(csr_rowC)):
    csr_rowC[i] += 1
    

  csr_val.insert(insert_index,val)
  csr_col.insert(insert_index,col)




matrix = [[10,20,0,0,0,0],[0,30,0,40,0,0],[0,0,50,60,70,0],[0,0,0,0,0,80]] #access [ROW][COLUMN]
csr_columns = []
csr_rowCounts = [0,0,0,0,0]
csr_values = []

for i in range(4):
  for j in range(6):
    csr_write(i,j,matrix[i][j],csr_columns,csr_values,csr_rowCounts)
print(csr_values)
print(csr_columns)
print(csr_rowCounts)
print("INSERTION")
csr_write(0,2,-3,csr_columns,csr_values,csr_rowCounts)
print(csr_values)
print(csr_columns)
print(csr_rowCounts)
