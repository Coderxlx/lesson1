info = {
    "city" : "Ternopil",
    "temperature" : -5
}

print(info["city"])

info["temperature"] -= 5
print(info)

print('country' in info)
print(info.get('country', 'Ukraine'))

info["date"] = '27.05.2019'
print(len(info))