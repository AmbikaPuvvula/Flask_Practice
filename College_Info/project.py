from flask import Flask,render_template,url_for,request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///collegeinfo.sqlite3'

mydb = SQLAlchemy(app)

class Signup(mydb.Model):
	id = mydb.Column(mydb.Integer,primary_key=True)
	s_name = mydb.Column(mydb.String(200))
	s_rno = mydb.Column(mydb.String(50))
	s_branch = mydb.Column(mydb.String(100))
	s_mno = mydb.Column(mydb.String(50))
	s_email = mydb.Column(mydb.String(200))

	def __init__(self,name,rollno,branch,mobileno,mailid):
		self.s_name = name
		self.s_rno = rollno
		self.s_branch = branch
		self.s_mno = mobileno
		self.s_email = mailid


@app.route('/myportal/signup',methods = ['GET','POST'])
def signup():
	if request.method == 'POST':
		data = request.form
		#print(data)
		stu_name = data['name']
		stu_rno = data['rno']
		stu_branch = data['branch']
		stu_mno = data['mno']
		stu_mail = data['email']
		#print(stu_name,stu_rno,stu_branch,stu_mno,stu_mail)

		sgn = Signup(stu_name,stu_rno,stu_branch,stu_mno,stu_mail)
		mydb.session.add(sgn)
		mydb.session.commit()
		return render_template('status.html')
	return render_template('signup.html')

@app.route('/myportal/studentlist')
def show():
	return render_template('showdetails.html',data = Signup.query.all())
if __name__ == '__main__':
	mydb.create_all()
	app.run(debug=True)