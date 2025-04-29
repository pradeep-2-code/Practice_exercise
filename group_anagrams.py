words = ["listen", "silent", "enlist", "rat", "tar", "art", "evil", "vile", "live"]
dic1 = []
for i in words:
    z = sorted(i)
    dic1.append(z)
dic1
dic2 = []
for k in dic1:
    new_str = "".join(k)
    dic2.append(new_str)
new_keys = list(set(dic2))
# creating three diff lists for each value in new_keys
listed1 = []
listed2 = []
listed3 = []
for w in words:
    for k in dic1:
        if len(w) == 6:
            if sorted(w) == sorted(k):
                listed1.append(w)
        elif len(w) == 3:
            if sorted(w) == sorted(k):
                listed2.append(w)
        else:
            if sorted(w) == sorted(k):
                listed3.append(w)
updated_list1 = list(set(listed1))
updated_list2 = list(set(listed2))
updated_list3 = list(set(listed3))
main_list = [updated_list1, updated_list2, updated_list3]
dic4 = {}
dic4[new_keys[0]] = updated_list3
dic4[new_keys[1]] = updated_list1
dic4[new_keys[2]] = updated_list2
print(dic4)
