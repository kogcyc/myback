

from flask import Flask, render_template, request
import os
import boto3
import json 

app = Flask(__name__)

@app.route("/")
def index():
	return render_template('html.html')

@app.route('/presign/')
def presign():
	boto_client = boto3.client('s3')

	bucket_name = os.environ.get('BUCKET')
	file_name = request.args.get('file-name')
	file_type = request.args.get('file-type')

	presigned_post = boto_client.generate_presigned_post(
		Bucket = bucket_name,
		Key = file_name,
		Fields = {"acl": "public-read", "Content-Type": file_type},
		Conditions = [
			{"acl": "public-read"},
			{"Content-Type": file_type}
		],
		ExpiresIn = 300
	)

	return json.dumps({
		'data': presigned_post
	})


