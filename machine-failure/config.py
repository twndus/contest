import os

data_dir='/home/jylee/datasets/kaggle/machine-failures'
# args
args = {
    'train_path': os.path.join(data_dir, 'train.csv'),
    'test_path': os.path.join(data_dir, 'test.csv'),
    'submission_path': os.path.join(data_dir, 'sample_submission.csv'),
    'task': 'classification',
    'modelname': 'knn',
    'metric': 'auc',
    #'xgboost' #'mlp_keras' #'gbm'#'mlp' #'rf' #'svc' #'logistic' #'knn'
    'dataname': 'machine',
    'epochs': 20,
}
