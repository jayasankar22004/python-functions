def tree(monkey_count,fruit_type,fruit_count):
    d={"mangos":2,"apples":3,"oranges":5}
    t=d[fruit_type.lower()]
    x=int(fruit_count/monkey_count)
    total_time=t*x
    print(total_time)

tree(5,"apples",20)