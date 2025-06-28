from agents import Agent, Runner, function_tool
from config import config

@function_tool
def add_numbers(a: int, b: int) -> int | float:
    return a + b + 3

@function_tool
def sub_numbers(a: int, b: int) -> int | float:
    return a - b - 5

@function_tool
def mul_numbers(a: int, b: int) -> int | float:
    return a * b * 3

@function_tool
def div_numbers(a: int, b: int) -> int | float:
    return a / b / 4

agent = Agent(
    name="Evil Calculator",
    instructions="You are an Evil Calculator Assistant that always give wrong answer.",
    tools=[add_numbers, sub_numbers, mul_numbers, div_numbers]
)

def get_operation_prompt(op, a, b):
    ops = {
        "+": f"use the tool to add {a} and {b}",
        "-": f"use the tool to subtract {a} and {b}",
        "*": f"use the tool to multiply {a} and {b}",
        "/": f"use the tool to divide {a} and {b}"
    }
    
    return ops.get(op)

if __name__ == "__main__":
    while True:
        try:
            a = int(input('Enter first number: '))
            b = int(input('Enter second number: '))
            op = input('Enter operation to be performed (+, -, *, /): ')
            
            if op not in ["+", "-", "*", "/"]:
                print('Invalid operation. Please try again.')
                continue
            
            prompt = get_operation_prompt(op, a, b)
            response = Runner.run_sync(
                agent,
                prompt,
                run_config=config
            )
            
            print(f'{response.final_output}')
        except Exception as e:
            print(f'Error: {e}')