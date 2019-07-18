from flask import Flask,redirect,url_for,render_template,request,flash
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydata.sqlite3'
db = SQLAlchemy(app)

class Sample(db.Model):
	id = db.Column(db.Integer,primary_key = True)
	name =db.Column(db.String(100))
	email = db.Column(db.String(50))
	phno = db.Column(db.String(200))

	def __init__(self,name,email,phno):
		self.name = name
		self.email = email
		self.phno = phno
@app.route('/welcome/<name>')
def msg1(name):
	return "<h2>Welcome "+ name + "</h2>"
@app.route('/welcome/<name>/<int:number>')
def msg2(name,number):
	return "<h2>Welcome "+ name +  "<br> My number is " + str(number) + "</h2>"
@app.route('/')
def msg3():
	return "<h2> Welcome to Python Lab </h2>"
@app.route('/home')
def home():
	return redirect(url_for('msg1',name="Ambika"))
@app.route('/admin')
def admin():
	return 'admin'
@app.route('/librarian')
def librarian():
	return 'librarian'
@app.route('/student')
def student():
	return 'student'
@app.route('/user/<name>')
def user(name):
	if name == 'admin':
		return redirect(url_for('admin'))
	if name == 'librarian':
		return redirect(url_for('librarian'))
	if name == 'student':
		return redirect(url_for('student'))
@app.route('/myhtml')
def myhtml():
	return render_template('sample.html')
@app.route('/myhtml/<name>')
def myhtml1(name):
	return render_template('sample.html',name1 = name)

@app.route('/mypage/register',methods = ['POST','GET'])
def register():
	if request.method == "POST":
		name = request.form['fname']
		mailid = request.form['emailid']
		mobileno = request.form['mobileno']
		flash("Registration Completed....")
		return render_template('loginform.html')
		#print(name,mailid,mobileno)
	flash("Register here....")
	return render_template('register.html')
@app.route('/mypage/login')
def login():
	return render_template('login.html')
@app.route('/mypage/loginform',methods = ['POST','GET'])
def loginform():
	if request.method == "POST":
		mailid = request.form['email']
		password = request.form['pswd']
		print(mailid,password)
	return render_template('loginform.html')
if __name__ == '__main__':
	app.secret_key = "secret"
	db.create_all()
	app.run(debug = True)