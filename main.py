import pandas as pd
import json

# 1. Load the Excel file
# Assuming your columns are: #, German Word, English Meaning, Russian Translation, English Mnemonic, Russian Mnemonic
df = pd.read_excel('vocabulary.xlsx')

# 2. Create a list to hold the JSON objects
json_data = []

for index, row in df.iterrows():
    # We construct the dictionary mapping Excel columns to JSON keys
    entry = {
        "id": row.iloc[0], # Column #
        "word": row.iloc[1], # German Word
        
        # These fields are missing in your Excel, so we leave them blank for now
        "sentence": "", 
        "sentence_translation_en": "",
        "sentence_translation_ru": "",
        
        # Existing data
        "translation_en": row.iloc[2], # English Meaning
        "translation_ru": row.iloc[3], # Russian Translation
        "sentence_mnemonics_en": row.iloc[4], # English Mnemonic
        "sentence_mnemonics_ru": row.iloc[5]  # Russian Mnemonic
    }
    json_data.append(entry)

# 3. Save to vocab.json
with open('vocab.json', 'w', encoding='utf-8') as f:
    json.dump(json_data, f, ensure_ascii=False, indent=2)

print("Success! vocab.json created.")