from libraries import *
from calculator import *
from image_viewer import *
from database_app import *
from plotting_app import *

from libraries import *

db_name = 'address_book.db'

def create_menu(root):
    def our_command():
        pass

    menu = Menu(root)
    root.config(menu=menu)

    file_menu = Menu(menu)
    menu.add_cascade(label='File', menu=file_menu)
    file_menu.add_command(label='New...', command=our_command)
    file_menu.add_separator()
    file_menu.add_command(label='Exit', command=root.quit)

    edit_menu = Menu(menu)
    menu.add_cascade(label='Edit', menu=edit_menu)
    edit_menu.add_command(label='Cut', command=our_command)
    edit_menu.add_command(label='Copy', command=our_command)

    option_menu = Menu(menu)
    menu.add_cascade(label='Options', menu=option_menu)
    option_menu.add_command(label='Find', command=our_command)
    option_menu.add_command(label='Find Next', command=our_command)

#Declare window size when called, use parameters of window and screen size to determine centerpoint
def center_window(window, width, height):
    # Gets both half the screen width/height and window width/height
    positionRight = int(window.winfo_screenwidth()/2 - width/2)
    positionDown = int(window.winfo_screenheight()/2 - height/2)

    # Positions the window in the center of the page.
    window.geometry("+{}+{}".format(positionRight, positionDown))
    size = "{}x{}".format(width, height)
    window.geometry(size)
    return window


def create_root():
    #Root of all widgets
    root = Tk()
    title_text = "TK Sesh"
    root.title(title_text)
    root.configure(bg='slategray4')
    center_window(root, 1500, 1000)

    #Change window icon
    p1 = PhotoImage(file='files/bitcoin.png')
    root.iconphoto(False, p1)
    return root


def create_sidebar():
    #Root of all widgets
    top = Toplevel()
    top.title('sidebar')
    top.geometry('300x500')
    close_button = Button(top, text='Close Sidebar', command=top.destroy).grid()
    return top



#Homepage function is main window which adds upon root
def homepage(root):
    generic_padx = 10
    generic_pady = 10


    #SIMPLE TEXT
    header_text = "TKinter Test Interface"
    header = Label(root, text=header_text).grid(row=0, column=0)





    #FRAMES
    #Main dashboard, 5 rows x 2 columns
    dashboard = LabelFrame(root, text='Dashboard', padx=30, pady=20)
    dashboard.grid(row=1, column=0)
    dashboard.configure(bg='slategray3')




    module_bg = 'slategray2'
    module_button_bg = 'skyblue'


    #APPS SECTION
    apps_frame = LabelFrame(dashboard, text='Apps', padx=generic_padx, pady=generic_pady, bg=module_bg)
    apps_frame.grid(row=1, column=1)


    app_padx = 30
    app_pady = 10

    Button(apps_frame, text='Calculator', command=calculator_app, padx=app_padx, pady=app_pady, bg=module_button_bg).grid()
    Button(apps_frame, text='Image Viewer', command=image_viewer_app, padx=app_padx, pady=app_pady, bg=module_button_bg).grid()
    Button(apps_frame, text='Database', command=database_app, padx=app_padx, pady=app_pady, bg=module_button_bg).grid()
    Button(apps_frame, text='Weather', command=weather_app, padx=app_padx, pady=app_pady, bg=module_button_bg).grid()
    Button(apps_frame, text='Plotting App', command=plotting_app, padx=app_padx, pady=app_pady, bg=module_button_bg).grid()







    #INPUT
    input_frame = LabelFrame(dashboard, text='Input Field', padx=generic_padx, pady=generic_pady, bg=module_bg)
    input_frame.grid(row=1, column=2)

    Label(input_frame, text="Enter Text:", bg=module_bg).grid(row=0)
    entry = Entry(input_frame, width=50)
    entry.grid(row=1, columnspan=2)

    #entry.insert(1, "Enter a cryptocurrency...") #Placeholder text
    input_text = entry.get()
    Label(input_frame, text='', bg=module_bg).grid(row=4)

    def display_input():
        Label(input_frame, text=entry.get(), bg=module_bg).grid(row=4)

    Button(input_frame, text="Click Here!", command=display_input, bg=module_button_bg).grid(row=3)







    #RADIOS
    radio_frame = LabelFrame(dashboard, text='Radio Buttons', padx=generic_padx, pady=generic_pady, bg=module_bg)
    radio_frame.grid(row=2, column=1)

    radios = [
        ("Option 1", 1),
        ("Option 2", 2),
        ("Option 3", 3),
        ("Option 4", 4),
        ("Option 5", 5),
    ]
    radio_val = IntVar()
    radio_val.set(0)

    def clicked_radio(val):
        Label(radio_frame, text=val, bg=module_bg).grid(row=len(radios)+1)


    for text, value in radios:
        radio = Radiobutton(radio_frame, text=text, variable=radio_val, value=value, bg=module_bg)
        radio.grid(column=0)

    Button(radio_frame, text="Select", command=lambda: clicked_radio(radio_val.get()), bg=module_button_bg).grid(column=0)








    #SCROLL BAR
    scroll_frame = LabelFrame(dashboard, text='Output Console', padx=generic_padx, pady=generic_pady, bg=module_bg)
    scroll_frame.grid(row=3, column=2)

    text_area = st.ScrolledText(scroll_frame, width=30, height=8, font=("Times New Roman", 15))
    text_area.grid(row=0, column=6, rowspan=10, pady=10, padx=10)

    # Inserting Text which is read only
    scrollbar_text = "Test"
    text_area.insert(INSERT, scrollbar_text)

    # Making the text read only
    text_area.configure(state='disabled')












    #BUTTON FRAME
    button_frame = LabelFrame(dashboard, text='Button Depot', padx=generic_padx, pady=generic_pady, bg=module_bg)
    button_frame.grid(row=2, column=2)

    #Exit Button
    Button(button_frame, text='Quit', command=root.quit, bg='yellow').grid(row=0, column=1)

    button_padx = 30
    button_pady = 20
    Button(button_frame, text='1', padx=button_padx, pady=button_pady, bg='red3').grid(row=1, column=0)
    Button(button_frame, text='2', padx=button_padx, pady=button_pady, bg='red3').grid(row=1, column=1)
    Button(button_frame, text='3', command=lambda: audio_buttons(), padx=button_padx, pady=button_pady, bg='green2').grid(row=1, column=2)
    Button(button_frame, text='4', padx=button_padx, pady=button_pady, bg='red3').grid(row=2, column=0)
    Button(button_frame, text='5', padx=button_padx, pady=button_pady, bg='red3').grid(row=2, column=1)
    Button(button_frame, text='6', padx=button_padx, pady=button_pady, bg='red3').grid(row=2, column=2)
    Button(button_frame, text='7', padx=button_padx, pady=button_pady, bg='red3').grid(row=3, column=0)
    Button(button_frame, text='8', padx=button_padx, pady=button_pady, bg='red3').grid(row=3, column=1)
    Button(button_frame, text='9', padx=button_padx, pady=button_pady, bg='red3').grid(row=3, column=2)

    #Broken Button
    Button(button_frame, text="Broken", state=DISABLED, bg=module_button_bg).grid(row=0, column=2)

    #MESSAGE BOXES
    # showinfo, showwarning, showerror, askquestion, askokcancel, askyesno
    def info_popup():
        messagebox.showinfo('Info', 'Testing...')

    def error_popup():
        messagebox.showerror('Error', 'Virus Detected')

    def ask_popup():
        response = messagebox.askquestion('Continue', 'Continue shutting down computer?')
        if response == 'yes':
            Label(button_frame, text='Shutting Down...').grid(row=10, column=3)
        else:
            Label(button_frame, text='Wrong Choice').grid(row=10, column=3)

    Button(button_frame, text='INFO', command=info_popup, bg='yellow').grid(row=10, column=0)
    Button(button_frame, text='ERROR', command=error_popup, bg='orange').grid(row=10, column=1)
    Button(button_frame, text='?', command=ask_popup, bg='yellow').grid(row=10, column=2)









    #FILE SEARCH FRAME
    #Will only return locatiom of file (c:\\ etc.)
    file_frame = LabelFrame(dashboard, text='File Search', padx=generic_padx, pady=generic_pady, bg=module_bg)
    file_frame.grid(row=1, column=3)

    def open_explorer():
        root.filename = filedialog.askopenfilename(initialdir="/", title="Select A File", filetypes=(('png files', '*.png'), ('all files', '*.*')))
        upload_label = Label(file_frame, text=root.filename, bg=module_bg).grid(row=2, column=0)

    Label(file_frame, text='Search for Files', bg=module_bg).grid(row=0, column=0)
    Button(file_frame, text='Browse', command=open_explorer, bg=module_button_bg).grid(row=1, column=0)




    #SLIDER FRAME
    slider_frame = LabelFrame(dashboard, text='Sliders', padx=generic_padx, pady=generic_pady, bg=module_bg)
    slider_frame.grid(row=3, column=1)

    vh_sum = 0
    Label(slider_frame, text="X + Y = " + str(vh_sum), bg=module_bg).grid(row=3, column=3)

    def slide(var):
        vh_sum = vertical.get() + horizontal.get()
        Label(slider_frame, text="X + Y = " + str(vh_sum), bg=module_bg).grid(row=3, column=3)

    horizontal = Scale(slider_frame, from_=0, to=1000, orient=HORIZONTAL, command=slide, bg=module_bg)
    Label(slider_frame, text="X-Slider", bg=module_bg).grid(row=0, column=0)
    horizontal.grid(row=1, column=0)

    vertical = Scale(slider_frame, from_=0, to=1000, command=slide, bg=module_bg)
    Label(slider_frame, text="Y-Slider", bg=module_bg).grid(row=0, column=1)
    vertical.grid(row=1, column=1)










    #CHECKBOXES FRAME
    checkbox_frame = LabelFrame(dashboard, text='Checkbox', padx=generic_padx, pady=generic_pady, bg=module_bg)
    checkbox_frame.grid(row=2, column=3)

    checkboxes = [
        ('Python', 'Python'),
        ('Java', 'Java'),
        ('C++', 'C++'),
        ('HTML', 'HTML'),
        ('CSS', 'CSS')
    ]

    # mode = IntVar()
    # mode.set(0)

    selected_checks = []

    def select_option(var):
        print(selected_checks)
        if var in selected_checks:
            selected_checks.remove(var)
        else:
            selected_checks.append(var)

    def display_options():
        for item in selected_checks:
            print(item)
            print(selected_checks)
            Label(checkbox_frame, text=str(item), bg=module_bg).grid(column=0)


    check_var = StringVar()

    for text, value in checkboxes:
        print(value)
        checkbox = Checkbutton(checkbox_frame, text=text, variable=value, command=lambda: select_option(value), onvalue=value, offvalue='', bg=module_bg)
        #checkbox = Checkbutton(checkbox_frame, text=text, variable=value, command=lambda: select_option(value), onvalue=1, offvalue=0)

        checkbox.grid(column=0)

        #checkbox.deselect()

    Button(checkbox_frame, text='Show Selection', command=display_options, bg=module_button_bg).grid(row=len(checkboxes)+1)





    #LIST BOXES
    #Create initial module frame for list boxes
    listbox_frame = LabelFrame(dashboard, text='List Boxes', padx=generic_padx, pady=generic_pady, bg=module_bg)
    listbox_frame.grid(row=3, column=4)

    #Frame within list box module
    listbox_subframe = Frame(listbox_frame)
    listbox_subframe.grid(row=1)

    listbox_scrollbar = Scrollbar(listbox_subframe, orient=VERTICAL)

    test_listbox = Listbox(listbox_subframe, width=10, yscrollcommand=listbox_scrollbar.set, selectmode=EXTENDED)
    test_listbox.grid(row=0, column=0)

    listbox_scrollbar.config(command=test_listbox.yview)
    listbox_scrollbar.grid(row=0, column=1, sticky=NS)



    cryptos = ['BTC', 'ETH', 'ADA', 'BNB', 'DOT', 'LINK', 'XRP', 'ETH', 'ADA', 'BNB', 'DOT', 'LINK', 'XRP']
    for item in cryptos:
        test_listbox.insert(END, item)

    def select_listbox():
        listbox_label.config(text=test_listbox.get(ANCHOR))

    def select_all_listbox():
        result = ''
        for item in test_listbox.curselection():
            result = result + str(test_listbox.get(item)) + '\n'
        listbox_label.config(text=result)

    def delete_listbox():
        #Highlighted object is ANCHOR
        test_listbox.delete(ANCHOR)
        listbox_label.config(text='')

    def delete_all_listbox():
        test_listbox.delete(0, END)
        listbox_label.config(text='')

    def delete_multiple_listbox():
        for item in reversed(test_listbox.curselection()):
            test_listbox.delete(item)



    Button(listbox_frame, text='Select', command=select_listbox, bg=module_button_bg).grid(row=2)
    Button(listbox_frame, text='Select All', command=select_all_listbox, bg=module_button_bg).grid(row=3)

    Button(listbox_frame, text='Delete', command=delete_listbox, bg=module_button_bg).grid(row=4)
    Button(listbox_frame, text='Delete All', command=delete_all_listbox, bg=module_button_bg).grid(row=5)
    Button(listbox_frame, text='Delete Multiple', command=delete_multiple_listbox, bg=module_button_bg).grid(row=6)

    listbox_label = Label(listbox_frame, text='', bg=module_bg)
    listbox_label.grid(row=10)







    #DROPDOWN FRAME
    dropdown_frame = LabelFrame(dashboard, text='List Boxes', padx=generic_padx, pady=generic_pady, bg=module_bg)
    dropdown_frame.grid(row=3, column=3)

    options = [
        'Monday',
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday',
        'Saturday',
        'Sunday'
    ]

    clicked = StringVar()
    clicked.set(options[0])

    def show_dropdown():
        Label(dropdown_frame, text=clicked.get(), bg=module_bg).grid(row=3)

    Label(dropdown_frame, text='Select a Day', bg=module_bg).grid(row=0)
    drop = OptionMenu(dropdown_frame, clicked, *options)
    drop.grid(row=1)

    Button(dropdown_frame, text='Show Selection', command=show_dropdown, bg=module_button_bg).grid(row=2)



    #SPINBOX FRAME
    spinbox_frame = LabelFrame(dashboard, text='Spinboxes', padx=generic_padx, pady=generic_pady, bg=module_bg)
    spinbox_frame.grid(row=2, column=4)

    test_spinbox = Spinbox(spinbox_frame, from_=0, to=10, increment=1, font=('Helvetica', 12))
    test_spinbox.grid(row=1)

    def grab():
        spinbox_label.config(text='Selected Option: ' + test_spinbox.get())

    Button(spinbox_frame, text='Submit', command=grab).grid(row=2)
    spinbox_label = Label(spinbox_frame, text='', bg=module_bg)
    spinbox_label.grid(row=3)



    #TREEVIEW FRAME
    treeview_frame = LabelFrame(dashboard, text='Treeview', padx=generic_padx, pady=generic_pady, bg=module_bg)
    treeview_frame.grid(row=1, column=5)

    treeview_subframe = Frame(treeview_frame)
    treeview_subframe.grid(row=0, column=0, pady=20)

    tree_scroll = Scrollbar(treeview_subframe, orient=VERTICAL)
    tree_scroll.grid(row=0, column=1, sticky=NS)

    tree_style = ttk.Style()
    tree_style.theme_use('alt')
    tree_style.configure('Treeview',
                         background='silver',
                         foreground='black',
                         rowheight=25,
                         fieldbackground='silver'
                         )
    tree_style.map('Treeview',
                   background=[('selected', 'blue')])

    tree = ttk.Treeview(treeview_subframe, yscrollcommand=tree_scroll.set)
    tree.grid(row=0, column=0)

    tree_scroll.config(command=tree.yview)


    tree['columns'] = ('Name', 'ID')

    tree.column('#0', width=0, stretch=NO)
    tree.column('Name', anchor=W, width=120)
    tree.column('ID', anchor=CENTER, width=40)

    tree.heading('Name', text='Name', anchor=W)
    tree.heading('ID', text='ID', anchor=CENTER)

    tree_data = [
        ['John', 1],
        ['Bob', 2],
        ['Alice', 3],
        ['John', 1],
        ['Bob', 2],
        ['Alice', 3],
        ['John', 1],
        ['Bob', 2],
        ['Alice', 3],
        ['John', 1],
        ['Bob', 2],
        ['Alice', 3],
        ['John', 1],
        ['Bob', 2],
        ['Alice', 3],
        ['John', 1],
        ['Bob', 2],
        ['Alice', 3],
        ['John', 1],
        ['Bob', 2],
        ['Alice', 3],
        ['John', 1],
        ['Bob', 2],
        ['Alice', 3],
        ['John', 1],
        ['Bob', 2],
        ['Alice', 3],
        ['John', 1],
        ['Bob', 2],
        ['Alice', 3],
        ['John', 1],
        ['Bob', 2],
        ['Alice', 3],
        ['John', 1],
        ['Bob', 2],
        ['Bob', 2],
        ['Alice', 3],
        ['John', 1],
        ['Bob', 2],
        ['Alice', 3],
        ['John', 1],
        ['Bob', 2],
        ['Alice', 3],
        ['John', 1],
        ['Bob', 2],
        ['Alice', 3],
        ['John', 1],
        ['Bob', 2],
        ['Alice', 3],
        ['John', 1],
        ['Bob', 2],
        ['Bob', 2],
        ['Alice', 3],
        ['John', 1],
        ['Bob', 2],
        ['Alice', 3],
        ['John', 1],
        ['Bob', 2],
        ['Alice', 3],
        ['John', 1],
        ['Bob', 2],
        ['Alice', 3],
        ['John', 1],
        ['Bob', 2],
        ['Alice', 3],
        ['John', 1],
        ['Bob', 2],
    ]

    tree.tag_configure('oddrow', background='white')
    tree.tag_configure('evenrow', background='lightblue')


    count = 0
    for item in tree_data:
        if count % 2 == 0:
            tree.insert(parent='', index='end', iid=count, text='', values=(item[0], item[1]), tags=('evenrow'))
        else:
            tree.insert(parent='', index='end', iid=count, text='', values=(item[0], item[1]), tags=('oddrow'))
        count += 1

    tree_entry_frame = Frame(treeview_subframe)
    tree_entry_frame.grid(row=2, column=0)

    name_label = Label(tree_entry_frame, text='Name')
    name_label.grid(row=0, column=0)

    id_label = Label(tree_entry_frame, text='ID')
    id_label.grid(row=0, column=1)

    name_entry = Entry(tree_entry_frame)
    name_entry.grid(row=1, column=0)

    id_entry = Entry(tree_entry_frame)
    id_entry.grid(row=1, column=1)

    def select_record():
        name_entry.delete(0, END)
        id_entry.delete(0, END)

        selected = tree.focus()
        values = tree.item(selected, 'values')

        name_entry.insert(0, values[0])
        id_entry.insert(0, values[1])

    #Need to pass event variable in
    def clicker(e):
        select_record()

    #Binding
    #tree.bind('<Double-1>', clicker)
    tree.bind('<ButtonRelease>', clicker)


    #SEARCH FRAME
    search_frame = LabelFrame(dashboard, text='Search', padx=generic_padx, pady=generic_pady, bg=module_bg)
    search_frame.grid(row=2, column=5)

    def update(data):
        search_list.delete(0, END)
        for item in data:
            search_list.insert(END, item)

    def fillout(e):
        search_entry.delete(0, END)
        search_entry.insert(0, search_list.get(ANCHOR))

    def check(e):
        typed = search_entry.get()
        if typed == '':
            data = toppings
        else:
            data = []
            for item in toppings:
                if typed.lower() in item.lower():
                    data.append(item)
        update(data)

    search_entry = Entry(search_frame, font=('Arial', 12))
    search_entry.grid(row=0)

    search_list = Listbox(search_frame, width=50)
    search_list.grid(row=1)

    toppings = ['Pepperoni', 'Sausage', 'Ham', 'Cheese', 'Pineapple', 'Beef', 'Onion', 'Olives', 'Bell Pepper', 'Chicken']
    update(toppings)
    search_list.bind("<<ListboxSelect>>", fillout)
    search_entry.bind("<KeyRelease>", check)



def calculator_app():
    top = Toplevel()
    top.title('Calculator')
    center_window(top, 290, 435)

    e = Entry(top, width=35, borderwidth=5)
    e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

    def button_click(number):
        current = e.get()
        new_number = str(current) + str(number)
        e.delete(0, END)
        e.insert(0, new_number)

    def button_clear():
        e.delete(0, END)

    def button_equal():
        second_num = e.get()
        e.delete(0, END)

        if math == 'addition':
            e.insert(0, f_num + float(second_num))
        elif math == 'subtraction':
            e.insert(0, f_num - float(second_num))
        elif math == 'multiplication':
            e.insert(0, f_num * float(second_num))
        elif math == 'division':
            e.insert(0, f_num / float(second_num))


    def button_add():
        first_num = e.get()
        global f_num
        global math
        math = 'addition'
        f_num = float(first_num)
        e.delete(0, END)

    def button_subtract():
        first_num = e.get()
        global f_num
        global math
        math = 'subtraction'
        f_num = float(first_num)
        e.delete(0, END)

    def button_multiply():
        first_num = e.get()
        global f_num
        global math
        math = 'multiplication'
        f_num = float(first_num)
        e.delete(0, END)

    def button_divide():
        first_num = e.get()
        global f_num
        global math
        math = 'division'
        f_num = float(first_num)
        e.delete(0, END)


    #lambda: is needed to pass parameters in function
    button_1 = Button(top, text='1', padx=40, pady=20, command=lambda: button_click(1))
    button_2 = Button(top, text='2', padx=40, pady=20, command=lambda: button_click(2))
    button_3 = Button(top, text='3', padx=40, pady=20, command=lambda: button_click(3))
    button_4 = Button(top, text='4', padx=40, pady=20, command=lambda: button_click(4))
    button_5 = Button(top, text='5', padx=40, pady=20, command=lambda: button_click(5))
    button_6 = Button(top, text='6', padx=40, pady=20, command=lambda: button_click(6))
    button_7 = Button(top, text='7', padx=40, pady=20, command=lambda: button_click(7))
    button_8 = Button(top, text='8', padx=40, pady=20, command=lambda: button_click(8))
    button_9 = Button(top, text='9', padx=40, pady=20, command=lambda: button_click(9))
    button_0 = Button(top, text='0', padx=40, pady=20, command=lambda: button_click(0))

    button_add = Button(top, text='+', padx=39, pady=20, command=button_add)
    button_equal = Button(top, text='=', padx=90, pady=20, command=button_equal)
    button_clear = Button(top, text='C', padx=91, pady=20, command=button_clear)

    button_subtract = Button(top, text='-', padx=41, pady=20, command=button_subtract)
    button_multiply = Button(top, text='x', padx=40, pady=20, command=button_multiply)
    button_divide = Button(top, text='/', padx=40, pady=20, command=button_divide)


    button_1.grid(row=3, column=0)
    button_2.grid(row=3, column=1)
    button_3.grid(row=3, column=2)

    button_4.grid(row=2, column=0)
    button_5.grid(row=2, column=1)
    button_6.grid(row=2, column=2)

    button_7.grid(row=1, column=0)
    button_8.grid(row=1, column=1)
    button_9.grid(row=1, column=2)

    button_0.grid(row=4, column=0)
    button_add.grid(row=5, column=0)
    button_equal.grid(row=5, column=1, columnspan=2)
    button_clear.grid(row=4, column=1, columnspan=2)

    button_subtract.grid(row=6, column=0)
    button_multiply.grid(row=6, column=1)
    button_divide.grid(row=6, column=2)


def image_viewer_app():
    global image_label
    top = Toplevel()
    top.title('Image Viewer')

    center_window(top, 850, 900)

    #Check folder for any files and add them to image_list
    folder = 'images'
    image_files = [f for f in listdir(folder) if isfile(join(folder, f))]
    image_list = []

    for filename in image_files:
        file = os.path.join(folder, filename)
        image_object = ImageTk.PhotoImage(Image.open(file))
        image_list.append(image_object)

    status = Label(top, text="Image 1 of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)

    image_label = Label(top, image=image_list[0])
    image_label.grid(row=0, column=0, columnspan=3)


    def forward(image_number):
        global image_label
        global button_forward
        global button_back

        image_label.grid_forget()
        image_label = Label(top, image=image_list[image_number-1])

        if image_number == len(image_list):
            button_forward = Button(top, text=">>", state=DISABLED)
        else:
            button_forward = Button(top, text=">>", command=lambda: forward(image_number+1))
        button_back = Button(top, text="<<", command=lambda: back(image_number-1))

        image_label.grid(row=0, column=0, columnspan=3)
        button_back.grid(row=1, column=0)
        button_forward.grid(row=1, column=2)

        status = Label(top, text="Image " + str(image_number) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
        status.grid(row=2, column=0, columnspan=3, sticky=W+E)

    def back(image_number):
        global image_label
        global button_forward
        global button_back

        image_label.grid_forget()
        image_label = Label(top, image=image_list[image_number-1])

        button_forward = Button(top, text=">>", command=lambda: forward(image_number+1))
        if image_number == 1:
            button_back = Button(top, text="<<", state=DISABLED)
        else:
            button_back = Button(top, text="<<", command=lambda: back(image_number-1))

        image_label.grid(row=0, column=0, columnspan=3)
        button_back.grid(row=1, column=0)
        button_forward.grid(row=1, column=2)

        status = Label(top, text="Image " + str(image_number) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
        status.grid(row=2, column=0, columnspan=3, sticky=W+E)

    button_back = Button(top, text="<<", command=back, state=DISABLED)
    button_exit = Button(top, text="Exit", command=top.destroy)
    button_forward = Button(top, text=">>", command=lambda: forward(2))


    button_back.grid(row=1, column=0)
    button_exit.grid(row=1, column=1)
    button_forward.grid(row=1, column=2)

    status.grid(row=2, column=0, columnspan=3, sticky=W+E)



def database_app():
    top = Toplevel()
    top.title('Database')
    center_window(top, 400, 600)

    # Connect to database and create cursor
    conn = sqlite3.connect(db_name)
    c = conn.cursor()


    #Create Table
    def create_address_table():
        c.execute("""CREATE TABLE addresses (
            first_name text,
            last_name text,
            address text,
            city text,
            state text,
            zipcode integer
            )""")
    #create_address_table()

    def delete():
        conn = sqlite3.connect(db_name)
        c = conn.cursor()

        c.execute("DELETE from addresses WHERE oid=" + delete_box.get())

        conn.commit()
        conn.close()

    def update():
        conn = sqlite3.connect(db_name)
        c = conn.cursor()

        record_id = delete_box.get()
        c.execute("""UPDATE addresses SET
                    first_name = :first,
                    last_name = :last,
                    address = :address,
                    city = :city,
                    state = :state,
                    zipcode = :zipcode
                    
                    WHERE oid = :oid""",
        {
            'first': f_name_editor.get(),
            'last': l_name_editor.get(),
            'address': address_editor.get(),
            'city': city_editor.get(),
            'state': state_editor.get(),
            'zipcode': zipcode_editor.get(),

            'oid': record_id
        })

        conn.commit()
        conn.close()
        editor.destroy()


    def edit():
        #Open editor in new window
        global editor
        editor = Toplevel()
        editor.title('Update Record')
        center_window(editor, 400, 300)

        conn = sqlite3.connect(db_name)
        c = conn.cursor()


        record_id = delete_box.get()
        c.execute("SELECT * FROM addresses WHERE oid = " + record_id)
        records = c.fetchall()


        global f_name_editor
        global l_name_editor
        global address_editor
        global city_editor
        global state_editor
        global zipcode_editor


        # Entry Fields
        f_name_label = Label(editor, text="First Name").grid(row=0, column=0, pady=(10, 0))
        f_name_editor = Entry(editor, width=30)
        f_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))

        l_name_label = Label(editor, text="Last Name").grid(row=1, column=0)
        l_name_editor = Entry(editor, width=30)
        l_name_editor.grid(row=1, column=1)

        address_label = Label(editor, text="Address").grid(row=2, column=0)
        address_editor = Entry(editor, width=30)
        address_editor.grid(row=2, column=1)

        city_label = Label(editor, text="State").grid(row=3, column=0)
        city_editor = Entry(editor, width=30)
        city_editor.grid(row=3, column=1)

        state_label = Label(editor, text="City").grid(row=4, column=0)
        state_editor = Entry(editor, width=30)
        state_editor.grid(row=4, column=1)

        zipcode_label = Label(editor, text="Zipcode").grid(row=5, column=0)
        zipcode_editor = Entry(editor, width=30)
        zipcode_editor.grid(row=5, column=1)



        for record in records:
            f_name_editor.insert(0, record[0])
            l_name_editor.insert(0, record[1])
            address_editor.insert(0, record[2])
            city_editor.insert(0, record[3])
            state_editor.insert(0, record[4])
            zipcode_editor.insert(0, record[5])


        # Save Button
        save_button = Button(editor, text="Save Record", command=update)
        save_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10, ipadx=145)


        conn.commit()
        conn.close()

    def submit():
        conn = sqlite3.connect(db_name)
        c = conn.cursor()
        c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
                  {
                      'f_name': f_name.get(),
                      'l_name': l_name.get(),
                      'address': address.get(),
                      'city': city.get(),
                      'state': state.get(),
                      'zipcode': zipcode.get()
                  })
        conn.commit()
        conn.close()

        f_name.delete(0, END)
        l_name.delete(0, END)
        address.delete(0, END)
        city.delete(0, END)
        state.delete(0, END)
        zipcode.delete(0, END)

    def query():
        conn = sqlite3.connect(db_name)
        c = conn.cursor()

        c.execute("SELECT *, oid FROM addresses")
        # c.fetchone()
        records = c.fetchall()
        # c.fetchmany(10)

        print_records = ''
        for record in records:
            print_records += str(record[0]) + ' ' + str(record[1]) + ' \t' + str(record[6]) + '\n'

        Label(top,text=print_records).grid(row=11, column=0, columnspan=2)

        conn.commit()
        conn.close()



    #Entry Fields
    f_name_label = Label(top, text="First Name").grid(row=0, column=0, pady=(10,0))
    f_name = Entry(top, width=30)
    f_name.grid(row=0, column=1, padx=20, pady=(10,0))

    l_name_label = Label(top, text="Last Name").grid(row=1, column=0)
    l_name = Entry(top, width=30)
    l_name.grid(row=1, column=1)

    address_label = Label(top, text="Address").grid(row=2, column=0)
    address = Entry(top, width=30)
    address.grid(row=2, column=1)

    city_label = Label(top, text="State").grid(row=3, column=0)
    city = Entry(top, width=30)
    city.grid(row=3, column=1)

    state_label = Label(top, text="City").grid(row=4, column=0)
    state = Entry(top, width=30)
    state.grid(row=4, column=1)

    zipcode_label = Label(top, text="Zipcode").grid(row=5, column=0)
    zipcode = Entry(top, width=30)
    zipcode.grid(row=5, column=1)


    delete_box_label = Label(top, text="Edit/Delete ID").grid(row=9, column=0, pady=5)
    delete_box = Entry(top, width=30)
    delete_box.grid(row=9, column=1, pady=5)



    #Submit Button
    submit_button = Button(top, text="Add Record to Database", command=submit)
    submit_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10, ipadx=100)

    #Query Button
    query_button = Button(top, text="Show Records", command=query)
    query_button.grid(row=7, column=0, columnspan=2, padx=10, pady=10, ipadx=137)

    #Delete Button
    delete_button = Button(top, text="Delete Record", command=delete)
    delete_button.grid(row=10, column=0, columnspan=2, padx=10, pady=10, ipadx=136)

    #Edit Button
    edit_button = Button(top, text="Edit Record", command=edit)
    edit_button.grid(row=12, column=0, columnspan=2, padx=10, pady=10, ipadx=143)

    #Commit and close connection
    conn.commit()
    conn.close()


def weather_app():
    top = Toplevel()
    top.title('Weather')
    center_window(top, 300, 300)



def plotting_app():
    top = Toplevel()
    top.title('Data Analysis')
    center_window(top, 300, 300)

    def graph():
        house_prices = np.random.normal(200000, 25000, 5000)
        plt.hist(house_prices, 200)
        plt.show()

    Button(top, text="Plot Graph", command=graph).grid(row=5)


def audio_buttons():
    pygame.mixer.init()

    pygame.mixer.music.load('files/audio.mp3')
    pygame.mixer.music.play(loops=0)




def main():
    root = create_root()
    create_menu(root)
    #sidebar = create_sidebar()


    homepage(root)



    root.mainloop()





if __name__ == '__main__':
    main()