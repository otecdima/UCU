str = "thisissometextthatiwrotetext"
substr = "text"
inserttxt = "XX"
new_string = (inserttxt+substr).join(str.split(substr))
print (new_string)