# BASIC CALCULATOR PROJECT
from tkinter import Tk, Button, Label, Message, StringVar
import math

class calculator:
    global input_digit, disp, n, count_s, count_md, count_p, count_py, count_sr, count_n, disp
    def __init__(self, disp):
        self.disp = ''
        
    #-------------------------------------------------------------------------------------------->
    def error_msg():
        disp_cont_0.set('SYNTAX Error!')
        disp_cont_1.set('')
        input_digit = ''; disp = ''; n = ''
        count_md = 0; count_p = 0; count_py = 0; count_s = 0; count_sr = 0; count_n = 0
    #-------------------------------------------------------------------------------------------->
    def click(self,number,text):

        num = str(number)
        # LIMIT THE NUMBER OF INPUT TO FIT IN THE SCREEN
        if len(disp) < 23: 
            if num.isdigit():
                if disp != '' and disp[len(disp)-1] == 's': pass
                elif input_digit != '' and input_digit[len(input_digit)-2] == '**' and input_digit[len(input_digit)-1] != '2':
                    # LIMITER AFTER PRESSING xy
                    if count_n < 2:
                        n += num; count_n += 1
                        disp = disp + str(text)
                        disp_cont_0.set(disp)
                    else: pass
                else:
                    n += num
                    disp = disp + str(text)
                    disp_cont_0.set(disp)
                count_md = 0; count_p = 0; count_py = 0; count_sr = 0; count_a = 0
            elif number == '.':
                # CHECK IF USER PRESS THE . BUTTON TWICE IN A ROW
                if count_s < 1:
                    n += num
                    disp = disp + str(text)
                    disp_cont_0.set(disp)
                    count_s += 1
                else: pass
            elif number == 'a': # FIX ME
                if input_digit == '' or not input_digit[len(input_digit)-1].isdigit():
                    try:
                        if total != '0' or total != '':
                            # CHECK IF USER PRESS THE ANS BUTTON TWICE IN A ROW
                            if count_a < 1:
                                input_digit += total
                                disp = disp + str(text)
                                disp_cont_0.set(disp)
                                count_a += 1
                                n = ''
                            # IF YES THROW AN ERROR MESSAGE AND RESET THE COUNTER
                            else: error_msg(); count_a = 0
                        else: pass
                    except: pass
                else: pass
                count_md = 0; count_p = 0; count_py = 0; count_s = 0; count_sr = 0
            elif number == 's': # FIX ME
                counter = 1
                if input_digit == '':
                    try:
                        if n != '':
                            sr = math.sqrt(float(n))
                            input_digit += str(sr)
                            disp = disp + str(text)
                            disp_cont_0.set(disp)
                            n = ''
                        else: pass
                    except: pass
                else:
                    try: 
                        input_digit += n
                        # CHECK IF THE LAST CHAR OF THE STRING IS DIGIT
                        if input_digit[len(input_digit)-counter] == '.' and disp[len(disp)-counter] == '.' or input_digit[len(input_digit)-counter].isdigit() and disp[len(disp)-counter].isdigit():
                            while input_digit[len(input_digit)-counter] == '.' or input_digit[len(input_digit)-counter].isdigit():
                                counter += 1
                            ez = input_digit[len(input_digit)-(counter-1):]
                            input_digit = input_digit[:-(counter-1)]
                            input_digit += 'math.sqrt(%s)'%ez
                            disp = disp + str(text)
                            disp_cont_0.set(disp)
                            n = ''
                        else: pass
                    except: error_msg()
                print(input_digit)
                count_md = 0; count_p = 0; count_py = 0; count_s = 0; count_a = 0
            elif number == 'p':
                input_digit += n
                # CHECK IF USER PRESS THE x² BUTTON TWICE IN A ROW
                if count_p < 1:
                    input_digit += '**2'
                    disp = disp + str(text)
                    disp_cont_0.set(disp)
                    count_p += 1
                    n = ''
                else: pass
                count_md = 0; count_py = 0; count_s = 0; count_sr = 0; count_a = 0
            elif number == 'py':
                try:
                    input_digit += ('%g'%float(n))
                    # CHECK IF USER PRESS THE xy BUTTON TWICE IN A ROW
                    if count_py < 1:
                        input_digit += '**'
                        disp = disp + str(text)
                        disp_cont_0.set(disp)
                        count_py += 1
                        n = ''
                    else: pass
                except: error_msg()
                count_md = 0; count_p = 0; count_s = 0; count_sr = 0; count_a = 0
            else:
                if number == '*' or number == '/' or number == '+' or number == '-':
                    try:
                        # CHECK IF USER PRESS THE * or / or + or - BUTTON TWICE IN A ROW
                        if count_md < 1:
                            if n == '': pass
                            else: input_digit += ('%g'%float(n))
                            n = ''
                            input_digit = input_digit + num
                            disp = disp + str(text)
                            disp_cont_0.set(disp)
                            count_md += 1
                        # IF YES, REPLACE IT
                        else:
                            input_digit = input_digit[:-1]
                            disp = disp[:-1]
                            input_digit = input_digit + num
                            disp = disp + str(text)
                            disp_cont_0.set(disp)
                    except: pass
                    count_p = 0; count_py = 0; count_s = 0; count_sr = 0; count_a = 0; count_n = 0
                else:
                    if n == '': pass
                    else: input_digit += ('%g'%float(n))
                    n = ''
                    input_digit = input_digit + num
                    disp = disp + str(text)
                    disp_cont_0.set(disp)
                    count_md = 0
        else: pass
#-------------------------------------------------------------------------------------------->
# CLEAR EVERYTHING ON THE SCREEN AND RESET ALL EXCEPT FOR THE TOTAL(ans)
def clear():

    input_digit = ''; disp = ''; n = ''
    disp_cont_0.set(''); disp_cont_1.set('')
    count_a = 0; count_p = 0; count_md = 0; count_s = 0; count_py = 0; count_sr = 0; count_n = 0
#-------------------------------------------------------------------------------------------->
def equal():

    answer = ''
    if n == '': pass
    else:
        try: input_digit += ('%g'%float(n))
        except: error_msg()
    if input_digit == '': pass
    else:
        try:
            answer = eval(input_digit)
        except ZeroDivisionError as merror:
            disp_cont_0.set('Error! ' + str(merror)) # ('Math Error!')
            disp_cont_1.set('')
            input_digit = ''; disp = ''; n = ''
        except: error_msg()
        else:
            disp_cont_1.set('%g'%float(answer))
            total = str(answer)
            input_digit = ''; disp = ''; n = ''
    # RESET COUNTER
    count_a = 0; count_p = 0; count_py = 0; count_md = 0; count_s = 0; count_sr = 0; count_n = 0

#===============================Creation of the GUI==========================================>
calc = Tk()
calc.title('Calculator')
# calc.iconbitmap(r'c:\Python36\DLLs\calc.ico') # DISABLE THIS IN LINUX
calc.resizable(0,0)
# INITIALIZE THE GLOBAL VARIABLE
input_digit = ''    # VARIABLE FOR EVALUATION
disp = ''           # DISPLAY VARIABLE
n = ''              # NUMBER VARIABLE
total = ''          # VARIABLE FOR ANSWER
# KEY PRESS COUNTER
count_p = 0; count_py = 0; count_a = 0; count_md = 0; count_s = 0; count_sr = 0; count_n = 0
# Style (Number)
fn_w = 'bold'; fn_f = 'arial'; fn_s = 15; fgn_c = 'black'; pdn_x = 20; pdn_y = 10
# Style (other)
f_w = 'bold'; f_f = 'arial'; f_s = 15; fg_c = 'white'; pd_x = 20; pd_y = 10; border = 6
#-------------------------------------------------------------------------------------------->
disp_cont_0 = StringVar() # TOP DISPLAY (LCD)
disp_cont_1 = StringVar() # BOTTOM DISPLAY (LCD)
# WIDGET SYNTAX: var_name = widget_name(master or parent window[varname = Tk()], option...)
lcd_0 = Label(calc, font = ('lucida console', 20), textvariable = disp_cont_0, anchor = 'w', width = 24,
                         bg = 'gray').grid(row = 1, columnspan = 6, padx = 6)
lcd_1 = Label(calc, font = ('lucida console', 20), textvariable = disp_cont_1, anchor = 'e', width = 24,
                         bg = 'gray').grid(row = 2, columnspan = 6, padx = 6)
txt_0 = Message(calc, font = ('papyrus', 12, 'bold'), width = 450, pady = 10,
			text = 'Principles of Programming Languages Project').grid(row = 0, columnspan = 6)
txt_1 = Message(calc, font = ('arial', 15, 'bold'), fg = 'blue', width = 350,
			text = 'PYTHON TKINTER').grid(row = 3, columnspan = 6)
# Button Row
button7 = Button(calc,
	    activebackground = 'blue',
	    activeforeground = 'black',
            padx = pdn_x,
            pady = pdn_y,
            bd = border,
            fg = fgn_c,
            font = (fn_f, fn_s, fn_w),
            text = '7',
            bg = 'white',
            command = lambda : calculator.click(calculator, 7, '7')).grid(row = 4, column = 0)
button8 = Button(calc,
	    activebackground = 'blue',
	    activeforeground = 'black',
            padx = pdn_x,
            pady = pdn_y,
            bd = border,
            fg = fgn_c,
            font = (fn_f, fn_s, fn_w),
            text = '8',
            bg = 'blue',
            command = lambda : click(8, '8')).grid(row = 4, column = 1)
button9 = Button(calc,
	    activebackground = 'white',
	    activeforeground = 'black',
            padx = pdn_x,
            pady = pdn_y,
            bd = border,
            fg = fgn_c,
            font = (fn_f, fn_s, fn_w),
            text = '9',
            bg = 'blue',
            command = lambda : click(9, '9')).grid(row = 4, column = 2)
division = Button(calc,
	    activebackground = 'white',
	    activeforeground = 'black',
            padx = 19,
            pady = pdn_y,
            bd = border,
            fg = fgn_c,
            font = (f_f, f_s, f_w),
            text = '÷',
            bg = 'blue',
            command = lambda : click('/', '÷')).grid(row = 4, column = 3, ipadx =3)
o_paren = Button(calc,
	    activebackground = 'red',
	    activeforeground = 'black',
            padx = 19,
            pady = pd_y,
            bd = border,
            fg = fg_c,
            font = (f_f, f_s, f_w),
            text = '(',
            bg = 'blue',
            command = lambda : click('(', '(')).grid(row = 4, column = 4, ipadx = 3)
c_paren = Button(calc,
	    activebackground = 'red',
	    activeforeground = 'black',
            padx = 19,
            pady = pd_y,
            bd = border,
            fg = fg_c,
            font = (f_f, f_s, f_w),
            text = ')',
            bg = 'blue',
            command = lambda : click(')',')')).grid(row = 4, column = 5, ipadx = 3)
# Row 
button4 = Button(calc,
	    activebackground = 'blue',
	    activeforeground = 'black',
            padx = pdn_x,
            pady = pdn_y,
            bd = border,
            fg = fgn_c,
            font = (fn_f, fn_s, fn_w),
            text = '4',
            bg = 'white',
            command = lambda : click(4, '4')).grid(row = 5, column = 0)
button5 = Button(calc,
	    activebackground = 'blue',
	    activeforeground = 'black',
            padx = pdn_x,
            pady = pdn_y,
            bd = border,
            fg = fgn_c,
            font = (fn_f, fn_s, fn_w),
            text = '5',
            bg = 'white',
            command = lambda : click(5, '5')).grid(row = 5, column = 1)
button6 = Button(calc,
	    activebackground = 'white',
	    activeforeground = 'black',
            padx = pdn_x,
            pady = pdn_y,
            bd = border,
            fg = fgn_c,
            font = (fn_f, fn_s, fn_w),
            text = '6',
            bg = 'blue',
            command = lambda : click(6,'6')).grid(row = 5, column = 2)
product = Button(calc,
	    activebackground = 'white',
	    activeforeground = 'black',
            padx = 19,
            pady = pd_y,
            bd = border,
            fg = fg_c,
            font = (f_f, f_s, f_w),
            text = 'x',
            bg = 'blue',
            command = lambda : click('*', '×')).grid(row = 5, column = 3, ipadx = 3)
sq_root = Button(calc,
	    activebackground = 'red',
	    activeforeground = 'black',
            padx = pd_x,
            pady = pd_y,
            bd = border,
            fg = fg_c,
            font = (f_f, f_s, f_w),
            text = '√',
            bg = 'blue',
            command = lambda : click('s', 'sqr')).grid(row = 5, column = 4)
pow_2 = Button(calc,
	    activebackground = 'red',
	    activeforeground = 'black',
            padx = 16,
            pady = pd_y,
            bd = border,
            fg = fg_c,
            font = (f_f, f_s, f_w),
            text = 'x²',
            bg = 'blue',
            command = lambda : click('p', '²')).grid(row = 5, column = 5)
# row 
button1 = Button(calc,
	    activebackground = 'blue',
	    activeforeground = 'black',
            padx = pdn_x,
            pady = pdn_y,
            bd = border,
            fg = fgn_c,
            font = (fn_f, fn_s, fn_w),
            text = '1',
            bg = 'white',
            command = lambda : click(1, '1')).grid(row = 6, column = 0)
button2 = Button(calc,
	    activebackground = 'blue',
	    activeforeground = 'black',
            padx = pdn_x,
            pady = pdn_y,
            bd = border,
            fg = fgn_c,
            font = (fn_f, fn_s, fn_w),
            text = '2',
            bg = 'white',
            command = lambda : click(2, '2')).grid(row = 6, column = 1)
button3 = Button(calc,
	    activebackground = 'white',
	    activeforeground = 'black',
            padx = pdn_x,
            pady = pdn_y,
            bd = border,
            fg = fgn_c,
            font = (fn_f, fn_s, fn_w),
            text = '3',
            bg = 'red',
            command = lambda : click(3,'3')).grid(row = 6, column = 2)
addition = Button(calc,
	    activebackground = 'white',
	    activeforeground = 'black',
            padx = 22,
            pady = pd_y,
            bd = border,
            fg = fg_c,
            font = (f_f, f_s, f_w),
            text = '+',
            bg = 'red',
            command = lambda : click('+','+')).grid(row = 6, column = 3)
pow_y = Button(calc,
	    activebackground = 'white',
	    activeforeground = 'black',
            padx = 17,
            pady = pd_y,
            bd = border,
            fg = fg_c,
            font = (f_f, f_s, f_w),
            text = 'xᵞ',
            bg = 'red',
            command = lambda : click('py','^')).grid(row = 6, column = 4)
equal = Button(calc,
	    activebackground = 'red',
	    activeforeground = 'black',
            padx = 19,
            pady = 44,
            bd = border,
            fg = fg_c,
            font = (f_f, f_s, f_w),
            text = '=',
            bg = 'red',
            command = equal).grid(row = 6, column = 5, rowspan = 2)
# Row 
button0 = Button(calc,
	    activebackground = 'blue',
	    activeforeground = 'black',
            padx = pdn_x,
            pady = pdn_y,
            bd = border,
            fg = fgn_c,
            font = (fn_f, fn_s, fn_w),
            text = '0',
            bg = 'white',
            command = lambda : click(0, '0')).grid(row = 7, column = 0)
dot = Button(calc,
	    activebackground = 'blue',
	    activeforeground = 'black',
            padx = pdn_x,
            pady = pdn_y,
            bd = border,
            fg = fgn_c,
            font = (fn_f, fn_s, fn_w),
            text = '.',
            bg = 'red',
            command = lambda : click('.', '.')).grid(row = 7, column = 1, ipadx = 3)
clear = Button(calc,
	    activebackground = 'white',
	    activeforeground = 'black',
            padx = pd_x,
            pady = pd_y,
            bd = border,
            fg = fg_c,
            font = (f_f, f_s, f_w),
            text = 'c',
            bg = 'red',
            command = clear).grid(row = 7, column = 2)
subtract = Button(calc,
	    activebackground = 'white',
	    activeforeground = 'black',
            padx = 21,
            pady = pd_y,
            bd = border,
            fg = fg_c,
            font = (f_f, f_s, f_w),
            text = '-',
            bg = 'red',
            command = lambda : click('-', '-')).grid(row = 7, column = 3, ipadx = 3)
total = Button(calc,
	    activebackground = 'red',
	    activeforeground = 'black',
            padx = 9,
            pady = pd_y,
            bd = border,
            fg = fg_c,
            font = (f_f, f_s, f_w),
            text = 'ans',
            bg = 'red',
            command = lambda : click('a', 'ans')).grid(row = 7, column = 4)
txt_2 = Message(calc, font = ('papyrus', 9, 'bold'), 
		width = 450,
                pady = 10,
		text = '').grid(row = 8, columnspan = 6)
calc.mainloop()
