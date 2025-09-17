"""
Algebra Engine for Student Analysis
===================================

This module provides core algebraic functionality for student learning and analysis.
It includes basic operations, equation solving, and student performance tracking.
"""

import math
import re
from typing import Dict, List, Tuple, Union, Optional
from dataclasses import dataclass
from datetime import datetime


@dataclass
class StudentAttempt:
    """Records a student's attempt at solving an algebra problem."""
    student_id: str
    problem: str
    answer: Union[float, str]
    correct_answer: Union[float, str]
    is_correct: bool
    timestamp: datetime
    time_taken: float  # in seconds


class AlgebraEngine:
    """Core algebra engine for basic operations and equation solving."""
    
    def __init__(self):
        self.variables = {}
    
    def evaluate_expression(self, expression: str) -> float:
        """
        Safely evaluate a mathematical expression.
        
        Args:
            expression: String containing mathematical expression
            
        Returns:
            Result of the evaluation
            
        Raises:
            ValueError: If expression is invalid
        """
        # Remove whitespace
        expression = expression.replace(' ', '')
        
        # Basic validation - only allow safe characters
        allowed_chars = set('0123456789+-*/()x.^')
        if not all(c in allowed_chars for c in expression):
            raise ValueError("Invalid characters in expression")
        
        # Replace x with variable value if it exists
        if 'x' in expression and 'x' in self.variables:
            x_value = self.variables['x']
            # Replace x with the value, but be careful with expressions like "2x"
            expression = re.sub(r'(\d)x', r'\1*' + str(x_value), expression)
            expression = expression.replace('x', str(x_value))
        
        # Replace ^ with ** for Python exponentiation
        expression = expression.replace('^', '**')
        
        try:
            # Use eval safely with limited scope
            result = eval(expression, {"__builtins__": {}}, {})
            return float(result)
        except Exception as e:
            raise ValueError(f"Cannot evaluate expression: {e}")
    
    def solve_linear_equation(self, equation: str) -> float:
        """
        Solve a linear equation of the form ax + b = cx + d.
        
        Args:
            equation: String like "2x + 3 = 7" or "2x + 9 = 3x - 1"
            
        Returns:
            Value of x that solves the equation
        """
        # Split equation into left and right sides
        if '=' not in equation:
            raise ValueError("Equation must contain '=' sign")
        
        left, right = equation.split('=')
        left = left.strip()
        right = right.strip()
        
        # Parse both sides to extract coefficients and constants
        left_coeff, left_const = self._parse_linear_expression(left)
        right_coeff, right_const = self._parse_linear_expression(right)
        
        # Rearrange to (left_coeff - right_coeff)x = right_const - left_const
        final_coeff = left_coeff - right_coeff
        final_const = right_const - left_const
        
        if abs(final_coeff) < 1e-10:
            if abs(final_const) < 1e-10:
                raise ValueError("Infinite solutions - equation is an identity")
            else:
                raise ValueError("No solution - equation is inconsistent")
        
        solution = final_const / final_coeff
        return solution
    
    def _parse_linear_expression(self, expr: str) -> Tuple[float, float]:
        """
        Parse a linear expression to extract coefficient of x and constant term.
        
        Args:
            expr: Expression like "2x + 3", "4x - 5", "7", or "x"
            
        Returns:
            Tuple of (coefficient_of_x, constant_term)
        """
        expr = expr.replace(' ', '')
        
        # If expression is just a number
        if 'x' not in expr:
            try:
                return (0.0, float(expr))
            except ValueError:
                raise ValueError(f"Invalid expression: {expr}")
        
        # Pattern to match terms like +2x, -3x, +x, -x, +5, -7
        # Split by + and - while keeping the signs
        parts = re.split(r'([+-])', expr)
        if parts[0] == '':
            parts = parts[1:]  # Remove empty first element if expr starts with + or -
        
        coeff = 0.0
        const = 0.0
        
        i = 0
        while i < len(parts):
            sign = 1
            term = parts[i]
            
            # Handle sign
            if term in ['+', '-']:
                sign = 1 if term == '+' else -1
                i += 1
                if i >= len(parts):
                    break
                term = parts[i]
            elif i > 0:
                # If there's no explicit sign, it's positive
                sign = 1
            
            # Check if this term contains x
            if 'x' in term:
                # Extract coefficient
                coeff_part = term.replace('x', '')
                if coeff_part == '' or coeff_part == '+':
                    coeff += sign * 1.0
                elif coeff_part == '-':
                    coeff += sign * -1.0
                else:
                    try:
                        coeff += sign * float(coeff_part)
                    except ValueError:
                        raise ValueError(f"Invalid coefficient in term: {term}")
            else:
                # This is a constant term
                try:
                    const += sign * float(term)
                except ValueError:
                    raise ValueError(f"Invalid constant term: {term}")
            
            i += 1
        
        return (coeff, const)
    
    def solve_quadratic_equation(self, a: float, b: float, c: float) -> Tuple[Optional[float], Optional[float]]:
        """
        Solve quadratic equation ax^2 + bx + c = 0 using quadratic formula.
        
        Args:
            a, b, c: Coefficients of the quadratic equation
            
        Returns:
            Tuple of two solutions (may contain None for complex solutions)
        """
        if a == 0:
            raise ValueError("Coefficient 'a' cannot be zero for quadratic equation")
        
        discriminant = b**2 - 4*a*c
        
        if discriminant < 0:
            return (None, None)  # Complex solutions
        elif discriminant == 0:
            solution = -b / (2*a)
            return (solution, solution)
        else:
            sqrt_discriminant = math.sqrt(discriminant)
            solution1 = (-b + sqrt_discriminant) / (2*a)
            solution2 = (-b - sqrt_discriminant) / (2*a)
            return (solution1, solution2)
    
    def set_variable(self, name: str, value: float):
        """Set a variable value for use in expressions."""
        self.variables[name] = value
    
    def get_variable(self, name: str) -> Optional[float]:
        """Get a variable value."""
        return self.variables.get(name)


class StudentAnalyzer:
    """Analyzes student performance in algebra problems."""
    
    def __init__(self):
        self.attempts: List[StudentAttempt] = []
        self.algebra_engine = AlgebraEngine()
    
    def add_attempt(self, student_id: str, problem: str, student_answer: Union[float, str], 
                   correct_answer: Union[float, str], time_taken: float):
        """Record a student's attempt at solving a problem."""
        is_correct = self._check_answer(student_answer, correct_answer)
        attempt = StudentAttempt(
            student_id=student_id,
            problem=problem,
            answer=student_answer,
            correct_answer=correct_answer,
            is_correct=is_correct,
            timestamp=datetime.now(),
            time_taken=time_taken
        )
        self.attempts.append(attempt)
    
    def _check_answer(self, student_answer: Union[float, str], correct_answer: Union[float, str]) -> bool:
        """Check if student answer matches correct answer with tolerance."""
        try:
            if isinstance(student_answer, str):
                student_val = float(student_answer)
            else:
                student_val = float(student_answer)
            
            if isinstance(correct_answer, str):
                correct_val = float(correct_answer)
            else:
                correct_val = float(correct_answer)
            
            # Use small tolerance for floating point comparison
            return abs(student_val - correct_val) < 1e-6
        except (ValueError, TypeError):
            return str(student_answer).strip() == str(correct_answer).strip()
    
    def get_student_performance(self, student_id: str) -> Dict:
        """Get performance statistics for a specific student."""
        student_attempts = [a for a in self.attempts if a.student_id == student_id]
        
        if not student_attempts:
            return {"error": "No attempts found for student"}
        
        total_attempts = len(student_attempts)
        correct_attempts = sum(1 for a in student_attempts if a.is_correct)
        accuracy = correct_attempts / total_attempts
        
        avg_time = sum(a.time_taken for a in student_attempts) / total_attempts
        
        return {
            "student_id": student_id,
            "total_attempts": total_attempts,
            "correct_attempts": correct_attempts,
            "accuracy": accuracy,
            "average_time": avg_time,
            "latest_attempt": student_attempts[-1].timestamp
        }
    
    def get_class_performance(self) -> Dict:
        """Get overall class performance statistics."""
        if not self.attempts:
            return {"error": "No attempts recorded"}
        
        total_attempts = len(self.attempts)
        correct_attempts = sum(1 for a in self.attempts if a.is_correct)
        
        students = set(a.student_id for a in self.attempts)
        student_performances = []
        
        for student in students:
            perf = self.get_student_performance(student)
            if "error" not in perf:
                student_performances.append(perf)
        
        avg_class_accuracy = sum(p["accuracy"] for p in student_performances) / len(student_performances)
        avg_class_time = sum(p["average_time"] for p in student_performances) / len(student_performances)
        
        return {
            "total_students": len(students),
            "total_attempts": total_attempts,
            "overall_accuracy": correct_attempts / total_attempts,
            "average_class_accuracy": avg_class_accuracy,
            "average_class_time": avg_class_time,
            "student_performances": student_performances
        }
    
    def generate_practice_problems(self, difficulty: str = "easy") -> List[Dict]:
        """Generate practice problems based on difficulty level."""
        problems = []
        
        if difficulty == "easy":
            # Simple linear equations
            problems.extend([
                {"problem": "x + 5 = 12", "answer": 7, "type": "linear"},
                {"problem": "2x = 10", "answer": 5, "type": "linear"},
                {"problem": "3x - 4 = 8", "answer": 4, "type": "linear"},
                {"problem": "x - 7 = 3", "answer": 10, "type": "linear"}
            ])
        elif difficulty == "medium":
            # More complex linear equations
            problems.extend([
                {"problem": "4x + 7 = 23", "answer": 4, "type": "linear"},
                {"problem": "5x - 12 = 18", "answer": 6, "type": "linear"},
                {"problem": "2x + 9 = 3x - 1", "answer": 10, "type": "linear"},
                {"problem": "7x - 5 = 2x + 15", "answer": 4, "type": "linear"}
            ])
        elif difficulty == "hard":
            # Quadratic equations and complex problems
            problems.extend([
                {"problem": "x^2 - 5x + 6 = 0", "answer": [2, 3], "type": "quadratic"},
                {"problem": "2x^2 + 3x - 2 = 0", "answer": [0.5, -2], "type": "quadratic"},
                {"problem": "x^2 - 4 = 0", "answer": [2, -2], "type": "quadratic"}
            ])
        
        return problems