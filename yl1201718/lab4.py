#1+2+extra
class Animal(object):
	def __init__(self,sound,name,age,favorite_color):
		self.sound = sound
		self.name = name
		self.age = age
		self.favorite_color = favorite_color
	def eat(self,food):
		print("Yummy!! "+ self.name + "is eating " + food)
	def description(self):
		print(self.name + " is " + self.age + " years old and loves the color " + self.favorite_color)
	def make_sound(self,num):
		print(self.sound * num)

animal1 = Animal("barks","Tomas","2","pink")
#(animal1.eat("IceCream"))
#(animal1.description())
#(animal1.make_sound(5))

#3
class Person(object):
	def __init__(self,name,age,city,gender):
		self.name = name
		self.age = age
		self.city = city
		self.gender = gender
	def fav_breakfast(self,fav_breakfast):
		print(self.name + "s favorite breakfast is "+ fav_breakfast)
	def description(self):
		print (self.name +" is "+ self.age +" years old and lives in "+ self.city +" , "+self.name +" is a "+ self.gender)
	def fav_sport (self,fav_sport):
		print (self.name + "s favorit sport is " + fav_sport)


Tom = Person("Tom","17","Jerusalem","boy")
(Tom.description())
(Tom.fav_breakfast("eggs"))
(Tom.fav_sport("soccer"))

#4
class song(object):
	def __init__(self,lyrics):
		self.lyrics = lyrics
	def sing_me_a_song(self):
		for i in self.lyrics:
			print(i)

Flower_song = song(["Roses are red, "
			"Violets are blue, "
			"I wrote this poem for you." ])

Flower_song.sing_me_a_song()