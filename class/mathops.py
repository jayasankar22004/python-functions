class MathOps:
    @staticmethod
    def is_even(num):
        return num % 2 == 0
print(MathOps.is_even(10))
m = MathOps()
print(m.is_even(15))