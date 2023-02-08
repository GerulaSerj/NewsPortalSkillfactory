from django import template

register = template.Library()


@register.filter()
def censor(text):
    bad_words = ('редиска', 'Редиска','редис', 'Редис', 'Редиса', 'редиса')

    for b_word in bad_words:
        for word in text.split():
            if word.lower().count(b_word) and len(word) > len(b_word):
                text = text.replace(word, f"{word[0]}{'*' * (len(b_word) - 1)}{word[-1]}")
    return text