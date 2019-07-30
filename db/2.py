import json
ws_list=[
    {"id":1001,"wname":"python","year":"2019","status":1,"company":"heraizen"},
    {"id":1002,"wname":"web","year":"2018","status":1,"company":"spaneous"}
    #[1003,"html",2019,1,"heriaozn"]

]
try:
    with open("ws.json","w",newline='')as file:
        json.dump(ws_list,file,indent=4)

except Exception as e:
    print(str(e))