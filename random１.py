#random関数挿入(Random function insertion)
import random


#1から10の数をランダムで出力(Output random numbers from 1 to 10)
print(random.randint(1,10))
print(random.uniform(1,10))
print(random.randrange(10))


#100から100の数をランダムで出力(Output random numbers from 100 to 100)
print(random.uniform(100,100))


#-100から100の少数をランダムで出力(Output random numbers from -100 to 100)
print(random.uniform(-100,100))


#0から1までの数をランダムで出力(Output random numbers from 0 to 1)
print(random.random())
