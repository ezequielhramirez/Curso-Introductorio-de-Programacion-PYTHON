courses = (
#     0       1           2          3             4
    "Python", "Django", "Ruby", "Ruby on Rails", "MySQL"

)

print(courses)

# ------------------------------------

# var1 = courses[0]
# var2 = courses[1]
# var3 = courses[2]
# var4 = courses[3]
# var5 = courses[4]

# print (
    
#     var1, var2, var3, var4, var5
    
# )
# ------------------------------------


# var1, var2, var3, var4, var5 = courses

var1, var2, *sub_courses, last_value = courses

print("\n-------------------------------------")
# print (var1, var2, var3, var4, var5)

print (
    var1, var2, sub_courses, last_value
)


