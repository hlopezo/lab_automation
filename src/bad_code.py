def calculate_accuracy(y_true, y_pred):

    correct = sum(1 for true, pred in zip(y_true, y_pred) if true == pred)
    return correct / len(y_true)
