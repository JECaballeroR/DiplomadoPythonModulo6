from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.metrics import r2_score


def get_X_y(df, y_name):
    """
    Splits a DataFrame in X (Features) and y (response variable)
    Parameters
    ----------
    df : DataFrame
        A DataFrame that has column features.
    y_name : str
        The name of the target varriable in the DataFrame.

    Returns
    -------
    X : DataFrame
        DataFrame with the features used to predict y.
    y : Array(int)
        Array with the response variable's values.
    """
    y = [y_name]
    X = [col for col in df.columns if col not in y]
    y = df[y].copy().values.flatten()
    X = pd.get_dummies(df[X].copy())
    return X, y


def pipeline_classifier(X, y, model, param_grid):
    """
    Creates a general Pipeline for sklearn classifiers.
    Applies GridSearchCV to optimize hyper parameters of the model.

    Parameters
    ----------
    X : {array-like, sparse matrix} of shape (n_samples, n_features)
        Input values
    y : {array-like, sparse matrix} of shape (n_samples)
        Target values
    model : sklearn.estimator object
        Instance of an estimator form sklearn.
    param_grid: dict or list of dictionaries
        Dictionary with parameters names (str) as keys and lists of parameter
        settings to try as values, or a list of such dictionaries, in which case
        the grids spanned by each dictionary in the list are explored.
        This enables searching over any sequence of parameter settings.

    Returns
    -------
    model : sklearn.estimator instance
        Fitted classifier or a fitted Pipeline in which the last estimator
        is a classifier.
    """
    pipe = make_pipeline(StandardScaler(), model)
    reg = GridSearchCV(pipe,
                       param_grid=param_grid,
                       cv=10,
                       refit=True,
                       scoring="r2",
                       n_jobs=-1)
    reg.fit(X, y)
    return reg

# Hay que filtrar y obtener los datos del modelo.
# Si no esto no corre!
# asignar valor a variable datos_modelo

X, y = get_X_y(datos_modelo, 'conteo')
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
rf_param_grid = {
    "randomforestregressor__criterion": ["squared_error", "absolute_error", "poisson"],
    "randomforestregressor__n_estimators": [100, 500, 100]}
modelo_cv = pipeline_classifier(X_train, y_train, RandomForestRegressor(), param_grid=rf_param_grid)
r2_score(y_test, modelo_cv.predict(X_test))