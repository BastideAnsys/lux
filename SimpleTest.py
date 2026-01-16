import tkinter as tk
root = tk.Tk()
root.title("This is a new title from branch3")
root.configure(background="darkgreen")
root.minsize(200, 200)
root.maxsize(500, 500)
root.geometry("300x300+50+50")

# Add BLue button
bouton = tk.Button(root, text="Cliquez ici", background="Blue", fg="white")
bouton.pack(pady=20)  # Display vertical

root.mainloop()