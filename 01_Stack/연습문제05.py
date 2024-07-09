def printReverse(msg, len):
  if len == 0:
    return
  else:
    print(msg[len-1], end ='')
    printReverse(msg, len-1)

instr = "hello"
printReverse(instr, len(instr))