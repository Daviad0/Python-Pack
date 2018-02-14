x = ""
y = ""
xory = False
calculator = "l"
calcvalue = "Y"
mmode = "T"
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
      print ("[PX] Show value of x")
      print ("[PY] Show value of y")
      print ("[M] Go into saved value mode")
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
    while xory == False:
      setvalue = input ("Enter in the value of X:\n[Calculator] > ")
      if setvalue == "":
        xory = False
        print ("Error Code c02: The variable has to have a value.")
      else:
        xory = True
      if setvalue.lower() == "x" or setvalue.lower() == "y":
        if setvalue.lower() == "x":
          print ("Error Code c01: Value entered is the same as existing value. Returning to main menu!")
        else:
          x = y
      else:
        if xory == True:
          x = float(setvalue)
      if xory == True:
        print ("[Value Set] > The value of X has been set to " + str(setvalue) + "\n")
        calculator = "l"
  if calculator.lower() == "sy":
while xory == False:
      setvalue = input ("Enter in the value of Y:\n[Calculator] > ")
      if setvalue == "":
        xory = False
        print ("Error Code c02: The variable has to have a value.")
      else:
        xory = True
      if setvalue.lower() == "x" or setvalue.lower() == "y":
        if setvalue.lower() == "y":
          print ("Error Code c01: Value entered is the same as existing value. Returning to main menu!")
        else:
          y = x
      else:
        if xory == True:
          y = float(setvalue)
      if xory == True:
        print ("[Value Set] > The value of Y has been set to " + str(setvalue) + "\n")
        calculator = "l"
  if calculator.lower() == "m":
    while mmode == "Y":
      mc = "l"
      m = 0
      while mc == "l":
        print ("< Saved Value Mode >")
        print ("Please choose an option (Type L to list options)")
        mc = input ("[MMode] > ")
        if mc == "l":
          print ("MMode Commands:")
          print ("[A] Add a value to the total")
          print ("[S] Subtract a value from the total")
          print ("[T] Multiply a number by the total")
          print ("[D] Divide the total by a number")
          print ("[P] Show the value of the total")
          print ("[R] Reset the value to '0'")
          print ("[E] Exit MMode (VALUES SAVED)")
      if mc.lower() == "a":
        print ("Enter a number to add to the total")
        mmv = input ("[MMode] > ")
        m += float(mmv)
        print ("Added " + str(mmv) + " to the total!")
      if mc.lower() == "s":
        print ("Enter a number to subtract from the total")
        mmv = input ("[MMode] > ")
        m -= float(mmv)
      print ("Subtracted " + str(mmv) + " from the total!")
      if mc.lower() == "t":
        print ("Enter a number to multiply the total by")
        mmv = input ("[MMode] > ")
        m *= float(mmv)
        print ("Multiplied the total by " + str(mmv))
      if mc.lower() == "d":
        print ("Enter a number to divide the total by")
        mmv = input ("[MMode] > ")
        m /= float(mmv)
        print ("Divided the total by " + str(mmv))
      if mc.lower() == "p":
        print ("Total value is " + str(m))
  if calculator.lower() == "px":
    if x == "":
      print ("x does not have a value!")
    else:
      print ("The value of x is " + str(x))
    calculator = "l"
      
    
