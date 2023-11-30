def get_summ(one, two, delimiter='&'):
    return f"{one}{delimiter}{two}".upper()

a = get_summ("Learn", "Python")
print(a)