import random

BUILTINS = {
	"$randomNumber10": lambda:random.randint(0, 10),
	"$randomNumber100": lambda:random.randint(0, 100),
	"$randomNumber1000": lambda:random.randint(0, 1000),
}