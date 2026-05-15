from flask import Flask, render_template, request, redirect, url_for
from db_config import get_connection

app = Flask(__name__)

db = get_connection()
cursor = db.cursor()


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/student', methods=['GET', 'POST'])
def student():
    if request.method == 'POST':
        
        enrollment = request.form['enrollment']
        name = request.form['name']
        email = request.form['email']
        course = request.form['course']
        stream = request.form['stream']
        year = int(request.form['year'])
        semester = int(request.form['semester'])
        fees_for = request.form['fees_for']
        amount = float(request.form['amount'])
        date = request.form['date']
        section = request.form['section']
        roll_no = int(request.form['roll_no'])
        bank_branch = request.form['bank_branch']
        account_number = request.form['account_number']
        utr_number = request.form['ifsc_code']

       
        query = """
        INSERT INTO payments (enrollment, name, email, course, stream, year, semester, fees_for, amount, date, section, roll_no, bank_branch, account_number, utr_number)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        try:
            cursor.execute(query, (enrollment, name, email, course, stream, year, semester, fees_for, amount, date, section, roll_no, bank_branch, account_number, utr_number ))
            db.commit()
            return render_template('payment_receipt.html', name=name, amount=amount, date=date)
        except Exception as e:
            db.rollback()
            return f"Error: {str(e)}", 500
    return render_template('student_form.html')

@app.route('/staff', methods=['GET', 'POST'])
def staff():
    if request.method == 'POST':
        password = request.form['password']
        if password == "admin123":  
            return redirect(url_for('staff_dashboard'))
        else:
            return "Invalid password", 403
    return render_template('staff_login.html')

@app.route('/staff_dashboard')
def staff_dashboard():
    return render_template('staff_dashboard.html')

@app.route('/view_all')
def view_all():
    
    query = """
    SELECT * FROM payments ORDER BY year ASC, semester ASC
    """
    cursor.execute(query)
    payments = cursor.fetchall()

    
    query = "SELECT SUM(amount) FROM payments"
    cursor.execute(query)
    total_amount = cursor.fetchone()[0]

    return render_template('view_all.html', payments=payments, total_amount=total_amount)

@app.route('/student_details', methods=['GET', 'POST'])
def student_details():
    if request.method == 'POST':
        enrollment = request.form['enrollment']
        query = "SELECT * FROM payments WHERE enrollment = %s"
        cursor.execute(query, (enrollment,))
        student = cursor.fetchone()

        if student:
            return render_template('student_details.html', student=student)
        else:
            return "This student has not paid.", 404
    return render_template('student_details.html')

if __name__ == '__main__':
    app.run(debug=True)
