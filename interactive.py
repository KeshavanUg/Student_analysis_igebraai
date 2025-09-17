#!/usr/bin/env python3
"""
Interactive Algebra Learning System
===================================

A simple command-line interface for the igebra project that allows users
to practice algebra problems and see their progress.
"""

import sys
import time
from main import AlgebraApp


def print_menu():
    """Display the main menu options."""
    print("\n" + "=" * 50)
    print("    Student Algebra Analysis System")
    print("=" * 50)
    print("1. Set Student ID")
    print("2. Practice Session (Easy)")
    print("3. Practice Session (Medium)")
    print("4. Practice Session (Hard)")
    print("5. Solve Single Equation")
    print("6. View Student Report")
    print("7. View Class Report")
    print("8. Run Demo")
    print("9. Exit")
    print("=" * 50)


def get_user_input(prompt, input_type=str, default=None):
    """Get user input with type validation."""
    while True:
        try:
            user_input = input(f"{prompt}: ").strip()
            if not user_input and default is not None:
                return default
            return input_type(user_input)
        except ValueError:
            print(f"Invalid input. Please enter a valid {input_type.__name__}.")
        except KeyboardInterrupt:
            print("\nExiting...")
            sys.exit(0)


def interactive_practice_session(app, difficulty):
    """Run an interactive practice session."""
    if not app.current_student_id:
        print("Please set a student ID first!")
        return
    
    print(f"\nStarting {difficulty} practice session for {app.current_student_id}")
    
    problems = app.analyzer.generate_practice_problems(difficulty)
    num_problems = min(len(problems), get_user_input("How many problems would you like to solve?", int, 3))
    
    correct_count = 0
    total_time = 0
    
    for i in range(num_problems):
        problem = problems[i]
        print(f"\nProblem {i+1}: {problem['problem']}")
        
        start_time = time.time()
        
        try:
            if problem['type'] == 'quadratic':
                print("For quadratic equations, enter two solutions separated by comma (e.g., 2, 3)")
                user_answer = input("Your answer: ").strip()
                student_answer = [float(x.strip()) for x in user_answer.split(',')]
                correct_answer = problem['answer']
            else:
                user_answer = input("Your answer: ").strip()
                student_answer = float(user_answer)
                # Calculate correct answer
                correct_answer = app.algebra_engine.solve_linear_equation(problem['problem'])
            
            end_time = time.time()
            time_taken = end_time - start_time
            total_time += time_taken
            
            # Record the attempt
            app.analyzer.add_attempt(
                app.current_student_id,
                problem['problem'],
                student_answer,
                correct_answer,
                time_taken
            )
            
            # Check if correct
            is_correct = app.analyzer.attempts[-1].is_correct
            if is_correct:
                print("✓ Correct! Great job!")
                correct_count += 1
            else:
                print(f"✗ Incorrect. The correct answer is: {correct_answer}")
            
            print(f"Time taken: {time_taken:.1f} seconds")
            
        except ValueError as e:
            print(f"Invalid input: {e}")
            continue
        except KeyboardInterrupt:
            print("\nSession interrupted by user.")
            break
    
    # Show session summary
    if num_problems > 0:
        accuracy = correct_count / num_problems
        avg_time = total_time / num_problems
        
        print(f"\n=== Session Summary ===")
        print(f"Problems completed: {num_problems}")
        print(f"Correct answers: {correct_count}")
        print(f"Accuracy: {accuracy:.2%}")
        print(f"Total time: {total_time:.1f} seconds")
        print(f"Average time per problem: {avg_time:.1f} seconds")


def solve_single_equation(app):
    """Allow user to solve a single equation."""
    equation = get_user_input("Enter an equation to solve (e.g., 2x + 5 = 13)")
    
    try:
        if 'x^2' in equation or 'x**2' in equation:
            print("For quadratic equations, please use the format: ax² + bx + c = 0")
            a = get_user_input("Enter coefficient a", float)
            b = get_user_input("Enter coefficient b", float)
            c = get_user_input("Enter coefficient c", float)
            app.solve_quadratic(a, b, c)
        else:
            app.solve_equation(equation)
    except Exception as e:
        print(f"Error: {e}")


def main():
    """Main interactive application loop."""
    app = AlgebraApp()
    
    print("Welcome to the Interactive Algebra Learning System!")
    print("This system helps you practice algebra and tracks your progress.")
    
    while True:
        print_menu()
        
        try:
            choice = get_user_input("Select an option (1-9)", int)
            
            if choice == 1:
                student_id = get_user_input("Enter your student ID")
                app.set_student(student_id)
                
            elif choice == 2:
                interactive_practice_session(app, "easy")
                
            elif choice == 3:
                interactive_practice_session(app, "medium")
                
            elif choice == 4:
                interactive_practice_session(app, "hard")
                
            elif choice == 5:
                solve_single_equation(app)
                
            elif choice == 6:
                if app.current_student_id:
                    app.show_student_report()
                else:
                    student_id = get_user_input("Enter student ID to view report")
                    app.show_student_report(student_id)
                
            elif choice == 7:
                app.show_class_report()
                
            elif choice == 8:
                print("\nRunning demonstration...")
                # Create a temporary app for demo
                demo_app = AlgebraApp()
                students = ["Alice", "Bob", "Charlie"]
                
                for student in students:
                    demo_app.set_student(student)
                    if student == "Alice":
                        demo_app.demo_session("easy", 2)
                    elif student == "Bob":
                        demo_app.demo_session("medium", 2)
                    else:
                        demo_app.demo_session("hard", 2)
                
                for student in students:
                    demo_app.show_student_report(student)
                demo_app.show_class_report()
                
            elif choice == 9:
                print("Thank you for using the Algebra Learning System!")
                print("Keep practicing and you'll master algebra in no time!")
                sys.exit(0)
                
            else:
                print("Invalid choice. Please select a number from 1-9.")
                
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            sys.exit(0)
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()