from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.metrics import r2_score


def get_X_y(df, y_name):
    """
    Obtiene X y y
    """
    y = [y_name]
    X = [col for col in df.columns if col not in y]
    y = df[y].copy().values.flatten()
    X = pd.get_dummies(df[X].copy(), drop_first=True)
    return X, y


def pipeline_classifier(X, y, model, param_grid):
    """
    Hace un pipeline de regresion
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