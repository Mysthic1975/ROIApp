import tkinter as tk
from tkinter import ttk


# ROI = Return on Investment (Kapitalrendite) Formel: ROI=(Investition/Gewinn)×100
class ROIApp:
    def __init__(self, master):
        self.master = master
        master.title("Finanzrechner")

        # Label und Entry für Investition
        self.label = tk.Label(master, text="Investition:")
        self.label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

        self.investment_entry = ttk.Entry(master)
        self.investment_entry.grid(row=0, column=1, padx=10, pady=10, sticky=tk.E)

        # Label und Entry für Gewinn
        self.label = tk.Label(master, text="Gewinn:")
        self.label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

        self.profit_entry = ttk.Entry(master)
        self.profit_entry.grid(row=1, column=1, padx=10, pady=10, sticky=tk.E)

        # Button zum Berechnen
        self.calculate_button = tk.Button(master, text="Berechnen", command=self.calculate_roi)
        self.calculate_button.grid(row=2, column=0, columnspan=2, pady=20)

        # Label für das Ergebnis
        self.result_label = tk.Label(master, text="")
        self.result_label.grid(row=3, column=0, columnspan=2)

    def calculate_roi(self):
        try:
            # Versuche, Investition und Gewinn in Gleitkommazahlen umzuwandeln
            investment = float(self.investment_entry.get())
            profit = float(self.profit_entry.get())

            # Berechne ROI
            roi = (profit / investment) * 100

            # Zeige das Ergebnis an
            result_text = f"ROI: {roi:.2f}%"
            self.result_label.config(text=result_text)

        except ValueError:
            # Bei ungültigen Eingaben zeige eine Fehlermeldung an
            self.result_label.config(text="Bitte gültige Zahlen eingeben.")


if __name__ == "__main__":
    # Erstelle Tkinter-Fenster und starte die Hauptanwendung
    root = tk.Tk()
    app = ROIApp(root)
    root.geometry("300x200")
    root.mainloop()
