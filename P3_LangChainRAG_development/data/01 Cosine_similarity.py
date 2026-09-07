import numpy as np

"""
Calculate the cosine similarity between two vectors (measures directional similarity, removing magnitude effects)

Parameters:
    vec_a (np.array): Vector A
    vec_b (np.array): Vector B
Returns:
    float: Cosine similarity result (range [-1, 1], closer to 1 means more aligned)
Formula:
    cos_sim = (vec_a · vec_b) / (||vec_a|| × ||vec_b||)
    Decomposition:
    1. Dot Product: vec_a · vec_b = vec_a[0]×vec_b[0] + vec_a[1]×vec_b[1] + ... + vec_a[n]×vec_b[n]
    2. Magnitude: ||vec_a|| = √(vec_a[0]² + vec_a[1]² + ... + vec_a[n]²)
    3. Magnitude: ||vec_b|| = √(vec_b[0]² + vec_b[1]² + ... + vec_b[n]²)

A: [0.5, 0.5]
B: [0.7, 0.7]
C: [0.7, 0.5]
D: [-0.6, -0.5]
"""


def get_dot(vec_a, vec_b):
    """Calculate the dot product of two vectors: the sum of the products of corresponding elements."""
    if len(vec_a) != len(vec_b):
        raise ValueError("Both vectors must have the same dimension")

    dot_sum = 0
    for a, b in zip(vec_a, vec_b):
        dot_sum += a * b

    return dot_sum


def get_norm(vec):
    """Calculate the magnitude (norm) of a vector: square each element, sum them, and take the square root."""
    sum_square = 0
    for v in vec:
        sum_square += v * v

    # Calculate square root using numpy's sqrt function
    return np.sqrt(sum_square)


def cosine_similarity(vec_a, vec_b):
    """Cosine similarity: dot product of two vectors divided by the product of their magnitudes."""

    result = get_dot(vec_a, vec_b) / (get_norm(vec_a) * get_norm(vec_b))
    return result


if __name__ == "__main__":
    vec_a = [0.5, 0.5]
    vec_b = [0.7, 0.7]
    vec_c = [0.7, 0.5]
    vec_d = [-0.6, -0.5]

    print("ab:", cosine_similarity(vec_a, vec_b))
    print("ac:", cosine_similarity(vec_a, vec_c))
    print("ad:", cosine_similarity(vec_a, vec_d))