some_text = 'Осень самая красивая пора года. \
    Недаром у Александра Сергеевича Пушкина осень бала самой любимой порой года. \
    Нельзя не восхищаться той красотой, которую нам дарит осень. абвА какабв красабвиво осеабвнью вабв лабвесу!'

def del_words(some_text):
    some_text = list(filter(lambda x: 'абв' not in x, some_text.split()))
    return " ".join(some_text)

new_text = del_words(some_text)
print(new_text)