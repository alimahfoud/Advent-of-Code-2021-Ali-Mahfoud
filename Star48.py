from itertools import product
data = []
with open("/home/alimahfoud24/ALI/inputDay24.txt") as file:
    line = file.readline()
    while line:
        data.append(line.strip('\n'))
        line = file.readline()
digit_1 = data[0:(len(data)//14)]
digit_2 = data[(len(data)//14):(2*(len(data)//14))]
digit_3 = data[(2*(len(data)//14)):(3*(len(data)//14))]
digit_4 = data[(3*(len(data)//14)):(4*(len(data)//14))]
digit_5 = data[(4*(len(data)//14)):(5*(len(data)//14))]
digit_6 = data[(5*(len(data)//14)):(6*(len(data)//14))]
digit_7 = data[(6*(len(data)//14)):(7*(len(data)//14))]
digit_8 = data[(7*(len(data)//14)):(8*(len(data)//14))]
digit_9 = data[(8*(len(data)//14)):(9*(len(data)//14))]
digit_10 = data[(9*(len(data)//14)):(10*(len(data)//14))]
digit_11 = data[(10*(len(data)//14)):(11*(len(data)//14))]
digit_12 = data[(11*(len(data)//14)):(12*(len(data)//14))]
digit_13 = data[(12*(len(data)//14)):(13*(len(data)//14))]
digit_14 = data[(13*(len(data)//14)):(14*(len(data)//14))]
digits = [digit_1]+[digit_2]+[digit_3]+[digit_4]+[digit_5]+[digit_6]+[digit_7] + \
    [digit_8]+[digit_9]+[digit_10]+[digit_11]+[digit_12]+[digit_13]+[digit_14]
digits_type_1 = [0]*14
digits_type_2 = [0]*14
i = 0
while i < len(digits):
    if '-' in digits[i][5]:
        digits_type_1[i] = 0
        digits_type_2[i] = int(digits[i][5][(digits[i][5].index('-')+1):])
        i += 1
    else:
        digits_type_1[i] = int(digits[i][15][(digits[i][5].index('x')+2):])
        digits_type_2[i] = 0
        i += 1

for DIGITS in product(range(1, 10), repeat=7):
    z = 0
    Result_list = [0] * 14
    d = 0
    valid = 0
    for i in range(14):
        addition = digits_type_1[i]
        substraction = digits_type_2[i]
        if addition != 0:
            z = z * 26 + DIGITS[d] + addition
            Result_list[i] = DIGITS[d]
            d += 1
        else:
            Result_list[i] = ((z % 26) - substraction)
            z //= 26
            if not (1 <= Result_list[i] <= 9):
                valid = 1

    if valid == 0:
        Result = sum(d * 10**i for i, d in enumerate(Result_list[::-1]))
        break
print('The smallest model number accepted by MONAD is:', Result)
