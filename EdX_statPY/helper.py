import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


def fit_and_plot_linear(x, y):
    """
    Fits a linear regression model and plots the data and regression line.

    Parameters:
    x (array-like): Predictor variable (feature).
    y (array-like): Response variable (target).

    Returns:
    r2_train (float): R-squared value for the training data.
    r2_test (float): R-squared value for the testing data.
    """
    # Reshape x to 2D array (required for scikit-learn)
    x = x.reshape(-1, 1)

    # Split the data into training and testing sets
    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.2, random_state=42
    )

    # Fit a linear regression model
    model = LinearRegression()
    model.fit(x_train, y_train)

    # Predict on training and testing data
    y_train_pred = model.predict(x_train)
    y_test_pred = model.predict(x_test)

    # Compute R-squared values
    r2_train = r2_score(y_train, y_train_pred)
    r2_test = r2_score(y_test, y_test_pred)

    # Plot the data and regression line
    plt.scatter(x_train, y_train, color="blue", label="Train Data")
    plt.scatter(x_test, y_test, color="green", label="Test Data")
    plt.plot(x_train, y_train_pred, color="red", label="Regression Line")
    plt.xlabel("Predictor")
    plt.ylabel("Sales")
    plt.legend()
    plt.title("Linear Regression Fit")
    plt.show()

    return r2_train, r2_test


def fit_and_plot_multi(x, y):
    """
    Fits a multiple linear regression model and plots the data (for 2D x).
    """
    # Fit a linear regression model
    model = LinearRegression()
    model.fit(x, y)

    # Predict y values
    y_pred = model.predict(x)

    # Plot the data and regression plane (for 2D x)
    if x.shape[1] == 2:
        fig = plt.figure()
        ax = fig.add_subplot(111, projection="3d")
        ax.scatter(x[:, 0], x[:, 1], y, color="blue", label="Data")
        ax.plot_trisurf(
            x[:, 0], x[:, 1], y_pred, color="red", alpha=0.5, label="Regression Plane"
        )
        ax.set_xlabel("X1")
        ax.set_ylabel("X2")
        ax.set_zlabel("Y")
        ax.legend()
        plt.title("Multiple Linear Regression Fit")
        plt.show()
    else:
        print("fit_and_plot_multi only supports 2D x data.")
