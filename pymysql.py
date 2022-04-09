def to_csv():
    import pandas as pd
    ni=int(input("enter your preference"))
    if ni==1:
        col=int(input("enter the number of columns"))
        colum_list=[]
        for i in range (1,col+1):
            colum_name=input("enter the name of column number"+" "+str(i) )
            colum_list.append(colum_name)
        for j in range (0,len(colum_list)):
            print("the name of column number"+" "+str(j+1)+" "+"of your csv file will be",colum_list[j])
        ro=int(input("enter the number of rows"))
        dict1_list=[]
        for k in range(0,len(colum_list)):
            col1=[]
            for j in range(1,ro+1):
                ao=colum_list[k]
                am="enter the"+" "+str(j)+" "+"value of column"+" "+(ao)
                c1=input(am)
                col1.append(c1)
            dict1_list.append(col1)
        dicto={}
        for m in range (0,len(colum_list)):
            dicto[colum_list[m]]=dict1_list[m]
        print(dicto)
        df=pd.DataFrame(dicto)
        nm=input("enter the name by which you want your csv file to be saved")
        df.to_csv(nm+".csv")
        print(nm+".csv file exported successfully") 
#main
to_csv()         