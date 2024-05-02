
import sys
from PyQt6.QtWidgets import *
from PyQt6.uic import loadUi
import mysql.connector
import random 
import re

def fetch_questions_for_code(code):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Durva2909#",
        database="durva"
    )
    cursor = conn.cursor()
    query = "SELECT question, option1, option2, option3, option4 FROM quiz_que WHERE code = %s"
    cursor.execute(query, (code,))
    questions_data = cursor.fetchall()
    cursor.close()
    conn.close()

    questions = []
    for data in questions_data:
        question = {
            "text": data[0],
            "options": data[1:5]
        }
        questions.append(question)

    return questions

# Function to fetch questions based on the entered code
def fetch_questions_for_entered_code(entered_code):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Durva2909#",
        database="durva"
    )
    cursor = conn.cursor()
    query = "SELECT question, option1, option2, option3, option4 FROM quiz_que WHERE code = %s"
    cursor.execute(query, (entered_code,))
    questions_data = cursor.fetchall()
    cursor.close()
    conn.close()

    questions = []
    for data in questions_data:
        question = {
            "text": data[0],
            "options": data[1:5]
        }
        questions.append(question)

    return questions

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
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Durva2909#",
            database="durva"
        )

        cursor = conn.cursor()
        query = "SELECT username, password FROM student WHERE username = %s AND password = %s"
        data = (username, password)
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

    def gotoScreen2(self):
        screen2 = Screen2()
        widget.addWidget(screen2)
        widget.setCurrentIndex(widget.currentIndex() - 2)

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
        pattern = r"^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$"
        return re.match(pattern, email)

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

    def gotoScreen2(self):
        screen2=Screen2()
        widget.addWidget(screen2)
        widget.setCurrentIndex(widget.currentIndex()-3)
        

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

        self.joinbutton.clicked.connect(self.fetch_and_display_questions)

    def fetch_and_display_questions(self):
        entered_code = self.lineEdit.text() 
        if entered_code:  # Checking if the input is empty
            questions = fetch_questions_for_entered_code(entered_code)
            if questions:
                # Display questions on the UI
                self.display_questions(questions)
            else:
                QMessageBox.critical(self, "Error", "No questions found for the entered code")
        else:
            QMessageBox.critical(self, "Error", "Please enter a code")

    def display_questions(self, questions):
        # Implement code to display questions on the UI
        pass


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
        self.next_button.clicked.connect(self.next_question)

    def load_questions(self):
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Durva2909#",
            database="durva"
        )
        cursor = conn.cursor()
        query = "SELECT question, option1, option2, option3, option4 FROM quiz_que WHERE code = %s"
        cursor.execute(query, (self.code,))
        questions_data = cursor.fetchall()
        cursor.close()
        conn.close()

        for data in questions_data:
            question = {
                "text": data[0],
                "options": data[1:5]
            }
            self.questions.append(question)

        if self.questions:
            self.display_question(self.questions[0])
        else:
            QMessageBox.critical(self, "Error", "No questions found for the given code")

    def next_question(self):
        if self.current_question_index < len(self.questions) - 1:
            self.current_question_index += 1
            self.display_question(self.questions[self.current_question_index])
        else:
            QMessageBox.information(self, "Info", "No more questions")

    def display_question(self, question):
        self.question_label.setText(question["text"])
        self.option1_button.setText(question["options"][0])
        self.option2_button.setText(question["options"][1])
        self.option3_button.setText(question["options"][2])
        self.option4_button.setText(question["options"][3])


class Teacherlogin(QMainWindow):
    def __init__(self):
        super(Teacherlogin,self).__init__()
        loadUi("teacherlogin.ui", self)
        self.loginbutton.clicked.connect(self.login)

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
        
        self.pushButton.clicked.connect(self.gotoCreateque)
        self.pushButton_4.clicked.connect(self.gotoScreen2)

    def gotoCreateque(self):
        createque = Createque()
        widget.addWidget(createque)
        widget.setCurrentIndex(widget.currentIndex() + 1)
    
    def gotoScreen2(self):
        screen2 = Screen2()
        widget.addWidget(screen2)
        widget.setCurrentIndex(widget.currentIndex() - 6)

class Createque(QMainWindow):
    def __init__(self):
        super(Createque,self).__init__()
        loadUi("createque.ui", self)
        self.savebtn.clicked.connect(self.gotoPublish)
        self.pushButton.clicked.connect(self.gotoCreatequiz)
        self.savebtn.clicked.connect(self.save_question)
        
    def gotoPublish(self):
        publish = Publish()
        widget.addWidget(publish)
        widget.setCurrentIndex(widget.currentIndex() + 1)
    
    def gotoCreatequiz(self):
        createquiz = Createquiz()
        widget.addWidget(createquiz)
        widget.setCurrentIndex(widget.currentIndex() - 1)

    def save_question(self,code):
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
        
        code = autocode.label_2.text()

        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Durva2909#",
            database="durva"
        )
    
        cursor = conn.cursor()
        query = "INSERT INTO quiz_que (question, option1, option2, option3, option4, correct_option, code) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        data = (question_text, option1_text, option2_text, option3_text, option4_text, correct_option, code)
        cursor.execute(query, data)
        conn.commit()
        cursor.close()
        conn.close()
        QMessageBox.information(self, "Success", "Question saved successfully")

class Publish(QMainWindow):
    def __init__(self):
        super(Publish, self).__init__()
        loadUi("publish.ui", self)
        self.pushButton_2.clicked.connect(self.gotoAutocode)
        self.pushButton.clicked.connect(self.gotoCreateque)

    def gotoAutocode(self):
        autocode = Autocode()
        widget.addWidget(autocode)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotoCreateque(self):
        createque = Createque()
        widget.addWidget(createque)
        widget.setCurrentIndex(widget.currentIndex() - 1)

class Autocode(QMainWindow):
    def __init__(self):
        super(Autocode,self).__init__()
        loadUi("autocode.ui", self)
        self.pushButton_2.clicked.connect(self.gotoPublish)
        six_digit_code = self.generate_six_digit_code()
        self.label_2.setText(six_digit_code)

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
widget.show()
app.exec()


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
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Durva2909#",
            database="durva"
        )

        cursor = conn.cursor()
        query = "SELECT username, password FROM student WHERE username = %s AND password = %s"
        data = (username, password)
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

    def gotoScreen2(self):
        screen2 = Screen2()
        widget.addWidget(screen2)
        widget.setCurrentIndex(widget.currentIndex() - 2)

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
        pattern = r"^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$"
        return re.match(pattern, email)

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

    def gotoScreen2(self):
        screen2=Screen2()
        widget.addWidget(screen2)
        widget.setCurrentIndex(widget.currentIndex()-3)
        

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
            attempt_quiz = Attemptquiz(code)
            widget.addWidget(attempt_quiz)
            widget.setCurrentIndex(widget.currentIndex() + 6)
        else:
            QMessageBox.critical(self, "Error", "Please enter a code")

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
        self.next_button.clicked.connect(self.next_question)

    def load_questions(self):
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Durva2909#",
            database="durva"
        )
        cursor = conn.cursor()
        query = "SELECT question, option1, option2, option3, option4 FROM quiz_que WHERE code = %s"
        cursor.execute(query, (self.code,))
        questions_data = cursor.fetchall()
        cursor.close()
        conn.close()

        for data in questions_data:
            question = {
                "text": data[0],
                "options": data[1:5]
            }
            self.questions.append(question)

        if self.questions:
            self.display_question(self.questions[0])
        else:
            QMessageBox.critical(self, "Error", "No questions found for the given code")

    def next_question(self):
        if self.current_question_index < len(self.questions) - 1:
            self.current_question_index += 1
            self.display_question(self.questions[self.current_question_index])
        else:
            QMessageBox.information(self, "Info", "No more questions")

    def display_question(self, question):
        self.question_label.setText(question["text"])
        self.option1_button.setText(question["options"][0])
        self.option2_button.setText(question["options"][1])
        self.option3_button.setText(question["options"][2])
        self.option4_button.setText(question["options"][3])


class Teacherlogin(QMainWindow):
    def __init__(self):
        super(Teacherlogin,self).__init__()
        loadUi("teacherlogin.ui", self)
        self.loginbutton.clicked.connect(self.login)

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
        
        self.pushButton.clicked.connect(self.gotoCreateque)
        self.pushButton_4.clicked.connect(self.gotoScreen2)

    def gotoCreateque(self):
        createque = Createque()
        widget.addWidget(createque)
        widget.setCurrentIndex(widget.currentIndex() + 1)
    
    def gotoScreen2(self):
        screen2 = Screen2()
        widget.addWidget(screen2)
        widget.setCurrentIndex(widget.currentIndex() - 6)

class Createque(QMainWindow):
    def __init__(self):
        super(Createque,self).__init__()
        loadUi("createque.ui", self)
        self.savebtn.clicked.connect(self.gotoPublish)
        self.pushButton.clicked.connect(self.gotoCreatequiz)
        self.savebtn.clicked.connect(self.save_question)
        
    def gotoPublish(self):
        publish = Publish()
        widget.addWidget(publish)
        widget.setCurrentIndex(widget.currentIndex() + 1)
    
    def gotoCreatequiz(self):
        createquiz = Createquiz()
        widget.addWidget(createquiz)
        widget.setCurrentIndex(widget.currentIndex() - 1)

    def save_question(self,code):
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
        
        code = autocode.label_2.text()

        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Durva2909#",
            database="durva"
        )
    
        cursor = conn.cursor()
        query = "INSERT INTO quiz_que (question, option1, option2, option3, option4, correct_option, code) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        data = (question_text, option1_text, option2_text, option3_text, option4_text, correct_option, code)
        cursor.execute(query, data)
        conn.commit()
        cursor.close()
        conn.close()
        QMessageBox.information(self, "Success", "Question saved successfully")

class Publish(QMainWindow):
    def __init__(self):
        super(Publish, self).__init__()
        loadUi("publish.ui", self)
        self.pushButton_2.clicked.connect(self.gotoAutocode)
        self.pushButton.clicked.connect(self.gotoCreateque)

    def gotoAutocode(self):
        autocode = Autocode()
        widget.addWidget(autocode)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotoCreateque(self):
        createque = Createque()
        widget.addWidget(createque)
        widget.setCurrentIndex(widget.currentIndex() - 1)

class Autocode(QMainWindow):
    def __init__(self):
        super(Autocode,self).__init__()
        loadUi("autocode.ui", self)
        self.pushButton_2.clicked.connect(self.gotoPublish)
        six_digit_code = self.generate_six_digit_code()
        self.label_2.setText(six_digit_code)

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
attemptquiz = Attemptquiz(code)
all_codes = fetch_all_codes()

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
widget.show()
app.exec()
