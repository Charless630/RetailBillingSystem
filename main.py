from tkinter import *
from tkinter import messagebox
import random, os, tempfile, smtplib
# Functionality PART

def clear():
    bathsoapEntry.delete(0, END)
    facecreamEntry.delete(0, END)
    facewashEntry.delete(0, END)
    hairsprayEntry.delete(0, END)
    hairgelEntry.delete(0, END)
    bodylotionEntry.delete(0, END)
    riceEntry.delete(0, END)
    oilEntry.delete(0, END)
    daalEntry.delete(0, END)
    wheatEntry.delete(0, END)
    sugarEntry.delete(0, END)
    teaEntry.delete(0, END)
    maazaEntry.delete(0, END)
    pepsiEntry.delete(0, END)
    spriteEntry.delete(0, END)
    dewEntry.delete(0, END)
    frootiEntry.delete(0, END)
    cocacolaEntry.delete(0, END)
    
    cosmeticpriceEntry.delete(0, END)
    grocerypriceEntry.delete(0, END)
    drinkspriceEntry.delete(0, END)
    
    cosmetictaxEntry.delete(0, END)
    grocerytaxEntry.delete(0, END)
    drinkstaxEntry.delete(0, END)
    
    nameEntry.delete(0, END)
    phoneEntry.delete(0, END)
    billnumberEntry.delete(0, END)
    textarea.delete(1.0, END)
    
    bathsoapEntry.insert(0,0)
    facecreamEntry.insert(0,0)
    facewashEntry.insert(0,0)
    hairsprayEntry.insert(0,0)
    hairgelEntry.insert(0,0)
    bodylotionEntry.insert(0,0)
    riceEntry.insert(0,0)
    oilEntry.insert(0,0)
    daalEntry.insert(0,0)
    wheatEntry.insert(0,0)
    sugarEntry.insert(0,0)
    teaEntry.insert(0,0)
    maazaEntry.insert(0,0)
    pepsiEntry.insert(0,0)
    spriteEntry.insert(0,0)
    dewEntry.insert(0,0)
    frootiEntry.insert(0,0)
    cocacolaEntry.insert(0,0)
    
    cosmeticpriceEntry.insert(0,0)
    grocerypriceEntry.insert(0,0)
    drinkspriceEntry.insert(0,0)
    
    cosmetictaxEntry.insert(0,0)
    grocerytaxEntry.insert(0,0)
    drinkstaxEntry.insert(0,0)

def send_email():
    def send_gmail():
        try:
            ob = smtplib.SMTP('smtp.gmail.com', 587)
            ob.starttls()
            ob.login(senderEntry.get(), passwordEntry.get())
            message = email_textarea.get(1.0, END)
            ob.sendmail(senderEntry.get(), recieverEntry.get(), message)
            ob.quit()
            messagebox.showinfo('Success', 'Email Sent Successfully!', parent = root1)
            root1.destroy()
        except:
            messagebox.showerror('Error', 'Something Went Wrong. Please Try Again!', parent = root1)
        
        
    if textarea.get(1.0, END) == '\n':
        messagebox.showerror('Error', 'Bill is Empty!')
    else:
        root1=Toplevel()
        root1.grab_set()
        root1.title('Send Email')
        root1.config(bg='gray20')
        root1.resizable(0,0)
        
        senderFrame = LabelFrame(root1, text='SENDER', font=('arial', 16, 'bold'), bd=6, bg='gray20',
                                 fg='antiquewhite')
        senderFrame.grid(row=0, column=0, padx=40, pady=20)
        
        senderLabel=Label(senderFrame, text="Sender's Email", font=('arial', 14, 'bold'), bg='gray20',
                                 fg='antiquewhite')
        senderLabel.grid(row=0, column=0, padx=10, pady=10)
        
        senderEntry = Entry(senderFrame, font=('arial', 14, 'bold'), bd=2, width=23, relief=RIDGE)
        senderEntry.grid(row=0, column=1, padx=10, pady=8)
        
        passwordLabel=Label(senderFrame, text="Password", font=('arial', 14, 'bold'), bg='gray20',
                                 fg='antiquewhite')
        passwordLabel.grid(row=1, column=0, padx=10, pady=10)
        
        passwordEntry = Entry(senderFrame, font=('arial', 14, 'bold'), bd=2, width=23, relief=RIDGE,
                              show='*')
        passwordEntry.grid(row=1, column=1, padx=10, pady=8)
        
        recipientFrame = LabelFrame(root1, text='RECIPIENT', font=('arial', 16, 'bold'), bd=6, bg='gray20',
                                 fg='antiquewhite')
        recipientFrame.grid(row=1, column=0, padx=40, pady=20)
        
        recieverLabel=Label(recipientFrame, text="Email Address", font=('arial', 14, 'bold'), bg='gray20',
                                 fg='antiquewhite')
        recieverLabel.grid(row=0, column=0, padx=10, pady=10)
        
        recieverEntry = Entry(recipientFrame, font=('arial', 14, 'bold'), bd=2, width=23, relief=RIDGE)
        recieverEntry.grid(row=0, column=1, padx=10, pady=8)
        
        messageLabel=Label(recipientFrame, text="Message", font=('arial', 14, 'bold'), bg='gray20',
                                 fg='antiquewhite')
        messageLabel.grid(row=1, column=0, padx=10, pady=10, columnspan=2)
        
        email_textarea=Text(recipientFrame, font=('arial', 14, 'bold'), bd=2, relief=SUNKEN,
                            width=43, height=11)
        email_textarea.grid(row=2, column=0, columnspan=2)
        email_textarea.delete(1.0, END)
        email_textarea.insert(END, textarea.get(1.0, END).replace('=', '').replace('-', '').replace('\t\t\t', '\t\t'))
        
        sendButton = Button(root1, text='SEND', font=('arial', 16, 'bold'), width=15, command=send_gmail)
        sendButton.grid(row=2, column=0, pady=10)
        
        
        root1.mainloop()

def search_bill():
    for i in os.listdir('Bills/'):
        if i.split('.')[0] == billnumberEntry.get():
            f = open(f'Bills/{i}', 'r')
            textarea.delete('1.0', END)
            for data in f:
                textarea.insert(END, data)
            f.close()
            break
    else:
        messagebox.showerror('Error', 'Bill Not Found!')
        
def print_bill():
    if textarea.get(1.0, END) == '\n':
        messagebox.showerror('Error', 'Bill is Empty!')
    else:
        file = tempfile.mktemp('.txt')
        open(file, 'w').write(textarea.get(1.0, END))
        os.startfile(file, 'print')


if not os.path.exists('Bills'):
    os.mkdir('Bills')

def save_bill():
    global billnumber
    result = messagebox.askyesno('Confirm', 'Do you want to save the bill?')
    if result:
        bill_content = textarea.get(1.0, END)
        file = open(f'Bills/{billnumber}.txt', 'w')
        file.write(bill_content)
        file.close()
        messagebox.showinfo('Saved', f'Bill Number {billnumber} is saved successfully!')
        billnumber = random.randint(500, 1000)

billnumber = random.randint(500, 1000)

def bill_area():
    if nameEntry.get()=='' or phoneEntry.get()=='':
        messagebox.showerror('Error', 'Customer Details are Required!')
    elif cosmeticpriceEntry.get()=='' and grocerypriceEntry.get()=='' and drinkspriceEntry.get()=='':
        messagebox.showerror('Error', 'No Products are Selected!')
    elif cosmeticpriceEntry.get()=='0 Ft' and grocerypriceEntry.get()=='0 Ft' and drinkspriceEntry.get()=='0 Ft':
        messagebox.showerror('Error', 'No Products are Selected!')
    else:
        textarea.delete(1.0, END)
        textarea.insert(END, '\t\t**Welcome Customer!**\n')
        textarea.insert(END, f'\nBill Number: {billnumber}')
        textarea.insert(END, f'\nCustomer Name: {nameEntry.get()}')
        textarea.insert(END, f'\nCustomer Phone Number: {phoneEntry.get()}')
        textarea.insert(END, '\n======================================================')
        textarea.insert(END, 'Product\t\t\tQuantity\t\t\tPrice')
        textarea.insert(END, '\n======================================================')
        if bathsoapEntry.get()!='0':
            textarea.insert(END, f'\nBath Soap\t\t\t{bathsoapEntry.get()}\t\t\t{soapprice} Ft')
        if facecreamEntry.get()!='0':
            textarea.insert(END, f'\nFace Cream\t\t\t{facecreamEntry.get()}\t\t\t{facecreamprice} Ft')
        if facewashEntry.get()!='0':
            textarea.insert(END, f'\nFace Wash\t\t\t{facewashEntry.get()}\t\t\t{facewashprice} Ft')
        if hairsprayEntry.get()!='0':
            textarea.insert(END, f'\nHair Spray\t\t\t{hairsprayEntry.get()}\t\t\t{hairsprayprice} Ft')
        if hairgelEntry.get()!='0':
            textarea.insert(END, f'\nHair Gel\t\t\t{hairgelEntry.get()}\t\t\t{hairgelprice} Ft')
        if bodylotionEntry.get()!='0':
            textarea.insert(END, f'\nBody Lotion\t\t\t{bodylotionEntry.get()}\t\t\t{bodylotionprice} Ft')
        if riceEntry.get()!='0':
            textarea.insert(END, f'\nRice\t\t\t{riceEntry.get()}\t\t\t{riceprice} Ft')
        if oilEntry.get()!='0':
            textarea.insert(END, f'\nOil\t\t\t{oilEntry.get()}\t\t\t{oilprice} Ft')
        if daalEntry.get()!='0':
            textarea.insert(END, f'\nDaal\t\t\t{daalEntry.get()}\t\t\t{daalprice} Ft')
        if wheatEntry.get()!='0':
            textarea.insert(END, f'\nWheat\t\t\t{wheatEntry.get()}\t\t\t{wheatprice} Ft')
        if sugarEntry.get()!='0':
            textarea.insert(END, f'\nSugar\t\t\t{sugarEntry.get()}\t\t\t{sugarprice} Ft')
        if teaEntry.get()!='0':
            textarea.insert(END, f'\nTea\t\t\t{teaEntry.get()}\t\t\t{teaprice} Ft')
        if maazaEntry.get()!='0':
            textarea.insert(END, f'\nMaaza\t\t\t{maazaEntry.get()}\t\t\t{maazaprice} Ft')
        if pepsiEntry.get()!='0':
            textarea.insert(END, f'\nPepsi\t\t\t{pepsiEntry.get()}\t\t\t{pepsiprice} Ft')
        if spriteEntry.get()!='0':
            textarea.insert(END, f'\nSprite\t\t\t{spriteEntry.get()}\t\t\t{spriteprice} Ft')
        if dewEntry.get()!='0':
            textarea.insert(END, f'\nDew\t\t\t{dewEntry.get()}\t\t\t{dewprice} Ft')
        if frootiEntry.get()!='0':
            textarea.insert(END, f'\nFrooti\t\t\t{frootiEntry.get()}\t\t\t{frootiprice} Ft')
        if cocacolaEntry.get()!='0':
            textarea.insert(END, f'\nCoca Cola\t\t\t{cocacolaEntry.get()}\t\t\t{cocacolaprice} Ft')
        textarea.insert(END, '\n------------------------------------------------------')
        
        if cosmetictaxEntry.get()!='0.0 Ft':
            textarea.insert(END, f'\nCosmetic Tax\t\t\t\t{cosmetictaxEntry.get()} Ft')
        if grocerytaxEntry.get()!='0.0 Ft':
            textarea.insert(END, f'\nGrocery Tax\t\t\t\t{grocerytaxEntry.get()} Ft')
        if drinkstaxEntry.get()!='0.0 Ft':
            textarea.insert(END, f'\nDrinks Tax\t\t\t\t{drinkstaxEntry.get()} Ft')
        textarea.insert(END, '\n------------------------------------------------------')
        textarea.insert(END, f'\n\nTotal Bill\t\t\t\t{totalbill} Ft')
        textarea.insert(END, '\n------------------------------------------------------')
        save_bill()

def total():
    global soapprice, facecreamprice, facewashprice, hairsprayprice, hairgelprice, bodylotionprice
    global riceprice, oilprice, daalprice, wheatprice, sugarprice, teaprice
    global maazaprice, pepsiprice, spriteprice, dewprice, frootiprice, cocacolaprice
    global cosmetictax, grocerytax, drinkstax
    global totalbill
    # cosmetic price calculation
    soapprice = int(bathsoapEntry.get())*20
    facecreamprice = int(facecreamEntry.get())*50
    facewashprice = int(facewashEntry.get())*25
    hairsprayprice = int(hairsprayEntry.get())*50
    hairgelprice = int(hairgelEntry.get())*150
    bodylotionprice = int(bodylotionEntry.get())*75
    
    totalcosmeticprice = soapprice+facecreamprice+facewashprice+hairsprayprice+hairgelprice+bodylotionprice
    cosmeticpriceEntry.delete(0, END)
    cosmeticpriceEntry.insert(0, f'{totalcosmeticprice} Ft')
    cosmetictax = totalcosmeticprice*0.27
    cosmetictaxEntry.delete(0, END)
    cosmetictaxEntry.insert(0, f'{cosmetictax} Ft')
    
    # grocery price calculation
    riceprice = int(riceEntry.get())*20
    oilprice = int(oilEntry.get())*80
    daalprice = int(daalEntry.get())*12
    wheatprice = int(wheatEntry.get())*20
    sugarprice = int(sugarEntry.get())*70
    teaprice = int(teaEntry.get())*45
    
    totalgroceryprice = riceprice+oilprice+daalprice+wheatprice+sugarprice+teaprice
    grocerypriceEntry.delete(0, END)
    grocerypriceEntry.insert(0, f'{totalgroceryprice} Ft')
    grocerytax = totalgroceryprice*0.27
    grocerytaxEntry.delete(0, END)
    grocerytaxEntry.insert(0, f'{grocerytax} Ft')
    
     # cold drink price calculation
    maazaprice = int(maazaEntry.get())*20
    pepsiprice = int(pepsiEntry.get())*50
    spriteprice = int(spriteEntry.get())*45
    dewprice = int(dewEntry.get())*70
    frootiprice = int(frootiEntry.get())*15
    cocacolaprice = int(cocacolaEntry.get())*50
    
    totaldrinkprice = maazaprice+pepsiprice+spriteprice+dewprice+frootiprice+cocacolaprice
    drinkspriceEntry.delete(0, END)
    drinkspriceEntry.insert(0, f'{totaldrinkprice} Ft')
    drinkstax = totaldrinkprice*0.27
    drinkstaxEntry.delete(0, END)
    drinkstaxEntry.insert(0, f'{drinkstax} Ft')
    
    totalbill=totalcosmeticprice+totalgroceryprice+totaldrinkprice+cosmetictax+grocerytax+drinkstax
    
# GUI PART
root = Tk()
root.title("Retail Billing System")
root.geometry("1270x685")
root.resizable(0,0)
root.iconbitmap('icon.ico')

headingLabel = Label(root, text='Retail Billing System', font=('times new roman', 30, 'bold'),
                     bg='gray20', fg='antiquewhite', bd=12, relief=GROOVE)
headingLabel.pack(fill=X)

customer_details_frame = LabelFrame(root, text='Customer Details', font=('times new roman', 15, 'bold'),
                                    fg='antiquewhite', bd=8, relief=GROOVE, bg='gray20')
customer_details_frame.pack(fill=X)

nameLabel = Label(customer_details_frame, text='Name', font=('times new roman', 15, 'bold'), bg='gray20',
                  fg='aliceblue')
nameLabel.grid(row=0, column=0, padx=20)

nameEntry = Entry(customer_details_frame, font=('arial', 15), bd=7, width=18)
nameEntry.grid(row=0, column=1, padx=8)

phoneLabel = Label(customer_details_frame, text='Phone Number', font=('times new roman', 15, 'bold'), bg='gray20',
                  fg='aliceblue')
phoneLabel.grid(row=0, column=2, padx=20, pady=2)

phoneEntry = Entry(customer_details_frame, font=('arial', 15), bd=7, width=18)
phoneEntry.grid(row=0, column=3, padx=8)

billnumberLabel = Label(customer_details_frame, text='Bill Number', font=('times new roman', 15, 'bold'), bg='gray20',
                  fg='aliceblue')
billnumberLabel.grid(row=0, column=4, padx=20, pady=2)

billnumberEntry = Entry(customer_details_frame, font=('arial', 15), bd=7, width=18)
billnumberEntry.grid(row=0, column=5, padx=8)

searchButton = Button(customer_details_frame, text='Search',
                      font=('arial', 12, 'bold'), bd=7, width=10, command=search_bill)
searchButton.grid(row=0, column=6, padx=20, pady=8)

productsFrame = Frame(root)
productsFrame.pack()

cosmeticsFrame = LabelFrame(productsFrame, text='Comestics', font=('times new roman', 15, 'bold'),
                                    fg='antiquewhite', bd=8, relief=GROOVE, bg='gray20')
cosmeticsFrame.grid(row=0, column=0)

bathsoapLabel = Label(cosmeticsFrame, text='Bath Soap', font=('times new roman', 15, 'bold'), bg='gray20',
                  fg='aliceblue')
bathsoapLabel.grid(row=0, column=0, pady=9, padx=10, sticky='w')
bathsoapEntry = Entry(cosmeticsFrame, font=('arial', 15, 'bold'), width=10, bd=5)
bathsoapEntry.grid(row=0, column=1, pady=9, padx=10)
bathsoapEntry.insert(0,0)

facecreamLabel = Label(cosmeticsFrame, text='Face Cream', font=('times new roman', 15, 'bold'), bg='gray20',
                  fg='aliceblue')
facecreamLabel.grid(row=1, column=0, pady=9, padx=10, sticky='w')
facecreamEntry = Entry(cosmeticsFrame, font=('arial', 15, 'bold'), width=10, bd=5)
facecreamEntry.grid(row=1, column=1, pady=9, padx=10)
facecreamEntry.insert(0,0)

facewashLabel = Label(cosmeticsFrame, text='Face Wash', font=('times new roman', 15, 'bold'), bg='gray20',
                  fg='aliceblue')
facewashLabel.grid(row=2, column=0, pady=9, padx=10, sticky='w')
facewashEntry = Entry(cosmeticsFrame, font=('arial', 15, 'bold'), width=10, bd=5)
facewashEntry.grid(row=2, column=1, pady=9, padx=10)
facewashEntry.insert(0,0)

hairsprayLabel = Label(cosmeticsFrame, text='Hair Spray', font=('times new roman', 15, 'bold'), bg='gray20',
                  fg='aliceblue')
hairsprayLabel.grid(row=3, column=0, pady=9, padx=10, sticky='w')
hairsprayEntry = Entry(cosmeticsFrame, font=('arial', 15, 'bold'), width=10, bd=5)
hairsprayEntry.grid(row=3, column=1, pady=9, padx=10)
hairsprayEntry.insert(0,0)

hairgelLabel = Label(cosmeticsFrame, text='Hair Gel', font=('times new roman', 15, 'bold'), bg='gray20',
                  fg='aliceblue')
hairgelLabel.grid(row=4, column=0, pady=9, padx=10, sticky='w')
hairgelEntry = Entry(cosmeticsFrame, font=('arial', 15, 'bold'), width=10, bd=5)
hairgelEntry.grid(row=4, column=1, pady=9, padx=10)
hairgelEntry.insert(0,0)

bodylotionLabel = Label(cosmeticsFrame, text='Body Lotion', font=('times new roman', 15, 'bold'), bg='gray20',
                  fg='aliceblue')
bodylotionLabel.grid(row=5, column=0, pady=9, padx=10, sticky='w')
bodylotionEntry = Entry(cosmeticsFrame, font=('arial', 15, 'bold'), width=10, bd=5)
bodylotionEntry.grid(row=5, column=1, pady=9, padx=10)
bodylotionEntry.insert(0,0)

groceryFrame = LabelFrame(productsFrame, text='Grocery', font=('times new roman', 15, 'bold'),
                                    fg='antiquewhite', bd=8, relief=GROOVE, bg='gray20')
groceryFrame.grid(row=0, column=1)

riceLabel = Label(groceryFrame, text='Rice', font=('times new roman', 15, 'bold'), bg='gray20',
                  fg='aliceblue')
riceLabel.grid(row=0, column=0, pady=9, padx=10, sticky='w')
riceEntry = Entry(groceryFrame, font=('arial', 15, 'bold'), width=10, bd=5)
riceEntry.grid(row=0, column=1, pady=9, padx=10)
riceEntry.insert(0,0)

oilLabel = Label(groceryFrame, text='Oil', font=('times new roman', 15, 'bold'), bg='gray20',
                  fg='aliceblue')
oilLabel.grid(row=1, column=0, pady=9, padx=10, sticky='w')
oilEntry = Entry(groceryFrame, font=('arial', 15, 'bold'), width=10, bd=5)
oilEntry.grid(row=1, column=1, pady=9, padx=10)
oilEntry.insert(0,0)

daalLabel = Label(groceryFrame, text='Daal', font=('times new roman', 15, 'bold'), bg='gray20',
                  fg='aliceblue')
daalLabel.grid(row=2, column=0, pady=9, padx=10, sticky='w')
daalEntry = Entry(groceryFrame, font=('arial', 15, 'bold'), width=10, bd=5)
daalEntry.grid(row=2, column=1, pady=9, padx=10)
daalEntry.insert(0,0)

wheatLabel = Label(groceryFrame, text='Wheat', font=('times new roman', 15, 'bold'), bg='gray20',
                  fg='aliceblue')
wheatLabel.grid(row=3, column=0, pady=9, padx=10, sticky='w')
wheatEntry = Entry(groceryFrame, font=('arial', 15, 'bold'), width=10, bd=5)
wheatEntry.grid(row=3, column=1, pady=9, padx=10)
wheatEntry.insert(0,0)

sugarLabel = Label(groceryFrame, text='Sugar', font=('times new roman', 15, 'bold'), bg='gray20',
                  fg='aliceblue')
sugarLabel.grid(row=4, column=0, pady=9, padx=10, sticky='w')
sugarEntry = Entry(groceryFrame, font=('arial', 15, 'bold'), width=10, bd=5)
sugarEntry.grid(row=4, column=1, pady=9, padx=10)
sugarEntry.insert(0,0)

teaLabel = Label(groceryFrame, text='Tea', font=('times new roman', 15, 'bold'), bg='gray20',
                  fg='aliceblue')
teaLabel.grid(row=5, column=0, pady=9, padx=10, sticky='w')
teaEntry = Entry(groceryFrame, font=('arial', 15, 'bold'), width=10, bd=5)
teaEntry.grid(row=5, column=1, pady=9, padx=10)
teaEntry.insert(0,0)

drinksFrame = LabelFrame(productsFrame, text='Cold Drinks', font=('times new roman', 15, 'bold'),
                                    fg='antiquewhite', bd=8, relief=GROOVE, bg='gray20')
drinksFrame.grid(row=0, column=2)

maazaLabel = Label(drinksFrame, text='Maaza', font=('times new roman', 15, 'bold'), bg='gray20',
                  fg='aliceblue')
maazaLabel.grid(row=0, column=0, pady=9, padx=10, sticky='w')
maazaEntry = Entry(drinksFrame, font=('arial', 15, 'bold'), width=10, bd=5)
maazaEntry.grid(row=0, column=1, pady=9, padx=10)
maazaEntry.insert(0,0)

pepsiLabel = Label(drinksFrame, text='Pepsi', font=('times new roman', 15, 'bold'), bg='gray20',
                  fg='aliceblue')
pepsiLabel.grid(row=1, column=0, pady=9, padx=10, sticky='w')
pepsiEntry = Entry(drinksFrame, font=('arial', 15, 'bold'), width=10, bd=5)
pepsiEntry.grid(row=1, column=1, pady=9, padx=10)
pepsiEntry.insert(0,0)

spriteLabel = Label(drinksFrame, text='Sprite', font=('times new roman', 15, 'bold'), bg='gray20',
                  fg='aliceblue')
spriteLabel.grid(row=2, column=0, pady=9, padx=10, sticky='w')
spriteEntry = Entry(drinksFrame, font=('arial', 15, 'bold'), width=10, bd=5)
spriteEntry.grid(row=2, column=1, pady=9, padx=10)
spriteEntry.insert(0,0)

dewLabel = Label(drinksFrame, text='Dew', font=('times new roman', 15, 'bold'), bg='gray20',
                  fg='aliceblue')
dewLabel.grid(row=3, column=0, pady=9, padx=10, sticky='w')
dewEntry = Entry(drinksFrame, font=('arial', 15, 'bold'), width=10, bd=5)
dewEntry.grid(row=3, column=1, pady=9, padx=10)
dewEntry.insert(0,0)

frootiLabel = Label(drinksFrame, text='Frooti', font=('times new roman', 15, 'bold'), bg='gray20',
                  fg='aliceblue')
frootiLabel.grid(row=4, column=0, pady=9, padx=10, sticky='w')
frootiEntry = Entry(drinksFrame, font=('arial', 15, 'bold'), width=10, bd=5)
frootiEntry.grid(row=4, column=1, pady=9, padx=10)
frootiEntry.insert(0,0)

cocacolaLabel = Label(drinksFrame, text='Coca Cola', font=('times new roman', 15, 'bold'), bg='gray20',
                  fg='aliceblue')
cocacolaLabel.grid(row=5, column=0, pady=9, padx=10, sticky='w')
cocacolaEntry = Entry(drinksFrame, font=('arial', 15, 'bold'), width=10, bd=5)
cocacolaEntry.grid(row=5, column=1, pady=9, padx=10)
cocacolaEntry.insert(0,0)

billframe = Frame(productsFrame, bd=8, relief=GROOVE)
billframe.grid(row=0, column=3, padx=10)

billareaLabel = Label(billframe, text='Bill Area', font=('times new roman', 15, 'bold'), bd=7,
                      relief=GROOVE)
billareaLabel.pack(fill=X)

# Creating the scrollbar and text area
scrollbar = Scrollbar(billframe, orient=VERTICAL)
scrollbar.pack(side=RIGHT, fill=Y)
textarea=Text(billframe, height=18, width=54, yscrollcommand=scrollbar.set)
textarea.pack()
scrollbar.config(command=textarea.yview)

billmenuFrame = LabelFrame(root, text='Bill Menu', font=('times new roman', 15, 'bold'),
                                    fg='antiquewhite', bd=8, relief=GROOVE, bg='gray20')
billmenuFrame.pack()

cosmeticpriceLabel = Label(billmenuFrame, text='Cosmetic Price', font=('times new roman', 14, 'bold'), bg='gray20',
                  fg='aliceblue')
cosmeticpriceLabel.grid(row=0, column=0, pady=6, padx=10, sticky='w')
cosmeticpriceEntry = Entry(billmenuFrame, font=('arial', 14, 'bold'), width=10, bd=5)
cosmeticpriceEntry.grid(row=0, column=1, pady=6, padx=10)

grocerypriceLabel = Label(billmenuFrame, text='Grocery Price', font=('times new roman', 14, 'bold'), bg='gray20',
                  fg='aliceblue')
grocerypriceLabel.grid(row=1, column=0, pady=6, padx=10, sticky='w')
grocerypriceEntry = Entry(billmenuFrame, font=('arial', 14, 'bold'), width=10, bd=5)
grocerypriceEntry.grid(row=1, column=1, pady=6, padx=10)

drinkspriceLabel = Label(billmenuFrame, text='Cold Drink Price', font=('times new roman', 14, 'bold'), bg='gray20',
                  fg='aliceblue')
drinkspriceLabel.grid(row=2, column=0, pady=6, padx=10, sticky='w')
drinkspriceEntry = Entry(billmenuFrame, font=('arial', 14, 'bold'), width=10, bd=5)
drinkspriceEntry.grid(row=2, column=1, pady=6, padx=10)

cosmetictaxLabel = Label(billmenuFrame, text='Cosmetic Tax', font=('times new roman', 14, 'bold'), bg='gray20',
                  fg='aliceblue')
cosmetictaxLabel.grid(row=0, column=2, pady=6, padx=10, sticky='w')
cosmetictaxEntry = Entry(billmenuFrame, font=('arial', 14, 'bold'), width=10, bd=5)
cosmetictaxEntry.grid(row=0, column=3, pady=6, padx=10)

grocerytaxLabel = Label(billmenuFrame, text='Grocery Tax', font=('times new roman', 14, 'bold'), bg='gray20',
                  fg='aliceblue')
grocerytaxLabel.grid(row=1, column=2, pady=6, padx=10, sticky='w')
grocerytaxEntry = Entry(billmenuFrame, font=('arial', 14, 'bold'), width=10, bd=5)
grocerytaxEntry.grid(row=1, column=3, pady=6, padx=10)

drinkstaxLabel = Label(billmenuFrame, text='Cold Drink Tax', font=('times new roman', 14, 'bold'), bg='gray20',
                  fg='aliceblue')
drinkstaxLabel.grid(row=2, column=2, pady=6, padx=10, sticky='w')
drinkstaxEntry = Entry(billmenuFrame, font=('arial', 14, 'bold'), width=10, bd=5)
drinkstaxEntry.grid(row=2, column=3, pady=6, padx=10)

buttonFrame = Frame(billmenuFrame, bd=8, relief=GROOVE)
buttonFrame.grid(row=0, column=4, rowspan=3)

totalButton = Button(buttonFrame, text='Total', font=('arial', 16, 'bold'), bg='gray20', fg='aliceblue',
                     bd=5, width=8, pady=10, command=total)
totalButton.grid(row=0, column=0, pady=20, padx=5)

billButton = Button(buttonFrame, text='Bill', font=('arial', 16, 'bold'), bg='gray20', fg='aliceblue',
                     bd=5, width=8, pady=10, command=bill_area)
billButton.grid(row=0, column=1, pady=20, padx=5)

emailButton = Button(buttonFrame, text='Email', font=('arial', 16, 'bold'), bg='gray20', fg='aliceblue',
                     bd=5, width=8, pady=10, command=send_email)
emailButton.grid(row=0, column=2, pady=20, padx=5)

printButton = Button(buttonFrame, text='Print', font=('arial', 16, 'bold'), bg='gray20', fg='aliceblue',
                     bd=5, width=8, pady=10, command=print_bill)
printButton.grid(row=0, column=3, pady=20, padx=5)

clearButton = Button(buttonFrame, text='Clear', font=('arial', 16, 'bold'), bg='gray20', fg='aliceblue',
                     bd=5, width=8, pady=10, command=clear)
clearButton.grid(row=0, column=4, pady=20, padx=5)

root.mainloop()
