from tkinter import Y


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
def py_mysqlc():
    import mysql.connector as c
    usr=input("input user name:")
    password=input("input your password:")
    dtbse=input("the name of the database:")
    con=c.connect(host="localhost", user=usr, passwd=password, database=dtbse)
    if con.is_connected():
        print ("sucessfully connected")
def pmsql_data():
    import mysql.connector as c
    usr=input("input user name:")
    password=input("input your password:")
    dtbse=input("the name of the database:")
    con=c.connect(host="localhost", user=usr, passwd=password, database=dtbse)
    if con.is_connected():
        print ("sucessfully connected")
    cursor=con.cursor(buffered=True)
    table_name=input("table name:")
    cursor.execute("select * from"+" "+table_name)
    num_fields = len(cursor.description)
    field_names = [i[0] for i in cursor.description]
    print(field_names)
    l=[]
    x="y"
    while x=="y":
        L=[]
        for i in range(0,len(field_names)):
            a=input("enter the value of"+" "+field_names[i]+":")
            L.append(a)
        l.append(L)
        x=input("enter more data? y/n:")
    print (l)
    integ=[]
    tups=[]
    for i in range (0,len(field_names)):
        h=input("is"+" "+field_names[i]+" "+"is an integer?y/n")
        if h=='y':
            integ.append(i)
            tups.append({})
        else:
            tups.append('{}')
    tupl=tuple(tups)
    for i in range (0,len(l)):
        for k in integ:
            l[i][k]=int(l[i][k])
    print(l)
    for i in range(0,len(l)):
        if len(tupl)==1:
            query="Insert into marks_tables values"+str(tupl).format(l[i][0])
            print(query)
            cursor.execute(query)
            con.commit()
            print("data inserted succesfully")
        elif len(tupl)==2:
            query="Insert into marks_tables values"+str(tupl).format(l[i][0],l[i][1])
            print(query)
            cursor.execute(query)
            con.commit()
            print("data inserted succesfully")
        elif len(tupl)==3:
            query="Insert into"+" "+table_name+" "+"values"+str(tupl).format(l[i][0],l[i][1],l[i][2])
            cursor.execute(query)
            con.commit()
            print("data inserted succesfully")
        elif len(tupl)==4:
            query="Insert into"+" "+table_name+" "+"values"+str(tupl).format(l[i][0],l[i][1],l[i][2],l[i][3])
            print(query)
            cursor.execute(query)
            con.commit()
            print("data inserted succesfully")
        elif len(tupl)==5:
            query="Insert into"+" "+table_name+" "+"values"+str(tupl).format(l[i][0],l[i][1],l[i][2],l[i][3],l[i][4])
            print(query)
            cursor.execute(query)
            con.commit()
            print("data inserted succesfully")
        elif len(tupl)==6:
            query="Insert into"+" "+table_name+" "+"values"+str(tupl).format(l[i][0],l[i][1],l[i][2],l[i][3],l[i][4],l[i][5])
            print(query)
            cursor.execute(query)
            con.commit()
            print("data inserted succesfully")
        elif len(tupl)==7:
            query="Insert into"+" "+table_name+" "+"values"+str(tupl).format(l[i][0],l[i][1],l[i][2],l[i][3],l[i][4],l[i][5],l[i][6])
            print(query)
            cursor.execute(query)
            con.commit()
            print("data inserted succesfully")
        elif len(tupl)==8:
            query="Insert into"+" "+table_name+" "+"values"+str(tupl).format(l[i][0],l[i][1],l[i][2],l[i][3],l[i][4],l[i][5],l[i][6],l[i][7])
            print(query)
            cursor.execute(query)
            con.commit()
            print("data inserted succesfully")
        elif len(tupl)==9:
            query="Insert into"+" "+table_name+" "+"values"+str(tupl).format(l[i][0],l[i][1],l[i][2],l[i][3],l[i][4],l[i][5],l[i][6],l[i][7],l[i][8])
            print(query)
            cursor.execute(query)
            con.commit()
            print(i,"data inserted succesfully")
def fetch_fromSql(tn):
    import mysql.connector as c
    usr=input("input user name:")
    password=input("input your password:")
    dtbse=input("the name of the database:")
    con=c.connect(host="localhost", user=usr, passwd=password, database=dtbse)
    cursor=con.cursor(buffered=True)
    iu=int(input("1.fetch all data /n 2.fetch only one row /n 3.fetch specific no. of rows:"))
    if iu==1:
        sql_select_Query = "select * from"+" "+tn
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        
        print("Total number of rows in table: ", cursor.rowcount)
        print(records)
        for row in records:
            print(row)
        a=input("exit")
    elif iu==3:
        mySql_select_Query = "select * from"+" "+tn
        
        cursor.execute(mySql_select_Query)
        row_count = int(input("number of rows you want:"))
        records = cursor.fetchmany(row_count)
        print(records)

        print("Total number of rows is: ", cursor.rowcount)
        print("Printing ", row_count, " Laptop record using cursor.fetchmany")
        for row in records:
            print(row)
    elif iu==2:
        mySql_select_Query = "select * from"+" "+tn
        cursor.execute(mySql_select_Query)
        record = cursor.fetchone()
        print(record)    
    
    






#main
to_csv()
x=input("enter the name of .csv file:")
csv_tograph(x)  
c=input("do you want to enter data in mysql through python?y/n:")
if c=='y':
    pmsql_data()
tn=input("enter the table name:")
fetch_fromSql(tn)




