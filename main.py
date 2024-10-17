import csv
import json
import os

def csv_to_json(csv_file_path, json_file_path):
    """
    Converte un file CSV in un file JSON.
    
    :param csv_file_path: Percorso del file CSV di input.
    :param json_file_path: Percorso del file JSON di output.
    """
    data = []
    
    # Leggi il file CSV
    with open(csv_file_path, encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        
        # Aggiungi ogni riga del CSV come dizionario alla lista 'data'
        for row in csv_reader:
            data.append(row)

    # Scrivi i dati nel file JSON
    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)

def file_exists(file_path):
    """
    Verifica se un file esiste.
    
    :param file_path: Percorso del file.
    :return: True se il file esiste, False altrimenti.
    """
    return os.path.isfile(file_path)

def main():
    """
    Funzione principale che esegue la conversione del CSV in JSON.
    """
    csv_file_path = '../Pandas/pokemon.csv'
    json_file_path = '../Pandas/pokemon.json'  # Specifica il percorso del file JSON
    
    if file_exists(csv_file_path):
        csv_to_json(csv_file_path, json_file_path)
        print(f'File JSON generato correttamente: {json_file_path}')
    else:
        print(f'Il file CSV specificato non esiste: {csv_file_path}')

if __name__ == "__main__":
    main()