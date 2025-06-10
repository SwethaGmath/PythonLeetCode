l = [{"name":"swetha", "age":20, "sex":"feamle"},{"name":"eshu", "age":2, "sex":"feamle"},{"name":"lokesh", "age":20, "sex":"amle"}]
for items in l:
    print(items)
    if "sex" in items.keys():
        del items["sex"]

print(l)
