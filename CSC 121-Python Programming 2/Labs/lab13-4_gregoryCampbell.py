# Gregory Campbell      lab 13-4    March 7, 2022
"""
    This program converts Celcius temperatures to Fahrenheit temperatures
    using a GUI. The user enters a Celcius temperature and then clicks a
    button to see the equivalent Fahrenheit temperature
"""
import tkinter

#========== GUI class definition
class CelciusToFahrenheit:
    def __init__(self):
        # create main window widget
        self.__create_main_window()

        # create 3 frames to group widgets
        self.__create_frames()

        # create and pack the widgets for the top frame, which hold a label and entry field
        self.__create_top_frame_widgets()

        # create and pack the widgets for the middle frame, which holds a label and result field
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
        self.main_window.title('Celcius to Fahrenheit Converter')
        self.main_window.geometry('350x160-1200-600')       # set default size of window
        self.main_window['bg'] = '#99badd'                  # set new background color

    # create 3 frames to group widgets
    def __create_frames(self):
        self.top_frame = tkinter.Frame(self.main_window)
        self.mid_frame = tkinter.Frame(self.main_window)
        self.bot_frame = tkinter.Frame(self.main_window)
        self.top_frame['bg'] = '#99badd'        # set frame background color
        self.mid_frame['bg'] = '#99badd'
        self.bot_frame['bg'] = '#99badd'

    # create and pack the widgets for the top frame, which hold a label and entry field
    def __create_top_frame_widgets(self):
        self.prompt_label = tkinter.Label(self.top_frame, text = 'Celcius Temperature: ')
        self.celcius_entry = tkinter.Entry(self.top_frame, width = 10)
        self.prompt_label['bg'] = '#99badd'     # set label background color

        # pack the widgets
        self.prompt_label.pack(side = 'left', pady = 20)
        self.celcius_entry.pack(side = 'left', pady = 20)

    # create and pack the widgets for the middle frame, which holds a label and result field
    def __create_mid_frame_widgets(self):
        self.result_label = tkinter.Label(self.mid_frame, text = 'Fahrenheit conversion:')
        self.result_label['bg'] = '#99badd'     # set label background color

        # need to create a StringVar object to hold result value
        self.value = tkinter.StringVar()

         # create a label and associate it with the stringvAr obj
        self.fahrenheit_label = tkinter.Label(self.mid_frame, textvariable = self.value)
        self.fahrenheit_label['bg'] = '#99badd'

        # pack the middle frame's widgets
        self.result_label.pack(side = 'left')
        self.fahrenheit_label.pack(side = 'left')

    # create and pack the widgets for the bottom frame, which holds a Convert and Quit button
    def __create_bottom_frame_widgets(self):
        self.calc_button = tkinter.Button(self.bot_frame, text = 'Convert to Fahrenheit', command = self.convert_to_fahrenheit)
        self.quit_button = tkinter.Button(self.bot_frame, text = 'Quit', command = self.main_window.destroy)

        # pack the widgets
        self.calc_button.pack(side = 'left', padx = 5, pady = 20)
        self.quit_button.pack(side = 'left', padx = 5, pady = 20)

    # pack the frames
    def __pack_frames(self):
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bot_frame.pack()

    # convert_to_fahrenheit takes a celcius temperature and converts it to degrees fahrenheit
    def convert_to_fahrenheit(self):
        # get the temperature to convert
        celcius = float(self.celcius_entry.get())

        # convert to fahrenheit
        fahrenheit = round(((9 / 5) * celcius) + 32, 2)

        # convert fahrenhet to string and store it in StringVar obj. This will automatically update the fahrenheit_label widget
        self.value.set(fahrenheit)

#========== create an instance of the class
if __name__ == '__main__':
    CelciusToFahrenheit()