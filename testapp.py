import tkinter as tk

def ma_fonction():
    print("Fonction exécutée !")
    root.after(1000, ma_fonction)

# Crée la fenêtre principale
root = tk.Tk()
root.title("Exemple Tkinter")

ma_fonction()

root.mainloop()
