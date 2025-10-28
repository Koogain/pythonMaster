first_word = str(input('첫번째 단어: '))
second_word = str(input('두번째 단어: '))

set1 = set(first_word)
set2 = set(second_word)

same_word = set1 & set2

result = (same_word)

print(result)