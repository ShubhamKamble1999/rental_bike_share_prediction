import sys
from bike.exception import BikingException
from bike.logger import logging
from bike.entity.config_entity import DataIngestionConfig,DataValidationConfig,DataTransformationConfig,ModelEvaluationConfig,ModelTrainerConfig,ModelPusherConfig,TrainingPipelineConfig
from bike.util.util import read_yaml_file
from bike.constant import *

class Configuration():

    def __init__(
        self,
        config_file_path:str=CONFIG_FILE_PATH,
        current_time_stamp:str=CURRENT_TIME_STAMP,
    ) -> None:
        try:
            self.config_info = read_yaml_file(file_path=config_file_path)
            self.training_pipeline_config = self.get_training_pipeline_config() # First create artifact file, to append them ferther use
            self.time_stamp = current_time_stamp
        except Exception as e:
            raise BikingException(e,sys) from e

    def get_data_ingestion_config(self) ->DataIngestionConfig: # ----> Function to call the entity
        try:
            artifact_dir = self.training_pipeline_config.artifact_dir # ROOT-DIR\\bike\\artifact
            data_ingestion_artifact_dir = os.path.join(
                artifact_dir,
                DATA_INGESTION_ARTIFACT_DIR,
                self.time_stamp
            ) # ROOT-DIR\\bike\\artifact\\data_ingestion\\(time-stamp)

            data_ingestion_info = self.config_info[DATA_INGESTION_CONFIG_KEY]
            dataset_download_url = data_ingestion_info[DATA_INGESTION_DOWNLOAD_URL_KEY] # Download Image 
            
            tgz_download_url = os.path.join(
                data_ingestion_artifact_dir,
                data_ingestion_info[DATA_INGESTION_TGZ_DOWNLOAD_DIR_KEY]
            ) # ROOT-DIR\\bike\\artifact\\data_ingestion\\(time-stamp)\\tgz-file

            raw_data_dir = os.path.join(
                data_ingestion_artifact_dir,
                data_ingestion_info[DATA_INGESTION_RAW_DATA_DIR_KEY]
            ) # ROOT-DIR\\bike\\artifact\\data_ingestion\\(time-stamp)\\raw_data-file

            ingested_data_dir = os.path.join(
                data_ingestion_artifact_dir,
                data_ingestion_info[DATA_INGESTION_INGESTED_DIR_NAME_KEY],

            ) # ROOT-DIR\\bike\\artifact\\data_ingestion\\(time-stamp)\\ingested_dir

            ingested_train_dir = os.path.join(
                ingested_data_dir,
                data_ingestion_info[DATA_INGESTION_TRAIN_DIR_KEY]
            ) # ROOT-DIR\\bike\\artifact\\data_ingestion\\(time-stamp)\\ingested_train_dir

            ingested_test_dir = os.path.join(
                ingested_data_dir,
                data_ingestion_info[DATA_INGESTION_TEST_DIR_KEY]
            ) # ROOT-DIR\\bike\\artifact\\data_ingestion\\(time-stamp)\\ingested_test_dir

            tgz_download_url =tgz_download_url
            raw_data_dir =raw_data_dir
            ingested_train_dir =ingested_train_dir
            ingested_test_dir = ingested_test_dir

            data_ingestion_config = DataIngestionConfig(
                dataset_download_url = dataset_download_url,
                tgz_download_url = tgz_download_url, 
                raw_data_dir=raw_data_dir,
                ingested_train_dir=ingested_train_dir,
                ingested_test_dir=ingested_test_dir
            )
            logging.info(f"Data Ingestion config: {data_ingestion_config}")
            return data_ingestion_config
        except Exception as e:
            raise BikingException(e,sys) from e

    def get_data_validation_config(self) ->DataValidationConfig:
        try:
            pass
        except Exception as e:
            raise BikingException(e,sys) from e

    def get_data_transformation_config(self) ->DataTransformationConfig:
        try:
            pass
        except Exception as e:
            raise BikingException(e,sys) from e

    def get_model_trainer_config(self) ->ModelTrainerConfig:
        try:
            pass
        except Exception as e:
            raise BikingException(e,sys) from e

    def get_model_evaluation_config(self)->ModelEvaluationConfig:
        try:
            pass
        except Exception as e:
            raise BikingException(e,sys) from e

    def get_model_pusher_config(self)->ModelPusherConfig:
        try:
            pass
        except Exception as e:
            raise BikingException(e,sys) from e

    def get_training_pipeline_config(self)->TrainingPipelineConfig:
        try:
            traning_pipeline_config = self.config_info[TRAINING_PIPELINE_CONFIG_KEY]
            artifact_dir = os.path.join(
                ROOT_DIR,
                traning_pipeline_config[TRAINING_PIPELINE_NAME_KEY],
                traning_pipeline_config[TRAINING_PIPELINE_ARTIFACT_DIR_KEY]
            ) # creating the directory for artifacts.
              # :- ROOT-DIR\\bike\\artifact

            # Creating the pipeline for training data
            training_pipeline_config = TrainingPipelineConfig(artifact_dir=artifact_dir)
            logging.info(f"Training pipeline config : {training_pipeline_config}")
            return training_pipeline_config
        except Exception as e:
            raise BikingException(e,sys) from e
