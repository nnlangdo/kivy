from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.label import Label
import mysql.connector 

Builder.load_file('crm.kv')
# Window.size = (400, 700)

class MyLayout(Widget):
    def clear(self):
        self.ids.first_name_input.text = ""
        self.ids.last_name_input.text = ""
        self.ids.address1_input.text = ""
        self.ids.address2_input.text = ""
        self.ids.city_input.text = ""
        self.ids.state_input.text = ""
        self.ids.zipcode_input.text = ""
        self.ids.country_input.text = ""
        self.ids.phone_input.text = ""
        self.ids.email_input.text = ""
        self.ids.paymentmethod_input.text = ""
        self.ids.discountcode_input.text = ""
        self.ids.pricepaid_input.text = ""

    # def add_customer(self):
    #     sql_command = "INSERT INTO customers (first_name, last_name, zipcode, price_paid, email, address_1, address_2, city, state, country, phone, payment_method, discount_code)\
    #         VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    #     values = (self.root.ids.first_name_input.text,
    #         self.ids.last_name_input.text,
    #         self.ids.address1_input.text,
    #         self.ids.address2_input.text,
    #         self.ids.city_input.text,
    #         self.ids.state_input.text,
    #         self.ids.zipcode_input.text,
    #         self.ids.country_input.text,
    #         self.ids.phone_input.text,
    #         self.ids.email_input.text,
    #         self.ids.paymentmethod_input.text,
    #         self.ids.discountcode_input.text,
    #         self.ids.pricepaid_input.text)
    #     my_cursor.execute(sql_command, values)

        # Commit the change to the database
        # mydb.commit()
        # clear fields

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "nnldg@2022",
    database = "nnldg",
)
# check to see connection to MYSQL was created
# print(mydb)

# create a cursur and initialize it
my_cursor = mydb.cursor()

# create database
# my_cursor.execute("CREATE DATABASE nnldg")

# Test database is created
# my_cursor.execute("SHOW DATABASES")
# for db in my_cursor:
#     print(db)

# Create a table
my_cursor.execute("CREATE TABLE IF NOT EXISTS customers (\
    first_name VARCHAR(255),\
    last_name VARCHAR(255),\
    zipcode INT(6),\
    price_paid DECIMAL(10,2),\
    user_id INT AUTO_INCREMENT PRIMARY KEY)")

# Alter table
'''
my_cursor.execute("ALTER TABLE customers ADD ( \
    email VARCHAR(255),\
    address_1 VARCHAR(255),\
    address_2 VARCHAR(255),\
    city VARCHAR(50),\
    state VARCHAR(50),\
    country VARCHAR(255),\
    phone VARCHAR(255),\
    payment_method VARCHAR(50),\
    discount_code VARCHAR(255))")
'''


# show table
# my_cursor.execute("SELECT * FROM customers")
# print(my_cursor.description)
# for thing in my_cursor.description:
    # print(thing)

# create labels


class AwesomeApp(App):
    def build(self):
        Window.clearcolor = (0, 1, 1, 1)
        return MyLayout()

if __name__=='__main__':
    AwesomeApp().run()
