from sklearn.grid_search import GridSerarchCV
from sklearn.grid_search import RandomizedSearchCV

k_range(1,31)
param_grid = dict(n_neighbors=k_range)
grid = GridSerarchCV(knn, param_grid, cv=10, scoring='accuracy')

grid.fit(X,y)

print(grid.grid_scores_)
print(grid.grid_scores_[0].cv_validation_scores)
print(grid.grid_scores_[0].mean_validation_score)

print(grid.best_score_)
print(grid.best_params_)
print(grid.best_estimator_)



k_range = range(1,31)
weight_options = ['uniform','distance']
param_grid = dict(n_neighbors=k_range, weights=weight_options)

grid = GridSerarchCV(knn,param_grid, cv=10, scoring='accuracy')
grid.fit(X,y)

grid.predict([3,5,4,2])



param_dist = dict(n_neighbors=k_range, weights=weight_options)

rand = RandomizedSearchCV(knn,param_dist, cv=10, scoring='accuracy', n_iter=10)
rand.fit(X,y)
rand.grid_scores_







