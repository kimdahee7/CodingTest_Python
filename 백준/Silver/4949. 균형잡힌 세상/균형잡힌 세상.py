def main(): 
  while True:
    s= input()
    if s == ".":
      break
    stack1 = []
    for i in s:
      if i == "(" or i == "[":
        stack1.append(i)
      if i == ")":
        if len(stack1) != 0 and stack1[len(stack1)-1] == "(":
          stack1.pop()
        else:
          stack1.append("i")
      if i == "]":
        if len(stack1) != 0 and stack1[len(stack1)-1] == "[":
          stack1.pop()
        else:
          stack1.append(i)
    if len(stack1) == 0:
      print("yes")
    else:
      print("no")
main()