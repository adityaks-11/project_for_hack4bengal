def to_csv():
    import pandas as pd
    ni=int(input("enter your preference:"))
    if ni==1:
        col=int(input("enter the number of columns:"))
        colum_list=[]
        for i in range (1,col+1):
            colum_name=input("enter the name of column number"+" "+str(i)+":" )
            colum_list.append(colum_name)
        for j in range (0,len(colum_list)):
            print("the name of column number"+" "+str(j+1)+" "+"of your csv file will be",colum_list[j])
        ro=int(input("enter the number of rows:"))
        dict1_list=[]
        for k in range(0,len(colum_list)):
            col1=[]
            ty=input("is"+" "+colum_list[k]+" "+"an integer? y/n:")
            if ty=='n':
                for j in range(1,ro+1):
                    ao=colum_list[k]
                    am="enter the"+" "+str(j)+" "+"value of column"+" "+(ao)+":"
                    c1=input(am)
                    col1.append(c1)
                dict1_list.append(col1)
            elif ty=='y':
                 for j in range(1,ro+1):
                    ao=colum_list[k]
                    am="enter the"+" "+str(j)+" "+"value of column"+" "+(ao)+":"
                    c1=int(input(am))
                    col1.append(c1)
                 dict1_list.append(col1)
        dicto={}
        for m in range (0,len(colum_list)):
            dicto[colum_list[m]]=dict1_list[m]
        print(dicto)
        df=pd.DataFrame(dicto)
        nm=input("enter the name by which you want your csv file to be saved:")
        df.to_csv(nm+".csv")
        print(nm+".csv file exported successfully") 

def csv_tograph(x):
    #x=name of the csv file
    import pandas as pd
    from matplotlib import pyplot as plt
    ans='y'
    while ans=='y':
        nm=x+'.csv'
        a= pd.read_csv(nm)
        print("1.Line graph")
        print("2.Double line graph")
        print("3.Bar graph")
        print("4.Histogram")
        print("5.Pie chart")
        typ=int(input("enter the number of the type of graph you want:"))
        if typ==1:
            pm1=input("enter the name of field from"+" "+nm+" "+"for x-axis:")
            pm2=input("enter the name of field from"+" "+nm+" "+"for y-axis:")
            xl=input("enter the label of x-axis:")
            yl=input("enter the label of y-axis:")
            titl=input("enter the title of the graph:")
            plt.plot(a[pm1],a[pm2])
            plt.xlabel(xl)
            plt.ylabel(yl)
            plt.title(titl)
            plt.show()
        elif typ==2:
            pm1=input("enter the name of field from"+" "+nm+" "+"for x-axis:")
            pm2a=input("enter the first line parameter:")
            pm2b=input("enter the second line parameter:")
            pm2an=input("enter the name of first parameter:")
            pm2bn=input("enter the name of second parameter:")
            xl=input("enter the label of x-axis:")
            yl=input("enter the label of y-axis:")

            titl=input("enter the title of the graph:")
            plt.plot(a[pm1],a[pm2a],label=pm2an)
            plt.plot(a[pm1],a[pm2b],label=pm2bn)
            plt.xlabel(xl)
            plt.ylabel(yl)
            plt.title(titl)
            plt.legend()
            plt.show()
        elif typ==3:
            pm1=input("enter the name of field from"+" "+nm+" "+"for x-axis:")
            pm2=input("enter the name of field from"+" "+nm+" "+"for y-axis:")
            xl=input("enter the label of x-axis:")
            yl=input("enter the label of y-axis:")
            titl=input("enter the title of the graph:")
            wid=input("enter the width of the bars,else press n for default width:")
            if wid=='n':
                wid=0.5
            else:
                wid=float(wid)
            plt.bar(a[pm1],a[pm2],width=wid)
            plt.xlabel(xl)
            plt.ylabel(yl)
            plt.title(titl)
            plt.show()
        elif typ==4:
            pm=input("enter the name of field from"+" "+nm+" "+"for histogram:")
            xl=input("enter the label of x-axis:")
            yl=input("enter the label of y-axis:")
            titl=input("enter the title of the graph:")
            plt.hist(a[pm])
            plt.xlabel(xl)
            plt.ylabel(yl)
            plt.title(titl)
            plt.show()
        elif typ==5:
            pm1=input("enter the name of field from"+" "+nm+" "+"for name of sectors of pie chart:")
            pm2=input("enter the name of field from"+" "+nm+" "+"for values:")
            titl=input("enter the title of the graph:")
            exp=input("do you want any sector(s) exploded? y/n:")
            if exp=='y':
                l=[]
                for i in range(0,len(a[pm1])):
                    ep=input("do you want"+" "+str(a[pm1][i])+" "+"exploded?y/n:")
                    if ep=='y':
                        vl=float(input("input the value by which it would be exploded:"))
                        l.append(vl)
                    else:
                        l.append(0)
            else:
                l=[]
                for i in range(0,len(a[pm1])):
                    l.append(0)
            #print(l1)
            pct=input("do you want percentage of every sector?y/n:")
            if pct=='y':
                plt.pie(a[pm2],labels=a[pm1],autopct='%0.1f%%',explode=tuple(l))
            else:
                plt.pie(a[pm2],labels=a[pm1],explode=tuple(l))
            plt.title(titl)
            plt.show()






#main
#to_csv()
x=input("enter the name of .csv file:")
csv_tograph(x)         