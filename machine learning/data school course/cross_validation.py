from sklearn.cross_validation import KFold, cross_val_score

kf = KFold(25, n_folds=5, suffle=False)

print(cross_val_score(knn, X, y, cv=10, scoring='accuracy').mean())


print(cross_val_score(logreg, X, y, cv=10, scoring='mean_square_error').mean())
