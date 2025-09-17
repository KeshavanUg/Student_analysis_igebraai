# Student Algebra Analysis Project (igebra)

A comprehensive Python-based system for teaching algebra and analyzing student performance. This project provides tools for students to practice algebraic equations and for teachers to track and analyze student progress.

## Features

### Core Algebra Engine
- **Linear Equation Solving**: Solve equations like `2x + 5 = 13` or `2x + 9 = 3x - 1`
- **Quadratic Equation Solving**: Solve quadratic equations using the quadratic formula
- **Expression Evaluation**: Safely evaluate mathematical expressions
- **Variable Management**: Set and use variables in calculations

### Student Analysis System
- **Performance Tracking**: Track individual student attempts and performance
- **Class Analytics**: Analyze overall class performance and trends
- **Practice Problem Generation**: Generate problems at different difficulty levels
- **Time Tracking**: Monitor how long students take to solve problems
- **Accuracy Analysis**: Calculate success rates and identify areas for improvement

## Project Structure

```
Student_analysis_igebraai/
├── README.md              # This documentation
├── requirements.txt       # Project dependencies (none - uses standard library)
├── algebra_engine.py      # Core algebra functionality
├── main.py               # Main application with demo
└── test_algebra.py       # Test script for functionality verification
```

## Quick Start

### Running the Demo
```bash
python3 main.py
```

This will run a demonstration showing:
- Multiple students solving problems at different difficulty levels
- Individual performance reports
- Class-wide analytics
- Equation solving examples

### Running Tests
```bash
python3 test_algebra.py
```

This will test all core functionality including equation solving and student analysis features.

## Usage Examples

### Basic Equation Solving

```python
from algebra_engine import AlgebraEngine

engine = AlgebraEngine()

# Solve linear equations
solution = engine.solve_linear_equation("2x + 5 = 13")
print(f"x = {solution}")  # Output: x = 4.0

# Solve quadratic equations
sol1, sol2 = engine.solve_quadratic_equation(1, -5, 6)  # x² - 5x + 6 = 0
print(f"Solutions: {sol1}, {sol2}")  # Output: Solutions: 3.0, 2.0
```

### Student Performance Tracking

```python
from algebra_engine import StudentAnalyzer

analyzer = StudentAnalyzer()

# Record student attempts
analyzer.add_attempt("Alice", "x + 5 = 12", 7, 7, 2.5)  # Correct answer
analyzer.add_attempt("Alice", "2x = 10", 4, 5, 3.0)     # Incorrect answer

# Get performance report
performance = analyzer.get_student_performance("Alice")
print(f"Accuracy: {performance['accuracy']:.2%}")
```

### Interactive Practice Session

```python
from main import AlgebraApp

app = AlgebraApp()
app.set_student("StudentName")
app.practice_session(difficulty="medium", num_problems=5)
```

## Supported Equation Types

### Linear Equations
- Simple form: `x + 5 = 12`
- With coefficients: `2x + 3 = 7`
- Variables on both sides: `2x + 9 = 3x - 1`
- Negative coefficients: `3x - 4 = 8`

### Quadratic Equations
- Standard form: `ax² + bx + c = 0`
- Supports real and complex solutions
- Uses quadratic formula for reliable results

## Difficulty Levels

### Easy
- Simple linear equations: `x + a = b`, `ax = b`
- Basic addition/subtraction with x

### Medium  
- Linear equations with coefficients: `ax + b = c`
- Variables on both sides: `ax + b = cx + d`

### Hard
- Quadratic equations: `ax² + bx + c = 0`
- Complex algebraic expressions

## Educational Benefits

### For Students
- **Practice**: Structured practice problems at appropriate difficulty levels
- **Immediate Feedback**: Instant verification of answers
- **Progress Tracking**: See improvement over time
- **Time Management**: Learn to solve problems efficiently

### For Teachers
- **Performance Analytics**: Detailed insights into student performance
- **Class Overview**: Understand class-wide strengths and weaknesses
- **Individual Reports**: Track each student's progress
- **Data-Driven Instruction**: Make informed decisions about teaching strategies

## Technical Details

### Dependencies
- **Python 3.6+**: Core language requirement
- **Standard Library Only**: No external dependencies required
- **Cross-Platform**: Works on Windows, macOS, and Linux

### Architecture
- **Modular Design**: Separate engine and analysis components
- **Safe Evaluation**: Secure mathematical expression evaluation
- **Data Classes**: Type-safe data structures for student records
- **Error Handling**: Comprehensive error checking and user-friendly messages

## Future Enhancements

Potential areas for expansion:
- Web interface for easier access
- Database integration for persistent storage
- Advanced statistical analysis
- Graphical visualization of student progress
- Support for more complex algebraic concepts
- Integration with Learning Management Systems (LMS)

## Contributing

This project is designed to be educational and extensible. Areas for contribution:
- Additional equation types (logarithmic, exponential)
- Enhanced user interface
- More sophisticated analytics
- Performance optimizations
- Additional test coverage

## License

This project is designed for educational purposes. Feel free to use, modify, and distribute for educational applications.