
# emulate 'C' style
format = "Welcome %s what a %s player"
print(format)
values = ("Sachin", "superb")
print(values)

print(format % values)
print("-" * 60)

format = "Welcome %s, your rating of %.3f, what a %s player"
print(format % ("Sachin", 4, "superb"))
print(format % ("Sachin", 4.7, "superb"))
print(format % ("Sachin", 4.7876399, "superb"))

print("Welcome %s, your rating of %.3f, what a %s player" % ("Sachin", 4.789999, "superb"))
print("-" * 60)

# emulate unix style
from string import Template
tmpl = Template("Welcome $name, what a $adj player")
print(tmpl)
print(tmpl.substitute(name="Sachin", adj="Superb"))

print("-" * 60)
# format of strings in python
print("Welcome {}, what a {} player for {}".format("Sachin", "class", "India"))
print("Welcome {0}, what a {1} player for {2}".format("Sachin", "class", "India"))
print("Welcome {name}, what a {adj} player for {ctr}".format(name="Sachin", adj="class", ctr="India"))

print("Welcome {name}, with a rating of {rat}, what a {adj} player for {ctr}".format(name="Sachin", adj="class", rat=4, ctr="India"))

print("Welcome {name}, with a rating of {rat:.3f}, what a {adj} player for {ctr}".format(name="Sachin", adj="class", rat=4, ctr="India"))

print("Welcome {name}, with a rating of {rat:.3f}, what a {adj} player for {ctr}".format(name="Sachin", adj="class", rat=4.867956, ctr="India"))

print("-" * 60)
# interpolation
from math import pi, e
print(f"The value of PI = {pi} and Euler's constant = {e}")

print("-" * 60)
print("The value of PI = {} and Eulers constant = {} and magic number is {}".format(pi, e, 40585))

name = ['Sachin', "Tendulkar"]
print("Mr.{name}".format(name=name))
print("Mr.{name[0]} {name[1]}".format(name=name))

print("-" * 60)
print(__name__)     # name of the module

import math
print(math.__name__)
print("The {mod.__name__} module gives the value of pi={mod.pi} and eulers constant = {mod.e}".format(mod=math))

print("-" * 60)
# conversions
print("{val} {val} {val}".format(val = "A"))
# s = string, r = raw_string, a = ascii converted string
print("{val!s} {val!r} {val!a}".format(val = "A"))

print("-" * 60)
print("{num} {num} {num}".format(num=36))
print("{num:10} {num:f} {num:b}".format(num=36))
print("{num:5} {num:f} {num:b}".format(num=36))
print("{num:5} {num:f} {num:b}".format(num=3656457567))

print("-" * 60)
# alignment
print("{num:15}Tendulkar".format(num="Sachin"))
print("{num:15}Tendulkar".format(num=36))
print("{num:<15}Tendulkar".format(num="Sachin"))    # left aligned
print("{num:^15}Tendulkar".format(num="Sachin"))    # center aligned
print("{num:>15}Tendulkar".format(num="Sachin"))    # right aligned
print("{num:-^60}".format(num="Sachin"))
print("Sachin".center(60, "-"))

print("-" * 60)
# extraction
print("{}".format("Sachin Tendulkar"))
print("{:.6}".format("Sachin Tendulkar"))

print("{pi:10.2}".format(pi=pi))
print("{pi:10.3}".format(pi=pi))
print("{pi:10.4}".format(pi=pi))
print("{pi:10.5}".format(pi=pi))

print("-" * 60)
print("One google is {}".format(10 ** 100))
print("One google is {:,}".format(10 ** 100))

print("-" * 60)
print("{pi:010.2}".format(pi=pi))
print("{pi:010.3}".format(pi=pi))
print("{pi:010.4}".format(pi=pi))

print("{0:10.2f}\n{1:10.2f}".format(pi, -pi))

print("-" * 60)

width = 50
price_width = 10
item_width = width - price_width

header_fmt = '{{:{}}}{{:>{}}}'.format(item_width, price_width)
fmt = '{{:{}}}{{:>{}.2f}}'.format(item_width, price_width)
print('=' * width)
print(header_fmt.format('Item', 'Price'))
print('=' * width)

print(fmt.format('Apples', 0.4))
print(fmt.format('Pears', 0.5))
print(fmt.format('Cantaloupes', 1.92))
print(fmt.format('Dried Apricots (16 oz.)', 8))
print(fmt.format('Prunes (4 lbs.)', 12))
print('=' * width)
