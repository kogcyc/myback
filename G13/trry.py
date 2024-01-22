import sys

def execute_python_command(command):
    try:
        result = eval(command)
        print("Result:", result)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 app.py 'python command'")
        sys.exit(1)

    python_command = sys.argv[1]
    execute_python_command(python_command)

