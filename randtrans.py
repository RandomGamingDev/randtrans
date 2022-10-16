import random
import googletrans

langs = googletrans.LANGUAGES
translator = googletrans.Translator()
result = ""

def RandomlyTranslate(times, lang):
    global langs
    global translator
    global result

    prevLang = lang
    for i in range(times - 1):
        currentLang = random.choice(list(langs))
        result = translator.translate(result, src=prevLang, dest=currentLang).text
        prevLang = currentLang
    result = translator.translate(result, src=prevLang, dest=lang).text
    return result
