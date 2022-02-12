from kivy.lang import Builder
from kivymd.app import MDApp
import sqlite3

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = "BlueGray"

        # Create database or connect to one
        conn = sqlite3.connect('first_db.db')

        # Create a cursor
        c = conn.cursor()
        # Create a table
        c.execute("""CREATE TABLE if not exists customers(
            name text
        )
        """)
        # Commit changes
        conn.commit()
        # close connection
        conn.close()

        return Builder.load_file('test_mysql.kv')

    def submit(self):
                conn = sqlite3.connect('first_db.db')

                # Create a cursor
                c = conn.cursor()
                # Add record
                c.execute("INSERT INTO customers VALUES (:first)",
                {
                    'first': self.root.ids.word_input.text,
                }
                )
                # Add a sms
                self.root.ids.word_label.text = f'{self.root.ids.word_input.text} Added'

                # clear the input box
                self.root.ids.word_input.text = ""
                # Commit changes
                conn.commit()
                # close connection
                conn.close()

    def records(self):
                        conn = sqlite3.connect('first_db.db')

                        # Create a cursor
                        c = conn.cursor()
                        # Grab records from database
                        c.execute("SELECT * FROM customers")
                        records = c.fetchall()

                        word = " "
                        # loop 
                        for record in records:
                            word = f'{word}\n{record[0]}'
                            self.root.ids.word_label.text = f'{word}'

                        # Commit changes
                        conn.commit()
                        # close connection
                        conn.close()


    

MainApp().run()