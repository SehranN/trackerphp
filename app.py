import json
from flask import Flask, render_template, request, g
from flask_mysqldb import MySQL
from flask import request
import yaml

import mysql.connector


# mysql1 is mydb now
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Xcvbnm%69",
    port=3306,
    database="billing"
)
# cur or cursor is mycursor now



app = Flask(__name__)
#configure db
db = yaml.safe_load(open('db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']

mysql1 = MySQL(app)
@app.route('/postCust_bal',methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        #Fetch form data
        userDetails = request.form
        accNo = userDetails['accNo']
        dates = userDetails['date']
        cashDebit =   userDetails['cashDebit']
        goldDebit =   userDetails['goldDebit']
        cashCredit = userDetails['cashCredit']
        goldCredit = userDetails['goldCredit']
        billType =     userDetails['billType']
        billNo =         userDetails['billNo']
        sNo =               userDetails['sNo']
        mycursor = mydb.cursor()
        mycursor.execute("INSERT INTO cust_bal(accNo, date, cashDebit, goldDebit, cashCredit, goldCredit, billType, billNo, sNo) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)", (accNo, dates, cashDebit, goldDebit, cashCredit, goldCredit, billType, billNo, sNo))
        mydb.commit()
        mycursor.close()
        return'sucess'
    return render_template("index.html")
       


@app.route('/getCust_bal')
def users():
    cur = mydb.cursor()
    resultValue = cur.execute("SELECT * FROM cust_bal")
    print(resultValue, "this is the result value")
    # if resultValue > 0:
    userDetails = cur.fetchall()
    cur.close()
    return json.dumps(userDetails)
        
    

# /postCustomer will change to /post...
# posyCutomer() will change to post....()  
# accNo, name, etc on the left will change to the name of headings in that specific table
# same with the accNo, name, etc will change with same spelling and cases  
# INSERT INTO customer will change to INSERT INTO newTableName
# in the brackets after table name will be the column names
# inside the brackets of VALUES() the number of %s will be the number of columns in the table
# inside the third bracket right after the values bracket will again be the column name with the same cases
@app.route('/postCustomer',methods=['GET', 'POST'])
def postCustomer():
    if request.method == "POST":
        
            #Fetch form data
        userDetails = request.form
        accNo =       userDetails['accNo']
        name =        userDetails['name']
        phoneNo =   userDetails['phoneNo']
        email =   userDetails['email']
        company =  userDetails['company']
        vattNo =  userDetails['vattNo']
        address =    userDetails['address']
        oldCash =      userDetails['oldCash']
        oldGold =         userDetails['oldGold']
        mycursor = mydb.cursor()
        mycursor.execute("INSERT INTO customer(accNo, name, phoneNo, email, company, vattNo, address, oldCash, oldGold ) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)", (accNo, name, phoneNo, email, company, vattNo, address, oldCash, oldGold))
        mydb.commit()
        mycursor.close()
        return'sucess'
    
    


# /getCustomer will change into /get...
# getCustomer() will change into get..()
# in the 4th line where we define resultValue SELECT * FROM customer will change into SELECT * FROM newTableName
@app.route('/getCustomer')
def getCustomer():
    cur = mydb.cursor()
    resultValue = cur.execute("SELECT * FROM customer")
    userDetails = cur.fetchall()
    cur.close()
    return  json.dumps(userDetails)
        
    


@app.route('/postexp_items',methods=['GET', 'POST'])
def postexp_items():
    if request.method == "POST":
        
        #Fetch form data
       userDetails = request.form
       Item_No = userDetails['Item_No']
       Item_Name = userDetails['Item_Name']
       mycursor = mydb.cursor()
       mycursor.execute("INSERT INTO exp_items(Item_No, Item_Name ) VALUES(%s, %s)", (Item_No, Item_Name))
       mydb.commit()
       mycursor.close()
       return'sucess'

   
@app.route('/getexp_items')
def getexp_items():
    cur = mydb.cursor()
    resultValue = cur.execute("SELECT * FROM exp_items")
    
    userDetails = cur.fetchall()
    cur.close()
    return  json.dumps(userDetails)
    
    
    
@app.route('/postExpenseBalance',methods=['GET', 'POST'])
def postexpensebalance():
    if request.method == "POST":
    
        #Fetch form data
        userDetails = request.form
        id =       userDetails['id']
        Date =        userDetails['Date']
        Item_Name =   userDetails['Item_Name']
        Amount =   userDetails['Amount']
        Notes =  userDetails['Notes']
        mycursor = mydb.cursor()
        mycursor.execute("INSERT INTO expensebalance(id, date, Item_Name, Amount, Notes ) VALUES(%s, %s, %s, %s, %s)", (id, Date, Item_Name, Amount, Notes))
        mydb.commit()
        mycursor.close()
        return'sucess'
    return render_template("index.html")
    
@app.route('/getexpensebalance')
def getexpensebalance():
    cur = mydb.cursor()
    resultValue = cur.execute("SELECT * FROM expensebalance")
    
    userDetails = cur.fetchall()
    cur.close()
    return  json.dumps(userDetails) 




    
@app.route('/postitems',methods=['GET', 'POST'])
def postitems():
    if request.method == "POST":
    
        #Fetch form data
        userDetails = request.form
        Item_No =       userDetails['Item_No']
        Item_Name =        userDetails['Item_Name']
        Purity =   userDetails['Purity']
        Labour =   userDetails['Labour']
        Vat =  userDetails['Vat']
        mycursor = mydb.cursor()
        mycursor.execute("INSERT INTO items(Item_No, Item_Name, Purity, Labour, Vat ) VALUES(%s, %s, %s, %s, %s)", (Item_No, Item_Name, Purity, Labour, Vat))
        mydb.commit()
        mycursor.close()
        return'sucess'
    return render_template("index.html")

@app.route('/getitems')
def getitems():
    cur = mydb.cursor()
    resultValue = cur.execute("SELECT * FROM items")
    
    userDetails = cur.fetchall()
    cur.close()
    return  json.dumps(userDetails) 



@app.route('/postpayable_bills',methods=['GET', 'POST'])
def postpayable_bills():
    if request.method == "POST":
    
        #Fetch form data
        userDetails = request.form
        date = userDetails['date']
        accNo =        userDetails['accNo']
        name =   userDetails['name']
        totalGross =   userDetails['totalGross']
        totalBase =  userDetails['totalBase']
        totalCash =   userDetails['totalCash']
        totalLabour =   userDetails['totalLabour']
        grandTotal =  userDetails['grandTotal']
        billNo =   userDetails['billNo']
        sNo =  userDetails['sNo']
        mycursor = mydb.cursor()
        mycursor.execute("INSERT INTO payable_bills(date, accNo, name, totalGross, totalBase, totalCash, totalLabour, grandTotal, billNo, sNo ) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (date, accNo, name, totalGross, totalBase, totalCash, totalLabour, grandTotal, billNo, sNo))
        mydb.commit()
        mycursor.close()
        return'sucess'
    return render_template("index.html")

@app.route('/getpayable_bills')
def getpayable_bills():
    cur = mydb.cursor()
    resultValue = cur.execute("SELECT * FROM payable_bills")
    
    userDetails = cur.fetchall()
    cur.close()
    return  json.dumps(userDetails) 



@app.route('/postpayable_items',methods=['GET', 'POST'])
def postpayable_items():
    if request.method == "POST":
    
        #Fetch form data
        userDetails = request.form
        date = userDetails['date']
        accNo =        userDetails['accNo']
        name =   userDetails['name']
        itemName =   userDetails['itemName']
        notes =  userDetails['notes']
        grossW =   userDetails['grossW']
        K =   userDetails['K']
        baseW =  userDetails['baseW']
        cash =   userDetails['cash']
        labour =  userDetails['labour']
        totalLabour =  userDetails['totalLabour']
        billNo =   userDetails['billNo']
        sNo =  userDetails['sNo']
        mycursor = mydb.cursor()
        mycursor.execute("INSERT INTO payable_items(date, accNo, name, itemName, notes, grossW, K, baseW, cash, labour, totalLabour, billNo, sNo ) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s ,%s)", (date, accNo, name, itemName, notes, grossW, K, baseW, cash, labour, totalLabour, billNo, sNo))
        mydb.commit()
        mycursor.close()
        return'sucess'
    return render_template("index.html")

@app.route('/getpayable_items')
def getpayable_items():
    cur = mydb.cursor()
    resultValue = cur.execute("SELECT * FROM payable_items")
    
    userDetails = cur.fetchall()
    cur.close()
    return  json.dumps(userDetails) 


@app.route('/postpurchase_bills',methods=['GET', 'POST'])
def postpurchase_bills():
    if request.method == "POST":
    
        #Fetch form data
        userDetails = request.form
        date = userDetails['date']
        accNo =        userDetails['accNo']
        name =   userDetails['name']
        totalGross =   userDetails['totalGross']
        totalBase =  userDetails['totalBase']
        totalLab =   userDetails['totalLab']
        totalVat =   userDetails['totalVat']
        grandTotal =  userDetails['grandTotal']
        billNo =   userDetails['billNo']
        sNo =  userDetails['sNo']
        mycursor = mydb.cursor()
        mycursor.execute("INSERT INTO purchase_bills(date, accNo, name, totalGross, totalBase, totalLab, totalVat, grandTotal, billNo, sNo ) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (date, accNo, name, totalGross, totalBase, totalLab, totalVat, grandTotal, billNo, sNo))
        mydb.commit()
        mycursor.close()
        return'sucess'
    return render_template("index.html")

@app.route('/getpurchase_bills')
def getpurchase_bills():
    cur = mydb.cursor()
    resultValue = cur.execute("SELECT * FROM purchase_bills")
    
    userDetails = cur.fetchall()
    cur.close()
    return  json.dumps(userDetails) 





@app.route('/postpurchase_items',methods=['GET', 'POST'])
def postpurchase_items():
    if request.method == "POST":
    
        #Fetch form data
        userDetails = request.form
        date = userDetails['date']
        accNo =        userDetails['accNo']
        name =   userDetails['name']
        itemName =   userDetails['itemName']
        notes =  userDetails['notes']
        grossW =   userDetails['grossW']
        K =   userDetails['K']
        baseW =  userDetails['baseW']
        labperGram =   userDetails['labPerGram']
        totalLab =  userDetails['totalLab']
        total =  userDetails['total']
        vat =  userDetails['vat']
        totalVat =  userDetails['totalVat']
        billNo =   userDetails['billNo']
        sNo =  userDetails['sNo']
        mycursor = mydb.cursor()
        mycursor.execute("INSERT INTO purchase_items(date, accNo, name, itemName, notes, grossW, K, baseW, labPerGram, totalLab, total, vat, totalVat, billNo, sNo) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s ,%s, %s, %s)", (date, accNo, name, itemName, notes, grossW, K, baseW, labperGram, totalLab, total, vat, totalVat, billNo, sNo))
        mydb.commit()
        mycursor.close()
        return'sucess'
    return render_template("index.html")

@app.route('/getpurchase_items')
def getpurchase_items():
    cur = mydb.cursor()
    resultValue = cur.execute("SELECT * FROM purchase_items")
    
    userDetails = cur.fetchall()
    cur.close()
    return  json.dumps(userDetails) 




@app.route('/postpurchaseret_bills',methods=['GET', 'POST'])
def postpurchaseret_bills():
    if request.method == "POST":
    
        #Fetch form data
        userDetails = request.form
        date = userDetails['date']
        accNo =        userDetails['accNo']
        name =   userDetails['name']
        totalGross =   userDetails['totalGross']
        totalBase =  userDetails['totalBase']
        totalLab =   userDetails['totalLab']
        totalVat =   userDetails['totalVat']
        grandTotal =  userDetails['grandTotal']
        billNo =   userDetails['billNo']
        sNo =  userDetails['sNo']
        mycursor = mydb.cursor()
        mycursor.execute("INSERT INTO purchaseret_bills(date, accNo, name, totalGross, totalBase, totalLab, totalVat, grandTotal, billNo, sNo ) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (date, accNo, name, totalGross, totalBase, totalLab, totalVat, grandTotal, billNo, sNo))
        mydb.commit()
        mycursor.close()
        return'sucess'
    return render_template("index.html")


@app.route('/getpurchaseret_bills')
def getpurchaseret_bills():
    cur = mydb.cursor()
    resultValue = cur.execute("SELECT * FROM purchaseret_bills")
    
    userDetails = cur.fetchall()
    cur.close()
    return  json.dumps(userDetails) 



@app.route('/postpurchaseret_items',methods=['GET', 'POST'])
def postpurchaseret_items():
    if request.method == "POST":
    
        #Fetch form data
        userDetails = request.form
        date = userDetails['date']
        accNo =        userDetails['accNo']
        name =   userDetails['name']
        itemName =   userDetails['itemName']
        notes =  userDetails['notes']
        grossW =   userDetails['grossW']
        K =   userDetails['K']
        baseW =  userDetails['baseW']
        labperGram =   userDetails['labPerGram']
        totalLab =  userDetails['totalLab']
        total =  userDetails['total']
        vat =  userDetails['vat']
        totalVat =  userDetails['totalVat']
        billNo =   userDetails['billNo']
        sNo =  userDetails['sNo']
        mycursor = mydb.cursor()
        mycursor.execute("INSERT INTO purchaseret_items(date, accNo, name, itemName, notes, grossW, K, baseW, labPerGram, totalLab, total, vat, totalVat, billNo, sNo) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s ,%s, %s, %s)", (date, accNo, name, itemName, notes, grossW, K, baseW, labperGram, totalLab, total, vat, totalVat, billNo, sNo))
        mydb.commit()
        mycursor.close()
        return'sucess'
    return render_template("index.html")


@app.route('/getpurchaseret_items')
def getpurchaseret_items():
    cur = mydb.cursor()
    resultValue = cur.execute("SELECT * FROM purchaseret_items")
    
    userDetails = cur.fetchall()
    cur.close()
    return  json.dumps(userDetails) 





@app.route('/postrecieving_bills',methods=['GET', 'POST'])
def postrecieving_bills():
    if request.method == "POST":
    
        #Fetch form data
        userDetails = request.form
        date = userDetails['date']
        accNo =        userDetails['accNo']
        name =   userDetails['name']
        totalGross =   userDetails['totalGross']
        totalBase =  userDetails['totalBase']
        totalCash =   userDetails['totalCash']
        totalLabour =   userDetails['totalLabour']
        grandTotal =  userDetails['grandTotal']
        billNo =   userDetails['billNo']
        sNo =  userDetails['sNo']
        mycursor = mydb.cursor()
        mycursor.execute("INSERT INTO recieving_bills(date, accNo, name, totalGross, totalBase, totalCash, totalLabour, grandTotal, billNo, sNo ) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (date, accNo, name, totalGross, totalBase, totalCash, totalLabour, grandTotal, billNo, sNo))
        mydb.commit()
        mycursor.close()
        return'sucess'
    return render_template("index.html")

@app.route('/getrecieving_bills')
def getrecieving_bills():
    cur = mydb.cursor()
    resultValue = cur.execute("SELECT * FROM recieving_bills")
    
    userDetails = cur.fetchall()
    cur.close()
    return  json.dumps(userDetails) 






@app.route('/postrecieving_items',methods=['GET', 'POST'])
def postrecieving_items():
    if request.method == "POST":
    
        #Fetch form data
        userDetails = request.form
        date = userDetails['date']
        accNo =        userDetails['accNo']
        name =   userDetails['name']
        itemName =   userDetails['itemName']
        notes =  userDetails['notes']
        grossW =   userDetails['grossW']
        K =   userDetails['K']
        baseW =  userDetails['baseW']
        cash =   userDetails['cash']
        labour =  userDetails['labour']
        totalLabour =  userDetails['totalLabour']
        billNo =   userDetails['billNo']
        sNo =  userDetails['sNo']
        mycursor = mydb.cursor()
        mycursor.execute("INSERT INTO recieving_items(date, accNo, name, itemName, notes, grossW, K, baseW, cash, labour, totalLabour, billNo, sNo) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s ,%s)", (date, accNo, name, itemName, notes, grossW, K, baseW, cash, labour, totalLabour, billNo, sNo))
        mydb.commit()
        mycursor.close()
        return'sucess'
    return render_template("index.html")

@app.route('/getrecieving_items')
def getrecieving_items():
    cur = mydb.cursor()
    resultValue = cur.execute("SELECT * FROM recieving_items")
    
    userDetails = cur.fetchall()
    cur.close()
    return  json.dumps(userDetails) 






@app.route('/postsales_bills',methods=['GET', 'POST'])
def postsales_bills():
    if request.method == "POST":
    
        #Fetch form data
        userDetails = request.form
        date = userDetails['date']
        accNo =        userDetails['accNo']
        name =   userDetails['name']
        totalGross =   userDetails['totalGross']
        totalBase =  userDetails['totalBase']
        totalLab =   userDetails['totalLab']
        totalVat =   userDetails['totalVat']
        grandTotal =  userDetails['grandTotal']
        billNo =   userDetails['billNo']
        sNo =  userDetails['sNo']
        mycursor = mydb.cursor()
        mycursor.execute("INSERT INTO sales_bills(date, accNo, name, totalGross, totalBase, totalLab, totalVat, grandTotal, billNo, sNo ) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (date, accNo, name, totalGross, totalBase, totalLab, totalVat, grandTotal, billNo, sNo))
        mydb.commit()
        mycursor.close()
        return'sucess'
    
    
@app.route('/getsales_bills')
def getsales_bills():
    cur = mydb.cursor()
    resultValue = cur.execute("SELECT * FROM sales_bills")
    
    userDetails = cur.fetchall()
    cur.close()
    return  json.dumps(userDetails) 




@app.route('/postsales_items',methods=['GET', 'POST'])
def postsales_items():
    if request.method == "POST":
    
        #Fetch form data
        userDetails = request.form
        date = userDetails['date']
        accNo =        userDetails['accNo']
        name =   userDetails['name']
        itemName =   userDetails['itemName']
        notes =  userDetails['notes']
        grossW =   userDetails['grossW']
        K =   userDetails['K']
        baseW =  userDetails['baseW']
        labperGram =   userDetails['labPerGram']
        totalLab =  userDetails['totalLab']
        total =  userDetails['total']
        vat =  userDetails['vat']
        totalVat =  userDetails['totalVat']
        billNo =   userDetails['billNo']
        sNo =  userDetails['sNo']
        mycursor = mydb.cursor()
        mycursor.execute("INSERT INTO sales_items(date, accNo, name, itemName, notes, grossW, K, baseW, labPerGram, totalLab, total, vat, totalVat, billNo, sNo) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s ,%s, %s, %s)", (date, accNo, name, itemName, notes, grossW, K, baseW, labperGram, totalLab, total, vat, totalVat, billNo, sNo))
        mydb.commit()
        mycursor.close()
        return'sucess'
    return render_template("index.html")

@app.route('/getsales_items')
def getsales_items():
    cur = mydb.cursor()
    resultValue = cur.execute("SELECT * FROM sales_items")
    
    userDetails = cur.fetchall()
    cur.close()
    return  json.dumps(userDetails) 



@app.route('/postsalesret_bills',methods=['GET', 'POST'])
def postsalesret_bills():
    if request.method == "POST":
    
        #Fetch form data
        userDetails = request.form
        date = userDetails['date']
        accNo =        userDetails['accNo']
        name =   userDetails['name']
        totalGross =   userDetails['totalGross']
        totalBase =  userDetails['totalBase']
        totalLab =   userDetails['totalLab']
        totalVat =   userDetails['totalVat']
        grandTotal =  userDetails['grandTotal']
        billNo =   userDetails['billNo']
        sNo =  userDetails['sNo']
        mycursor = mydb.cursor()
        mycursor.execute("INSERT INTO salesret_bills(date, accNo, name, totalGross, totalBase, totalLab, totalVat, grandTotal, billNo, sNo ) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (date, accNo, name, totalGross, totalBase, totalLab, totalVat, grandTotal, billNo, sNo))
        mydb.commit()
        mycursor.close()
        return'sucess'

@app.route('/getsalesret_bills')
def getsalesret_bills():
    cur = mydb.cursor()
    resultValue = cur.execute("SELECT * FROM salesret_bills")
    
    userDetails = cur.fetchall()
    cur.close()
    return  json.dumps(userDetails)     





@app.route('/postsalesret_items',methods=['GET', 'POST'])
def postsalesret_items():
    if request.method == "POST":
    
        #Fetch form data
        userDetails = request.form
        date = userDetails['date']
        accNo =        userDetails['accNo']
        name =   userDetails['name']
        itemName =   userDetails['itemName']
        notes =  userDetails['notes']
        grossW =   userDetails['grossW']
        K =   userDetails['K']
        baseW =  userDetails['baseW']
        labperGram =   userDetails['labPerGram']
        totalLab =  userDetails['totalLab']
        total =  userDetails['total']
        vat =  userDetails['vat']
        totalVat =  userDetails['totalVat']
        billNo =   userDetails['billNo']
        sNo =  userDetails['sNo']
        mycursor = mydb.cursor()
        mycursor.execute("INSERT INTO salesret_items(date, accNo, name, itemName, notes, grossW, K, baseW, labPerGram, totalLab, total, vat, totalVat, billNo, sNo) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s ,%s, %s, %s)", (date, accNo, name, itemName, notes, grossW, K, baseW, labperGram, totalLab, total, vat, totalVat, billNo, sNo))
        mydb.commit()
        mycursor.close()
        return'sucess'
    return render_template("index.html")
 
 
@app.route('/getsalesret_items')
def getsalesret_items():
    cur = mydb.cursor()
    resultValue = cur.execute("SELECT * FROM salesret_items")
    
    userDetails = cur.fetchall()
    cur.close()
    return  json.dumps(userDetails)  
    
    


# @app.route('/test')
# def test():
#     connection = mysql.connector.connect(
#             host="trail3server.mysql.database.azure.com",
#             user="sehran",
#             password="Noor123!",
#             database="billing",
#             ssl_verify_identity=True,
#             ssl_ca='DigiCertGlobalRootCA.crt (7).pem'
#     )
#     cursor = connection.cursor()
#     query = cursor.execute("SELECT * FROM cust_bal")
#     result = cursor.fetchall()
#     return render_template('test.html', testData = result)


    
# @app.route("/")
# def root_route():
#    return "Flask app running!!!"


# @app.route("/get_api/<item1>",methods = ["GET"])
# def get_method(item1):
#     name=request.args.get("name")
#     company=request.args.get("company")
#     item1_var= request.view_args['item1']
#     print(item1_var)
#     print("name= "+ name)
#     print("company= "+ company)
#     return_string= "name= "+ name + "|" + "company= "+ company
#     return return_string
    
 


    
    
    

if __name__== '__main__':
    app.run(debug=True)
