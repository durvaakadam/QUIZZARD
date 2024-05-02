import sys
from PyQt6.QtWidgets import *
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QDialog,QLineEdit
from PyQt6.uic import loadUi
from PyQt6.QtCore import Qt
import mysql.connector
import random 
import re
import pandas as pd
import smtplib
from email.mime.text import MIMEText
import json
from urllib.request import urlopen

def fetch_all_codes():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Durva2909#",
        database="durva"
    )
    cursor = conn.cursor()
    query = "SELECT DISTINCT code FROM quiz_que"
    cursor.execute(query)
    codes = [row[0] for row in cursor.fetchall()]
    cursor.close()
    conn.close()
    return codes

def fetch_questions_for_code(code):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Durva2909#",
        database="durva"
    )
    cursor = conn.cursor()
    query = "SELECT question, option1, option2, option3, option4, qno FROM quiz_que WHERE code = %s"
    cursor.execute(query, (code,))
    questions_data = cursor.fetchall()
    cursor.close()
    conn.close()

    questions = []
    for data in questions_data:
        question = {
            "text": data[0],
            "options": data[1:5],
            "qno": data[5]
        }
        questions.append(question)

    return questions

all_codes = fetch_all_codes()
all_questions = {}
for code in all_codes:
    questions = fetch_questions_for_code(code)
    all_questions[code] = questions

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        loadUi("student1.ui", self)
        self.pushButton.clicked.connect(self.gotoScreen2)
        
    def gotoScreen2(self):
        screen2 = Screen2()
        widget.addWidget(screen2)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class Screen2(QMainWindow):
    def __init__(self):
        super(Screen2,self).__init__()
        loadUi("screen2.ui",self)
        self.pushButton_4.clicked.connect(self.gotoScreen3)
        self.pushButton.clicked.connect(self.gotoMainWindow)
        self.pushButton_5.clicked.connect(self.gotoSignup)
        self.b3.clicked.connect(self.gotoSignupteach)
        self.pushButton_2.clicked.connect(self.gotoTeacherlogin)
        self.pushButton_3.clicked.connect(self.show_popup)


    def show_popup(self):
        # Create a QMessageBox
        QMessageBox.information(self, "Coming soon!", "This feature is coming soon!")

    def gotoScreen3(self):
        screen3 = Screen3()
        widget.addWidget(screen3)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotoMainWindow(self):
        mainwindow = MainWindow()
        widget.addWidget(mainwindow)
        widget.setCurrentIndex(widget.currentIndex() - 1)
    
    def gotoSignup(self):
        signup = Signup()
        widget.addWidget(signup)
        widget.setCurrentIndex(widget.currentIndex() + 2)

    def gotoSignupteach(self):
        signupteach = Signupteach()
        widget.addWidget(signupteach)
        widget.setCurrentIndex(widget.currentIndex() + 3)
    
    def gotoTeacherlogin(self):
        teacherlogin = Teacherlogin()
        widget.addWidget(teacherlogin)
        widget.setCurrentIndex(widget.currentIndex() + 5)


class Screen3(QMainWindow):
    def __init__(self):
        super(Screen3, self).__init__()
        loadUi("screen3.ui", self)
        self.pushButton.clicked.connect(self.gotoScreen2)
        self.loginbutton.clicked.connect(self.login)
       

    def gotoScreen2(self):      
        screen2 = Screen2()
        widget.addWidget(screen2)
        widget.setCurrentIndex(widget.currentIndex() - 1)

    def login(self):
        self.username = self.lineEdit.text()  # Store the entered username
        password = self.lineEdit_2.text()
        
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Durva2909#",
            database="durva"
        )

        cursor = conn.cursor()
        query = "SELECT username, password FROM student WHERE username = %s AND password = %s"
        data = (self.username, password)  # Use stored username here
        cursor.execute(query, data)
        result = cursor.fetchone()
        cursor.close()
        conn.close()

        if result:
            self.gotoStudentjoin()
            QMessageBox.information(self, "Success", "Login successful")
        else:
            QMessageBox.critical(self, "Error", "Invalid username or password")
    
    def gotoStudentjoin(self):
        studentjoin = Studentjoin()
        widget.addWidget(studentjoin)
        widget.setCurrentIndex(widget.currentIndex() + 3)

    




class Signup(QMainWindow):
    def __init__(self):
        super(Signup,self).__init__()
        loadUi("signup.ui",self)
        self.r2.clicked.connect(self.signup)
        self.pushButton_2.clicked.connect(self.gotoScreen2)
        self.pushButton.clicked.connect(self.gotoScreen3)

    def fetch_student_emails(self):
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Durva2909#",
            database="durva"
        )
        cursor = conn.cursor()
        query = "SELECT email FROM student"
        cursor.execute(query)
        emails = [row[0] for row in cursor.fetchall()]
        cursor.close()
        conn.close()
        return emails

    def gotoScreen2(self):
        screen2 = Screen2()
        widget.addWidget(screen2)
        widget.setCurrentIndex(widget.currentIndex() - 2)

    def gotoScreen3(self):
        screen3 = Screen3()
        widget.addWidget(screen3)
        widget.setCurrentIndex(widget.currentIndex() - 1)

    def signup(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        phone = self.lineEdit_5.text()
        email = self.lineEdit_6.text()

        if not all([username, password, phone, email]):
            QMessageBox.critical(self, "Error", "Please fill in all fields")
            return

        if not self.validate_email(email):
            QMessageBox.critical(self, "Error", "Please enter a valid email address")
            return

        if not self.validate_phone(phone):
            QMessageBox.critical(self, "Error", "Please enter a valid 10-digit phone number")
            return

        if not self.validate_password(password):
            QMessageBox.critical(self, "Error", "Password must contain at least one uppercase letter, one lowercase letter, one digit, and one special character")
            return

        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Durva2909#",
            database="durva"
        )

        cursor = conn.cursor()
        query = "INSERT INTO student(username, password,phone,email) VALUES (%s, %s,%s,%s)"
        data = (username,password,phone,email)
        cursor.execute(query, data)
        conn.commit()
        cursor.close()
        conn.close()
        QMessageBox.information(self, "Success", "Data entered successfully")

    def validate_email(self, email):
        # Check if the email ends with "@student.sfit.ac.in"
        return email.endswith("@gmail.com")

    def validate_phone(self, phone):
        return len(phone) == 10 and phone.isdigit()

    def validate_password(self, password):
        return any(c.isupper() for c in password) and \
               any(c.islower() for c in password) and \
               any(c.isdigit() for c in password) and \
               any(not c.isalnum() for c in password)


        
class Signupteach(QMainWindow):
    def __init__(self):
        super(Signupteach,self).__init__()
        loadUi("signupteach.ui",self)
        self.r2.clicked.connect(self.signupteach)
        self.pushButton_2.clicked.connect(self.gotoScreen2)
        self.pushButton.clicked.connect(self.gotoTeacherlogin)

    def gotoScreen2(self):
        screen2=Screen2()
        widget.addWidget(screen2)
        widget.setCurrentIndex(widget.currentIndex()-3)

    def gotoTeacherlogin(self):
        teacherlogin=Teacherlogin()
        widget.addWidget(teacherlogin)
        widget.setCurrentIndex(widget.currentIndex()+2)
        

    #MYSQL DATABASE
    def signupteach(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        phone = self.lineEdit_5.text()
        email = self.lineEdit_6.text()

        if not all([username, password, phone, email]):
            QMessageBox.critical(self, "Error", "Please fill in all fields")
            return

        if not self.validate_email(email):
            QMessageBox.critical(self, "Error", "Please enter a valid email address")
            return

        if not self.validate_phone(phone):
            QMessageBox.critical(self, "Error", "Please enter a valid 10-digit phone number")
            return

        if not self.validate_password(password):
            QMessageBox.critical(self, "Error", "Password must contain at least one uppercase letter, one lowercase letter, one digit, and one special character")
            return

        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Durva2909#",
            database="durva"
        )

        cursor = conn.cursor()
        query = "INSERT INTO teacher (username, password,phone,email) VALUES (%s, %s,%s,%s)"
        data = (username,password,phone,email)
        cursor.execute(query, data)
        conn.commit()
        cursor.close()
        conn.close()
        QMessageBox.information(self, "Success", "Data entered successfully")

    def validate_email(self, email):
        pattern = r"^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$"
        return re.match(pattern, email)

    def validate_phone(self, phone):
        return len(phone) == 10 and phone.isdigit()

    def validate_password(self, password):
        return any(c.isupper() for c in password) and \
               any(c.islower() for c in password) and \
               any(c.isdigit() for c in password) and \
               any(not c.isalnum() for c in password)
        

class Studentjoin(QMainWindow):
    def __init__(self):  
        super(Studentjoin, self).__init__()
        loadUi("studentjoin.ui", self)  # Load the UI file

        self.joinbutton.clicked.connect(self.attemptquiz)

    def attemptquiz(self):
        code = self.lineEdit.text()
        if code:  # Checking if the input is empty
            # Fetch organization information
            org_value = self.fetch_organization()
           
            if org_value:
                # Check if the code is correct and organization matches
                if self.check_code_correctness(code, org_value):
                    attempt_quiz = Attemptquiz(code)
                    widget.addWidget(attempt_quiz)
                    widget.setCurrentIndex(widget.currentIndex() + 6)
                else:
                    QMessageBox.critical(self, "Error", "Incorrect code or organization. Please enter a valid code and organization.")
            else:
                QMessageBox.critical(self, "Error", "Failed to fetch organization information. Please try again.")
        else:
            QMessageBox.critical(self, "Error", "Please enter a code")

    def fetch_organization(self):
        try:
            # Fetch organization information
            url = 'http://ipinfo.io/json'
            response = urlopen(url)
            data = json.load(response)
            return data.get('org', 'Unknown')  # Default to 'Unknown' if 'org' key is not present
        except Exception as e:
            print("Error fetching organization:", e)
            return None

    def check_code_correctness(self, code, org_value):
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Durva2909#",
                database="durva"
            )
            cursor = conn.cursor()

            # Execute a query to check if the code and organization exist in the database
            query = "SELECT COUNT(*) FROM quiz_que WHERE code = %s AND organization = %s"
            cursor.execute(query, (code, org_value))
            count = cursor.fetchone()[0]

            cursor.close()
            conn.close()

            # If count is greater than 0, it means the code and organization exist
            return count > 0
        except mysql.connector.Error as err:
            print("Error:", err)  # Handle the error appropriately
            return False


class Attemptquiz(QMainWindow):
    def __init__(self, code):
        super(Attemptquiz, self).__init__()
        self.code = code
        self.questions = []
        self.current_question_index = 0
        self.setup_ui()
        self.load_questions()
    
    def setup_ui(self):
        loadUi("attemptquiz.ui", self)
     
        # Highlight: Connect next_button to save_attempt method
        self.next_button.clicked.connect(self.save_attempt)
        self.next_button.clicked.connect(self.next_question)

    def load_questions(self):
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Durva2909#",
            database="durva"
        )
        cursor = conn.cursor()
        query = "SELECT question, option1, option2, option3, option4, qno FROM quiz_que WHERE code = %s"
        cursor.execute(query, (self.code,))
        questions_data = cursor.fetchall()
        cursor.close()

        for data in questions_data:
            question = {
                "text": data[0],
                "options": data[1:5],
                "qno": data[5]  # Fetch qno from database
            }
            self.questions.append(question)

        if self.questions:
            self.display_question(self.questions[0])
        else:
            QMessageBox.critical(self, "Error", "No questions found for the given code")
            app.exec()

    def display_question(self, question):
        self.question_label.setText(question["text"])
        self.option1_button.setText(question["options"][0])
        self.option2_button.setText(question["options"][1])
        self.option3_button.setText(question["options"][2])
        self.option4_button.setText(question["options"][3])
        self.label_2.setText(str(question["qno"]))  # Display qno in ques_no object

    def save_attempt(self):
        username = screen3.username
        radio_button = 1 if self.radioButton.isChecked() else (
            2 if self.radioButton_2.isChecked() else (
                3 if self.radioButton_3.isChecked() else 4
            )
        )

        if radio_button is not None:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Durva2909#",
                database="durva"
            )
            cursor = conn.cursor()

            # Fetch the current question number
            current_question = self.questions[self.current_question_index]
            current_question_number = current_question["qno"]

            # Retrieve correct_option for the current question
            query_correct_option = "SELECT correct_option FROM quiz_que WHERE code = %s AND qno = %s"
            cursor.execute(query_correct_option, (self.code, current_question_number))
            correct_option = cursor.fetchone()[0]

            # Determine marks
            marks = 2 if radio_button == correct_option else 0
            
            # Insert attempt into database with marks
            query_insert_attempt = "INSERT INTO attempted (username, radio_button, input_code, ques_no, marks) VALUES (%s, %s, %s, %s, %s)"
            data = (username, radio_button, self.code, current_question_number, marks)
            cursor.execute(query_insert_attempt, data)
            

            conn.commit()
            cursor.close()
            conn.close()

    def next_question(self):
        if self.current_question_index < len(self.questions) -1 :
            self.current_question_index += 1
            self.display_question(self.questions[self.current_question_index])
        else:
            QMessageBox.information(self, "End of Questions", "You have reached the end of the questions.")
            self.calculate_total_marks()
            

    def calculate_total_marks(self):
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Durva2909#",
            database="durva"
        )
        cursor = conn.cursor()
        
    # Fetch the total marks obtained by the user
       
        query_total_marks = "SELECT SUM(marks) FROM attempted WHERE input_code = %s"
        cursor.execute(query_total_marks, (self.code,))
        total_marks = cursor.fetchone()[0]
    
    
    # Fetch the benchmark for the code
        query_benchmark = "SELECT benchmark FROM bmark WHERE code = %s"
        cursor.execute(query_benchmark, (self.code,))
        benchmark = cursor.fetchone()[0]

        # Compare total marks with benchmark
        attendance_status = "present" if total_marks >= benchmark else "absent"
       
        # Display result in QMessageBox
        message = f"End of Questions\n\nTotal Marks: {total_marks}\nAttendance: {attendance_status}"
        QMessageBox.information(self, "End of Questions", message)

        self.transition_to_attendance(attendance_status, total_marks)
    

        query_truncate = "TRUNCATE TABLE attempted"
        cursor.execute(query_truncate)
        cursor.close()
        conn.close()

    def transition_to_attendance(self, attendance_status, total_marks):
        # Closing the current window
        self.close()

        # Opening the Attendance window
        self.attendance_page = Attendance()
        self.attendance_page.update_labels(attendance_status, total_marks)
        self.attendance_page.show()


    def store_total_marks(self, total_marks):
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Durva2909#",
            database="durva"
        )
        cursor = conn.cursor()

        # Insert total marks into the tmark table
        query_insert_total_marks = "INSERT INTO tmark (code, total_marks) VALUES (%s, %s)"
        data = (self.code, total_marks)
        cursor.execute(query_insert_total_marks, data)

        conn.commit()
        cursor.close()
        conn.close()

class Attendance(QMainWindow):
    def __init__(self):
        super(Attendance,self).__init__()
        loadUi("attendance.ui", self)
        
    def update_labels(self, attendance_status, total_marks):
        self.label.setText(attendance_status)
        self.label_2.setText(str(total_marks))


class Teacherlogin(QMainWindow):
    def __init__(self):
        super(Teacherlogin,self).__init__()
        loadUi("teacherlogin.ui", self)
        self.loginbutton.clicked.connect(self.login)
        self.pushButton.clicked.connect(self.gotoScreen2)


    def gotoScreen2(self):
        screen2=Screen2()
        widget.addWidget(screen2)
        widget.setCurrentIndex(widget.currentIndex()-5)

    def login(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Durva2909#",
            database="durva"
        )

        cursor = conn.cursor()
        query = "SELECT username, password FROM teacher WHERE username = %s AND password = %s"
        data = (username, password)
        cursor.execute(query, data)
        result = cursor.fetchone()
        cursor.close()
        conn.close()

        if result:
            self.gotoCreatequiz()
            QMessageBox.information(self, "Success", "Login successful")
        else:
            QMessageBox.critical(self, "Error", "Invalid username or password")

    def gotoCreatequiz(self):
        createquiz = Createquiz()
        widget.addWidget(createquiz)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class Createquiz(QMainWindow):
    def __init__(self):
        super(Createquiz,self).__init__()
        loadUi("createquiz.ui", self)
        
        self.pushButton.clicked.connect(self.gotoPublish)
        self.pushButton_4.clicked.connect(self.gotoScreen2)
        self.pushButton_2.clicked.connect(self.show_popup)
        self.pushButton_3.clicked.connect(self.show_popup)
    
    def show_popup(self):
        # Create a QMessageBox
        QMessageBox.information(self, "Coming soon!", "This feature is coming soon!")
        

    def gotoPublish(self):
        publish = Publish()
        widget.addWidget(publish)
        widget.setCurrentIndex(widget.currentIndex() + 2)
    
    def gotoScreen2(self):
        screen2 = Screen2()
        widget.addWidget(screen2)
        widget.setCurrentIndex(widget.currentIndex() - 6)


class Createque(QMainWindow):
    def __init__(self):
        super(Createque, self).__init__()
        loadUi("createque.ui", self)
        self.savebtn.clicked.connect(self.gotoAutocode)
        self.pushButton.clicked.connect(self.gotoCreatequiz)
        self.savebtn_2.clicked.connect(self.add_question)  # Connect savebtn_2 to add_question method
        self.savebtn.clicked.connect(self.save_questions)  # Connect savebtn to save_questions method
        self.question_count = 0  # Initialize question count
        self.label_3.setText(str(self.question_count + 1))  # Set initial label text

    def gotoAutocode(self):
        autocode=Autocode()
        widget.addWidget(autocode)
        widget.setCurrentIndex(widget.currentIndex() + 2)

    def gotoCreatequiz(self):
        createquiz = Createquiz()
        widget.addWidget(createquiz)
        widget.setCurrentIndex(widget.currentIndex() - 1)

    def add_question(self):
        # Increment question count
        self.question_count += 1

        # Retrieve question and options from UI
        question_text = self.question.toPlainText()
        option1_text = self.ans1.toPlainText()
        option2_text = self.ans2.toPlainText()
        option3_text = self.ans3.toPlainText()
        option4_text = self.ans4.toPlainText()

        # Determine correct option
        correct_option = 1
        if self.radioButton_2.isChecked():
            correct_option = 2
        elif self.radioButton_3.isChecked():
            correct_option = 3
        elif self.radioButton_4.isChecked():
            correct_option = 4

        # Store question data in a dictionary
        question_data = {
            "question_text": question_text,
            "options": [option1_text, option2_text, option3_text, option4_text],
            "correct_option": correct_option,
            "qno": self.question_count  # Incremented question count
        }

        # Store question data in a list
        if not hasattr(self, 'questions'):
            self.questions = []  # Initialize questions list
        self.questions.append(question_data)

        # Update label_3 text with the new question count
        self.label_3.setText(str(self.question_count + 1))

        # Clear input fields
        self.question.clear()
        self.ans1.clear()
        self.ans2.clear()
        self.ans3.clear()
        self.ans4.clear()
        self.radioButton.setChecked(True)  # Reset radio button

        QMessageBox.information(self, "Success", f"Question {self.question_count} added successfully")

    def save_questions(self):
    # Check if there are questions to save
        if hasattr(self, 'questions') and len(self.questions) > 0:
            self.add_question()  # Add pending question from UI if any

    # Check if there are questions to save after adding pending question
        if not hasattr(self, 'questions') or len(self.questions) == 0:
            QMessageBox.warning(self, "No Questions", "No questions added to save")
            return

        # Get the code
        
        url = 'http://ipinfo.io/json'
        response = urlopen(url)
        data = json.load(response)
        org_value = data.get('org', 'Unknown')  # Default to 'Unknown' if 'org' key is not present

        code = autocode.label_2.text()

        # Save each question to the database
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Durva2909#",
            database="durva"
        )

        cursor = conn.cursor()
        query = "INSERT INTO quiz_que (question, option1, option2, option3, option4, correct_option, code, qno,organization) VALUES (%s, %s, %s, %s, %s, %s, %s, %s,%s)"
        
        for question_data in self.questions:
            data = (
                question_data["question_text"],
                question_data["options"][0],
                question_data["options"][1],
                question_data["options"][2],
                question_data["options"][3],
                question_data["correct_option"],
                code,
                question_data["qno"],
                org_value
                
            )
            cursor.execute(query, data)

        conn.commit()
        cursor.close()
        conn.close()

        # Clear questions list
        self.questions = []

        QMessageBox.information(self, "Success", "Questions saved successfully")

class Publish(QMainWindow):
    def __init__(self):
        super(Publish, self).__init__()
        loadUi("publish.ui", self)
        self.pushButton_2.clicked.connect(self.gotoCreateque)
        self.pushButton.clicked.connect(self.gotoCreatequiz)
        self.excel.clicked.connect(self.gotoExcel)
        self.excel.clicked.connect(self.save_benchmark)
        self.pushButton_2.clicked.connect(self.save_benchmark)
        
        self.benchmark = None
        
    def gotoCreatequiz(self):
        createquiz = Createquiz()
        widget.addWidget(createquiz)
        widget.setCurrentIndex(widget.currentIndex() - 2)

    def gotoCreateque(self):
        if self.bscore.text() == "":
            QMessageBox.warning(self, "Warning", "Please enter your benchmark before proceeding to Excel.")
        else:
            createque = Createque()
            widget.addWidget(createque)
            widget.setCurrentIndex(widget.currentIndex() - 1)
        
    def gotoExcel(self):
        if self.bscore.text() == "":
            QMessageBox.warning(self, "Warning", "Please enter your benchmark before proceeding.")
        else:
            excel = ExcelViewer()
            widget.addWidget(excel)
            widget.setCurrentIndex(widget.currentIndex() + 3)
        
    def save_benchmark(self):
        code = autocode.label_2.text()
        self.benchmark = self.bscore.text()
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Durva2909#",
            database="durva"
        )
    
        cursor = conn.cursor()
        query = "INSERT INTO bmark (code,benchmark) VALUES (%s,%s) "
        cursor.execute(query, (code, self.benchmark))
        conn.commit()
        cursor.close()
        conn.close()
        QMessageBox.information(self, "Success", "Benchmark saved succesfully!")


class ExcelViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("loadque.ui", self)
        self.loadButton_2.clicked.connect(self.load_excel_file)
        self.publish.clicked.connect(self.save_to_database)
        self.publish.clicked.connect(self.gotoAutocode)
        
    def gotoAutocode(self):
        autocode=Autocode()
        widget.addWidget(autocode)
        widget.setCurrentIndex(widget.currentIndex() - 2)

    def load_excel_file(self):
        file_dialog = QFileDialog()  
        options = file_dialog.options()  
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Excel File", "", "Excel Files (.xlsx);;All Files ()", options=options)
        if file_path:
            try:
                df = pd.read_excel(file_path)
                self.populate_table(df)  
                self.statusLabel.setText(f"Loaded file: {file_path}")
            except Exception as e:
                self.statusLabel.setText(f"Error loading file: {e}")

    def populate_table(self, df):
        if isinstance(df, pd.DataFrame):
            self.tableWidget.setRowCount(df.shape[0])
            self.tableWidget.setColumnCount(df.shape[1])
            self.tableWidget.setHorizontalHeaderLabels(df.columns)

            for i, row in df.iterrows():
                for j, value in enumerate(row):
                    if isinstance(value, (int, float)):
                        item = QTableWidgetItem()
                        item.setData(Qt.ItemDataRole.DisplayRole, value)
                    else:
                        item = QTableWidgetItem(str(value))
                    self.tableWidget.setItem(i, j, item)

    def save_to_database(self):
        
        
        url = 'http://ipinfo.io/json'
        response = urlopen(url)
        data = json.load(response)
        org_value = data.get('org', 'Unknown')  # Default to 'Unknown' if 'org' key is not present
        
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Durva2909#",
            database="durva"
        )
        cursor = conn.cursor()

        # Iterate through rows of the UI table widget
        for row in range(self.tableWidget.rowCount()):
            question_text = self.tableWidget.item(row, 0).text()
            option1 = self.tableWidget.item(row, 1).text()
            option2 = self.tableWidget.item(row, 2).text()
            option3 = self.tableWidget.item(row, 3).text()
            option4 = self.tableWidget.item(row, 4).text()
            code = autocode.label_2.text()
            correct_option= self.tableWidget.item(row, 5).text()  # Assuming correct option is in column 6

            # Insert data into the database
            query = "INSERT INTO quiz_que (question, option1, option2, option3, option4, correct_option,code,qno,organization) VALUES (%s,%s,%s, %s, %s, %s, %s, %s,%s)"
            data = (question_text, option1, option2, option3, option4, correct_option,code,row+1,org_value)
            cursor.execute(query, data)

        conn.commit()
        cursor.close()
        conn.close()

        QMessageBox.information(self, "Success", "Data saved to database successfully")

class Autocode(QMainWindow):
    def __init__(self):
        super(Autocode,self).__init__()
        loadUi("autocode.ui", self)
        self.pushButton_2.clicked.connect(self.gotoPublish)
        six_digit_code = self.generate_six_digit_code()
        self.label_2.setText(six_digit_code)
        self.pushButton.clicked.connect(self.send_emails)

    def send_emails(self):
        subject = "QUIZZARD"
        sender = "durvakadam204@gmail.com"
        password = "hgnduxjcdphyjlmw"

        # Retrieve email addresses from Signup class
        recipients = self.fetch_student_emails()

        if recipients:
            code = self.label_2.text()
            body = f"Your code is: {code}"
            self.send_email(subject, body, sender, recipients, password)
            QMessageBox.information(self, "Success", "Emails sent successfully.")
        else:
            print("No student emails found.")


    def fetch_student_emails(self):
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Durva2909#",
            database="durva"
        )
        cursor = conn.cursor()
        query = "SELECT email FROM student"
        cursor.execute(query)
        emails = [row[0] for row in cursor.fetchall()]
        cursor.close()
        conn.close()
        return emails

        print("2")

    def send_email(self, subject, body, sender, recipients, password):
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = ', '.join(recipients)
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
            smtp_server.login(sender, password)
            smtp_server.sendmail(sender, recipients, msg.as_string())
        print("Message sent")
        print("3")

    def generate_six_digit_code(self):
        six_digit_code = self.generate_six_digit_code()
        self.label_2.setText(six_digit_code)
        
    def generate_six_digit_code(self):
        return str(random.randint(100000, 999999))
    
    def gotoPublish(self):
        code = self.label_2.text()  # Retrieve the generated code
        createque.save_question(code)
        publish=Publish()
        widget.addWidget(publish)
        widget.setCurrentIndex(widget.currentIndex()-1)

    

app =QApplication(sys.argv)
widget=QStackedWidget()

mainwindow=MainWindow()
screen2=Screen2()
screen3=Screen3()
signup=Signup()
signupteach=Signupteach()
studentjoin=Studentjoin()
teacherlogin=Teacherlogin()
createquiz=Createquiz()
createque=Createque()
publish=Publish()
autocode=Autocode()
attemptquiz = Attemptquiz(code)  # Passing the fetched code here
excelviewer=ExcelViewer()
attendance=Attendance()

widget.addWidget(mainwindow)
widget.addWidget(screen2)
widget.addWidget(screen3)
widget.addWidget(signup)
widget.addWidget(signupteach)
widget.addWidget(studentjoin)
widget.addWidget(teacherlogin)
widget.addWidget(createquiz)
widget.addWidget(createque)
widget.addWidget(publish)
widget.addWidget(autocode)
widget.addWidget(attemptquiz)
widget.addWidget(excelviewer)
widget.addWidget(attendance)
widget.show()
app.exec()