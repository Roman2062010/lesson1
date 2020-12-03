a = {"city": "Москва", "temperature": "20"}
print(a["city"])
a["temperature"] = int(a["temperature"]) - 5
print(a["temperature"])
print(a)

print('country' in a) #способ №0

print(a.get("country")) #способ №1

a["country"] = "Россия"
a["date"] = "27.05.2019" 
print(len(a))