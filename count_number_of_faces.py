import cv2
import numpy as np
import dlib

# dlib install on the windows 
# and the file or get tne info from  web

# Open the default camera to capture
# faces and use the dlib library 
# to get coordinates.
# (0) in VideoCapture() is used to
# connect to your computer's deafult camera
cap = cv2.VideoCapture(0)
# Get the coordiantes
detector = dlib.get_frontal_face_detector()

# count the number of faces
# Capture the frames contiously
# Convert the farmes to grayscale(not necessary)
# Take an iterator i and initialize it to zero
# Each time you get the coordinates to the face
# structure in the frame, increment the iterator by 1.
# Plot the bix around each detected face along
# with its face count

while True:
	# Capture frame-by-frame
	ret, frame = cap.read()
	frame = cv2.flip(frame, 1)

	# Our operation on the frame come here
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	faces = detector(gray)

	# Counter to count number of faces
	i = 0

	for faces in faces:
		x, y = face.left(), face.top()
		x1, y1 = face.right(), face.bottom()
		cv2.rectangle(frame, (x, y), (x1, y1), (0, 255, 0), 2)

		# Increment the iterator each time you get the coordinates.
		i = i + 1

		# Adding the faces number to the box detecting faces
		cv2.putText(frame, 'face num'+str(i), (x-10, y-10),
			cv2.FRONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
		print(face, i)

		# Display the resulting frame
		cv2.imshow('frame', frame)

# Enter kry 'q' to break the loop
if cv2.waitKey(1) & 0xFF == ord('q'):
	break

# When everything done, release
# the capture and destroy the windows
cap.release()
cv2.destroyAllWindows()

# we are ** done anf we need dlib and run the program