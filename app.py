from flask import Flask
from flask import request, jsonify
import cv2
import boto3

app = Flask(__name__)

@app.route('/LiveCapture', methods=['POST'])
def capture():
	s3 = boto3.resource("s3")
	videoCaptureObject = cv2.VideoCapture(-1)
	result = True
	while(result):
		ret,frame = videoCaptureObject.read()
		img_str = cv2.imencode('.jpg', frame)[1].tobytes()
		s3.Object('livecapture-image','NewPicture.jpg').put(Body = img_str)
		result = False
	videoCaptureObject.release()
	cv2.destroyAllWindows()
	return "Image Captured and Uploaded to livecapture-image S3 Bucket"

if __name__ == "__main__":
	app.run(debug=True)


