Grades1 = {"Eve": "Not graded", "Frank": 88, "Grace": -5, "Henry": 105, "Ivy": 91}
new_dic = {}
another_dic = {}
count = 0
for k, v in Grades1.items():
    if isinstance(v, int):
        if v < 0 or v > 100:
            print(f"Warning: Invalid grade range for {k}")
            count += 1
        else:
            new_dic[k] = v
    else:
        print(f"Warning: Invalid grade format for {k} ")
        count += 1

values = new_dic.values()
another_dic["Highest"] = max(values)
another_dic["lowest"] = min(values)
another_dic["average"] = sum(values) / len(values)
another_dic["count"] = len(values)
another_dic["Errors"] = count
print(another_dic)
