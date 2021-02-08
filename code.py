import tkinter as tk
from requests import get
from json import loads
frame = tk.Tk()
label = tk.Label(frame, text='Źródłem pochodzenia danych jest \nInstytut Meteorologii i Gospodarki Wodnej - Państwowy Instytut Badawczy\n\n WPISZ MIASTO', width=60).pack(pady=8, padx=10)
entry = tk.Entry(0, width=60, borderwidth=2)
entry.pack(padx=5)
def main():
    url = 'https://danepubliczne.imgw.pl/api/data/synop'
    response = get(url)
    city = entry.get()
    for row in loads(response.text):
        time, temp =row['godzina_pomiaru'], row['temperatura']
        if row['stacja'] in city: entry.insert(20, f' - temperatura o godzinie {time} wynosiła {temp} °C ')
button = tk.Button(frame, text='Sprawdź temperaturę', padx=30, background='sky blue',fg = 'black', command=main).pack(pady=5, padx = 5)
frame.mainloop()