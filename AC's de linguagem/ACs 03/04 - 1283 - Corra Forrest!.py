tempo = []
while True:
    num = int(input())
    if num < 0:
        break
    tempo.append(num)
media = sum(tempo) / len(tempo)
print(f'MEDIA: {media:.2f}')
for c in tempo:
    if c < media:
        print(c)
