from flask import Flask,redirect,url_for,render_template,request,flash
app = Flask(__name__)
@app.route('/home/loginform',methods = ['POST','GET'])
def loginform():
	if request.method == 'POST':
		mailid = request.form['email']
		password = request.form['pswd']
		#print(mailid,password)
		return render_template('details.html',email = mailid,pswd = password)
	return render_template('loginform.html')

@app.route('/home/registerform',methods = ['POST','GET'])
def registerform():
	if request.method == 'POST':
		name = request.form['name']
		rollno = request.form['rno']
		branch = request.form['branch']
		email = request.form['email']

		#print(mailid,password)
		return render_template('details.html',name = name,rollno = rollno,branch = branch,email = email)
	return render_template('registerform.html')


if __name__ == '__main__':
	app.secret_key = "key"
	app.run(debug=True)