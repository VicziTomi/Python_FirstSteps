import firstmodule as mod
import platform
import datetime
import json

mod.greeting("Cuki")
a = mod.person1["country"]
print(a)

x = platform.system()
print(x)

y = dir(platform)
print(y)

print(dir(mod))

z = datetime.datetime.now()
print(z)
print(z.year)
print(z.strftime("%a"))

ex_date = datetime.datetime(2019, 8, 24)
print(ex_date)

some_json = '{"name": "Cuki", "age": 32, "city": "Szeged"}'
parsed = json.loads(some_json)
print(parsed["name"], parsed["age"], parsed["city"])

