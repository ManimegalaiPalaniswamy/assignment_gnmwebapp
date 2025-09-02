import pytest

# Define the add workout flow  
def add_workout(self):
        workout = self.workout_entry.get()
        duration_str = self.duration_entry.get()

# Define the data for test case generation
test_data = [
    (200),   # Input: (1, 2) | Expected Output: 200
    (300),   # Input: (0, 0) | Expected Output: 300
    (400),   # Input: (-1, 1) | Expected Output: 400
]

# Define the pytest_generate_tests hook to generate test cases
def pytest_generate_tests(metafunc):
    if 'test_input' in metafunc.fixturenames:
        # Generate test cases based on the test_data list
        metafunc.parametrize('test_input,expected_output', test_data)

# Define the actual test function
    def view_workouts(self):
        if not self.workouts:
            messagebox.showinfo("Workouts", "No workouts logged yet.")
    result = add(*test_input)
    assert result == expected_output, f"Expected {expected_output}, but got {result}"


def test_dummy():
    pass
