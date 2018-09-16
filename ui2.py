from flask import Flask, render_template, request, json, session, url_for, redirect, flash
app = Flask(__name__)
import MySQLdb
import folium
import googlemaps
from datetime import datetime
db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="root",  # your password
                     db="SHOP") 

@app.route("/dashboard", methods = ['POST', 'GET'])
def View():
       

        gmaps = googlemaps.Client(key='AIzaSyCsMLoWwHSQcf4b3xk27aaft9TZykMc4-o')


        now = datetime.now()
        directions_result = gmaps.directions("12, 77",
                                     "13, 77",
                                     mode="driving",
                                     avoid="ferries",
                                     departure_time=now
                                    )

        data1=directions_result[0]['legs'][0]['distance']['text']
        data2=directions_result[0]['legs'][0]['duration']['text']

        return render_template('blind.html', data='Harry',data1=data1, data2=data2)
@app.route("/track", methods = ['POST', 'GET'])
def map():
        
        latlon = [ (12, 77), (12.1, 77), (12.2, 77)]
        mapit = folium.Map( location=[12, 77], zoom_start=15 )
        for coord in latlon:
            folium.Marker( location=[ coord[0], coord[1] ] ).add_to( mapit )
        folium.PolyLine(latlon).add_to(mapit)
        mapit.save( 'C:/python27/templates/track.html')
        return render_template('track.html')

@app.route("/map", methods = ['POST', 'GET'])
def map1():
        #latlon = [ (12, 77), (12.1, 77), (12.2, 77)]
        mapit = folium.Map( location=[12, 77], zoom_start=15 )
        folium.Marker( location=[ 12, 77 ]).add_to( mapit )
        mapit.save( 'C:/python27/templates/map.html')
        return render_template('map.html')
@app.route("/signUp", methods = ['POST', 'GET'])
def signUp():
        error=" "
        if request.method=='POST':
                if 'user' in request.form:
                        #print"x"
                        username= str(request.form["user"])
                        print ('username', username)
                        name= str(request.form["name"])
                        phone= str(request.form["phone"])
                        altphone= str(request.form["altphone"])
                        passw= str(request.form["password"])
                        password = sha256_crypt.encrypt(passw)
                        email= str(request.form["email"])
                        zipp = str(request.form['zip'])
                        city = str(request.form['city'])
                        area = str(request.form['area'])
                        street = str(request.form['street'])
                        houseno = str(request.form['house_no'])
                        cur = db.cursor()
                        cur.execute("SELECT UNAME FROM LOGIN WHERE UNAME = %s", (username,))
                        test = cur.fetchone()
                        print ('test', test)
                        if test:
                                print ('REPEAT')
                                return redirect(url_for("signUp", error = 'Someone\'s already using that username, please choose another one.'))
                        cur = db.cursor()
                        global customerid
                        print (customerid)
                        cur.execute("INSERT INTO CUSTOMER(CUSTID, CNAME, CUSERNAME, CEMAIL, CHOUSENO, CSTREET, CAREA, CCITY, CZIP) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)", (customerid + 1,name, username, email,houseno, street, area, city, zipp))
                        db.commit()
                        customerid = customerid + 1
                        #print 'a'
                        cur.execute("INSERT INTO LOGIN(ID, UNAME, PASS, AUTH) VALUES(%s, %s, %s, %s)", (customerid, username, password, 'C'))
                        db.commit()
                        cur.execute('INSERT INTO PHONE(UID, PHONENO) VALUES (%s, %s)', (customerid, phone,))
                        db.commit()
                        if(altphone):
                                #print 'altphone', altphone
                                cur.execute('INSERT INTO PHONE(UID, PHONENO) VALUES (%s, %s)', (customerid, altphone,))
                                db.commit()   
                        #print 'b'
                        return redirect(url_for("login" ))
        return render_template("register.html", error = " ")

@app.route("/signin",  methods = ['POST', 'GET'])
def login():
        #print 'y'
        error=" "
        if request.method== 'POST':
                #print 'x'
                if 'user' in request.form:
                        username= str(request.form["user"])
                        password= str(request.form["password"])
                        print(username)
                        print (password)
                        cur = db.cursor()
                        cur.execute("SELECT UNAME FROM LOGIN WHERE UNAME='"+username+"'")
                        user=cur.fetchone()
                        if user == None:
                                return redirect(url_for("signUp", error = 'We can\'t find that username in our records, please check what you\'ve entered.'))
                        else:
                                cur.execute("SELECT PASS FROM LOGIN WHERE UNAME='"+username+"'")
                                passw = cur.fetchone()
                                print (str(passw[0]))
                                print (password)
                                if sha256_crypt.verify(password, str(passw[0])):
                                        #print 'They are equal'
                                        cur.execute("SELECT AUTH FROM LOGIN WHERE UNAME='"+username+"'")
                                        auth = cur.fetchone()
                                        if auth[0]=='E' or auth[0]=='A':
                                                cur.execute("SELECT EID FROM EMPLOYEE WHERE EUSERNAME LIKE %s", (username,))
                                                data = cur.fetchone()
                                                global login
                                                login=int(data[0])
                                                #print 'login', type(login)
                                                return redirect(url_for("View", eid = login))
                                                
                                        else:
                                                cur.execute("SELECT CUSTID FROM CUSTOMER WHERE CUSERNAME LIKE %s", (username,))
                                                data = cur.fetchone()
                                                #global login
                                                login=int(data[0])
                                                return redirect(url_for("View", custid = login))
                                        
                                else :
                                        return redirect(url_for("login"))
        return render_template("signin.html", error = error)


        
if __name__ == "__main__":
    app.run()
