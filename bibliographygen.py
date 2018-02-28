print ("[Bibliography Generator]")
print ("Current MLA: MLA8")
print ("\nPress enter to continue...")
retry = False
authfirsttrue = False
authlasttrue = False
webtitletrue = False
urltrue = False
monthtrue = False
daytrue = False
yeartrue = False
input ("")
article = input ("Please enter the article title (Not required)\n> ")
while authfirsttrue == False:
  authfirst = input ("Please enter the author's first name (Include no spaces)\n> ")
  authfirsttrue = True
while authlasttrue == False:
  authlast = input ("Please enter the author's last name (Include no spaces)\n> ")
  authlasttrue = True
while webtitletrue == False:
  webtitle = input ("Please enter the website title\n> ")
  webtitletrue = True
if retry == False:
  sponser = input ("Please enter the publisher/sponser (Not required)\n> ")
while urltrue == False:
  url = input ("Please enter the URL of the website\n> ")
  urltrue = True
while monthtrue == False:
  monthpub = input ("What month was this published (Enter a number 1-12)\n> ")
  monthtrue = True
while daytrue == False:
  daypub = input ("What year was this published (Enter a number 1-31)\n> ")
  daytrue = True
while yeartrue == False:
  yearpub = input ("What day was this published (Enter a number [EX: 2018])\n> ")
  yeartrue = True
if authfirst == "":
  print ("Author's first name has no value!")
  authfirsttrue = False
else:
  authfirsttrue = True
if authlast == "":
  print ("Author's last name has no value!")
  authlasttrue = False
else:
  authlasttrue = True
if webtitle == "":
  print ("Website title has no value!")
  webtitletrue = False
else:
  webtitletrue = True
if url == "":
  print ("URL has no value!")
  urltrue = False
else:
  urltrue = True
if monthpub == "":
  print ("Published month has no value!")
  monthtrue = False
else:
  monthtrue = True
if daypub == "":
  print ("Published day has no value!")
  daytrue = False 
else:
  daytrue = True
if yearpub == "":
  print ("Published year has no value!")
  yeartrue = False
else:
  yeartrue = True
if authfirsttrue == False or authlasttrue == False or webtitletrue == False or urltrue == False or monthtrue == False or daytrue == False or yeartrue == False:
  print ("At least 1 error has been found in values given. Scanning for errors in dates...")
  retry = True
if sponser == "":
  if sponser == "" and article == "":
    print (authlast + ',' + authfirst + '. "' + webtitle + ', ' + daypub + ' ' + monthpub + '. ' + yearpub + ', ' + url + '.')
  else:
    print (authlast + ',' + authfirst + '. "' + article + '." ' + webtitle + ', ' + daypub + ' ' + monthpub + '. ' + yearpub + ', ' + url + '.')
elif article == "":
  print (authlast + ',' + authfirst + '." ' + webtitle + ', ' + sponser + ', ' + daypub + ' ' + monthpub + '. ' + yearpub + ', ' + url + '.')
else:
  print (authlast + ',' + authfirst + '. "' + article + '." ' + webtitle + ', ' + sponser + ', ' + daypub + ' ' + monthpub + '. ' + yearpub + ', ' + url + '.')
print ("\nBibliography generated. Please restart the program to make another one.")

       


