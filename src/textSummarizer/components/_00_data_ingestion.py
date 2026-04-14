import os
import urllib.request as request
import zipfile
from src.textSummarizer.logging import logger
from src.textSummarizer.entity import DataIngestionConfig
from src.textSummarizer.config.configuration import ConfigurationManager

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            logger.info(f"Downloading file from :[{self.config.source_URL}] into :[{self.config.local_data_file}]")

            file_name, headers = request.urlretrieve(
                url=self.config.source_URL, 
                filename=self.config.local_data_file
            )

            logger.info(f"File :[{self.config.local_data_file}] has been downloaded successfully.")
        else:
            logger.info(f"File :[{self.config.local_data_file}] already exists. Skipping download.")

    def unzip_and_save(self):      
        logger.info(f"Unzipping file :[{self.config.local_data_file}] to dir :[{self.config.unzip_dir}]")
        upzip_dir=self.config.unzip_dir
        os.makedirs(upzip_dir, exist_ok=True)

        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(self.config.unzip_dir)

        logger.info(f"File :[{self.config.local_data_file}] has been unzipped successfully.")