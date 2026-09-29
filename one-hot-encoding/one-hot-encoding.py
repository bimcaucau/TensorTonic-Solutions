import numpy as np

def one_hot(y: list, num_classes=None) -> np.ndarray:
    """
    Returns a NumPy array with shape (N, K).
    """
    # Write code here
    res = []
    if not num_classes:
        num_classes = int(max(y) + 1)
    for instance in y:
        onehot = np.zeros(num_classes)
        onehot[instance] = 1.0
        res.append(onehot)
    return np.array(res)
        
    