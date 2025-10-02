import random
alf='абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'
M=int(input("Введіть кількість слів: "))
N=int(input("Введіть довжину слова: "))
words=[]
for i in range(M):
    word=''.join(random.choice(alf) for i in range(N))
    words.append(word)
print('Згенеровані слова:',words)