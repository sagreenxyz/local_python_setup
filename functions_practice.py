def hello():
    print("Hello, user!")

hello()

def pack(a, b, c):
    return [a, b, c]

print(pack("This", "Is", "A test"))

def eat_lunch(lunch_list):
    i = 0
    for j in lunch_list:
        if i == 0:
            print("First I eat " + j)
            i += 1
        else:        
            print("Next I eat " + j)
    print("My lunchbox is empty!")

eat_lunch(["apple", "orange", "pear", "sandwich"])
