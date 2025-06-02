count = int(input())for i in range(1, count*2):   
  
if i< count+1:
  blink=" "* (count-i)
  star= "*" * (2*i-1)
  print(blink+star)
else:
  blink =" "*(i-count)
  star ="*" *(2*count-1 -2*(i-count))
  print(blink+star)
