

from flask import Flask, render_template, request, redirect, url_for
import os, json, boto3

app = Flask(__name__)

@app.route("/")
def index():
  return render_template('html.html')

@app.route('/presign/')
def presign():
  # Load necessary information into the application
  S3_BUCKET = os.environ.get('BUCKET')

  # Load required data from the request
  file_name = request.args.get('file-name')
  file_type = request.args.get('file-type')

  # Initialise the S3 client
  s3 = boto3.client('s3')

  # Generate and return the presigned URL
  presigned_post = s3.generate_presigned_post(
    Bucket = S3_BUCKET,
    Key = file_name,
    Fields = {"acl": "public-read", "Content-Type": file_type},
    Conditions = [
      {"acl": "public-read"},
      {"Content-Type": file_type}
    ],
    ExpiresIn = 3600
  )

  # Return the data to the client
  return json.dumps({
    'data': presigned_post,
    'url': 'https://%s.s3.amazonaws.com/%s' % (S3_BUCKET, file_name)
  })


if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5000))
  app.run(host='0.0.0.0', port = port)
