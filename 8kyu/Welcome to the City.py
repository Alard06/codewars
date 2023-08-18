def say_hello(name, city, state):
    if type(name) == list:
        return f'Hello, {" ".join(name)}! Welcome to {city}, {state}!'
    return f'Hello, {name}! Welcome to {city}, {state}!'

print(say_hello(['John', 'Smith'], 'Phoenix', 'Arizona'))
print(say_hello('John', 'Phoenix', 'Arizona'))

