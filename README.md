# Pinterest Data Pipeline

## Milestone 1: Batch Processing - Configure the EC2 Kafka client


The aim of the first milestone was to utilise batch processing which is a process for processing a large volume of data. The EC2 client utilises AWS, the creation of the .pem key pair file allowed the connection to the EC2 instance. An instance allows the user to choose the right instance type based upon the GPU and workload. Kafka was set up on the instance by installing it on my machine with the help of MSK which uses IAM. Using IAM it allowed me to understand the use of cluster authentication which allowss the creation of the EC2 role. Once all is done correctly it allowed me to make kafka topics.


## Milestone 2: Batch Processing - Connecting an MSK cluster to an S3 bucket

The second milestone consited of using the S3 bucket that was created in S3 to then connect it via the MSK connect. Firstly the S3 bucket had to be seen if the and making a note of the bucket name. Which was "user-<your_UserId>-bucket". The use of EC2 client was needed to download the confluent.io Amazon s3 connector and then copying it to the S3 bucket. Then the creation of the custom plugin had to be done by using the MSK connect. The use " <your_UserId>-plugin" was needed. Once it was all done it allowed me to move onto the connector creation. The kafka topics that was done in milestone 1 was needed by using regex. Which is a form of filtering in a string as I created 3 topics this needed to be used with "user id.*" . Once thats done the user would have to check on the IAM role to access permissions and making sure the right EC2 role is chosen. Then the connector was created. 

This is what the final outcome should be showing like so ![Alt text]([image link](https://ibb.co/bHgb4M6)https://ibb.co/bHgb4M6)







