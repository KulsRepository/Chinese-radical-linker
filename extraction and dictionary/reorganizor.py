import json

input = 'dictionary_raw.txt'
output = 'characters_data.json'

processed_data = {}

try:
    with open(input, 'r', encoding='utf-8') as file:
        for line in file:

            if not line.strip():
                continue

            entry = json.loads(line.strip())
            char = entry.get('character')
            pinyin_list = entry.get('pinyin', [])
            definition = entry.get('definition', '')
            radical_char = entry.get('radical')

            if char and radical_char is not None:

                display_pinyin = ' '.join(pinyin_list)
                display_definition = definition
                processed_data[char] = {
                    "pinyin": display_pinyin,
                    "definition": display_definition,
                    "radical_char": radical_char
                }
            else:
                print(f"Skipping entry due to missing data: {line.strip()}")

except FileNotFoundError:
    print(f"Error: The file '{input}' was not found.")
except json.JSONDecodeError as e:
    print(f"Error decoding JSON from '{input}' on line: {line.strip()}. Error: {e}") 
except Exception as e:
    print(f"An unexpected error occurred: {e}") 

if processed_data:
    with open(output, 'w', encoding='utf-8') as outfile:
        json.dump(processed_data, outfile, ensure_ascii=False, indent=4)
    print(f"Processed data successfully written to '{output}, succesfully processed {len(processed_data)} entries.'")
else:
    print("No data processed. This might mean the input file was empty, or no valid entries were found.")