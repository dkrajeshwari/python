count=0
try:
    with open("7.txt")as f:
        lines=f.readlines()
        w_count={}
        for line in lines:
            words=line.split(" ")
            for word in words:
                word=word.strip()
                word=word.strip("\n")
                word=word.replace(',','')
                word=word.replace('.','')
                try:
                    w_count[dict]+=1
                except KeyError:
                    w_count[word]=1    
        max_val=max(w_count.values())
        for k,v in w_count.items():
            if v==max_val:
                print(f"{k}:{v}")
        for key in w_count.keys():
            if key in ['and','but','if']:
                count+=1                     
           

except Exception as e:
    print(f"file not found plz check{e}")