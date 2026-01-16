import tkinter as tk
root = tk.Tk()
root.title("This is a new title from branch3")
root.configure(background="darkgreen")
root.minsize(200, 200)
root.maxsize(500, 500)
root.geometry("300x300+50+50")

# Ajout d'un bouton avec un fond rouge
bouton = tk.Button(root, text="Cliquez ici", background="red", fg="white")
bouton.pack(pady=20)  # Affiche le bouton avec un espace vertical

root.mainloop()