import pandas as pd
from datetime import datetime
import os
import ipywidgets as widgets
from IPython.display import display, clear_output

input_date = widgets.Text(
    value='01/02/2024',
    placeholder='DD/MM/AAAA',
    description='Data:',
    disabled=False
)

filter_button = widgets.Button(
    description='Filtrar CSV',
    button_style='success'
)

exit = widgets.Output()

def filtrar_csv(date_str):
    file_path = 'file.csv'

    if not os.path.exists(file_path):
        print(f"⚠️ Arquivo '{file_path}' não encontrado.")
        return

    try:
        filtered_date = datetime.strptime(date_str, "%d/%m/%Y")
    except ValueError:
        print("❌ Data inválida! Use o formato DD/MM/AAAA.")
        return

    df = pd.read_csv(file_path, delimiter=',', dtype=str)
    df['date'] = df['date'].str.strip()
    df['date'] = pd.to_datetime(df['date'], format='%d/%m/%Y', errors='coerce')
    df = df.dropna(subset=['date'])

    filtered_df = df[df['date'] == filtered_date]

    if filtered_df.empty:
        print("⚠️ Nenhum dado encontrado para a data informada.")
        return

    file_name = f"filtrado_{date_str.replace('/', '-')}.csv"
    filtered_df.to_csv(file_name, index=False)
    print(f"✅ Arquivo '{file_name}' criado com sucesso com {len(filtered_df)} linha(s).")

@exit.capture()
def ao_clicar(b):
    clear_output()
    print("⏳ Processando...")
    filtrar_csv(input_date.value)

filter_button.on_click(ao_clicar)

# Exibir o widget na tela
display(input_date, filter_button, exit)
