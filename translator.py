"""
not stable
"""
from googletrans import Translator, constants
from pprint import pprint


# init the google api translator
translator = Translator()

# translate spanish text to english text (default)
translation = translator.translate("Hola Mundo")
print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")

# specify source language
translation = translator.translate("wie gehts?", src="de")
print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")

# print translation and other data
pprint(translation.extra_data)

# translate more than a phase
sentences = [
    "hello everyone",
    "do you speak python?",
    "hack nasa with HTML",
    "good bye"
]
translations = translator.translate(sentences, dest="tr")
for translation in translations:
    print(f"{translation.orgin} ({translation.src}) --> {translation.text} ({translation.dest})")

# detect a language
detection = translator.detect("Random Sweet Honey Ice Tea")
print("Language code: ", detection.lang)
print("Confidence", detection.confidence)

# print the detected language
print("Language: ", constants.LANGUAGES[detection.lang])

# print all available languages
print("Total supported languages: ", len(constants.LANGUAGES))
print("Languages:")

pprint(constants.LANGUAGES)
