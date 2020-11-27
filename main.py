print("**********************")
print("  Miegu kalkulators   ")
print("  Viktorija Abramova   ")
print("***********************")

name = input('Привет, как тебя зовут?: ')
print('Привет, ' + name + '!')
while True:
  recommendation_max = input('Сколько часов рекомендуется максимум ко сну: ')
  recommendation_min = input('Сколько часов рекомендуется минимум ко сну: ')
  try:
    recommendation_max = float(recommendation_max)
    recommendation_min = float(recommendation_min)
  except:
    print('\nВремя должно указываться только в цифрах!')
    continue
  if recommendation_max <= 0 or recommendation_max <= 0:
    print('\nВремя должно указываться положительными цифрами!')
    continue
  elif recommendation_max >= 24 or recommendation_max >= 24:
    print('\nНевозвожно спать более 24-ёх часов в сутки!')
    continue
  elif recommendation_max <= recommendation_min:
    print('\nМаксимальное рекомендуемое время для сна должно быть больше минимального!')
    continue
  break

   
while True:
  your_sleep = input('Сколько часов вы спите: ')
  try:
    your_sleep = float(your_sleep)
  except:
    print('\nВремя должно указываться только в цифрах!')
    continue
  if your_sleep <= 0:
    print('\nВремя должно указываться положительными цифрами!')
    continue
  elif your_sleep >= 24:
    print('\nНевозвожно спать более 24-ёх часов в сутки!')
    continue
  break


while True:
  weight = input('Введите ваш вес в киллогарммах: ')
  try:
    weight = float(weight)
  except:
    print('\nВремя должно указываться только в цифрах!')
    continue
  if weight <= 0:
    print('\nВремя должно указываться положительными цифрами!')
    continue
  break

too_many = your_sleep - recommendation_max
too_little = recommendation_min - your_sleep
slimming = weight * your_sleep
if your_sleep < recommendation_min:
    print('Вы недосыпаете! Вам следует спать больше на', too_little, 'часов.')
elif your_sleep > recommendation_max:
    print('У вас пересып! Вам следует спать меньше на', too_many, 'часов.')
else:
    print('Ваш сон идеально сбалансирован!)')

print('Сейчас вы теряете во время сна приблизительно', slimming, 'ккал')