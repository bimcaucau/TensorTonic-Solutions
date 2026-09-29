import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    # Write code here
    a = np.array(a)
    b = np.array(b)
    return float(np.dot(a,b) / (np.linalg.norm(a) * np.linalg.norm(b))) if np.linalg.norm(a) * np.linalg.norm(b) != 0 else float(0)