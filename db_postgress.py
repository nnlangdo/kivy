from kivy.lang import Builder
from kivymd.app import MDApp
import psycopg2

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = "BlueGray"

        # Create database or connect to one
        conn = psycopg2.connect(
        host = "ec2-44-193-188-118.compute-1.amazonaws.com",
        database = "d33plvmask99cq",
        user = "edcijjsianoskw",
        password = "395d33c3628a669d36af2bf20d1b3089055d268e0990db9f092ef4013f44353b",
        port = "5432",
        )
        # Create a cursor
        c = conn.cursor()
        # Create a table
        c.execute("""CREATE TABLE if not exists customers(
            name TEXT);
        """)
        # check if table is created 
        # c.execute("SELECT * FROM customers")
        # print(c.description)

        # Commit changes
        conn.commit()
        # close connection
        conn.close()

        return Builder.load_file('db_postgress.kv')

    def submit(self):
                conn = psycopg2.connect(
                host = "ec2-44-193-188-118.compute-1.amazonaws.com",
                database = "d33plvmask99cq",
                user = "edcijjsianoskw",
                password = "395d33c3628a669d36af2bf20d1b3089055d268e0990db9f092ef4013f44353b",
                port = "5432",
                )

                # Create a cursor
                c = conn.cursor()
                # Add record

                sql_command = "INSERT INTO customers (name) VALUES (%s)"
                values = (self.root.ids.word_input.text,)

                c.execute(sql_command, values)


                # Add a sms
                self.root.ids.word_label.text = f'{self.root.ids.word_input.text} Added'

                # clear the input box
                self.root.ids.word_input.text = ""
                # Commit changes
                conn.commit()
                # close connection
                conn.close()

    def records(self):
                        conn = psycopg2.connect(
                        host = "ec2-44-193-188-118.compute-1.amazonaws.com",
                        database = "d33plvmask99cq",
                        user = "edcijjsianoskw",
                        password = "395d33c3628a669d36af2bf20d1b3089055d268e0990db9f092ef4013f44353b",
                        port = "5432",
                        )

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