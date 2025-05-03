col = {"pepe": 3, "maria": 17, "juan": 24, "sebastian":19, "fernandes": 7}

for name, age in col.copy().items():
    if age < 18:
        del col[name]

print(col)