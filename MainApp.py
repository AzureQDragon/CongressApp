'''
Copyright © 2017 Daniel Moon, Luke Moon, Michael Kricheldorf
All Rights Reserved. This code may not be reproduced or reused in any manner whatsoever
without the consent of the writer.
'''



import random
import tkinter as tk

root = tk.Tk()

#helv36 = tk.tkFont.Font(family='Helvetica',
#        size=36, weight='bold')
#parallel lists
class Application(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
#--------------------------------------Variables--------------------------------
        self.master =  master
        self.createWidgets()
        self.atomic_mass = [1.008, 4.0026, 6.94, 9.0122, 10.81, 12.011, 13.007, 15.999, 18.998,
                      20.180, 22.990, 24.305, 26.982, 28.085, 30.974, 32.06, 35.45, 39.948,
                      39.098, 40.078, 44.956, 47.867, 50.942, 51.996, 54.938, 55.845, 58.933,
                      58.693, 63.546, 65.38, 69.723, 72.630, 74.922, 78.971, 79.904, 83.798,
                      85.468, 87.62, 88.906, 91.224, 92.906, 95.95, 98, 101.07, 102.9, 106.42,
                      107.87, 112.41, 114.82, 118.71, 121.76, 127.60, 126.90, 131.29, 132.91,
                      137.33, 138.91, 140.12, 140.91, 144.24, 145, 150.36, 151.96, 157.25, 158.93,
                      162.50, 164.93, 167.26, 168.93, 173.05, 174.97, 178.49, 180.95, 183.84,
                      186.21, 190.23, 192.22, 195.08, 196.97, 200.59, 204.38, 207.2, 208.98,
                      209, 210, 222, 223, 226, 227, 232.04, 231.04, 238.03, 237, 244, 243, 247,
                      247, 251, 252, 257, 258, 259, 266, 267, 268, 269, 270, 277, 278, 281,
                      282, 285, 286, 289, 290, 293, 294, 294]

        self.atomic_symbol= ["H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne", "Na", "Mg", "Al",
                         "Si", "P", "S", "Cl", "Ar", "K", "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe",
                         "Co", "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr", "Rb", "Sr", "Y",
                         "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Sb", "Te",
                         "I", "Xe", "Cs", "Ba", "La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb",
                         "Dy", "Ho", "Er", "Tm", "Yb", "Lu", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt",
                         "Au", "Hg", "Tl", "Pb", "Bi", "Po", "At", "Rn", "Fr", "Ra", "Ac", "Th", "Pa",
                         "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm", "Md", "No", "Lr", "Rf",
                         "Db", "Sg", "Bh", "Hs", "Mt", "Ds", "Rg", "Cn" , "Nh", "Fl", "Mc", "Lv", "Ts", "Og"]

        self.element_names = ["Hydrogen", "Helium", "Lithium", "Beryllium", "Boron", "Carbon",
                    "Nitrogen", "Oxygen", "Fluorine", "Neon", "Sodium", "Magnesium",
                    "Aluminium", "Silicon", "Phosphorus", "Sulfur", "Chlorine", "Argon",
                    "Potassium", "Calcium", "Scandium", "Titainiium", "Vanadium", "Chromium",
                    "Manganese", "Iron", "Cobalt", "Nickel", "Copper", "Zinc", "Gallium",
                    "Germanium", "Arsenic", "Selenium", "Bromine", "Krypton", "Rubidium",
                    "Strontium", "Yttrium", "Zirconium", "Niobium", "Molybdenum", "Technetium",
                    "Ruthenium", "Rhodium", "Palladium", "Silver", "Cadmium", "Indium", "Tin",
                    "Antimony", "Tellurium", "Iodine", "Xenon", "Caesium", "Barium", "Lanthanum",
                    "Cerium", "Praseodymium", "Neodymium", "Promethium", "Samarium", "Europium",
                    "Gadolinium", "Terbium", "Dysprosium", "Holmium", "Erbium", "Thulium",
                    "Ytterbium", "Lutetium", "Hafnium", "Tantalum", "Tungsten", "Rhenium",
                    "Osmium", "Iridium", "Platinum", "Gold", "Mercury", "Thallium", "Lead",
                    "Bismuth", "Polonium", "Astatine", "Radon", "Francium", "Radium",
                    "Actinium", "Thorium", "Protactinium", "Uranium", "Neptunium", "Plutonium",
                    "Americium", "Curium", "Berkelium", "Californium", "Einsteinium", "Fermium",
                    "Mendelevium", "Nobelium", "Lawrencium", "Rutherfordium", "Dubnium", "Seaborgium",
                    "Bohrium", "Hassium", "Meitnerium", "Darmstadtium", "Roentgenium", "Copernicium",
                    "Nihonium", "Flerovium", "Moscovium", "Livermorium", "Tennessine", "Organesson"]
        self.atomic_number = []
        for i in range(1, 119):
            self.atomic_number.append(i)
        self.element_charge = ['']
        self.cp_atomic_symbol = self.atomic_symbol
        self.cp_atomic_number = self.atomic_number
        self.cp_atomic_mass =self.atomic_mass
        self.displayed = False
        self.score = 0
        self.display_element = tk.StringVar(master)
        self.display_element.set(self.element_names[0])
        self.current_answer = ''
        self.element = ''
        self.question = ["The atomic number of this element is: ", "The atomic mass of this element is: ", "The atomic symbol of this element is: "]
        self.atomic_number_question = self.question[0]
        self.atomic_mass_questions = self.question[1]
        self.atomic_symbol_questions = self.question [2]
        self.question_pool = [self.atomic_number_question, self.atomic_mass_questions, self.atomic_symbol_questions]
        self.answer_pool = [self.atomic_number, self.atomic_mass, self.atomic_symbol]
        #self.total_label_text = tk.Text()
        #self.total_label = tk.Label(master, textvariable=self.correct)
        self.quest_text = tk.StringVar()
        self.correct = ''
        vcmd = master.register(self.validate) # we have to wrap the command
        self.user_answer = ''
        self.score = 0
        self.current_answer_int = 0
#--------------------------------------------Labels-----------------------------------------------
        self.correct_label = tk.Label(master, text = self.correct, bg = 'ghost white')
        self.element_label = tk.Label(master, text = self.display_element, bg = 'medium purple')
        self.score_label = tk.Label(master, text = 'Score: ' + str(self.score), bg='PaleGreen1')
        self.label = tk.Label(master, text= self.atomic_number_question, bg = 'ghost white')
#-----------------------------------------Buttons & Entry-------------------------------------------
        self.answer_button = tk.Button(master, text='Answer',  relief= 'flat', bg = "gray38", command= self.combine_func(self.delete_entry, self.checkAnswer))
        self.idk_button = tk.Button(master, text = 'Give up', command=self.outputAnswer, relief='flat', bg = "gray38")
        self.user_input = tk.Entry(master, validate="key", validatecommand=(vcmd, '%P'))
        self.skip_button = tk.Button(master, text = 'Skip', command=self.skipQuestion, relief = 'flat', bg = "gray38")
#--------------------------------------------layout----------------------------------------------
        self.grid(sticky=tk.E)
        self.idk_button.grid(row=2, column=4, padx = 5)
        self.element_label.grid(row=1, column =2, pady = 30)
        self.element_label.configure(font=("Verdana", 30))
        self.label.grid(row=2, column=0, sticky=tk.W)
        self.user_input.grid(row=2, column=2)
        self.score_label.grid(row=0, column=0)#, sticky=tk.E+tk.N)#, sticky=tk.S+tk.W)
        self.user_input.anchor()
        self.label.configure(text= self.atomic_number_question)
        self.answer_button.grid(row=2, column=5)
        self.correct_label.grid(row=1, column=0)
        self.skip_button.grid(row=2, column=3, padx=5)
#---------------------------------------------Setup------------------------------------------------
        self.qAGen()
#---------------------------------------------Functions-------------------------------------------
    def combine_func(self, *funcs):
        def combined_func(*args, **kwargs):
            for f in funcs:
                f(*args, **kwargs)
        return combined_func

    def qAGen(self):
        # generates random "element", but actually the element's index, so (<atomicNumber> - 1)
        random_element = random.randrange(118)
        random_num = random.randrange(3)
        # generates the question using the random_element index within one of the question pools
        self.current_answer = str(self.answer_pool[random_num][random_element])
        self.current_question= str(self.question_pool[random_num])
        self.element = self.element_names[random_element]
        self.display_element.set(self.element)
        self.element_label.configure(text = self.display_element.get(), bg = 'medium purple')
        #self.element_names[random_element]
        self.update()
    def delete_entry(self):
        self.user_input.delete(0, 'end')
    def skipQuestion(self):
        self.qAGen()
    def update(self):
        self.quest_text.set(self.current_question)
        self.label.configure(text = self.current_question)
    #Validatest the user input and outputs true so that th %p can be validated.
    def outputAnswer(self):
        if self.displayed == False:
            self.displayed = True
            self.score -= 1
        self.score_label.configure(text='Score ' + str(self.score))
        self.element_label.configure(text=self.element+': '+ self.current_answer, bg='tomato')
    def validate(self, new_input):
        if not new_input: # the field is being cleared
            self.user_answer = ''
            return True

        try:
            answer = str(new_input)
            self.user_answer = answer
            print(self.user_answer)
            return True
        except ValueError:
            return False

    def checkAnswer(self):
        # just checks if the user's answer is the same as the actual answer (currentAnswer =? user_answer)\
        print(self.current_answer)
        if self.user_answer.lower() == self.current_answer.lower() and self.displayed == False:
            print("true")
            #generates next question and answer for element
            self.qAGen()
            self.quest_text.set(self.current_question)
            self.display_element.set(self.element)
            self.score += 1
            self.score_label.configure(text='Score ' + str(self.score))
            self.correct = 'Correct'
            self.correct_label.configure(text=self.correct, bg = 'PaleGreen1')
            return True
        elif self.user_answer.lower() == self.current_answer.lower():
            self.qAGen()
            self.quest_text.set(self.current_question)
            self.display_element.set(self.element)
            self.score_label.configure(text='Score ' + str(self.score))
            self.correct = 'Correct'
            self.correct_label.configure(text=self.correct, bg = 'PaleGreen1')
        else:# self.user_answer.lower() !='md':# self.current_answer:
            print("false")
            self.score -= .5
            self.score_label.configure(text='Score ' + str(self.score))
            self.correct = 'Incorrect'
            self.correct_label.configure(text=self.correct, bg = 'tomato')
            return False


    def createWidgets(self):

        top=self.winfo_toplevel()
        #top.rowconfigure(0, weight=2)
        #top.columnconfigure(0, weight=1)
        #self.rowconfigure(0, weight=.5)   # HEY DAN! I don't know what all this tkinter nonsense means but make sure that the variable
        #self.columnconfigure(0, weight=.5)  # you use for user input transfers to the variable named "user_answer" in my functions
root.configure(background = 'ghost white')
#configures size of the window and initiates the running of the UI along with the title of the window
app = Application(root)
#app.master.geometry('700x300')
app.master.title('PTM')
app.mainloop()


'''
if __name__ == '__main__':
    main()
'''
