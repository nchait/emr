from pyspark.sql import SparkSession 
from pyspark.sql. functions import col

S3_DATA_SOURCE_PATH = 's3://nchait-test-bucket/data-source/survey_results_public.csv'
S3_DATA_OUTPUT_PATH = 's3://nchait-test-bucket/data-output'

def main():
    spark = SparkSession.builder.appName('NChaitDemoApp').getOrCreate()
    all_data = spark.read.csv(S3_DATA_SOURCE_PATH, header=True)
    print('Total number of records in the source data: %s' % all_data.count())
    selected_data = all_data.where((col('Country') == 'United States') & (col('WorkweekHrs') > 45))
    print ('The number of negineers who work more than 45 hours a week in the US is: %s' % selected_data.count())
    selected_data.write.mode('overwrite') .parquet (S3_DATA_OUTPUT_PATH)
    print('Selected data was successfully saved to s3: %s' % S3_DATA_OUTPUT_PATH)

if __name__ == '__main__':
    main()