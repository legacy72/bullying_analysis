import pandas as pd

from bullying.sentiment_analysis.utils.constants import LEVENSHTEIN_DATASET


def fix_word_with_levenshtein_distance(word):
    """
    Исправление опечаток в слове на основе расстояния Левенштейна

    :arg word - слово, которое нужно исправить
    :return исправленное слово (если есть в датасете) или само слово, которое было на входе (если нет в датасете)
    """
    df = pd.read_csv(LEVENSHTEIN_DATASET, sep=';')
    try:
        max_weight = max(df[df['MISTAKE'] == word]['WEIGHT'])
        fixed_word = df[(df['MISTAKE'] == word) & (df['WEIGHT'] == max_weight)].values[0][0]
        return fixed_word
    except ValueError:
        return word
