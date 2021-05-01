from flask import Flask,render_template, Response, request, redirect, url_for
import pymysql
import socket
from datetime import datetime,date

# s = socket.socket()
# host = socket.gethostname() 
# port = 12397
# ip_address = socket.gethostbyname(host)
# print(ip_address)
# s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# s.bind((ip_address,port))
# conn = pymysql.connect(host=ip_address, user="%", password="", database="medical",charset='utf8mb4',port=3306)


app=Flask(__name__)
optiondata=""

# mysql = MySQL()
# app.config['MYSQL_DATABASE_USER'] = 'root'
# app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
# app.config['MYSQL_DATABASE_DB'] = 'medical'
# app.config['MYSQL_DATABASE_HOST'] = 'localhost'
# mysql.init_app(app)
datalst=list()
column_all=['Name','Address','Area','Total beds','Occupied beds','Available beds','Total Ventilators','Total Ambulance','Total Remdesivir','Total Oxygen Cylinder']
column_beds=['Name','Address','Area','Total beds','Occupied beds','Available beds']
column_oxygen=['Name','Address','Area','Total Oxygen Cylinders']
column_remdesivir=['Name','Address','Area','Total Remdesivir vaccine']
tiffin_area=['Name','Area','Address','Phone Number']
temp=list()
@app.route("/",methods=['GET','POST'])
def home():
    # conn = mysql.connect()
    # cursor =conn.cursor()
    # cursor.execute("SELECT area from hospital_details order by area asc")
    # optiondata1 = cursor.fetchall()
    # optiondata1=list(optiondata1)
    # print("Hello")
#     print(optiondata1)
#     for i in range(0,5):
#         print("hi")
#     for x in optiondata1:
#         print(x)
#         if x not in temp2:
#             temp2.append(x)
#     print(temp2)
#     return render_template("search.html",temp=temp2)
# @app.route("/home",methods =['POST','GET'])
# def home():
    return render_template("FAQ.html")

# @app.route("/view")
# def view():
#     return render_template("view.html")

# @app.route("/about")
# def about():
#     return render_template("about.html")

# @app.route("/logo")
# def logo():
#     return render_template("search.html")

# @app.route("/tiffin")
# def tiffin():
#     print('hello')
#     # conn = mysql.connect()
#     cursor =conn.cursor()
#     cursor.execute("SELECT area from tiffin_services order by area asc")
#     optiondata = cursor.fetchall()
#     optiondata=list(optiondata)
#     print(optiondata)
#     for i in range(0,5):
#         print("hi")
#     for x in optiondata:
#         print(x)
#         if x not in temp:
#             temp.append(x)
#     print(temp)
#     return render_template("tiffin.html",optiondata=temp)

# @app.route("/blog")
# def blog():
#     return render_template("blog.html")
# @app.route("/faq")
# def faq():
#     return render_template("FAQs.html")

# @app.route("/department")
# def department():
#     return render_template("department.html")

# @app.route("/elements")
# def elements():
#     return render_template("elements.html")

# @app.route("/contact")
# def contact():
#     return render_template("contact.html")

# temp2=[]
# @app.route("/search")
# def search():
#     # conn = mysql.connect()
#     cursor =conn.cursor()
#     cursor.execute("SELECT area from hospital_details order by area asc")
#     optiondata1 = cursor.fetchall()
#     optiondata1=list(optiondata1)
#     print(optiondata1)
#     for i in range(0,5):
#         print("hi")
#     for x in optiondata1:
#         print(x)
#         if x not in temp2:
#             temp2.append(x)
#     print(temp2)
#     return render_template("search.html",temp=temp2)

# @app.route("/plasma")
# def plasma():
#     return render_template("plasma.html")

# @app.route("/covid_updates")
# def covid_updates():
#     return render_template("covid_updates.html")

# @app.route("/Everyday brings new choices",methods =['POST'])
# def search_word():
#         print("hello")
#         if request.method == "POST":
#                 x = request.form
#                 print(x)
#                 name=x['arealst']
#                 categ=x['category']
#                 print(name)
#                 # conn = mysql.connect()
#                 cursor =conn.cursor()
#                 if categ=='no_of_beds':
#                     cursor.execute("SELECT hd.name,hd.address,hd.area,hs.no_of_beds,hs.no_of_occupy,hs.no_of_empty from hospital_details hd inner join hospital_services hs on hd.hid=hs.hospital_id and hd.area=%s",(name))
#                     data = cursor.fetchall()
#                     print(data)
#                     datalst=column_beds
#                 elif categ=='no_of_oxygen':
#                     cursor.execute("SELECT hd.name,hd.address,hd.area,hs.no_of_oxygen from hospital_details hd inner join hospital_services hs on hd.hid=hs.hospital_id and hd.area=%s",(name))
#                     data = cursor.fetchall()
#                     print(data)
#                     datalst=column_oxygen
#                 elif categ=='no_of_remdesivir':
#                     cursor.execute("SELECT hd.name,hd.address,hd.area,hs.no_of_remdi from hospital_details hd inner join hospital_services hs on hd.hid=hs.hospital_id and hd.area=%s",(name))
#                     data = cursor.fetchall()
#                     print(data)
#                     datalst=column_remdesivir              
#                 else:
#                     cursor.execute("SELECT hd.name,hd.address,hd.area,hs.no_of_beds,hs.no_of_occupy,hs.no_of_empty,hs.no_of_venti,hs.no_of_ambulance,hs.no_of_remdi ,hs.no_of_oxygen from hospital_details hd inner join hospital_services hs on hd.hid=hs.hospital_id and hd.area=%s",(name))
#                     data = cursor.fetchall()
#                     print(data)
#                     datalst=column_all          
#                 # conn = mysql.connect()
#                 cursor =conn.cursor()
#                 cursor.execute("SELECT area from hospital_details order by area asc")
#                 optiondata1 = cursor.fetchall()
#                 optiondata1=list(optiondata1)
#                 print(optiondata1)
#                 for i in range(0,5):
#                     print("hi")
#                 for x in optiondata1:
#                     print(x)
#                     if x not in temp2:
#                         temp2.append(x)
#                 print(temp2)
#                 #conn = MySQLdb.connect(host="localhost",
#                 #               user="root",
#                 #               passwd="root",
#                 #               db="medical")
#                 #cursor = conn.cursor()
#                 # mydb = mysql.connector.connect( host="localhost",user="root",password="root",database="medical",auth_plugin='mysql_native_password')
#                 #cursor = mydb.cursor()
#                 #cursor.execute("select hid from hospital_details where name=%s", (name))
#                 #row= cursor.fetchall()
#                 #print(row)

#         return render_template('search.html',data=data,columns=datalst,temp=temp2)
# # date_lst=[]
# # date_neg=[]
# @app.route("/plasma_donor",methods =['POST'])
# def plasma_donor():
#         print("hello")
#         if request.method == "POST":
#                 x = request.form
#                 print(x)
#                 name=x['username']
#                 vaccine=x['vaccine_yes']
#                 passed=x['passed_yes']
#                 surgery=x['surgery_yes']
#                 disease=x['disease_yes']
#                 #print("hi"+vaccine)
#                 no=x['phone']
#                 no=int(no)
#                 #print(no)
#                 #print(type(no))
#                 blood=x['blood']
#                 age=x['age']
#                 # print(date_lst)
#                 # final_date=date_lst[2]+"-"+date_lst[0]+"-"+date_lst[1]
#                 # positive=.strptime(positive,'%m-%d-%Y')
#                 # print(positive)
#                 negative=str(x['negative_date'])
#                 date_neg=negative.replace("/",'')
#                 #final_dateneg=date_neg[2]+"-"+date_neg[0]+"-"+date_neg[1]
#                 # #print(name)
#                 print(date_neg)
#                 date_neg=date_neg.replace("-","")
#                 print(date_neg)
#                 year=int(date_neg[0:4])
#                 month=int(date_neg[4:6])
#                 day=int(date_neg[6:])
#                 print(year,month,day)
#                 #count_date=date_neg.split("-")
                
#                 # count_date=count_date.replace("'","")
#                 # count_date=int(count_date)

#                 today=str(date.today())
#                 date_today=today.replace("/",'')
#                 date_today=today.replace("-",'')
#                 year1=int(date_today[0:4])
#                 month1=int(date_today[4:6])
#                 day1=int(date_today[6:])
#                 print(year1,month1,day1)
#                 # today=str(today)
#                 # today_date=today.split("-")
#                 # today_date=int(today_date)
#                 f_date = date(year, month, day)
#                 l_date = date(year1, month1, day1)
#                 delta = l_date - f_date
#                 print(delta)
#                 delta1=str(delta)
#                 delta1=delta1.replace(" days, 0:00:00","")
#                 delta1=int(delta1)
#                 print(delta1)
#                 # conn = mysql.connect()
#                 cursor =conn.cursor()
#                 query="insert into plasma_donor(name,phone,blood,age,negative_date,vaccinated,passed,surgery,disease,days) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
#                 val=(name,int(no),blood,int(age),date_neg,vaccine,passed,surgery,disease,int(delta1))
#                 cursor.execute(query,val)
#                 # print(delta.days)
#                 # cursor.execute("select datediff(curdate(),negative_date) from plasma_donor where vaccinated='No' and surgery='No' and disease='No' ")
#                 # for i in merge:
#                 #     if i==name:
#                 #         print()
#                 # print(merge)
#                 # merge=str(total_days)
#                 # merge=str(merge).replace('(','')
#                 # merge=str(merge).replace(',)','')
#                 # merge=str(merge).replace("((",'')
#                 # merge=str(merge).replace("'",'')
#                 # print(merge)
#                 # query1="insert into no_of_days(days) values(%s) "
#                 # values=(int(delta1))
#                 # cursor.execute(query1,values)
#                 # data = cursor.fetchall()
#                 # print(data)
#                 #datalst=column_beds
#                 #conn = MySQLdb.connect(host="localhost",
#                 #               user="root",
#                 #               passwd="root",
#                 #               db="medical")
#                 #cursor = conn.cursor()
#                 # mydb = mysql.connector.connect( host="localhost",user="root",password="root",database="medical",auth_plugin='mysql_native_password')
#                 #cursor = mydb.cursor()
#                 #cursor.execute("select hid from hospital_details where name=%s", (name))
#                 #row= cursor.fetchall()
#                 #print(row)
#                 conn.commit()
#                 return render_template("plasma.html")

# @app.route("/tiffin_service",methods =['POST'])
# def search_tiffin():
#         print("hello")
#         if request.method == "POST":
#                 x = request.form
#                 print(x)
#                 name=x['tiffins']
#                 print("name:"+name)
#                 # conn = mysql.connect()
#                 cursor =conn.cursor()
#                 cursor.execute("SELECT name,area,address,phone from tiffin_services where area=%s",(name))
#                 tiffin = cursor.fetchall()
#                 print(tiffin)
#                 columns=tiffin_area
#                 cursor.execute("SELECT area from tiffin_services order by area asc")
#                 optiondata = cursor.fetchall()
#                 for x in temp:
#                     if x not in temp:
#                         temp.append(x)
#                 print(temp)
#                 #optiondata=list(optiondata)
#                 #conn = MySQLdb.connect(host="localhost",
#                 #               user="root",
#                 #               passwd="root",
#                 #               db="medical")
#                 #cursor = conn.cursor()
#                 # mydb = mysql.connector.connect( host="localhost",user="root",password="root",database="medical",auth_plugin='mysql_native_password')
#                 #cursor = mydb.cursor()
#                 #cursor.execute("select hid from hospital_details where name=%s", (name))
#                 #row= cursor.fetchall()
#                 #print(row)

#         return render_template('tiffin.html',tiffin=tiffin,columns=columns,optiondata=temp)

# @app.route("/register")
# def register():
#         print("hello")
#         # conn = mysql.connect()
#         cursor =conn.cursor()
#         day=int(21)
#         cursor.execute("SELECT name,blood,age,DATE_FORMAT(negative_date,'%d-%m-%Y'),days,vaccinated,passed,surgery,disease,phone from plasma_donor where vaccinated='No' and surgery='No' and disease='No'  and days > 21 ")
#         plasma_data=cursor.fetchall()
#         print(plasma_data)
#         plasma_columns=["Name","Blood Group","Age","Tested Negative","Days from tested negative","Vaccine Taken","Passed Any major disease","Surgery done in 6-12 months","Any Disease","Mobile no"]
#         #columns=tiffin_area
#         #cursor.execute("SELECT area from tiffin_services order by area asc")
#         #optiondata = cursor.fetchall()
#         # for x in temp:
#         # if x not in temp:
#         # temp.append(x)
#         # print(temp)
#         #         #optiondata=list(optiondata)
#                 #conn = MySQLdb.connect(host="localhost",
#                 #               user="root",
#                 #               passwd="root",
#                 #               db="medical")
#                 #cursor = conn.cursor()
#                 # mydb = mysql.connector.connect( host="localhost",user="root",password="root",database="medical",auth_plugin='mysql_native_password')
#                 #cursor = mydb.cursor()
#                 #cursor.execute("select hid from hospital_details where name=%s", (name))
#                 #row= cursor.fetchall()
#                 #print(row)

#         return render_template("register.html",plasma_data=plasma_data,plasma_columns=plasma_columns)

if __name__=="__main__":
    app.run(debug="false",host=ip_address,port=8080)