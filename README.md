# Pinterest Data Pipeline

## Description
Trying to emulate how pinterest internal data pipeline works.

### Architecture Diagram

![Architecture Overview](/pinterest-data-pipeline/images/CloudPinterestPipeline.jpeg)

### Tools 
- AWS
- API Gateway
- EC2
- MSK
- DataBricks
- MWAA
- Kinesis


## Batch Processing - Configure the EC2 Kafka client
EC2 - Amazon Elastic Compute Cloud (EC2) is a key component of Amazon Web Services (AWS) and plays a vital role in cloud computing. EC2 provides a scalable and flexible infrastructure for hosting virtual servers, also known as instances, in the cloud. 

Kafka - Apache Kafka is a relatively new open-source technology for distributed data storage optimized for ingesting and processing streaming data in real-time. It provides three main focuses to the user  the first being to publish and subscribe to streams of records, to store streams of records in the order in which records were generated and lastly to process streams of records in real-time. Many coroprations from fortune 500 use Kafka for example Netflix, Lyft and Uber this is to leverage the technology stack in order to allow real-time data streaming and real-time data processing at scale.

Batch processing which is a process for processing a large volume of data. The EC2 client utilises AWS, the creation of the .pem key pair file allowed the connection to the EC2 instance. An instance allows the user to choose the right instance type based upon the GPU and workload. Kafka was set up on the instance by installing it on my machine with the help of MSK which uses IAM. Using IAM it allowed me to understand the use of cluster authentication which allowss the creation of the EC2 role. Once all is done correctly it allowed the creation of the kafka topics.


## Batch Processing - Connecting an MSK cluster to an S3 bucket
MSK - Amazon Managed Streaming for Apache Kafka (Amazon MSK) is a fully managed service used to build and run applications that use Apache Kafka to process data. Apache Kafka is an open-source technology for distributed data storage, optimized for ingesting and processing streaming data in real-time.

S3 - Amazon S3, also known as Simple Storage Service, is a scalable and highly available object storage service provided by AWS. Its primary purpose is to store and retrieve large amounts of data reliably, securely, and cost-effectively. S3 it's benefit is that it integrates with other AWS services, allowing seamless data transfer and integration with analytics, machine learning, and other data processing workflows. 

Using the S3 bucket that was created in S3 to then connect it via the MSK connect. Firstly the S3 bucket had to be seen if the and making a note of the bucket name. Which was "user-<your_UserId>-bucket". The use of EC2 client was needed to download the confluent.io Amazon s3 connector and then copying it to the S3 bucket. Then the creation of the custom plugin had to be done by using the MSK connect. The use " <your_UserId>-plugin" was needed. Once it was all done it allowed me to move onto the connector creation. The kafka topics that was done in in the configuriation of the EC2 client was needed by using regex. Which is a form of filtering in a string as I created 3 topics this needed to be used with "user id.*" . Once thats done the user would have to check on the IAM role to access permissions and making sure the right EC2 role is chosen. Then the connector was created. 

This is what the final outcome should be showing like so ![Alt text]([image link](https://ibb.co/bHgb4M6)https://ibb.co/bHgb4M6)


## Batch Processing - Configure the API in API Gateway

API Gateway -  Amazon API Gateway is an AWS service that allows the creation, maintenance and securing of scalable REST, HTTP and Websocket APIs. APIs can be created to access AWS services and other web services or data stored in the AWS Cloud. As a developer, you can use the service to create APIs that serve your client's applications or that are available to third-party app developers. There is three types of API's which are REST and HTTPS API. Rest API's are favoured than HTTP due to the latency is better. However with HTTPS this type of API was created by Amazon in 2019 and it does not offer as many features as REST APIs, and it only has regional endpoint support on AWS. This particular part of the project focused on using an intergration of a REST API due to the benefits it had such as the security and the regional support.

The use of API with using kafka was done by creation of the PROXY intergration. Secondly the resource when it was made by creating a HTTP ANY method which will be shown below. The correct PublicDNS had to be added from the EC2 then this allowed the deployment of the API to be done and the Invork URL to be extracted. Then the installation of the confluent package had to be installed in the Kafka EC2 client which could allow  the REST proxy to perform IAM authentication to the MSK cluster by modifying the kafka-rest.properties file by using nano. Leading to the REST proxy to be started. For the user to send data to the API. The modification of the file of the batch.py had to be done by using the Invoke URL that was done earlier it can be used to send data to your Kafka topics. The final response should be "200" for the status code.

This is what the final outcome should be showing like so ![Alt text]([image link](https://rb.gy/3563dl)https://rb.gy/3563dl)


## Batch Processing - Databricks
Databricks is built upon Apache Spark, a powerful open-source distributed computing system that enables parallel processing of large datasets. Spark provides a unified analytics engine for big data processing, offering high-level APIs in multiple programming languages like Scala, Python, and SQL. This integration with Spark allows the platform to facilitate the creation, deployment, and maintenance of enterprise-grade data solutions.

The Databricks Lakehouse Platform is a powerful solution for managing data at scale, offering a comprehensive environment that goes beyond data storage.  A Data Lake is a storage system that allows for the ingestion of large amounts of data without predefined structures. It provides flexibility, enabling storage of data in its raw format, making it suitable for a variety of data types. A Data Warehouse is a structured, high-performance database optimized for analytical queries. Unlike a Data Lake, it requires predefined schemas, organizing data into tables.

For data to be ran  entails the data to be queried from the post emulation script, also to add don’t have the running post script on while running data bricks as the table of rows will not be the same for when the databricks is ran. Kafka REST proxy should be ran in the terminal along side databricks to allow the same rows of the table to be the same for each data from in being 'user', 'pin' and 'geo'. 

This is what the final outcome should be showing like so ![Alt text]([image link](https://rb.gy/1qbed4)[https://rb.gy/1qbed4)

## Batch Processing - Spark on Databricks
Apache Spark, an open-source analytics engine, is proficient in managing extensive data workloads, including both batch and real-time analytics, and data processing tasks.

Cleaning the dataframes for pinterest posts,geolocation and users had to be done. Knowing which dataframes to join to and when to aggregrate and not is an important factor as certain syntax's allowed different schemas to be shown. The user can go through the "pinterest-data-pipeline" to see the different results that was achieved. 

A final outcome will be shown for example finding the most follower account depending on the age group and joining year, the extraction of the date joined was needed to be achieved
to obtain post_year.  ![Alt text]([image link](https://ibb.co/0204rcL)

## Batch Processing - AWS MWAA
AWS MWAA - Apache Airflow is a tool used to schedule and monitor different sequences of processes and tasks, referred to as workflows. The features that are 

Automatic setup: Allows for quick configuration where users can select the desired version of Apache Airflow when creating an MWAA environment.

Automatic scaling: Automatically adjusts the number of Airflow workers within set minimum and maximum thresholds based on workload demand. Workers are dynamically added or removed until the maximum limit is reached.

Integrated authentication and authorization via IAM and single sign-on (SSO). A SSO is s an authentication process that allows users to access multiple applications or services using a single set of login credentials (such as username and password).

Inherent security: Airflow workers and schedulers operate within MWAA's virtual private cloud (VPC), ensuring data encryption and default security measures.

Workflow monitoring: Utilizes AWS CloudWatch to monitor logs and metrics, facilitating the identification of errors or delays within workflows. 

By using a DAG, by uploading the file that was created in an MWAA enviroment in the S3 bucket the file "121d2a86d1ab_dag.py" can be viewed. This was done to allow the DAG to be ran daily via the pinterest_pipeline notebook in databricks. 

This is what the outcome should be for when the DAG is scheduled ![Alt text]([image link](https://ibb.co/DtJ5b1m)

When the DAG has succeeded it will look like this image shown ![Alt text]([image link](https://ibb.co/GkWkhPx)


## Stream Processing - AWS Kinesis
AWS Kinesis can collect streaming data such as event logs, social media feeds, application data, and IoT sensor data in real time or near real-time. Kinesis enables you to process and analyze this data as soon as it arrives, allowing you to respond instantly and gain timely analytics insights. Kinesis utilises four main services 

1) Kinesis Video Streams: a service used for stream processing of binary-encoded data, such as audio and video.
2) Kinesis Data Streams: a serverless streaming data service that makes it easy to capture, process, and store data streams.
3) Kinesis Data Firehose: an extract, transform, and load (ETL) service that captures, transforms, and delivers streaming data to data lakes, data stores, and analytics services.
4) Kinesis Data Analytics: a service that enables you to use SQL code to continuously read, process, and store data in near real time.

The utilisation of data streams was needed due to its nature of being a highly customizable AWS streaming solution. Highly customizable means that all parts involved with stream processing, such as data ingestion.

The first step was to create streams using the username each with each dataframe connoation as an example "streaming-<your_UserId>-pin". Then a rest API had to be created the API involved create,delete and describe streams.

The rest API will look like this ![Alt text]([image link](https://ibb.co/dmsHKnq)

Sending data to kinesis the script had to be created that was built upon the user_posting_emulation that is attached in this repo but in a seperate file known as user_streaming_emulation_1st_april.py. This allowed you to be able to send requests to the API adding one record at a time for the streams created.

Data had to be read from the streams this was utilised by using Databricks, to see the final outcome the user can look at the "Kinesis to DB" that is attached to the reporisity, the data was also transformed using cleaning methods.

Finally the streams were written in the "<your_UserId>_user_table" per stream examples will be shown below for each stream. 

![Alt text]([image link](https://ibb.co/3FJptWc) 

![Alt text]([image link](https://ibb.co/qyzJJK3)

![Alt text]([image link](https://ibb.co/GJ0nxqZ)
