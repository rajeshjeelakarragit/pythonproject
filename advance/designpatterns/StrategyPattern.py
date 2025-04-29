"""
The Strategy pattern defines a family of algorithms and makes them interchangeable.
"""


class Strategy:
    def execute(self):
        pass

class ConcreteStrategyA(Strategy):
    def execute(self):
        print("Executing Strategy A")

class ConcreteStrategyB(Strategy):
    def execute(self):
        print("Executing Strategy B")

class Context:
    def __init__(self, strategy):
        self._strategy = strategy

    def set_strategy(self, strategy):
        self._strategy = strategy

    def execute_strategy(self):
        self._strategy.execute()

# Usage
context = Context(ConcreteStrategyA())
context.execute_strategy()  # Executing Strategy A

context.set_strategy(ConcreteStrategyB())
context.execute_strategy()  # Executing Strategy B
