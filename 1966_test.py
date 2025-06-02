import os
import subprocess

testfile="1966.py"
testfile=os.path.join(os.path.dirname(__file__), testfile)
inputcase=[
    "3\n1 0\n5\n4 2\n1 2 3 4\n6 0\n1 1 9 1 1 1",
    "1\n6 3\n1 1 9 8 9 8",
    "1\n6 3\n9 8 9 7 8 7"
]

outputcase=[
    "1\n2\n5",
    "4",
    "5"
]

if not os.path.exists(testfile):
    print(f"File {testfile} does not exist.")
    os._exit(1)

def run_test(i):
    try:
        result = subprocess.run(['python3', testfile], input=inputcase[i], text=True, capture_output=True, check=True)
        if result.stdout.strip() == outputcase[i].strip():
            print("Test passed.")
        else:
            print("Test failed.")
            print("Output:")
            print(result.stdout.strip())
            print("Expected Output:")
            print(outputcase[i].strip())

    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr.strip()}")

if __name__ == "__main__":
    for i in range(len(inputcase)):
        print(f"Running test case {i+1}...")
        run_test(i)
    print("Test completed.")
