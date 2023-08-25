# Gregory Campbell      lab 13-6    March 7, 2022
"""
    This program creates a GUI that displays services available from a 
    fictional auto shop. The user can check boxes for services they
    want performed, and when they are finished, they can check a box to
    get the total of all charges.
"""
import tkinter

#=============global constants
# available services
OIL_CHANGE = 'Oil Change'
LUBE_JOB = 'Lube Job'
RADIATOR_FLUSH = 'Radiator Flush'
TRANSMISSION_FLUSH = 'Transmission Flush'
INSPECTION = 'Inspection'
MUFFLER_REPLACEMENT = 'Muffler Replacement'
TIRE_ROTATION = 'Tire Rotation'

# service prices
OIL_CHANGE_COST = 30
LUBE_JOB_COST = 20
RADIATOR_FLUSH_COST = 40
TRANSMISSION_FLUSH_COST = 100
INSPECTION_COST = 35
MUFFLER_REPLACEMENT_COST = 200
TIRE_ROTATION_COST = 20

#========== GUI class definition
class JoesAutomotive:
    

    def __init__(self):
        # create main window widget
        self.__create_main_window()

        # create 3 frames to group widgets
        self.__create_frames()

        # create and pack the widget for the top frame, which holds a label 
        self.__create_top_frame_widgets()

        # create and pack the widgets for the middle frame, which holds a series of checkboxes
        self.__create_mid_frame_widgets()
        
        # create and pack the widgets for the bottom frame, which holds a Convert and Quit button
        self.__create_bottom_frame_widgets()

        # pack the frames
        self.__pack_frames()
        
        # start main program loop
        tkinter.mainloop()

#========== methods

    def __create_main_window(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("Joe's Automotive")
        self.main_window.geometry('350x320-1200-600')       # set default size of window
        self.main_window['bg'] = '#99badd'                  # set new background color

    # create 3 frames to group widgets
    def __create_frames(self):
        self.top_frame = tkinter.Frame(self.main_window)
        self.mid_frame = tkinter.Frame(self.main_window)
        self.bot_frame = tkinter.Frame(self.main_window)
        self.top_frame['bg'] = '#99badd'        # set frame background color
        self.mid_frame['bg'] = '#99badd'
        self.bot_frame['bg'] = '#99badd'

    # create and pack the widget for the top frame, which holds a label
    def __create_top_frame_widgets(self):
        self.prompt_label = tkinter.Label(self.top_frame, text = ' Available Services and Prices\n--------------------------------')
        self.prompt_label['bg'] = '#99badd'     # set label background color

        # pack the widgets
        self.prompt_label.pack(side = 'top', pady = (20, 10))

    # create and pack the widgets for the middle frame, which holds a label and result field
    def __create_mid_frame_widgets(self):
        

        # create 7 IntVar objects, required to use check buttons
        self.cb_var1 = tkinter.IntVar()
        self.cb_var2 = tkinter.IntVar()
        self.cb_var3 = tkinter.IntVar()
        self.cb_var4 = tkinter.IntVar()
        self.cb_var5 = tkinter.IntVar()
        self.cb_var6 = tkinter.IntVar()
        self.cb_var7 = tkinter.IntVar()

        # initialize the intVar objects to 0 (unchecked)
        self.cb_var1.set(0)
        self.cb_var2.set(0)
        self.cb_var3.set(0)
        self.cb_var4.set(0)
        self.cb_var5.set(0)
        self.cb_var6.set(0)
        self.cb_var7.set(0)

        # create the ckeckbutton widgets in top frame
        self.cb1 = tkinter.Checkbutton(self.top_frame, text = f'{OIL_CHANGE}: ${OIL_CHANGE_COST}', variable = self.cb_var1, activebackground='#99badd')
        self.cb2 = tkinter.Checkbutton(self.top_frame, text = f'{LUBE_JOB}: ${LUBE_JOB_COST}', variable = self.cb_var2, activebackground='#99badd')
        self.cb3 = tkinter.Checkbutton(self.top_frame, text = f'{RADIATOR_FLUSH}: ${RADIATOR_FLUSH_COST}', variable = self.cb_var3, activebackground='#99badd')
        self.cb4 = tkinter.Checkbutton(self.top_frame, text = f'{TRANSMISSION_FLUSH}: ${TRANSMISSION_FLUSH_COST}', variable = self.cb_var4, activebackground='#99badd')
        self.cb5 = tkinter.Checkbutton(self.top_frame, text = f'{INSPECTION}: ${INSPECTION_COST}', variable = self.cb_var5, activebackground='#99badd')
        self.cb6 = tkinter.Checkbutton(self.top_frame, text = f'{MUFFLER_REPLACEMENT}: ${MUFFLER_REPLACEMENT_COST}', variable = self.cb_var6, activebackground='#99badd')
        self.cb7 = tkinter.Checkbutton(self.top_frame, text = f'{TIRE_ROTATION}: ${TIRE_ROTATION_COST}', variable = self.cb_var7, activebackground='#99badd')
        self.cb1['bg'] = '#99badd'      # change checkbutton background color
        self.cb2['bg'] = '#99badd'
        self.cb3['bg'] = '#99badd'
        self.cb4['bg'] = '#99badd'
        self.cb5['bg'] = '#99badd'
        self.cb6['bg'] = '#99badd'
        self.cb7['bg'] = '#99badd'

        # pack the Checkbuttons
        self.cb1.pack(anchor = 'w')
        self.cb2.pack(anchor = 'w')
        self.cb3.pack(anchor = 'w')
        self.cb4.pack(anchor = 'w')
        self.cb5.pack(anchor = 'w')
        self.cb6.pack(anchor = 'w')
        self.cb7.pack(anchor = 'w')

    # create and pack the widgets for the bottom frame, which holds a Get Total and Quit button
    def __create_bottom_frame_widgets(self):
        self.prompt_label = tkinter.Button(self.bot_frame, text = 'Current Total', command = self.get_total_cost)
        self.quit_button = tkinter.Button(self.bot_frame, text = 'Quit', command = self.main_window.destroy)

        #need to create a StringVar object to hold result value
        self.value = tkinter.StringVar()

        # create a label and associate it with the stringvAr obj
        self.current_total_label = tkinter.Label(self.bot_frame, textvariable = self.value)
        self.current_total_label['bg'] = '#99badd'

        # pack the widgets
        self.prompt_label.pack(side = 'left', padx = 5, pady = 20)
        self.current_total_label.pack(side = 'left', padx = 5, pady = 5)
        self.quit_button.pack(side = 'left', padx = 5, pady = 20)

    # pack the frames
    def __pack_frames(self):
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bot_frame.pack()

    # get_total_cost sums the cost of selected services
    def get_total_cost(self):
        # determine values of current selections
        if self.cb_var1.get() == 1:
            var1 = OIL_CHANGE_COST
        else:
            var1 = 0
        if self.cb_var2.get() == 1:
            var2 = LUBE_JOB_COST
        else:
            var2 = 0
        if self.cb_var3.get() == 1:
            var3 = RADIATOR_FLUSH_COST
        else:
            var3 = 0
        if self.cb_var4.get() == 1:
            var4 = TRANSMISSION_FLUSH_COST
        else:
            var4 = 0
        if self.cb_var5.get() == 1:
            var5 = INSPECTION_COST
        else:
            var5 = 0
        if self.cb_var6.get() == 1:
            var6 = MUFFLER_REPLACEMENT_COST
        else:
            var6 = 0
        if self.cb_var7.get() == 1:
            var7 = TIRE_ROTATION_COST
        else:
            var7 = 0

        # sum cost of choices, set that as the value to be displayed
        total_cost_of_selected_services = var1 + var2 + var3 + var4 + var5 + var6 + var7
        self.value.set(f'${total_cost_of_selected_services:.2f}')

#========== create an instance of the class
if __name__ == '__main__':
    JoesAutomotive()