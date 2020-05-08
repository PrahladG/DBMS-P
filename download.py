from flask import Flask,request,redirect,url_for,render_template,send_file,Blueprint
from flask_login import login_required, current_user,login_user,logout_user
from flask_wtf.file import FileField
from wtforms import SubmitField,TextField
import sqlite3
from flask_wtf import Form
from io import BytesIO
print("all are loaded")
download = Blueprint('download', __name__)
conn = sqlite3.connect('log/example.db')

@download.route('/uploads',methods=['GET','POST'])
@login_required
def uploads():
    k=request.form['long']
    if k =="algorithms":
        print(1)
        return algo_upload()
        
    elif k =="dbms":
        print(2)
        return dbms()
    elif k=="computerorganisation":
        return co()
    elif k=="linearalgebra":
        return la()
    elif k=="probability":
        return probability()
    elif k=="differential equations":
        return differentialequations()
    elif k=="calculus":
        return calculus()
    elif k=="datastructures":
        return datastructures()
    elif k=="c programming":
        return cp()
    elif k=="discrete structures for computing":
        return discrete()
    elif k=="concepts in engineering design":
        return ced()
    elif k=="systems thinking":
        return systems()
    elif k=="design history":
        return history()










































#_______________________________________________________________________________________________________________________________________________________
#history
#CAN UPLOAD TO history TABLE
@download.route('/history/upload',methods=['GET','POST'])
@login_required
def history():
    form=uploadform()
    if request.method=="POST":
        if form.validate_on_submit():
            file_name=form.file.data
            historybase(name=file_name.filename,data=file_name.read())
    return render_template("history.html",form=form)



#SHOWING THE AVAILABELE RECORDS
@download.route('/history/up', methods=["GET", "POST"])
@login_required
def history_up():
    form = uploadform()
    if request.method == "POST":
        conn= sqlite3.connect("log/example.db")
        cursor = conn.cursor()
        print("IN DATABASE FUNCTION ")
        c = cursor.execute(""" SELECT * FROM history """)
        records=c.fetchall()
        for i in range(len(records)):
            data=records[i][0]
            data_v=records[i][1]            
        return render_template("history_download.html", value=records)


#DOWNLOADING SPECIFIC FILE
@download.route('/history/down', methods=["GET", "POST"])
@login_required
def history_down():
    form = uploadform()
    i=int(request.form['number'])
    if request.method == "POST":
        conn= sqlite3.connect("log/example.db")
        cursor = conn.cursor()
        print("IN DATABASE FUNCTION ")
        c = cursor.execute(""" SELECT * FROM  history""")
        records=c.fetchall()
        data=records[i][0]
        data_v=records[i][1] 
        return send_file(BytesIO(data_v), attachment_filename='flask.pdf', as_attachment=False)

#CONNECT WITH APPROPRIATE DATABASE
def historybase(name,data):
    conn=sqlite3.connect('log/example.db')
    cursor=conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS history (name TEXT UNIQUE, data BLOP )')
    cursor.execute("""INSERT INTO history (name,data) VALUES (?,?)""",(name,data))
    conn.commit()
    cursor.close()
    conn.close()

#_________________________________________________________________________________________________________________________________













































#_______________________________________________________________________________________________________________________________________________________
#systems
#CAN UPLOAD TO systems TABLE
@download.route('/systems/upload',methods=['GET','POST'])
@login_required
def systems():
    form=uploadform()
    if request.method=="POST":
        if form.validate_on_submit():
            file_name=form.file.data
            systemsbase(name=file_name.filename,data=file_name.read())
    return render_template("systems.html",form=form)



#SHOWING THE AVAILABELE RECORDS
@download.route('/systems/up', methods=["GET", "POST"])
@login_required
def systems_up():
    form = uploadform()
    if request.method == "POST":
        conn= sqlite3.connect("example.db")
        cursor = conn.cursor()
        print("IN DATABASE FUNCTION ")
        c = cursor.execute(""" SELECT * FROM systems """)
        records=c.fetchall()
        for i in range(len(records)):
            data=records[i][0]
            data_v=records[i][1]            
        return render_template("systems_download.html", value=records)


#DOWNLOADING SPECIFIC FILE
@download.route('/systems/down', methods=["GET", "POST"])
@login_required
def systems_down():
    form = uploadform()
    i=int(request.form['number'])
    if request.method == "POST":
        conn= sqlite3.connect("example.db")
        cursor = conn.cursor()
        print("IN DATABASE FUNCTION ")
        c = cursor.execute(""" SELECT * FROM  systems""")
        records=c.fetchall()
        data=records[i][0]
        data_v=records[i][1] 
        return send_file(BytesIO(data_v), attachment_filename='flask.pdf', as_attachment=False)

#CONNECT WITH APPROPRIATE DATABASE
def systemsbase(name,data):
    conn=sqlite3.connect("example.db")
    cursor=conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS systems (name TEXT UNIQUE, data BLOP )')
    cursor.execute("""INSERT INTO systems (name,data) VALUES (?,?)""",(name,data))
    conn.commit()
    cursor.close()
    conn.close()

#_________________________________________________________________________________________________________________________________






























































#_______________________________________________________________________________________________________________________________________________________
#ced
#CAN UPLOAD TO ced TABLE
@download.route('/ced/upload',methods=['GET','POST'])
@login_required
def ced():
    form=uploadform()
    if request.method=="POST":
        if form.validate_on_submit():
            file_name=form.file.data
            cedbase(name=file_name.filename,data=file_name.read())
    return render_template("ced.html",form=form)



#SHOWING THE AVAILABELE RECORDS
@download.route('/ced/up', methods=["GET", "POST"])
@login_required
def ced_up():
    form = uploadform()
    if request.method == "POST":
        conn= sqlite3.connect("example.db")
        cursor = conn.cursor()
        print("IN DATABASE FUNCTION ")
        c = cursor.execute(""" SELECT * FROM ced """)
        records=c.fetchall()
        for i in range(len(records)):
            data=records[i][0]
            data_v=records[i][1]            
        return render_template("ced_download.html", value=records)


#DOWNLOADING SPECIFIC FILE
@download.route('/ced/down', methods=["GET", "POST"])
@login_required
def ced_down():
    form = uploadform()
    i=int(request.form['number'])
    if request.method == "POST":
        conn= sqlite3.connect("example.db")
        cursor = conn.cursor()
        print("IN DATABASE FUNCTION ")
        c = cursor.execute(""" SELECT * FROM  ced""")
        records=c.fetchall()
        data=records[i][0]
        data_v=records[i][1] 
        return send_file(BytesIO(data_v), attachment_filename='flask.pdf', as_attachment=False)

#CONNECT WITH APPROPRIATE DATABASE
def cedbase(name,data):
    conn=sqlite3.connect("example.db")
    cursor=conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS ced (name TEXT UNIQUE, data BLOP )')
    cursor.execute("""INSERT INTO ced (name,data) VALUES (?,?)""",(name,data))
    conn.commit()
    cursor.close()
    conn.close()

#_________________________________________________________________________________________________________________________________





























































































#_______________________________________________________________________________________________________________________________________________________
#discrete
# #CAN UPLOAD TO discrete TABLE
@download.route('/discrete/upload',methods=['GET','POST'])
@login_required
def discrete():
    form=uploadform()
    if request.method=="POST":
        if form.validate_on_submit():
            file_name=form.file.data
            discretebase(name=file_name.filename,data=file_name.read())
    return render_template("discrete.html",form=form)



#SHOWING THE AVAILABELE RECORDS
@download.route('/discrete/up', methods=["GET", "POST"])
@login_required
def discrete_up():
    form = uploadform()
    if request.method == "POST":
        conn= sqlite3.connect("example.db")
        cursor = conn.cursor()
        print("IN DATABASE FUNCTION ")
        c = cursor.execute(""" SELECT * FROM discrete """)
        records=c.fetchall()
        for i in range(len(records)):
            data=records[i][0]
            data_v=records[i][1]            
        return render_template("discrete_download.html", value=records)


#DOWNLOADING SPECIFIC FILE
@download.route('/discrete/down', methods=["GET", "POST"])
@login_required
def discrete_down():
    form = uploadform()
    i=int(request.form['number'])
    if request.method == "POST":
        conn= sqlite3.connect("example.db")
        cursor = conn.cursor()
        print("IN DATABASE FUNCTION ")
        c = cursor.execute(""" SELECT * FROM  discrete""")
        records=c.fetchall()
        data=records[i][0]
        data_v=records[i][1] 
        return send_file(BytesIO(data_v), attachment_filename='flask.pdf', as_attachment=False)

#CONNECT WITH APPROPRIATE DATABASE
def discretebase(name,data):
    conn=sqlite3.connect("example.db")
    cursor=conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS discrete (name TEXT UNIQUE, data BLOP )')
    cursor.execute("""INSERT INTO discrete (name,data) VALUES (?,?)""",(name,data))
    conn.commit()
    cursor.close()
    conn.close()

#_________________________________________________________________________________________________________________________________




































#_______________________________________________________________________________________________________________________________________________________
#c programming
# #CAN UPLOAD TO cp TABLE
@download.route('/cp/upload',methods=['GET','POST'])
@login_required
def cp():
    form=uploadform()
    if request.method=="POST":
        if form.validate_on_submit():
            file_name=form.file.data
            cpbase(name=file_name.filename,data=file_name.read())
    return render_template("cp.html",form=form)



#SHOWING THE AVAILABELE RECORDS
@download.route('/cp/up', methods=["GET", "POST"])
@login_required
def cp_up():
    form = uploadform()
    if request.method == "POST":
        conn= sqlite3.connect("example.db")
        cursor = conn.cursor()
        print("IN DATABASE FUNCTION ")
        c = cursor.execute(""" SELECT * FROM cp """)
        records=c.fetchall()
        for i in range(len(records)):
            data=records[i][0]
            data_v=records[i][1]            
        return render_template("cp_download.html", value=records)


#DOWNLOADING SPECIFIC FILE
@download.route('/cp/down', methods=["GET", "POST"])
@login_required
def cp_down():
    form = uploadform()
    i=int(request.form['number'])
    if request.method == "POST":
        conn= sqlite3.connect("example.db")
        cursor = conn.cursor()
        print("IN DATABASE FUNCTION ")
        c = cursor.execute(""" SELECT * FROM  cp""")
        records=c.fetchall()
        data=records[i][0]
        data_v=records[i][1] 
        return send_file(BytesIO(data_v), attachment_filename='flask.pdf', as_attachment=False)

#CONNECT WITH APPROPRIATE DATABASE
def cpbase(name,data):
    conn=sqlite3.connect("example.db")
    cursor=conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS cp (name TEXT UNIQUE, data BLOP )')
    cursor.execute("""INSERT INTO cp (name,data) VALUES (?,?)""",(name,data))
    conn.commit()
    cursor.close()
    conn.close()

#_________________________________________________________________________________________________________________________________
































































#_______________________________________________________________________________________________________________________________________________________
#datastructures ds table
# #CAN UPLOAD TO ds TABLE
@download.route('/ds/upload',methods=['GET','POST'])
@login_required
def datastructures():
    form=uploadform()
    if request.method=="POST":
        if form.validate_on_submit():
            file_name=form.file.data
            dsbase(name=file_name.filename,data=file_name.read())
    return render_template("ds.html",form=form)



#SHOWING THE AVAILABELE RECORDS
@download.route('/ds/up', methods=["GET", "POST"])
@login_required
def ds_up():
    form = uploadform()
    if request.method == "POST":
        conn= sqlite3.connect("example.db")
        cursor = conn.cursor()
        print("IN DATABASE FUNCTION ")
        c = cursor.execute(""" SELECT * FROM ds """)
        records=c.fetchall()
        for i in range(len(records)):
            data=records[i][0]
            data_v=records[i][1]            
        return render_template("ds_download.html", value=records)


#DOWNLOADING SPECIFIC FILE
@download.route('/ds/down', methods=["GET", "POST"])
@login_required
def ds_down():
    form = uploadform()
    i=int(request.form['number'])
    if request.method == "POST":
        conn= sqlite3.connect("example.db")
        cursor = conn.cursor()
        print("IN DATABASE FUNCTION ")
        c = cursor.execute(""" SELECT * FROM  ds""")
        records=c.fetchall()
        data=records[i][0]
        data_v=records[i][1] 
        return send_file(BytesIO(data_v), attachment_filename='flask.pdf', as_attachment=False)

#CONNECT WITH APPROPRIATE DATABASE
def dsbase(name,data):
    conn=sqlite3.connect("example.db")
    cursor=conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS ds (name TEXT UNIQUE, data BLOP )')
    cursor.execute("""INSERT INTO ds (name,data) VALUES (?,?)""",(name,data))
    conn.commit()
    cursor.close()
    conn.close()

#_________________________________________________________________________________________________________________________________










































#_______________________________________________________________________________________________________________________________________________________
#calculus cb table
# #CAN UPLOAD TO cb TABLE
@download.route('/c/upload',methods=['GET','POST'])
@login_required
def calculus():
    form=uploadform()
    if request.method=="POST":
        if form.validate_on_submit():
            file_name=form.file.data
            cbase(name=file_name.filename,data=file_name.read())
    return render_template("calculus.html",form=form)



#SHOWING THE AVAILABELE RECORDS
@download.route('/c/up', methods=["GET", "POST"])
@login_required
def c_up():
    form = uploadform()
    if request.method == "POST":
        conn= sqlite3.connect("example.db")
        cursor = conn.cursor()
        print("IN DATABASE FUNCTION ")
        c = cursor.execute(""" SELECT * FROM cb """)
        records=c.fetchall()
        for i in range(len(records)):
            data=records[i][0]
            data_v=records[i][1]            
        return render_template("calculus_download.html", value=records)


#DOWNLOADING SPECIFIC FILE
@download.route('/c/down', methods=["GET", "POST"])
@login_required
def c_down():
    form = uploadform()
    i=int(request.form['number'])
    if request.method == "POST":
        conn= sqlite3.connect("example.db")
        cursor = conn.cursor()
        print("IN DATABASE FUNCTION ")
        c = cursor.execute(""" SELECT * FROM  cb""")
        records=c.fetchall()
        data=records[i][0]
        data_v=records[i][1] 
        return send_file(BytesIO(data_v), attachment_filename='flask.pdf', as_attachment=False)

#CONNECT WITH APPROPRIATE DATABASE
def cbase(name,data):
    conn=sqlite3.connect("example.db")
    cursor=conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS cb (name TEXT UNIQUE, data BLOP )')
    cursor.execute("""INSERT INTO cb (name,data) VALUES (?,?)""",(name,data))
    conn.commit()
    cursor.close()
    conn.close()

#_________________________________________________________________________________________________________________________________






































































#_______________________________________________________________________________________________________________________________________________________
#differentialequations COURSE
#CAN UPLOAD TO de TABLE
@download.route('/de/upload',methods=['GET','POST'])
@login_required
def differentialequations():
    form=uploadform()
    if request.method=="POST":
        if form.validate_on_submit():
            file_name=form.file.data
            debase(name=file_name.filename,data=file_name.read())
    return render_template("de.html",form=form)



#SHOWING THE AVAILABELE RECORDS
@download.route('/de/up', methods=["GET", "POST"])
@login_required
def de_up():
    form = uploadform()
    if request.method == "POST":
        conn= sqlite3.connect("example.db")
        cursor = conn.cursor()
        print("IN DATABASE FUNCTION ")
        c = cursor.execute(""" SELECT * FROM de """)
        records=c.fetchall()
        for i in range(len(records)):
            data=records[i][0]
            data_v=records[i][1]            
        return render_template("de_download.html", value=records)


#DOWNLOADING SPECIFIC FILE
@download.route('/de/down', methods=["GET", "POST"])
@login_required
def de_down():
    form = uploadform()
    i=int(request.form['number'])
    if request.method == "POST":
        conn= sqlite3.connect("example.db")
        cursor = conn.cursor()
        print("IN DATABASE FUNCTION ")
        c = cursor.execute(""" SELECT * FROM  de""")
        records=c.fetchall()
        data=records[i][0]
        data_v=records[i][1] 
        return send_file(BytesIO(data_v), attachment_filename='flask.pdf', as_attachment=False)

#CONNECT WITH APPROPRIATE DATABASE
def debase(name,data):
    conn=sqlite3.connect("example.db")
    cursor=conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS de (name TEXT UNIQUE, data BLOP )')
    cursor.execute("""INSERT INTO de (name,data) VALUES (?,?)""",(name,data))
    conn.commit()
    cursor.close()
    conn.close()

#_________________________________________________________________________________________________________________________________






























































#_______________________________________________________________________________________________________________________________________________________
#probability COURSE
#CAN UPLOAD TO pb TABLE
@download.route('/pb/upload',methods=['GET','POST'])
@login_required
def probability():
    form=uploadform()
    if request.method=="POST":
        if form.validate_on_submit():
            file_name=form.file.data
            pbbase(name=file_name.filename,data=file_name.read())
    return render_template("pb.html",form=form)



#SHOWING THE AVAILABELE RECORDS
@download.route('/pb/up', methods=["GET", "POST"])
@login_required
def pb_up():
    form = uploadform()
    if request.method == "POST":
        conn= sqlite3.connect("example.db")
        cursor = conn.cursor()
        print("IN DATABASE FUNCTION ")
        c = cursor.execute(""" SELECT * FROM pb """)
        records=c.fetchall()
        for i in range(len(records)):
            data=records[i][0]
            data_v=records[i][1]            
        return render_template("pb_download.html", value=records)


#DOWNLOADING SPECIFIC FILE
@download.route('/pb/down', methods=["GET", "POST"])
def pb_down():
    form = uploadform()
    i=int(request.form['number'])
    if request.method == "POST":
        conn= sqlite3.connect("example.db")
        cursor = conn.cursor()
        print("IN DATABASE FUNCTION ")
        c = cursor.execute(""" SELECT * FROM  pb""")
        records=c.fetchall()
        data=records[i][0]
        data_v=records[i][1] 
        return send_file(BytesIO(data_v), attachment_filename='flask.pdf', as_attachment=False)

#CONNECT WITH APPROPRIATE DATABASE
def pbbase(name,data):
    conn=sqlite3.connect("example.db")
    cursor=conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS pb (name TEXT UNIQUE, data BLOP )')
    cursor.execute("""INSERT INTO pb (name,data) VALUES (?,?)""",(name,data))
    conn.commit()
    cursor.close()
    conn.close()

#_________________________________________________________________________________________________________________________________









































#_______________________________________________________________________________________________________________________________________________________
#linearalgebra COURSE
#CAN UPLOAD TO la TABLE
@download.route('/la/upload',methods=['GET','POST'])
@login_required
def la():
    form=uploadform()
    if request.method=="POST":
        if form.validate_on_submit():
            file_name=form.file.data
            labase(name=file_name.filename,data=file_name.read())
    return render_template("la.html",form=form)



#SHOWING THE AVAILABELE RECORDS
@download.route('/la/up', methods=["GET", "POST"])
def la_up():
    form = uploadform()
    if request.method == "POST":
        conn= sqlite3.connect("example.db")
        cursor = conn.cursor()
        print("IN DATABASE FUNCTION ")
        c = cursor.execute(""" SELECT * FROM la """)
        records=c.fetchall()
        for i in range(len(records)):
            data=records[i][0]
            data_v=records[i][1]            
        return render_template("la_download.html", value=records)


#DOWNLOADING SPECIFIC FILE
@download.route('/la/down', methods=["GET", "POST"])
def la_down():
    form = uploadform()
    i=int(request.form['number'])
    if request.method == "POST":
        conn= sqlite3.connect("example.db")
        cursor = conn.cursor()
        print("IN DATABASE FUNCTION ")
        c = cursor.execute(""" SELECT * FROM  la""")
        records=c.fetchall()
        data=records[i][0]
        data_v=records[i][1] 
        return send_file(BytesIO(data_v), attachment_filename='flask.pdf', as_attachment=False)

#CONNECT WITH APPROPRIATE DATABASE
def labase(name,data):
    conn=sqlite3.connect("example.db")
    cursor=conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS la (name TEXT UNIQUE, data BLOP )')
    cursor.execute("""INSERT INTO la (name,data) VALUES (?,?)""",(name,data))
    conn.commit()
    cursor.close()
    conn.close()

#_________________________________________________________________________________________________________________________________































#_______________________________________________________________________________________________________________________________________________________
#co COURSE
#CAN UPLOAD TO co TABLE
@download.route('/co/upload',methods=['GET','POST'])
@login_required
def co():
    form=uploadform()
    if request.method=="POST":
        if form.validate_on_submit():
            file_name=form.file.data
            cobase(name=file_name.filename,data=file_name.read())
    return render_template("co.html",form=form)



#SHOWING THE AVAILABELE RECORDS
@download.route('/co/up', methods=["GET", "POST"])
def co_up():
    form = uploadform()
    if request.method == "POST":
        conn= sqlite3.connect("example.db")
        cursor = conn.cursor()
        print("IN DATABASE FUNCTION ")
        c = cursor.execute(""" SELECT * FROM co """)
        records=c.fetchall()
        for i in range(len(records)):
            data=records[i][0]
            data_v=records[i][1]            
        return render_template("co_download.html", value=records)


#DOWNLOADING SPECIFIC FILE
@download.route('/co/down', methods=["GET", "POST"])
def co_down():
    form = uploadform()
    i=int(request.form['number'])
    if request.method == "POST":
        conn= sqlite3.connect("example.db")
        cursor = conn.cursor()
        print("IN DATABASE FUNCTION ")
        c = cursor.execute(""" SELECT * FROM  co""")
        records=c.fetchall()
        data=records[i][0]
        data_v=records[i][1] 
        return send_file(BytesIO(data_v), attachment_filename='flask.pdf', as_attachment=False)

#CONNECT WITH APPROPRIATE DATABASE
def cobase(name,data):
    conn=sqlite3.connect("example.db")
    cursor=conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS co (name TEXT UNIQUE, data BLOP )')
    cursor.execute("""INSERT INTO co (name,data) VALUES (?,?)""",(name,data))
    conn.commit()
    cursor.close()
    conn.close()

#_________________________________________________________________________________________________________________________________































#________________________________________________________________________________________________________________________________________________________________________________
#DBMS COURSE
#CAN UPLOAD TO DBMS TABLE





@download.route('/dbms/upload',methods=['GET','POST'])
@login_required
def dbms():
    form=uploadform()
    if request.method=="POST":
        if form.validate_on_submit():
            file_name=form.file.data
            dbmbase(name=file_name.filename,data=file_name.read())
    return render_template("dbms.html",form=form)



#SHOWING THE AVAILABELE RECORDS
@download.route('/dbms/up', methods=["GET", "POST"])
def dbms_up():
    form = uploadform()
    if request.method == "POST":
        conn= sqlite3.connect("example.db")
        cursor = conn.cursor()
        print("IN DATABASE FUNCTION ")
        c = cursor.execute(""" SELECT * FROM dbms """)
        records=c.fetchall()
        for i in range(len(records)):
            data=records[i][0]
            data_v=records[i][1]            
        return render_template("dbms_download.html", value=records)


#DOWNLOADING SPECIFIC FILE
@download.route('/dbms/down', methods=["GET", "POST"])
def dbms_down():
    form = uploadform()
    i=int(request.form['number'])
    if request.method == "POST":
        conn= sqlite3.connect("example.db")
        cursor = conn.cursor()
        print("IN DATABASE FUNCTION ")
        c = cursor.execute(""" SELECT * FROM  dbms""")
        records=c.fetchall()
        data=records[i][0]
        data_v=records[i][1] 
        return send_file(BytesIO(data_v), attachment_filename='flask.pdf', as_attachment=False)

#CONNECT WITH APPROPRIATE DATABASE
def dbmbase(name,data):
    conn=sqlite3.connect("example.db")
    cursor=conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS dbms (name TEXT UNIQUE, data BLOP )')
    cursor.execute("""INSERT INTO dbms (name,data) VALUES (?,?)""",(name,data))
    conn.commit()
    cursor.close()
    conn.close()

#______________________________________________________________________________________________________________________________________________________________________________

















        
#______________________________________________________________________________________________________________________________________________________________________________
#ALGORITHMS COURSE
#CAN UPLOAD TO ALGO TABLE
@download.route('/algorithms/upload',methods=['GET','POST'])
@login_required
def algo_upload():
    form=uploadform()
    if request.method=="POST":
        if form.validate_on_submit():
            file_name=form.file.data
            database(name=file_name.filename,data=file_name.read())
    return render_template("alone.html",form=form)



#SHOWING THE AVAILABELE RECORDS
@download.route('/algo/up', methods=["GET", "POST"])
def algo_up():
    form = uploadform()
    if request.method == "POST":
        conn= sqlite3.connect("example.db")
        cursor = conn.cursor()
        print("IN DATABASE FUNCTION ")
        c = cursor.execute(""" SELECT * FROM my_table """)
        records=c.fetchall()
        for i in range(len(records)):
            data=records[i][0]
            data_v=records[i][1]            
        return render_template("exp.html", value=records)


#DOWNLOADING SPECIFIC FILE
@download.route('/algo/down', methods=["GET", "POST"])
def algo_down():
    form = uploadform()
    i=int(request.form['number'])
    if request.method == "POST":
        conn= sqlite3.connect("example.db")
        cursor = conn.cursor()
        print("IN DATABASE FUNCTION ")
        c = cursor.execute(""" SELECT * FROM  my_table""")
        records=c.fetchall()
        data=records[i][0]
        data_v=records[i][1] 
        return send_file(BytesIO(data_v), attachment_filename='flask.pdf', as_attachment=False)

#CONNECT WITH APPROPRIATE DATABASE
def database(name,data):
    conn=sqlite3.connect("example.db")
    cursor=conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS my_table (name TEXT UNIQUE, data BLOP )')
    cursor.execute("""INSERT INTO my_table (name,data) VALUES (?,?)""",(name,data))
    conn.commit()
    cursor.close()
    conn.close()

#---------------------------------------------------------------------------------------------------
class uploadform(Form):
    file=FileField()
    submit=SubmitField("submit")
    down=SubmitField("download")
    download=SubmitField("download")

