import tkinter as tk
import backend
from tkinter import ttk, messagebox
from tkinter import *
from PIL import ImageTk, Image







def f_main():
    root = Tk()
    root.geometry("800x500")
    root["bg"] = "gray22"
    root.title("BadBet")


    def create_database():
        newWindow = Tk()
        newWindow.title = "Create database"
        newWindow.geometry("200x200")

        
        def clicked():
            name_db = txt.get()
            a = backend.create_db(name_db)
            messagebox.showinfo(title="Information", message=a)
            newWindow.destroy()
        

        Label(newWindow, text = "Enter the name of database").place(x=25, y=20)
        txt = Entry(newWindow)
        txt.place(x=40,y=50)
        Button(newWindow, text="Create", command=clicked).place(x=70, y=80) 


    def connect_database():
        newWindow = Tk()
        newWindow.title = "Connect database"
        newWindow.geometry("200x200")

        
        def clicked():
            name_db = txt.get()
            a = backend.connect_db(name_db)
            messagebox.showinfo(title="Information", message=a)
            newWindow.destroy()
        

        Label(newWindow, text = "Enter the name of database").place(x=25, y=20)
        txt = Entry(newWindow)
        txt.place(x=40,y=50)
        Button(newWindow, text="Connect", command=clicked).place(x=70, y=80)


    def delete_database():
        newWindow = Tk()
        newWindow.title = "Delete database"
        newWindow.geometry("200x200")

        
        def clicked():
            name_db = txt.get()
            text = backend.delete_db(name_db)
            messagebox.showinfo(title="Информационное сообщение", message=text, clicked=newWindow.destroy())
        

        Label(newWindow, text = "Enter the name of database").place(x=25, y=20)
        txt = Entry(newWindow)
        txt.place(x=40,y=50)
        Button(newWindow, text="Delete", command=clicked).place(x=70, y=80) 

        
    def show_table():
        newWindow = Tk()
        newWindow.title("Show table")
        newWindow.geometry("800x400")

        def show_treeview(heads, data):
            table = ttk.Treeview(newWindow, columns=heads, show='headings')
            for header in heads:
                table.heading(header, text=header, anchor='center')
                table.column(header, anchor='center')
            for row in data:
                table.insert('', tk.END, values=row)

            table.pack(expand=False, fill=tk.Y, side='bottom', anchor='s')
            

        
        def clicked_teams():
            data = backend.show_table_teams()
            heads = ['id', 'team_name']
            show_treeview(heads, data)

        def clicked_bets():
            data = backend.show_table_bets()
            heads = ['bet_id', 'user_id', 'match_id', 'outcome', 'sum_of_bet', 'coef', 'winning']
            show_treeview(heads, data)

        def clicked_players():
            data = backend.show_table_players()
            heads = ['player_id', 'player_name', 'player_position', 'team_name']
            show_treeview(heads, data)

        def clicked_matches():
            data = backend.show_table_matches()
            heads = ['match_id', 'match_date', 'home team', 'away team', 'match_result', 'score_home', 'score_away']
            show_treeview(heads, data)

        def clicked_users():
            data = backend.show_table_users()
            heads = ['user_id', 'phone number', 'first name', 'last name', 'gender', 'age']
            show_treeview(heads, data)


        Label(newWindow, text = "Choose the table").place(x=10, y=10)
        Button(newWindow, text="teams", height=2, width=10, command=clicked_teams).place(x=10, y=40) 
        Button(newWindow, text="players", height=2, width=10, command=clicked_players).place(x=90, y=40) 
        Button(newWindow, text="bets", height=2, width=10, command=clicked_bets).place(x=170, y=40) 
        Button(newWindow, text="matches", height=2, width=10, command=clicked_matches).place(x=250, y=40) 
        Button(newWindow, text="users", height=2, width=10, command=clicked_users).place(x=330, y=40) 
        newWindow.mainloop()


    def clean_table_bets():
        backend.delete_all_bets()
        messagebox.showinfo(title="Информационное сообщение", message='Table ''bets'' was cleaned')


    def clean_all_tables():
        backend.delete_all_tables()
        messagebox.showinfo(title="Информационное сообщение", message='All tables were cleaned')


    def delete_bet():
        newWindow = Tk()
        newWindow.title = "Delete bet"
        newWindow.geometry("200x200")

        
        def clicked():
            aid = txt.get()
            backend.f_delete_bet(aid)
            messagebox.showinfo(title="Информационное сообщение", message='Bet is deleted')
            newWindow.destroy()
        

        Label(newWindow, text = "Enter the id of bet").place(x=25, y=20)
        txt = Entry(newWindow)
        txt.place(x=40,y=50)
        Button(newWindow, text="Delete", command=clicked).place(x=70, y=80) 


    def delete_match():
        newWindow = Tk()
        newWindow.title = "Delete match"
        newWindow.geometry("200x200")

        
        def clicked():
            aid = txt.get()
            backend.f_delete_match(aid)
            messagebox.showinfo(title="Информационное сообщение", message='Match is deleted')
            newWindow.destroy()
        

        Label(newWindow, text = "Enter the id of match").place(x=25, y=20)
        txt = Entry(newWindow)
        txt.place(x=40,y=50)
        Button(newWindow, text="Delete", command=clicked).place(x=70, y=80) 


    def delete_bets_by_outcome():
        newWindow = Tk()
        newWindow.title = "Delete bet"
        newWindow.geometry("200x200")

        
        def clicked():
            aoutcome = txt.get()
            backend.delete_bets_by_result(aoutcome)
            messagebox.showinfo(title="Информационное сообщение", message='Bets are deleted')
            newWindow.destroy()
        

        Label(newWindow, text = "Enter the outcome: 1, X or 2").place(x=25, y=20)
        txt = Entry(newWindow)
        txt.place(x=40,y=50)
        Button(newWindow, text="Delete", command=clicked).place(x=70, y=80) 


    def search_bets_by_outcome():
        newWindow = Tk()
        newWindow.title("Show bets by outcome")
        newWindow.geometry("800x400")

        def show_treeview(heads, data):
            table = ttk.Treeview(newWindow, columns=heads, show='headings')
            for header in heads:
                table.heading(header, text=header, anchor='center')
                table.column(header, anchor='center')
            for row in data:
                table.insert('', tk.END, values=row)

            table.pack(expand=False, fill=tk.Y, side='bottom', anchor='s')

        
        def clicked():
            aoutcome = txt.get()
            data = backend.search_bets_by_result(aoutcome)
            heads = ['bet_id', 'user_id', 'match_id', 'outcome', 'sum_of_bet', 'coef', 'winning']
            show_treeview(heads, data)

        Label(newWindow, text = "Enter the outcome: 1, X or 2").place(x=25, y=20)
        txt = Entry(newWindow)
        txt.place(x=40,y=50)
        Button(newWindow, text="Show bets", command=clicked).place(x=70, y=80) 
        newWindow.mainloop()


    def update_user_info():
        newWindow = Tk()
        newWindow.title = "Update user info"
        newWindow.geometry("400x400")

        
        def clicked():
            aid = txt1.get()
            aphone = txt2.get()
            afirst_name = txt3.get()
            alast_name = txt4.get()
            agender = txt5.get()
            aage = txt6.get()
            try:
                backend.f_update_user(aid, aphone, afirst_name, alast_name, agender, aage)
                text = 'Data was updated'
            except:
                text = 'Incorrect data'
            finally:
                messagebox.showinfo(title="Information", message=text)
                
        

        Label(newWindow, text = "Enter user information").place(x=150, y=5)
        Label(newWindow, text = "Enter id").place(x=10, y=30)
        Label(newWindow, text = "Enter phone").place(x=10, y=60)
        Label(newWindow, text = "Enter first name").place(x=10, y=90)
        Label(newWindow, text = "Enter last name").place(x=10, y=120)
        Label(newWindow, text = "Enter gender").place(x=10, y=150)
        Label(newWindow, text = "Enter age").place(x=10, y=180)
        txt1 = Entry(newWindow)
        txt2 = Entry(newWindow)
        txt3 = Entry(newWindow)
        txt4 = Entry(newWindow)
        txt5 = Entry(newWindow)
        txt6 = Entry(newWindow)
        txt1.place(x=120,y=30)
        txt2.place(x=120,y=60)
        txt3.place(x=120,y=90)
        txt4.place(x=120,y=120)
        txt5.place(x=120,y=150)
        txt6.place(x=120,y=180)
        Button(newWindow, text="Update", command=clicked).place(x=150, y=220) 


    def add_data():
        newWindow = Tk()
        newWindow.title("Add data")
        newWindow.geometry("400x400")           

        def clicked_bets():
            def clicked():
                auser_id = txt1.get()
                amatch_id = txt2.get()
                aoutcome = txt3.get()
                asum_of_bet = txt4.get()
                acoef = txt5.get()
                try:
                    backend.add_bet(auser_id, amatch_id, aoutcome, asum_of_bet, acoef)
                    text = 'Success'
                except:
                    text = 'Incorrect data'
                finally:
                    messagebox.showinfo(title="Information", message=text)
                    
        

            Label(newWindow, text = "Enter bet information").place(x=10, y=100)
            Label(newWindow, text = "Enter user id:").place(x=10, y=130)
            Label(newWindow, text = "Enter match id:").place(x=10, y=160)
            Label(newWindow, text = "Enter outcome:").place(x=10, y=190)
            Label(newWindow, text = "Enter sum of bet:").place(x=10, y=220)
            Label(newWindow, text = "Enter coef:").place(x=10, y=250)
            txt1 = Entry(newWindow)
            txt2 = Entry(newWindow)
            txt3 = Entry(newWindow)
            txt4 = Entry(newWindow)
            txt5 = Entry(newWindow)
            txt1.place(x=120,y=130)
            txt2.place(x=120,y=160)
            txt3.place(x=120,y=190)
            txt4.place(x=120,y=220)
            txt5.place(x=120,y=250)
            Button(newWindow, text="Enter", command=clicked).place(x=150, y=300) 


        def clicked_matches():
            def clicked():
                amatch_date = txt1.get()
                ateam_id_home = txt2.get()
                ateam_id_away = txt3.get()
                amatch_result = txt4.get()
                ascore_home = txt5.get()
                ascore_away = txt6.get()
                try:
                    backend.add_match(amatch_date, ateam_id_home, ateam_id_away, amatch_result, ascore_home, ascore_away)
                    text = 'Success'
                except:
                    text = 'Incorrect data'
                finally:
                    messagebox.showinfo(title="Information", message=text)
                    
        

            Label(newWindow, text = "Enter match information").place(x=10, y=100)
            Label(newWindow, text = "Enter date:").place(x=10, y=130)
            Label(newWindow, text = "Enter id home team:").place(x=10, y=160)
            Label(newWindow, text = "Enter id away team:").place(x=10, y=190)
            Label(newWindow, text = "Enter result:").place(x=10, y=220)
            Label(newWindow, text = "Enter score home:").place(x=10, y=250)
            Label(newWindow, text = "Enter score away:").place(x=10, y=280)
            txt1 = Entry(newWindow)
            txt2 = Entry(newWindow)
            txt3 = Entry(newWindow)
            txt4 = Entry(newWindow)
            txt5 = Entry(newWindow)
            txt6 = Entry(newWindow)
            txt1.place(x=120,y=130)
            txt2.place(x=120,y=160)
            txt3.place(x=120,y=190)
            txt4.place(x=120,y=220)
            txt5.place(x=120,y=250)
            txt6.place(x=120,y=280)
            Button(newWindow, text="Enter", command=clicked).place(x=150, y=330) 

        def clicked_users():
            def clicked():
                aphone = txt1.get()
                afirst_name = txt2.get()
                alast_name = txt3.get()
                agender = txt4.get()
                aage = txt5.get()
                try:
                    backend.add_user(aphone, afirst_name, alast_name, agender, aage)
                    text = 'Success'
                except:
                    text = 'Incorrect data'
                finally:
                    messagebox.showinfo(title="Information", message=text)
                    
        

            Label(newWindow, text = "Enter user information").place(x=10, y=100)
            Label(newWindow, text = "Enter phone:").place(x=10, y=130)
            Label(newWindow, text = "Enter first name:").place(x=10, y=160)
            Label(newWindow, text = "Enter last name:").place(x=10, y=190)
            Label(newWindow, text = "Enter gender:").place(x=10, y=220)
            Label(newWindow, text = "Enter age:").place(x=10, y=250)
            txt1 = Entry(newWindow)
            txt2 = Entry(newWindow)
            txt3 = Entry(newWindow)
            txt4 = Entry(newWindow)
            txt5 = Entry(newWindow)
            txt1.place(x=120,y=130)
            txt2.place(x=120,y=160)
            txt3.place(x=120,y=190)
            txt4.place(x=120,y=220)
            txt5.place(x=120,y=250)
            Button(newWindow, text="Enter", command=clicked).place(x=150, y=300) 


        Label(newWindow, text = "Choose the table").place(x=10, y=10)
        Button(newWindow, text="matches", height=2, width=10, command=clicked_matches).place(x=10, y=40) 
        Button(newWindow, text="users", height=2, width=10, command=clicked_users).place(x=90, y=40) 
        Button(newWindow, text="bets", height=2, width=10, command=clicked_bets).place(x=170, y=40) 
        newWindow.mainloop()





    Button(root, text="Create database", height=2, width=25, bg='#567', fg='White', font=('arial bold', 12), command=create_database).place(x=290, y=10)
    Button(root, text="Delete database", height=3, width=15, bg='#567', fg='White', font=('arial bold', 12), command=delete_database).place(x=650, y=80)
    Button(root, text="Show table", height=3, width=15, bg='#567', fg='White', font=('arial bold', 12), command=show_table).place(x=650, y=220)
    Button(root, text="Clean table bets", height=3, width=15, bg='#567', fg='White', font=('arial bold', 12), command=clean_table_bets).place(x=650, y=290)
    Button(root, text="Clean all tables", height=3, width=15, bg='#567', fg='White', font=('arial bold', 12), command=clean_all_tables).place(x=650, y=360)
    Button(root, text="Add data", height=3, width=15, bg='#567', fg='White', font=('arial bold', 12), command=add_data).place(x=5, y=80)
    Button(root, text="Search bets", height=3, width=15, bg='#567', fg='White', font=('arial bold', 12), command=search_bets_by_outcome).place(x=5, y=150)
    Button(root, text="Update user", height=3, width=15, bg='#567', fg='White', font=('arial bold', 12), command=update_user_info).place(x=5, y=220)
    Button(root, text="Delete bets", height=3, width=15, bg='#567', fg='White', font=('arial bold', 12), command=delete_bets_by_outcome).place(x=5, y=290)
    Button(root, text="Delete match", height=3, width=15, bg='#567', fg='White', font=('arial bold', 12), command=delete_match).place(x=5, y=360)
    Button(root, text="Delete bet", height=3, width=15, bg='#567', fg='White', font=('arial bold', 12), command=delete_bet).place(x=650, y=150)
    Button(root, text="Connect to database", height=2, width=25, bg='#567', fg='White', font=('arial bold', 12), command=connect_database).place(x=290, y=430)

    Label(root,  text=f"User: {admin_name}", height=2, width=12, bg='#567', fg='White', font=('arial bold', 8)).place(x=10, y=10)
 

    img = ImageTk.PhotoImage(Image.open('2.PNG'))
    Label(root, image = img, height=200, width=350, bg = '#567').place(x=230, y=150)




    root.mainloop()

































def autorisation():
    def clicked():
        global admin_name
        admin_name = txt1.get()
        global admin_password
        admin_password = txt2.get()
        if (admin_name != 'admin1') or (admin_password != '111'):
            messagebox.showinfo(title="Information", message='Incorrect data', clicked=window.quit())
            
        else:
            backend.get_us_pa(admin_name, admin_password)
            window.destroy()
            f_main()
    window = Tk()
    window.geometry("300x200")
    window["bg"] = "gray22"
    window.title("Autorisation")
    ttk.Label(window, text = "Enter login").place(x=10, y=10)
    ttk.Label(window, text = "Enter password").place(x=10, y=40)
    txt1 = Entry(window)
    txt1.place(x=100,y=10)
    txt2 = Entry(window)
    txt2.place(x=100,y=40)
    ttk.Button(window, text="Enter", command=clicked).place(x=100, y=80)
    window.mainloop()

autorisation()