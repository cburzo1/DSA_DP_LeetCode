import datetime

'''s = "Date: 2026-12/01 -- 15-30-45"
dt1 = datetime.datetime(2000, 9, 4)

dt2 = datetime.datetime.strptime(s, "Date: %Y-%m/%d -- %H-%S-%M")

print(dt1, dt2)

print(dt2 - dt1)

td = dt2 - dt1

print(round(td.seconds/60), "minutes", "and", td.seconds%60, "seconds")'''

'''import csv

s = []

with open("sample_employees.csv", 'r') as file:
    content = csv.reader(file)
    next(content)
    for line in content:
        s.append(line[1:2][0])


print(s)'''

d = {
    "name": "chris",
    "job": "python guy",
    "hobby": "hmm...nothing?",
    "loadout":"weiner and balls"
}

keys = d.keys()
values = d.values()

print(keys, values)

for key in keys:
    if key == "job":
        print("value of job: ", d.get(key))

d = {"game": "elden ring"}

d.update({"job":"SPRING BOOT!!!"})

print(d.get("game"), d.get("job"))