class Model:
    def __init__(self, data):
        self.data = data

    def fit(self):
        raise NotImplementedError("This method should be overridden by subclasses")

    def predict(self, input_data):
        raise NotImplementedError("This method should be overridden by subclasses")

    def evaluate(self, test_data):
        raise NotImplementedError("This method should be overridden by subclasses")

    def export(self, filepath):
        """
        Export the model to the given filepath.
        """
        raise NotImplementedError("This method should be overridden by subclasses")

    def summary(self):
        print(f"Model summary:\nData shape: {getattr(self.data, 'shape', 'Unknown')}")

    def save(self, filepath):
        """
        Save the model to disk.
        """
        raise NotImplementedError("This method should be overridden by subclasses")

    def load(self, filepath):
        """
        Load the model from disk.
        """
        raise NotImplementedError("This method should be overridden by subclasses")

    def __str__(self):
        return f"Model(data={self.data})"
