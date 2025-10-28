#4-12 code
age = int(input('나이: '))
resting_HR = int(input('안정 시 심박수: '))
for a in range(40, 81, 10):
    intensity = a/100
    target_HR = (((220-age)-resting_HR)*intensity)+resting_HR
    print(f'강도: {a}%목표 심박수: {target_HR}bpm')