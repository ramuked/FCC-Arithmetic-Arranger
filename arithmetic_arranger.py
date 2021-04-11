import re


def arithmetic_arranger(problems,solve=False):

  if(len(problems)>5):
    return "Error: Too many problems."

  l1=""
  l2=""
  lines=""
  sumx = ""
  string = " "

  for task in problems:
    if re.search("[/]",task) or re.search("[*]",task):
      return "Error: Operator must be '+' or '-'."
    if re.search("[^\s0-9.+-]",task):
      return "Error: Numbers must only contain digits."
    
    num1=task.split(" ")[0];
    op=task.split(" ")[1]
    num2=task.split(" ")[2]
    
    if(len(num1)>4 or len(num2)>4):
      return "Error: Numbers cannot be more than four digits."
    
    sum = ""
    if(op == "+"):
      sum=str(int(num1)+int(num2))
    else:
      sum=str(int(num1)-int(num2))
    
    length=max(len(num1),len(num2))+2
    top=str(num1).rjust(length)
    bottom=op+ str(num2).rjust(length-1)

    line=""
    res=str(sum).rjust(length)
    for s in range(length):
      line+="-"
    
    if(task!=problems[-1]):
      l1+=top+"    "
      l2+=bottom + "    "
      lines+=line+"    "
      sumx+=res+"    "
    else:
      l1+=top
      l2+=bottom
      lines+=line
      sumx+=res
    
  if solve:
    string = l1+'\n'+l2+'\n'+lines+'\n'+sumx
  else:
    string = l1+'\n'+l2+'\n'+lines
  
  return string 

      









    

      
   