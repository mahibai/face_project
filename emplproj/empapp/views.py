from datetime import datetime
from django.shortcuts import render, HttpResponse
from django.db.models import Q
import time
from django.http import StreamingHttpResponse

from empapp.camera import IPWebCam, VideoCamera


# Create your views here.
#Display the 2 videos
def index(request):
    return render(request,'index.html')

#Every time you call the phone and laptop camera method gets frame
#More info found in camera.py
def gen(camera):
	while True:
		frame = camera.get_frame()
		yield (b'--frame\r\n'
				b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

#Method for laptop camera
def video_feed(request):
	return StreamingHttpResponse(gen(VideoCamera()),
                    #video type
					content_type='multipart/x-mixed-replace; boundary=frame')

#Method for phone camera
def webcam_feed(request):
	return StreamingHttpResponse(gen(IPWebCam()),
                    #video type
					content_type='multipart/x-mixed-replace; boundary=frame')