# src/tools.py
def calculator(expression):

    try:

        return str(
            eval(expression)
        )

    except Exception as e:

        return f"Calculation Error: {e}"