import json

# IMPORTANT: Make sure 'dictionary.txt' is in the same directory as this script,
# or provide the full path to your downloaded dictionary.txt file.
input_file_path = 'dictionary_raw.txt' # Renamed to be consistent
output_file_path = 'characters_data.json' # Renamed to be consistent

processed_data = {}

try:
    with open(input_file_path, 'r', encoding='utf-8') as file:
        for line_num, line in enumerate(file, 1): # Added line_num for better error reporting

            if not line.strip():
                continue

            try: # Nested try-except for JSON parsing errors per line
                entry = json.loads(line.strip())
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON on line {line_num} from '{input_file_path}': {e}. Line content: '{line.strip()}'")
                continue # Skip to the next line if this one is invalid JSON

            # CORRECTED: 'character' (singular) as per Make Me a Hanzi data structure
            char = entry.get('character')
            pinyin_list = entry.get('pinyin', [])
            definition = entry.get('definition', '')
            radical_char = entry.get('radical')

            if char and radical_char is not None:
                # Join pinyin list into a space-separated string
                display_pinyin = ' '.join(pinyin_list)
                # Definition is usually already a string, so no change needed
                display_definition = definition

                processed_data[char] = {
                    "pinyin": display_pinyin,
                    "definition": display_definition,
                    "radical_char": radical_char
                }
            else:
                # Improved skipping message
                print(f"Skipping entry on line {line_num} due to missing 'character' or 'radical' field: {line.strip()}")

except FileNotFoundError:
    print(f"Error: The file '{input_file_path}' was not found. Please check the path and filename.")
except Exception as e: # Catch any other unexpected errors
    print(f"An unexpected error occurred: {e}")

if processed_data:
    with open(output_file_path, 'w', encoding='utf-8') as outfile: # CORRECTED: 'outfile' here
        json.dump(processed_data, outfile, ensure_ascii=False, indent=4)
    print(f"Processed data successfully written to '{output_file_path}'. Successfully processed {len(processed_data)} entries.")
else:
    print("No data processed. This might mean the input file was empty, or no valid entries were found.")
