def roman_to_int(s):
    roman = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    total=0

    for i in range(len(s)):
        if i+1<len(s) and roman[s[i]]<roman[s[i+1]]:
            total-=roman[s[i]]
        else:
            total+=roman[s[i]]
    return total
print(roman_to_int("III"))     # 3
print(roman_to_int("IV"))      # 4
print(roman_to_int("IX"))      # 9
print(roman_to_int("LVIII"))   # 58
print(roman_to_int("MCMXCIV")) #1994