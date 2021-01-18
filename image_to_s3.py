from flask import Flask, render_template, request
import boto3
from werkzeug.utils import secure_filename
import key_config as keys

s3 = boto3.client('s3',
                    aws_access_key_id='access key here',
                    aws_secret_access_key= 'secret key here',
                    aws_session_token='key_config'
                    aws_session_token='k'
                     )
BUCKET_NAME='frv1'