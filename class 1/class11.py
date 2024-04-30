# String method

name="suffiyan"
name2="ahmed !!!!!!!!!!!!!!!!!!!!!"
name3="ahmed"
name4="hi hello  world"
name5="weLBUidewnufci76942"
name6="hi Hello  wOrld80294"
name7="     "
print(name.upper())
print(name.lower())
print(name2)
print(name2.rstrip('!')) # removes any trailing characters
print(name3.replace("ah","kh"))
print(name4.split(" ")) # convert  string into list
print(name4.capitalize()) 
print(name3.center(100)) 
print(name3.count("ahmed")) 
print(name2.endswith("!")) 
print(name4.endswith("lo" ,0,8)) 
print(name4.find("lo")) # if find method are worked so it's return index number
print(name4.find("to")) # and if no any thing in find method so it's return -1 which mean's false
print(name4.index("lo")) # if index number are not available to givin string so it's return a error which error is "valueError: substring not found"
print(name5.isalnum()) # if have A-Za-z0-9 are available in string without spacing so return ture otherwise it's return false
print(name6.isalnum()) 
print(name6.isalpha()) # if have A-Za-z are available in string without spacing so return ture otherwise it's return false and also number in the string so also return false
print(name3.isalpha()) # if have A-Za-z are available in string without spacing so return ture otherwise it's return false and also number in the string so also return false
print(name4.islower()) # it's check that if all characters are lowercase so return true otherwise false
print(name6.isprintable()) # if it's printable so return true otherwise false return
print(name7.isspace()) # if space are available in the string so return true otherwise false
print(name3.istitle()) # it's check if first letter are capital so return true otherwise false
print(name4.startswith("hi")) # it's check if first letter are available so return true otherwise false
print(name4.swapcase()) # if  uppercase string is so convert into lowercase and lowercase is so convert into upercase  
print(name4.title()) # it's convert to title means every first letter are capitale 