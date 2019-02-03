# Description

Simple python program to list and return items from a DynamoDB table.

# Packaging

Clone the repository and zip its content
```
cd py-aws-lambda-db-list-items
zip -r ../py-aws-lambda-db-list-items.zip .
```

# Installation & Usage 

Connect to AWS console and create a Lambda having this properties:
   - Runtime: `Python 3.6`
   - Role:
```
Allow: logs:CreateLogGroup
Allow: logs:CreateLogStream
Allow: logs:PutLogEvents
Allow: dynamodb:*

Resource: *
```
   - Environment variables: 
     - Add an environment variable named `dynamodbTableName` and containing the DynamoDB table name from where to get the items

Deploy the function code by uploading the zip package.
