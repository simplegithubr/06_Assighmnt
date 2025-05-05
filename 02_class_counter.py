
""""2. Using cls
Assignment:
Create a class Counter that keeps track of how many objects 
have been created. Use a class variable and a class 
method with cls to manage and display the count."""

class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1
    @classmethod
    def disply_count(cls):
        print(f"total objects created: {cls.count}")
c1 = Counter()
c2 = Counter()

Counter.disply_count()

        