flowers = {
    "iris_setosa": {
        "sepal_length": [3.6, 4.9, 4.8, 4.7],
        "sepal_width": [2.9, 3.3, 3.2, 3.1],
        "petal_length": [1.3, 1.2, 1.5, 1.4],
    },
    "iris_virginica": {
        "sepal_length": [7.2, 7.0, 7.9],
         "sepal_width": [3.1, 2.7, 2.8],
        "petal_length": [5.5, 5.5, 6.5],
    },
    "iris_versicolor": {
        "sepal_length": [6.5, 6.0, 6.1, 6.2, 6.3],
         "sepal_width": [2.8, 2.9, 2.4, 2.7, 2.7],
        "petal_length": [4.8, 4.7, 5.0, 4.9, 4.8],
    },
}


mean_sepal_length = (sum(flowers["iris_setosa"]["sepal_length"]) + sum(flowers["iris_virginica"]["sepal_length"]) + sum(flowers["iris_versicolor"]["sepal_length"])) / ((len(flowers["iris_setosa"]["sepal_length"])) + len(flowers["iris_virginica"]["sepal_length"]) + len(flowers["iris_versicolor"]["sepal_length"]))
mean_sepal_width = (sum(flowers["iris_setosa"]["sepal_width"]) + sum(flowers["iris_virginica"]["sepal_width"]) + sum(flowers["iris_versicolor"]["sepal_width"])) / ((len(flowers["iris_setosa"]["sepal_width"])) + len(flowers["iris_virginica"]["sepal_width"]) + len(flowers["iris_versicolor"]["sepal_width"]))
mean_petal_length = (sum(flowers["iris_setosa"]["petal_length"]) + sum(flowers["iris_virginica"]["petal_length"]) + sum(flowers["iris_versicolor"]["petal_length"])) / ((len(flowers["iris_setosa"]["petal_length"])) + len(flowers["iris_virginica"]["petal_length"]) + len(flowers["iris_versicolor"]["petal_length"]))

print(mean_sepal_length)
print(mean_sepal_width)
print(mean_petal_length)