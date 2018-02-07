x = 0
y = 0
calculator = "l"
calcvalue = "Y"
print ("PYTHON SIMPLE CALCULATOR")
while calcvalue == "Y":
  while calculator.lower() == "l":
    print ("[=] Please choose an option: [=]")
    print ("(Type 'L' to see a list of options)")
    calculator = input ("[Calculator] > ")
    if calculator == "l":
      print ("Calculator Commands:")
      print ("[A] Add 2 numbers (Can be x or y)")
      print ("[S] Subtract 2 numbers (Can be x or y)")
      print ("[T] Multiply 2 numbers (Can be x or y)")
      print ("[D] Divide 2 numbers (Can be x or y)")
      print ("[SX] Set value of x")
      print ("[SY] Set value of y")
      input ("")
  if calculator.lower() == "a":
    fn = input ("Enter in the first number! (Can be x or y)\n[Calculator] > ")
    sn = input ("Enter in the second number! (Can be x or y)\n[Calculator] > ")
    if fn.lower() == "x" or fn.lower() == "y":
      if fn.lower() == "x":
        fn = x
      else:
        fn = y
    if sn.lower() == "x" or sn.lower() == "y":
      if sn.lower() == "x":
        sn = x
      else:
        sn = y
    answer = float(fn) + float(sn)
    print ("[Result] > " + str(answer) + "\n")
    calculator = "l"
  if calculator.lower() == "s":
    fn = input ("Enter in the first number! (Can be x or y)\n[Calculator] > ")
    sn = input ("Enter in the second number! (Can be x or y)\n[Calculator] > ")
    if fn.lower() == "x" or fn.lower() == "y":
      if fn.lower() == "x":
        fn = x
      else:
        fn = y
    if sn.lower() == "x" or sn.lower() == "y":
      if sn.lower() == "x":
        sn = x
      else:
        sn = y
    answer = float(fn) - float(sn)
    print ("[Result] > " + str(answer) + "\n")
    calculator = "l"
  if calculator.lower() == "t":
    fn = input ("Enter in the first number! (Can be x or y)\n[Calculator] > ")
    sn = input ("Enter in the second number! (Can be x or y)\n[Calculator] > ")
    if fn.lower() == "x" or fn.lower() == "y":
      if fn.lower() == "x":
        fn = x
      else:
        fn = y
    if sn.lower() == "x" or sn.lower() == "y":
      if sn.lower() == "x":
        sn = x
      else:
        sn = y
    answer = float(fn) * float(sn)
    print ("[Result] > " + str(answer) + "\n")
    calculator = "l"
  if calculator.lower() == "d":
    fn = input ("Enter in the first number! (Can be x or y)\n[Calculator] > ")
    sn = input ("Enter in the second number! (Can be x or y)\n[Calculator] > ")
    if fn.lower() == "x" or fn.lower() == "y":
      if fn.lower() == "x":
        fn = x
      else:
        fn = y
    if sn.lower() == "x" or sn.lower() == "y":
      if sn.lower() == "x":
        sn = x
      else:
        sn = y
    answer = float(fn) / float(sn)
    print ("[Result] > " + str(answer) + "\n")
    calculator = "l"
  if calculator.lower() == "sx":
    setvalue = input ("Enter in the value of X:\n[Calculator] > ")
    if setvalue.lower() == "x" or setvalue.lower() == "y":
      if setvalue.lower() == "x":
        print ("Error Code c01: Value entered is the same as existing value. Returning to main menu!")
      else:
        x = y
    else:
      x = float(setvalue)
    print ("[Value Set] > The value of X has been set to " + str(setvalue) + "\n")
    calculator = "l"
  if calculator.lower() == "sy":
    setvalue = input ("Enter in the value of Y:\n[Calculator] > ")
    if setvalue.lower() == "x" or setvalue.lower() == "y":
      if setvalue.lower() == "y":
        print ("Error Code c01: Value entered is the same as existing value. Returning to main menu!")
      else:
        y = x
    else:
      y = float(setvalue)
    print ("[Value Set] > The value of Y has been set to " + str(setvalue) + "\n")
    calculator = "l"
