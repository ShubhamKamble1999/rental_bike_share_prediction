from collections import namedtuple

DataIngestionConfig = namedtuple(
    'DataIngestionConfig',
    ['dataset_download_url','tgz_download_url','raw_data_dir','ingested_train_dir','ingested_test_dir']
)

DataValidationConfig = namedtuple(
    "DataValidationConfig",
    ['schema_file_path']
)

DataTransformationConfig = namedtuple(
    "DataTransformationConfig",
    [#"add_bedroom_per_room", ----> Adding a column in the dataset of require
    "transformed_train_dir", # ----> Location of transformed data from train dataset (from -> DataIngestion.ingested_train_dir)
    "transformed_test_dir",
    "preprocessed_object_file_path"] # ----> Location of pickle file for transformed data
)

ModelTrainerConfig = namedtuple(
    "ModelTrainerConfig", 
    ["trained_model_file_path", # ----> Location of pickle file for model training
    "base_accuracy", # -----> Specify the base accuracy. (eg:- 90% base accuracy.)
    "model_config_file_path"]
)

ModelEvaluationConfig = namedtuple(
    "ModelEvaluationConfig", 
    ["model_evaluation_file_path", # -----> location of model file for evaluating the best model
    "time_stamp"] # -----> Timestamp of at what time model is compaired
)

ModelPusherConfig = namedtuple(
    "ModelPusherConfig", 
    ["export_dir_path"] # where i want to export my model ?
)

TrainingPipelineConfig = namedtuple(
    "TrainingPipelineConfig", 
    ["artifact_dir"]
)
