from kivy.lang import Builder
from kivymd.app import MDApp
import mysql.connector

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = "BlueGray"

        # Create database or connect to one
        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "nksprod@L2022",
            database = "second_db",
        )
        # Create a cursor
        c = mydb.cursor()
        # Create a table
        c.execute("CREATE DATABASE IF NOT EXISTS second_db")
        # check the database created
        # c.execute("SHOW DATABASES")
        # for db in c:
        #     print(db)

        # Create a Table
        c.execute("""CREATE TABLE if not exists customers(
            name VARCHAR(50)
        )
        """)
        # check if table is created 
        # c.execute("SELECT * FROM customers")
        # print(c.description)

        # Commit changes
        mydb.commit()
        # close connection
        mydb.close()

        return Builder.load_file('db_mysql.kv')

    def submit(self):
                mydb = mysql.connector.connect(
                host = "localhost",
                user = "root",
                passwd = "nksprod@L2022",
                database = "second_db",
                )

                # Create a cursor
                c = mydb.cursor()
                # Add record

                sql_command = "INSERT INTO customers (name) VALUES (%s)"
                values = (self.root.ids.word_input.text,)

                c.execute(sql_command, values)


                # Add a sms
                self.root.ids.word_label.text = f'{self.root.ids.word_input.text} Added'

                # clear the input box
                self.root.ids.word_input.text = ""
                # Commit changes
                mydb.commit()
                # close connection
                mydb.close()

    def records(self):
                        mydb = mysql.connector.connect(
                        host = "localhost",
                        user = "root",
                        passwd = "nksprod@L2022",
                        database = "second_db",
                        )


                        # Create a cursor
                        c = mydb.cursor()
                        # Grab records from database
                        c.execute("SELECT * FROM customers")
                        records = c.fetchall()

                        word = " "
                        # loop 
                        for record in records:
                            word = f'{word}\n{record[0]}'
                            self.root.ids.word_label.text = f'{word}'

                        # Commit changes
                        mydb.commit()
                        # close connection
                        mydb.close()


    

MainApp().run()