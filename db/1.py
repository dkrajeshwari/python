import csv
ws_list=[
    {"id":1001,"wname":"python","year":"2019","status":1,"company":"heraizen"},
    {"id":1002,"wname":"web","year":"2018","status":1,"company":"spaneous"}
    #[1003,"html",2019,1,"heriaozn"]

]
try:
    with open("as.csv","w")as file:
        heading=["id","wname","year","status","company"]
        obj=csv.DictWriter(file,fieldnames=heading)
        obj.writeheader()
        obj.writerows(ws_list)
except Exception as e:
    print(str(e))