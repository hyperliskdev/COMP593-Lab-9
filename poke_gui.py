from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from poke_api import get_pokemon

# Create a window
window = Tk()
window.title('Pokemon Viewer')


search_frame = ttk.LabelFrame(window, text='Search')
search_frame.grid(column=0, row=0, columnspan=2, padx=10, pady=10)

info_frame = ttk.LabelFrame(window, text='Info')
info_frame.grid(column=0, row=1, padx=10, pady=10)

stats_frame = ttk.LabelFrame(window, text='Stats')
stats_frame.grid(column=1, row=1, sticky=N, padx=10, pady=10)

# Search Group
search_label = ttk.Label(search_frame, text='Pokemon Name:')
search_label.grid(column=0, row=0)

search_entry = ttk.Entry(search_frame)
search_entry.grid(column=1, row=0, padx=10)

def handle_search():
    # Get the pokemon info from the api
    try:
        pokemon_info = get_pokemon(search_entry.get())
        
        info_height_value['text'] = pokemon_info['height']
        info_weight_value['text'] = pokemon_info['weight']
        info_type_value['text'] = pokemon_info['types'][0]['type']['name']
        
        stats_hp_value['value'] = pokemon_info['stats'][0]['base_stat']
        stats_att_value['value'] = pokemon_info['stats'][1]['base_stat']
        stats_def_value['value'] = pokemon_info['stats'][2]['base_stat']
        stats_spa_value['value'] = pokemon_info['stats'][3]['base_stat']
        stats_spd_value['value'] = pokemon_info['stats'][4]['base_stat']
        stats_spe_value['value'] = pokemon_info['stats'][5]['base_stat']
        

    except:
        messagebox.showerror('Pokemon Error', 'This pokemon does not exist.')



    return

search_btn = ttk.Button(search_frame, text='Search', command=handle_search)
search_btn.grid(column=2, row=0, padx=10)

# Info Group
info_height_header = ttk.Label(info_frame, text='Height:')
info_height_header.grid(column=0, row=0, padx=10)

info_height_value = ttk.Label(info_frame, text='0')
info_height_value.grid(column=1, row=0, padx=10)


info_weight_header = ttk.Label(info_frame, text='Weight:')
info_weight_header.grid(column=0, row=1, padx=10)

info_weight_value = ttk.Label(info_frame, text='0')
info_weight_value.grid(column=1, row=1, padx=10)

info_type_header = ttk.Label(info_frame, text='Type:')
info_type_header.grid(column=0, row=2, padx=10)

info_type_value = ttk.Label(info_frame, text='')
info_type_value.grid(column=1, row=2, padx=10)


# Stats Group
stats_hp_header = ttk.Label(stats_frame, text='HP:')
stats_hp_header.grid(column=0, row=0, padx=10)

stats_hp_value = ttk.Progressbar(stats_frame, orient=HORIZONTAL, length=100, maximum=255, mode='determinate')
stats_hp_value.grid(column=1, row=0, padx=10)

stats_att_header = ttk.Label(stats_frame, text='Attack:')
stats_att_header.grid(column=0, row=1, padx=10)

stats_att_value = ttk.Progressbar(stats_frame, orient=HORIZONTAL, length=100, maximum=255, mode='determinate')
stats_att_value.grid(column=1, row=1, padx=10)


stats_def_header = ttk.Label(stats_frame, text='Defense:')
stats_def_header.grid(column=0, row=2, padx=10)

stats_def_value = ttk.Progressbar(stats_frame, orient=HORIZONTAL, length=100, maximum=255, mode='determinate')
stats_def_value.grid(column=1, row=2, padx=10)

stats_spa_header = ttk.Label(stats_frame, text='Sp. Atk:')
stats_spa_header.grid(column=0, row=3, padx=10)

stats_spa_value = ttk.Progressbar(stats_frame, orient=HORIZONTAL, length=100, maximum=255, mode='determinate')
stats_spa_value.grid(column=1, row=3, padx=10)

stats_spd_header = ttk.Label(stats_frame, text='Sp. Def:')
stats_spd_header.grid(column=0, row=4, padx=10)

stats_spd_value = ttk.Progressbar(stats_frame, orient=HORIZONTAL, length=100, maximum=255, mode='determinate')
stats_spd_value.grid(column=1, row=4, padx=10)

stats_spe_header = ttk.Label(stats_frame, text='Speed:')
stats_spe_header.grid(column=0, row=5, padx=10)

stats_spe_value = ttk.Progressbar(stats_frame, orient=HORIZONTAL, length=100, maximum=255, mode='determinate')
stats_spe_value.grid(column=1, row=5, padx=10)



window.mainloop()
