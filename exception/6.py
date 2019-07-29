try:
    with open("5.txt")as fin ,open("6.txt","w")as fout:
        lines=fin.readlines()
        lines=[l.upper() for l in lines]
        fout.writelines(lines)

except Exception as e:
    print(f"File not found{e}")       