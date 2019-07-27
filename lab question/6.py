in_str="in few week you are good progammer"
for ch in in_str:
    if ch in ['a','e','i','o','u']:
        in_str=in_str.replace(ch,'')
print(in_str)        
