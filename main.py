from tkinter import *

root = Tk()
root.title("Retail Billing System")
root.geometry("1270x685")
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

searchButton = Button(customer_details_frame, text='Search', font=('arial', 12, 'bold'), bd=7, width=10)
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

facecreamLabel = Label(cosmeticsFrame, text='Face Cream', font=('times new roman', 15, 'bold'), bg='gray20',
                  fg='aliceblue')
facecreamLabel.grid(row=1, column=0, pady=9, padx=10, sticky='w')
facecreamEntry = Entry(cosmeticsFrame, font=('arial', 15, 'bold'), width=10, bd=5)
facecreamEntry.grid(row=1, column=1, pady=9, padx=10)

facewashLabel = Label(cosmeticsFrame, text='Face Wash', font=('times new roman', 15, 'bold'), bg='gray20',
                  fg='aliceblue')
facewashLabel.grid(row=2, column=0, pady=9, padx=10, sticky='w')
facewashEntry = Entry(cosmeticsFrame, font=('arial', 15, 'bold'), width=10, bd=5)
facewashEntry.grid(row=2, column=1, pady=9, padx=10)

hairsprayLabel = Label(cosmeticsFrame, text='Hair Spray', font=('times new roman', 15, 'bold'), bg='gray20',
                  fg='aliceblue')
hairsprayLabel.grid(row=3, column=0, pady=9, padx=10, sticky='w')
hairsprayEntry = Entry(cosmeticsFrame, font=('arial', 15, 'bold'), width=10, bd=5)
hairsprayEntry.grid(row=3, column=1, pady=9, padx=10)

hairgelLabel = Label(cosmeticsFrame, text='Hair Gel', font=('times new roman', 15, 'bold'), bg='gray20',
                  fg='aliceblue')
hairgelLabel.grid(row=4, column=0, pady=9, padx=10, sticky='w')
hairgelEntry = Entry(cosmeticsFrame, font=('arial', 15, 'bold'), width=10, bd=5)
hairgelEntry.grid(row=4, column=1, pady=9, padx=10)

bodylotionLabel = Label(cosmeticsFrame, text='Body Lotion', font=('times new roman', 15, 'bold'), bg='gray20',
                  fg='aliceblue')
bodylotionLabel.grid(row=5, column=0, pady=9, padx=10, sticky='w')
bodylotionEntry = Entry(cosmeticsFrame, font=('arial', 15, 'bold'), width=10, bd=5)
bodylotionEntry.grid(row=5, column=1, pady=9, padx=10)

groceryFrame = LabelFrame(productsFrame, text='Grocery', font=('times new roman', 15, 'bold'),
                                    fg='antiquewhite', bd=8, relief=GROOVE, bg='gray20')
groceryFrame.grid(row=0, column=1)

riceLabel = Label(groceryFrame, text='Rice', font=('times new roman', 15, 'bold'), bg='gray20',
                  fg='aliceblue')
riceLabel.grid(row=0, column=0, pady=9, padx=10, sticky='w')
riceEntry = Entry(groceryFrame, font=('arial', 15, 'bold'), width=10, bd=5)
riceEntry.grid(row=0, column=1, pady=9, padx=10)

oilLabel = Label(groceryFrame, text='Oil', font=('times new roman', 15, 'bold'), bg='gray20',
                  fg='aliceblue')
oilLabel.grid(row=1, column=0, pady=9, padx=10, sticky='w')
oilEntry = Entry(groceryFrame, font=('arial', 15, 'bold'), width=10, bd=5)
oilEntry.grid(row=1, column=1, pady=9, padx=10)

daalLabel = Label(groceryFrame, text='Daal', font=('times new roman', 15, 'bold'), bg='gray20',
                  fg='aliceblue')
daalLabel.grid(row=2, column=0, pady=9, padx=10, sticky='w')
daalEntry = Entry(groceryFrame, font=('arial', 15, 'bold'), width=10, bd=5)
daalEntry.grid(row=2, column=1, pady=9, padx=10)

wheatLabel = Label(groceryFrame, text='Wheat', font=('times new roman', 15, 'bold'), bg='gray20',
                  fg='aliceblue')
wheatLabel.grid(row=3, column=0, pady=9, padx=10, sticky='w')
wheatEntry = Entry(groceryFrame, font=('arial', 15, 'bold'), width=10, bd=5)
wheatEntry.grid(row=3, column=1, pady=9, padx=10)

sugarLabel = Label(groceryFrame, text='Sugar', font=('times new roman', 15, 'bold'), bg='gray20',
                  fg='aliceblue')
sugarLabel.grid(row=4, column=0, pady=9, padx=10, sticky='w')
sugarEntry = Entry(groceryFrame, font=('arial', 15, 'bold'), width=10, bd=5)
sugarEntry.grid(row=4, column=1, pady=9, padx=10)

teaLabel = Label(groceryFrame, text='Tea', font=('times new roman', 15, 'bold'), bg='gray20',
                  fg='aliceblue')
teaLabel.grid(row=5, column=0, pady=9, padx=10, sticky='w')
teaEntry = Entry(groceryFrame, font=('arial', 15, 'bold'), width=10, bd=5)
teaEntry.grid(row=5, column=1, pady=9, padx=10)

drinksFrame = LabelFrame(productsFrame, text='Cold Drinks', font=('times new roman', 15, 'bold'),
                                    fg='antiquewhite', bd=8, relief=GROOVE, bg='gray20')
drinksFrame.grid(row=0, column=2)

maazaLabel = Label(drinksFrame, text='Maaza', font=('times new roman', 15, 'bold'), bg='gray20',
                  fg='aliceblue')
maazaLabel.grid(row=0, column=0, pady=9, padx=10, sticky='w')
maazaEntry = Entry(drinksFrame, font=('arial', 15, 'bold'), width=10, bd=5)
maazaEntry.grid(row=0, column=1, pady=9, padx=10)

pepsiLabel = Label(drinksFrame, text='Pepsi', font=('times new roman', 15, 'bold'), bg='gray20',
                  fg='aliceblue')
pepsiLabel.grid(row=1, column=0, pady=9, padx=10, sticky='w')
pepsiEntry = Entry(drinksFrame, font=('arial', 15, 'bold'), width=10, bd=5)
pepsiEntry.grid(row=1, column=1, pady=9, padx=10)

spriteLabel = Label(drinksFrame, text='Sprite', font=('times new roman', 15, 'bold'), bg='gray20',
                  fg='aliceblue')
spriteLabel.grid(row=2, column=0, pady=9, padx=10, sticky='w')
spriteEntry = Entry(drinksFrame, font=('arial', 15, 'bold'), width=10, bd=5)
spriteEntry.grid(row=2, column=1, pady=9, padx=10)

dewLabel = Label(drinksFrame, text='Dew', font=('times new roman', 15, 'bold'), bg='gray20',
                  fg='aliceblue')
dewLabel.grid(row=3, column=0, pady=9, padx=10, sticky='w')
dewEntry = Entry(drinksFrame, font=('arial', 15, 'bold'), width=10, bd=5)
dewEntry.grid(row=3, column=1, pady=9, padx=10)

frootiLabel = Label(drinksFrame, text='Frooti', font=('times new roman', 15, 'bold'), bg='gray20',
                  fg='aliceblue')
frootiLabel.grid(row=4, column=0, pady=9, padx=10, sticky='w')
frootiEntry = Entry(drinksFrame, font=('arial', 15, 'bold'), width=10, bd=5)
frootiEntry.grid(row=4, column=1, pady=9, padx=10)

cocacolaLabel = Label(drinksFrame, text='Coca Cola', font=('times new roman', 15, 'bold'), bg='gray20',
                  fg='aliceblue')
cocacolaLabel.grid(row=5, column=0, pady=9, padx=10, sticky='w')
cocacolaEntry = Entry(drinksFrame, font=('arial', 15, 'bold'), width=10, bd=5)
cocacolaEntry.grid(row=5, column=1, pady=9, padx=10)

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
                     bd=5, width=8, pady=10)
totalButton.grid(row=0, column=0, pady=20, padx=5)

billButton = Button(buttonFrame, text='Bill', font=('arial', 16, 'bold'), bg='gray20', fg='aliceblue',
                     bd=5, width=8, pady=10)
billButton.grid(row=0, column=1, pady=20, padx=5)

emailButton = Button(buttonFrame, text='Email', font=('arial', 16, 'bold'), bg='gray20', fg='aliceblue',
                     bd=5, width=8, pady=10)
emailButton.grid(row=0, column=2, pady=20, padx=5)

printButton = Button(buttonFrame, text='Print', font=('arial', 16, 'bold'), bg='gray20', fg='aliceblue',
                     bd=5, width=8, pady=10)
printButton.grid(row=0, column=3, pady=20, padx=5)

clearButton = Button(buttonFrame, text='Clear', font=('arial', 16, 'bold'), bg='gray20', fg='aliceblue',
                     bd=5, width=8, pady=10)
clearButton.grid(row=0, column=4, pady=20, padx=5)

root.mainloop()
