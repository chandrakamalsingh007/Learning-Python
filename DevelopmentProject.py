import unittest
import time
import math
import sys

def gram_schmidt(matrix):
    rows, cols = len(matrix), len(matrix[0])
    orthogonal_matrix = [[0.0] * cols for _ in range(rows)]
    
    for i in range(cols):
        column_vector = [matrix[row][i] for row in range(rows)]
        for j in range(i):
            dot_product = sum(orthogonal_matrix[row][j] * column_vector[row] for row in range(rows))
            column_vector = [column_vector[row] - dot_product * orthogonal_matrix[row][j] for row in range(rows)]
        norm = math.sqrt(sum(x**2 for x in column_vector))
        if norm > 1e-10:
            orthogonal_matrix = [[column_vector[row] / norm if col == i else orthogonal_matrix[row][col] for col in range(cols)] for row in range(rows)]
        else:
            orthogonal_matrix = [[column_vector[row] if col == i else orthogonal_matrix[row][col] for col in range(cols)] for row in range(rows)]
    return orthogonal_matrix

def householder(matrix):
    rows, cols = len(matrix), len(matrix[0])
    orthogonal_matrix = [[1.0 if i == j else 0.0 for j in range(rows)] for i in range(rows)]
    upper_triangular_matrix = [row[:] for row in matrix]
    
    for i in range(cols):
        column_vector = [upper_triangular_matrix[row][i] for row in range(i, rows)]
        reflection_vector = [0.0] * len(column_vector)
        reflection_vector[0] = math.sqrt(sum(x**2 for x in column_vector))
        householder_vector = [column_vector[j] - reflection_vector[j] for j in range(len(column_vector))]
        householder_vector_norm = math.sqrt(sum(x**2 for x in householder_vector))
        if householder_vector_norm > 1e-10:
            householder_vector_normalized = [x / householder_vector_norm for x in householder_vector]
            for j in range(i, rows):
                for k in range(i, cols):
                    upper_triangular_matrix[j][k] -= 2.0 * householder_vector_normalized[j-i] * sum(householder_vector_normalized[m-i] * upper_triangular_matrix[m][k] for m in range(i, rows))
            for j in range(rows):
                for k in range(i, rows):
                    orthogonal_matrix[j][k] -= 2.0 * householder_vector_normalized[k-i] * sum(householder_vector_normalized[m-i] * orthogonal_matrix[j][m] for m in range(i, rows))
    return orthogonal_matrix

def measure_algorithm_performance(algorithm, matrix):
     start_time = time.time()  # Record the start time
     result = algorithm(matrix)  # Execute the algorithm
     end_time = time.time()  # Record the end time
     return result, end_time - start_time  # Return the result and performance metrics

def get_memory_usage():
    return sys.getsizeof(result) + sys.getsizeof(matrix)

class TestOrthogonalization(unittest.TestCase):
    def setUp(self):
        self.test_matrix = [[1.0, 1.0, 1.0],
                            [0.0, 1.0, 2.0],
                            [0.0, 0.0, 3.0]]

    def test_gram_schmidt(self):
        global result, matrix
        matrix = self.test_matrix
        result, execution_time = measure_algorithm_performance(gram_schmidt, self.test_matrix)
        expected_result = [[1.0, 0.0, 0.0],
                          [0.0, 1.0, 0.0],
                          [0.0, 0.0, 1.0]]  # Simplified expected result for demonstration
        print("Gram-Schmidt Result:")
        for row in result:
            print(row)
        print("Expected (QR) Result:")
        for row in expected_result:
            print(row)
        self.assertAlmostEqual(result[0][0], expected_result[0][0], places=5)
        self.assertAlmostEqual(result[1][1], expected_result[1][1], places=5)
        self.assertAlmostEqual(result[2][2], expected_result[2][2], places=5)
        print(f"Gram-Schmidt time: {execution_time}s, Memory: {get_memory_usage()} bytes")

    def test_householder_reflection(self):
        global result, matrix
        matrix = self.test_matrix
        result, execution_time= measure_algorithm_performance(householder, self.test_matrix)
        expected_result = [[1.0, 0.0, 0.0],
                          [0.0, 1.0, 0.0 ],
                          [0.0, 0.0, 1.0]]  # Simplified expected result for demonstration
        print("Householder Reflection Result:")
        for row in result:
            print(row)
        print("Expected (QR) Result:")
        for row in expected_result:
            print(row)
        self.assertAlmostEqual(result[0][0], expected_result[0][0], places=5)
        self.assertAlmostEqual(result[1][1], expected_result[1][1], places=5)
        self.assertAlmostEqual(result[2][2], expected_result[2][2], places=5)
        print(f"Householder reflection time: {execution_time}s, Memory: {get_memory_usage()} bytes")

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)