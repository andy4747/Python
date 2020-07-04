def reverse(data):
	for index in range(len(data)-1,-1,-1):
		yield data[index]

dt=reverse("asdf")
print(next(dt))
print(next(dt))
print(next(dt))
print(next(dt))