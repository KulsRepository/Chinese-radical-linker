This is a web-app capable of finding the definition and linked radical of around 9500 Chinese characters.

You most likely can't run it as a file on a browser due to a CORS error which occurs due to Google not liking to read local JSON files.

You can go to the folder where you downloaded this code throiugh cd-ing in cmd and then start a local server, then you can go to localhost 8888 with your browser 
(http://localhost:8000/) if it isnt used to be able to use this app
_________________________________________________________________________________________________

characters_data.json is a data-readable JSON file of 9500 most used Chinese characters, accompanied by their definitions and their corresponding radicals.
It was extracted from the GItHub for Make Me a Hanzi (https://github.com/skishore/makemeahanzi)'s dictionary.txt file downloaded as raw data into JSON format in characters_data.json.

you are free to use characters_data.json as you wish, I didn't find JSON chinese character + radical + definition data for Chinese (mandarin) characters anywhere on the internet so this
should be used as that resource.

radicals_details.json is all the radicals in all their forms
