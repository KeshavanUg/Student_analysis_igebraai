#!/usr/bin/env python3
"""
Student Algebra Analysis Application
===================================

Main application for the igebra project - provides an interactive interface
for students to practice algebra and for teachers to analyze student performance.
"""

import json
import time
from typing import Dict, List
from algebra_engine import AlgebraEngine, StudentAnalyzer


class AlgebraApp:
    """Main application class for the algebra learning system."""
    
    def __init__(self):
        self.analyzer = StudentAnalyzer()
        self.algebra_engine = AlgebraEngine()
        self.current_student_id = None
    
    def set_student(self, student_id: str):
        """Set the current student ID for tracking attempts."""
        self.current_student_id = student_id
        print(f"Current student set to: {student_id}")
    
    def practice_session(self, difficulty: str = "easy", num_problems: int = 5):
        """Run a practice session for the current student."""
        if not self.current_student_id:
            print("Please set a student ID first using set_student()")
            return
        
        problems = self.analyzer.generate_practice_problems(difficulty)
        if len(problems) < num_problems:
            num_problems = len(problems)
        
        print(f"\n=== Practice Session for {self.current_student_id} ===")
        print(f"Difficulty: {difficulty.upper()}")
        print(f"Number of problems: {num_problems}\n")
        
        session_results = []
        
        for i in range(num_problems):
            problem = problems[i]
            print(f"Problem {i+1}: {problem['problem']}")
            
            # Record start time
            start_time = time.time()
            
            # Get student answer (in real implementation, this would be user input)
            try:
                if problem['type'] == 'linear':
                    # Solve the problem to get the correct answer for demonstration
                    correct_answer = self.algebra_engine.solve_linear_equation(problem['problem'])
                    student_answer = input("Enter your answer: ")
                    student_answer = float(student_answer)
                elif problem['type'] == 'quadratic':
                    correct_answer = problem['answer']
                    student_answer = input("Enter your answers (comma separated for quadratic): ")
                    # Parse comma-separated values
                    student_answer = [float(x.strip()) for x in student_answer.split(',')]
                else:
                    correct_answer = problem['answer']
                    student_answer = input("Enter your answer: ")
                    student_answer = float(student_answer)
                
                # Record end time
                end_time = time.time()
                time_taken = end_time - start_time
                
                # Record the attempt
                self.analyzer.add_attempt(
                    self.current_student_id,
                    problem['problem'],
                    student_answer,
                    correct_answer,
                    time_taken
                )
                
                # Provide feedback
                is_correct = self.analyzer.attempts[-1].is_correct
                if is_correct:
                    print("✓ Correct! Well done.")
                else:
                    print(f"✗ Incorrect. The correct answer is: {correct_answer}")
                
                session_results.append({
                    'problem': problem['problem'],
                    'correct': is_correct,
                    'time': time_taken
                })
                
            except ValueError as e:
                print(f"Invalid input: {e}")
                continue
            except KeyboardInterrupt:
                print("\nSession interrupted by user.")
                break
            
            print()
        
        # Show session summary
        correct_count = sum(1 for r in session_results if r['correct'])
        accuracy = correct_count / len(session_results) if session_results else 0
        avg_time = sum(r['time'] for r in session_results) / len(session_results) if session_results else 0
        
        print("=== Session Summary ===")
        print(f"Problems completed: {len(session_results)}")
        print(f"Correct answers: {correct_count}")
        print(f"Accuracy: {accuracy:.2%}")
        print(f"Average time per problem: {avg_time:.1f} seconds")
    
    def demo_session(self, difficulty: str = "easy", num_problems: int = 3):
        """Run a demo session with pre-defined answers for demonstration."""
        if not self.current_student_id:
            print("Please set a student ID first using set_student()")
            return
        
        problems = self.analyzer.generate_practice_problems(difficulty)
        if len(problems) < num_problems:
            num_problems = len(problems)
        
        print(f"\n=== Demo Session for {self.current_student_id} ===")
        print(f"Difficulty: {difficulty.upper()}")
        print(f"Number of problems: {num_problems}\n")
        
        # Demo answers (some correct, some incorrect for demonstration)
        demo_answers = {
            "easy": [7, 5, 4.5],  # First two correct, third slightly wrong
            "medium": [4, 6, 9],  # First two correct, third wrong
            "hard": [[2, 3], [0.5, -2], [2, -2]]  # All correct for quadratic
        }
        
        answers = demo_answers.get(difficulty, [])
        
        for i in range(min(num_problems, len(answers))):
            problem = problems[i]
            student_answer = answers[i]
            
            print(f"Problem {i+1}: {problem['problem']}")
            print(f"Student answer: {student_answer}")
            
            # Simulate time taken (1-5 seconds)
            time_taken = 2.0 + i * 0.5
            
            # Get correct answer
            if problem['type'] == 'linear':
                correct_answer = self.algebra_engine.solve_linear_equation(problem['problem'])
            else:
                correct_answer = problem['answer']
            
            # Record the attempt
            self.analyzer.add_attempt(
                self.current_student_id,
                problem['problem'],
                student_answer,
                correct_answer,
                time_taken
            )
            
            # Provide feedback
            is_correct = self.analyzer.attempts[-1].is_correct
            if is_correct:
                print("✓ Correct!")
            else:
                print(f"✗ Incorrect. The correct answer is: {correct_answer}")
            
            print(f"Time taken: {time_taken:.1f} seconds\n")
    
    def show_student_report(self, student_id: str = None):
        """Show performance report for a student."""
        if student_id is None:
            student_id = self.current_student_id
        
        if not student_id:
            print("Please specify a student ID")
            return
        
        performance = self.analyzer.get_student_performance(student_id)
        
        if "error" in performance:
            print(f"Error: {performance['error']}")
            return
        
        print(f"\n=== Performance Report for {student_id} ===")
        print(f"Total attempts: {performance['total_attempts']}")
        print(f"Correct attempts: {performance['correct_attempts']}")
        print(f"Accuracy: {performance['accuracy']:.2%}")
        print(f"Average time per problem: {performance['average_time']:.1f} seconds")
        print(f"Latest attempt: {performance['latest_attempt'].strftime('%Y-%m-%d %H:%M:%S')}")
    
    def show_class_report(self):
        """Show overall class performance report."""
        performance = self.analyzer.get_class_performance()
        
        if "error" in performance:
            print(f"Error: {performance['error']}")
            return
        
        print("\n=== Class Performance Report ===")
        print(f"Total students: {performance['total_students']}")
        print(f"Total attempts: {performance['total_attempts']}")
        print(f"Overall accuracy: {performance['overall_accuracy']:.2%}")
        print(f"Average class accuracy: {performance['average_class_accuracy']:.2%}")
        print(f"Average class time: {performance['average_class_time']:.1f} seconds")
        
        print("\n--- Individual Student Performance ---")
        for student_perf in performance['student_performances']:
            print(f"{student_perf['student_id']}: "
                  f"{student_perf['accuracy']:.2%} accuracy, "
                  f"{student_perf['total_attempts']} attempts")
    
    def solve_equation(self, equation: str):
        """Solve a single equation and show the solution."""
        try:
            if 'x^2' in equation or 'x**2' in equation:
                print("Quadratic equations should be solved using solve_quadratic() method")
                return
            
            solution = self.algebra_engine.solve_linear_equation(equation)
            print(f"Solution for '{equation}': x = {solution}")
            
            # Verify the solution
            self.algebra_engine.set_variable('x', solution)
            left_side = equation.split('=')[0].strip()
            right_side = float(equation.split('=')[1].strip())
            
            try:
                left_result = self.algebra_engine.evaluate_expression(left_side)
                print(f"Verification: {left_side} = {left_result}, {right_side} = {right_side}")
                if abs(left_result - right_side) < 1e-6:
                    print("✓ Solution verified!")
                else:
                    print("✗ Solution verification failed")
            except Exception as e:
                print(f"Could not verify solution: {e}")
                
        except Exception as e:
            print(f"Error solving equation: {e}")
    
    def solve_quadratic(self, a: float, b: float, c: float):
        """Solve a quadratic equation ax² + bx + c = 0."""
        try:
            solution1, solution2 = self.algebra_engine.solve_quadratic_equation(a, b, c)
            
            print(f"Quadratic equation: {a}x² + {b}x + {c} = 0")
            
            if solution1 is None:
                print("No real solutions (complex roots)")
            elif solution1 == solution2:
                print(f"One solution (repeated root): x = {solution1}")
            else:
                print(f"Two solutions: x₁ = {solution1}, x₂ = {solution2}")
                
        except Exception as e:
            print(f"Error solving quadratic equation: {e}")


def main():
    """Main function to demonstrate the algebra application."""
    app = AlgebraApp()
    
    print("Welcome to the Student Algebra Analysis System!")
    print("=" * 50)
    
    # Demo with multiple students
    students = ["Alice", "Bob", "Charlie"]
    
    for student in students:
        app.set_student(student)
        
        # Run demo sessions with different difficulties
        if student == "Alice":
            app.demo_session("easy", 3)
        elif student == "Bob":
            app.demo_session("medium", 3)
        else:
            app.demo_session("hard", 2)
    
    # Show individual reports
    for student in students:
        app.show_student_report(student)
    
    # Show class report
    app.show_class_report()
    
    # Demonstrate equation solving
    print("\n=== Equation Solving Demo ===")
    app.solve_equation("2x + 5 = 13")
    app.solve_equation("3x - 7 = 14")
    app.solve_quadratic(1, -5, 6)  # x² - 5x + 6 = 0
    app.solve_quadratic(2, 3, -2)  # 2x² + 3x - 2 = 0


if __name__ == "__main__":
    main()