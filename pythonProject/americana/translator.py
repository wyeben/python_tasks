from translate import Translator

text = "my name is"

translate = Translator(to_lang='ja')
translation = translate.translate(text)
print(translation)