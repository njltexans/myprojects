# keyword arguments = an arguement preceded by an identifier
#                   Helps with readability
#                   order of the arguements does not matter 


def hello(greeting, title, first, last):
    print(f"{greeting} {title}{first} {last}")

hello("Hello", "Mr.", "Joe", "Joeyson")
hello("Hello", title="Mr.", first="Joe", last="Joeyson") # can define arguements and then can put them in any order (so long as they are after the ones that are being passed in)


for i in range(1, 11):
    print(i, end= " ")


def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

print(get_phone(first=827, last=7346, area=240, country=1))


