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




matrix = [[5,0,0,0],[0,8,0,0],[0,0,3,0],[0,6,0,0]] #access [ROW][COLUMN]
csr_columns = []
csr_rowCounts = [0,0,0,0,0]
csr_values = []

for i in range(4):
  for j in range(4):
    csr_write(i,j,matrix[i][j],csr_columns,csr_values,csr_rowCounts)
print(csr_values)
print(csr_columns)
print(csr_rowCounts)
