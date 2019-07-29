count_lines=0
count_word=0
try:
    with open("5.txt")as f:
        lines=f.readlines()
        for line in lines:
            print(line,end="")
            count_lines+=1
            words=line.split()
            for word in words:
                count_word+=1
        print(f"number of lines:{count_lines}")
        print(f"number of words:{count_word}")        

except Exception as e:
    print(f"file not found plz check{e}")