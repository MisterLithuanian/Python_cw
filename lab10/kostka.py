import tkinter as tk
import random

def rzuc_kostka():
    scianki = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    wylosowana = random.choice(scianki)
    label_wynik.config(text=wylosowana)
    kolor_kostki = ["#333333"]
    label_wynik.config(fg=random.choice(kolor_kostki))

root = tk.Tk()
root.title("Symulator Kostki")
root.geometry("500x550") 

label_wynik = tk.Label(root, text='\u2680', font=("Arial", 250), fg="#333333")
label_wynik.pack(expand=True, pady=20)

przycisk = tk.Button(
    root, 
    text="Rzut Kostka", 
    font=("Ariel", 24, "bold"), 
    bg="#333333",                
    fg="white",                 
    activebackground="#333333",   #
    activeforeground="white",
    padx=30,                      
    pady=15,                     
    cursor="hand2",               
    command=rzuc_kostka
)
przycisk.pack(pady=50)            

root.mainloop()