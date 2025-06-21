class Calculator:
    calculation_type = "Atithmetic Operations"

    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def multiply(cls, a, b):
        print(f"Calculation Type: {cls.calculation_type}")
        return a * b
