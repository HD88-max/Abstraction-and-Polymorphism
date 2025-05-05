# Write a program to create two classes for two different countries that consist of three methods to display the following information of respective country - capital, language and type of country. Then, use Polymorphism to create a common interface for both classes.
class India:
    def capital(self):
        print("Delhi is the capital of India.")
class England:
    def capital(self):
        print("London is the capital of England.")

obj1 = India()
obj2 = England()

for country in (obj1,obj2):
    country.capital()