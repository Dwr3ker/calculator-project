weight = int(input("what is your weight?"))
in_kg = int(weight / 2.2)
print("You weight " + str(weight / 2.2) + " in kilograms.")
gender = str(input("what is your gender?"))
age = int(input("What is your age?"))


def check_gender(gender):
    output = ''
    global in_kg
    # global gender
    if gender == "male":
        output = in_kg * 1.0 * 24
    else: 
        output = in_kg * .9 * 24
    return output
# print(check_gender(gender))

male_lean_factor =  [
    {"gender": "male", "age": list(range(10,15)), "lean": 1.0},
    {"gender": "male", "age": list(range(15,21)), "lean": 0.95},
    {"gender": "male", "age": list(range(21,29)), "lean": 0.90},
    {"gender": "male", "age": list(range(29, 101)), "lean": 0.85}
    
]

female_lean_factor = [
    {"gender": "female", "age": list(range(14, 19)), "lean": 1.0},
    {"gender": "female", "age": list(range(19, 29)), "lean": 0.95},
    {"gender": "female", "age": list(range(29, 39)), "lean": 0.90},
    {"gender": "female", "age": list(range(39, 101)), "lean": 0.85}
]
    


# print(lean_factor[0]["lean"])

# def lean_factor()

result = ''
if age in male_lean_factor[0]["age"]:
    result = str(check_gender(gender) * male_lean_factor[0]["lean"])
print("You need " + result + " Calories per day")
# if age in male_lean_factor[1]["age"]:
#     result = check_gender(gender) * male_lean_factor[1]["lean"]
# print(result)
# if age in male_lean_factor[2]["age"]:
#     result = check_gender(gender) * male_lean_factor[2]["lean"]
# print(result)
# if age in male_lean_factor[3]["age"]:
#     result = check_gender(gender) * male_lean_factor[3]["lean"]
# print(result)

if age in female_lean_factor[0]["age"]:
    result = str(check_gender(gender) * female_lean_factor[0]["lean"])
print("You need " + result + " Calories per day")
# if age in female_lean_factor[1]["age"]:
#     result = check_gender(gender) * female_lean_factor[1]["lean"]
# print(result)
# if age in female_lean_factor[2]["age"]:
#     result = check_gender(gender) * female_lean_factor[2]["lean"]
# print(result)
# if age in female_lean_factor[3]["age"]:
#     result = check_gender(gender) * female_lean_factor[3]["lean"]
# print(result)
