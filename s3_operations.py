#!/usr/bin/env python3
import boto3
import pandas as pd
import re
import csv


def testThis():
# Connect to S3
        s3 = boto3.client('s3')
        bucket_name = 'yipit-oscars-data'
        object_key = 'movie-details'

        # Read the contents of the S3 object
        response = s3.get_object(Bucket=bucket_name, Key=object_key,ResponseContentType='json')['Body'].read().decode('utf-8')

        string = response.strip('{}')
        pairs = string.split(', ')

        new_lst = []
        current_group = []
        in_group = False
        for item in pairs:
            if item == "[":
                in_group = True
            elif item == "]":
                in_group = False
                new_lst.append(current_group)
                current_group = []
            elif in_group:
                current_group.append(item)
            else:
                new_lst.append(item)

        obj = new_lst
        my_dict = {}
        grouping = []

        # converted string dict into a list for simpler formation of hashmap
        for item in obj:
            try:
                key, value = item.split(":")
                key = key.replace('"','')
                my_dict[key.strip()] = {}
                
                my_dict[key.strip()] = value.strip()
                sub_items = value.split(',')
                for sub_item in sub_items:
                    if key == 'Budget':
                        # sub_item.replace('"','')
                        sub_value = sub_item[3:5]
                        grouping.append(sub_value.strip())
                        my_dict[key] = int(sub_value)
                    else:
                        sub_key, sub_value = sub_item.split(',')
                        grouping.append(sub_value.strip())
                        my_dict[key.strip()][sub_key.strip()] = sub_value
            except ValueError:
                pass
            return my_dict
        
        # subset to only include wanted keys
        def filter_dict(original_dict, keys_to_keep):
            return {key: original_dict[key] for key in keys_to_keep}

        my_dict = filter_dict(my_dict, ['Title','Budget','Box Office', 'Release dates'])

        # conversion to csv
        def to_Csv(data, file_path):
            with open(file_path, 'w', newline='') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(data.keys())
                writer.writerow(data.values())

        to_Csv(my_dict, './oscar-output.csv')
         # setup dataframe 
        # df1 = pd.DataFrame([my_dict], index=[len([my_dict])], columns=['Title','Budget','Box Office', 'Release dates'])
        # print(df1)


print(testThis())



# def listBuckets():
#     buckets = []
#     # Run the AWS CLI command to list the contents of the S3 bucket
#     result = subprocess.run(["aws", "s3", "ls", f"s3://yipit-oscars-data"], stdout=subprocess.PIPE)

#     # Split the output into lines
#     lines = result.stdout.decode("utf-8").split("\n")

#     # for item in lines:
#     buckets.append(lines)
#     return buckets