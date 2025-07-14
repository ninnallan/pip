from pymongo import MongoClient
from PyQt5 import QtCore, QtGui, QtWidgets

client = MongoClient("mongodb://localhost:27017/")
db = client["restaurant"]
collection = db["menu"]

d = {"soda": 5.2, "wine": 5.6, "burger": 1.99, "tea": 2.5, "milk": 2.4, "chicken": 3.4}
for key, value in d.items():
    if not collection.find_one({"product": key}):
        collection.insert_one({"product": key, "price": value})


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)

        # Product input
        self.label = QtWidgets.QLabel("Product:", self.centralwidget)
        self.label.setGeometry(50, 50, 60, 30)
        self.product_input = QtWidgets.QLineEdit(self.centralwidget)
        self.product_input.setGeometry(120, 50, 150, 30)

        # Price input
        self.label_3 = QtWidgets.QLabel("Price:", self.centralwidget)
        self.label_3.setGeometry(50, 100, 60, 30)
        self.price_input = QtWidgets.QLineEdit(self.centralwidget)
        self.price_input.setGeometry(120, 100, 150, 30)

        # Change price button
        self.pushButton = QtWidgets.QPushButton("Change the price", self.centralwidget)
        self.pushButton.setGeometry(300, 50, 150, 30)
        self.pushButton.clicked.connect(self.change_price)

        # Decrease price button
        self.pushButton_2 = QtWidgets.QPushButton("Decrease the price", self.centralwidget)
        self.pushButton_2.setGeometry(300, 100, 150, 30)
        self.pushButton_2.clicked.connect(self.decrease_price)

        # Output label
        self.output = QtWidgets.QTextEdit(self.centralwidget)
        self.output.setGeometry(50, 160, 500, 200)
        self.output.setReadOnly(True)

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.show_menu()

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle("Menu Manager")

    def decrease_price(self):
        product = self.product_input.text().strip()
        item = collection.find_one({"product": product})

        if item:
            new_price = float(item['price']) - 2
            if new_price < 0:
                new_price = 0.0
            collection.update_one({"product": product}, {"$set": {"price": new_price}})
        else:
            self.output.setText("პროდუქტი ბაზაში არ მოიძებნა")

        self.show_menu()

    def change_price(self):
        product = self.product_input.text().strip()
        try:
            new_price = float(self.price_input.text().strip())
        except ValueError:
            self.output.setText("ფასი არასწორ ფორმატშია")
            return

        existing = collection.find_one({"product": product})
        if existing:
            collection.update_one({"product": product}, {"$set": {"price": new_price}})
        else:
            collection.insert_one({"product": product, "price": new_price})

        self.show_menu()

    def show_menu(self):
        all_items = collection.find()
        result = "მიმდინარე მენიუ:\n"
        for item in all_items:
            result += f"{item['product']}: {item['price']}\n"
        self.output.setText(result)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
