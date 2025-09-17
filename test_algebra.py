#!/usr/bin/env python3
"""
Simple test for the algebra engine functionality.
"""

from algebra_engine import AlgebraEngine, StudentAnalyzer

def test_algebra_engine():
    """Test the algebra engine functions."""
    engine = AlgebraEngine()
    
    print("Testing Algebra Engine")
    print("=" * 30)
    
    # Test expression evaluation
    engine.set_variable('x', 4)
    try:
        result = engine.evaluate_expression('2*4 + 5')
        print(f"2*4 + 5 = {result}")
        
        result = engine.evaluate_expression('2*x + 5')
        print(f"2*x + 5 (x=4) = {result}")
    except Exception as e:
        print(f"Error in expression evaluation: {e}")
    
    # Test linear equation solving
    equations = [
        "2x + 5 = 13",
        "3x - 7 = 14",
        "x + 5 = 12",
        "2x + 9 = 3x - 1"
    ]
    
    for eq in equations:
        try:
            solution = engine.solve_linear_equation(eq)
            print(f"Solution for '{eq}': x = {solution}")
            
            # Verify solution
            engine.set_variable('x', solution)
            left_side = eq.split('=')[0].strip()
            right_side = eq.split('=')[1].strip()
            
            # Manual verification for simple expressions
            if left_side == "2x + 5":
                left_val = 2 * solution + 5
            elif left_side == "3x - 7":
                left_val = 3 * solution - 7
            elif left_side == "x + 5":
                left_val = solution + 5
            elif left_side == "2x + 9":
                left_val = 2 * solution + 9
            else:
                left_val = "unknown"
            
            if right_side.isdigit() or (right_side.startswith('-') and right_side[1:].isdigit()):
                right_val = float(right_side)
            elif right_side == "3x - 1":
                right_val = 3 * solution - 1
            else:
                right_val = "unknown"
            
            if isinstance(left_val, (int, float)) and isinstance(right_val, (int, float)):
                if abs(left_val - right_val) < 1e-6:
                    print(f"✓ Verification: {left_val} = {right_val}")
                else:
                    print(f"✗ Verification failed: {left_val} ≠ {right_val}")
            
        except Exception as e:
            print(f"Error solving '{eq}': {e}")
        print()
    
    # Test quadratic equations
    print("Testing Quadratic Equations")
    print("-" * 30)
    
    quadratics = [
        (1, -5, 6),   # x² - 5x + 6 = 0
        (2, 3, -2),   # 2x² + 3x - 2 = 0
        (1, 0, -4)    # x² - 4 = 0
    ]
    
    for a, b, c in quadratics:
        try:
            sol1, sol2 = engine.solve_quadratic_equation(a, b, c)
            print(f"{a}x² + {b}x + {c} = 0")
            if sol1 is None:
                print("No real solutions")
            elif sol1 == sol2:
                print(f"One solution: x = {sol1}")
            else:
                print(f"Two solutions: x₁ = {sol1}, x₂ = {sol2}")
        except Exception as e:
            print(f"Error: {e}")
        print()

def test_student_analyzer():
    """Test the student analyzer functionality."""
    analyzer = StudentAnalyzer()
    
    print("Testing Student Analyzer")
    print("=" * 30)
    
    # Add some test attempts
    test_data = [
        ("Alice", "x + 5 = 12", 7, 7, 2.5),
        ("Alice", "2x = 10", 5, 5, 3.0),
        ("Alice", "3x - 4 = 8", 4.5, 4, 2.8),
        ("Bob", "x + 5 = 12", 7, 7, 1.8),
        ("Bob", "2x = 10", 4, 5, 2.2),
    ]
    
    for student, problem, answer, correct, time_taken in test_data:
        analyzer.add_attempt(student, problem, answer, correct, time_taken)
    
    # Test individual performance
    for student in ["Alice", "Bob"]:
        perf = analyzer.get_student_performance(student)
        print(f"Performance for {student}:")
        if "error" not in perf:
            print(f"  Accuracy: {perf['accuracy']:.2%}")
            print(f"  Total attempts: {perf['total_attempts']}")
            print(f"  Average time: {perf['average_time']:.1f}s")
        else:
            print(f"  {perf['error']}")
        print()
    
    # Test class performance
    class_perf = analyzer.get_class_performance()
    if "error" not in class_perf:
        print("Class Performance:")
        print(f"  Total students: {class_perf['total_students']}")
        print(f"  Overall accuracy: {class_perf['overall_accuracy']:.2%}")
        print(f"  Average class time: {class_perf['average_class_time']:.1f}s")

if __name__ == "__main__":
    test_algebra_engine()
    print("\n" + "=" * 50 + "\n")
    test_student_analyzer()