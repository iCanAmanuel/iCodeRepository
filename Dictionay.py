customer = {
    "name": "Amanuel",
    "age": 34,
    "is_verified": True
}
print(customer.get("sex", "Male"))
# add new key value with data
customer["address"] = "Massawa"
print(f'after add new key with data: Address= Massawa')
for data in customer:
    print(f' {data} = {customer[data]}')
print(f'Customer = {customer}')
print(f'key not exist send: {customer.get("birthdate")}')
print(customer.get("birthdate", "Apr 9 1989"))
print("")
print("convert numbers to words")

digits = input("Phone: ")
digit_maping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine"
}
output = ""
for ch in digits:
    output += digit_maping.get(ch, "!") + " "
print(output)
print("................listed veiew")
# oooooorrrrrrrr
for ch in digits:
  print(digit_maping.get(ch, "!"))


#         imoji converter
message = input(">")
words = message.split(' ')
emojis = {
    ":)": "😊",
    ":(": "😒",
}
greeting = ""
for word in words:
    greeting += emojis.get(word, word) + " "
print(greeting )