import random
import tkinter as tk

root = tk.Tk()

#helv36 = tk.tkFont.Font(family='Helvetica',
#        size=36, weight='bold')
#parallel lists

elementNames = ["Hydrogen", "Helium", "Lithium", "Beryllium", "Boron", "Carbon",
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
atomicNumber = []
for i in range(1, 119):
    atomicNumber.append(i)

atomicMass = [1.008, 4.0026, 6.94, 9.0122, 10.81, 12.011, 13.007, 15.999, 18.998,
              20.180, 22.990, 24.305, 26.982, 28.085, 30.974, 32.06, ]

funFacts = []

score = 0

questionPool = [atomicNumber, atomicMass, funFacts]
currentQuestion = ""
currentAnswer = []
randomElement = 0
userAnswer = ""

def qAGen():
    # generates random "element", but actually the element's index, so (<atomicNumber> - 1)
    randomElement = random.randrange(118)
    # generates the actual element(the answer)
    currentAnswer = atomicNumber[randomElement]
    # generates the question using the randomElement index within one of the question pools
    currentQuestion = random.choice(questionPool)[randomElement]

def isCorrect():
    # just checks if the user's answer is the same as the actual answer (currentAnswer =? userAnswer)
    if userAnswer.lower() == currentAnswer.lower():
        return True
    elif userAnswer.lower() != currentAnswer.lower():
        return False

class Application(tk.Frame):
    def __init__(self, master = None):
        tk.Frame.__init__(self, master)
        self.grid(sticky=tk.E)
        self.createWidgets()
        self.Correct = False
        #self.total_label_text = tk.Text()
        #self.total_label = tk.Label(master, textvariable=self.Correct)
        #self.label = tk.Label(master, text="Answer:")
        user_input1 = tk.Entry(master)


        #layout
        #self.label.grid(row=0, column=0, sticky=tk.W)
        user_input1.grid(row=0, column=0)
        user_input1.anchor()
    #def start(self):
    def createWidgets(self):

        top=self.winfo_toplevel()
        top.rowconfigure(0, weight=1)
        top.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)   # HEY DAN! I don't know what all this tkinter nonsense means but make sure that the variable
        self.columnconfigure(0, weight=1)  # you use for user input transfers to the variable named "userAnswer" in my functions
        #self.quit = tk.Button(self, text='Quit', command=self.quit)
        #self.quit.grid(row=0, column=0,
        #    sticky=tk.E)
        label = tk.Label(self,
            anchor="w",fg="white",bg="blue")

#configures size of the window and initiates the running of the UI along with the title of the window
app = Application()
app.master.geometry("600x600")
app.master.title('Periodic_flash_cards')
app.mainloop()


'''
if __name__ == '__main__':
    main()
'''
