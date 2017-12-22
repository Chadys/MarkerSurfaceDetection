import yaml
import os
import cv2
from cv2 import aruco
import numpy as np

# calibrationFile = "calibration.yaml"
# calibrationParams = cv2.FileStorage(calibrationFile, cv2.FILE_STORAGE_READ)
# camera_matrix = calibrationParams.getNode("cameraMatrix").mat()
# dist_coeffs = calibrationParams.getNode("distCoeffs").mat()
# If doesn't work
with open('calibration.yaml') as f:
    loadeddict = yaml.load(f)
camera_matrix = np.asarray(loadeddict.get('cameraMatrix'))
dist_coeffs = np.asarray(loadeddict.get('distCoeffs'))

aruco_dict = aruco.getPredefinedDictionary( aruco.DICT_6X6_1000 )
markerLength = 40   # Here, our measurement unit is centimetre.
markerSeparation = 8   # Here, our measurement unit is centimetre.
board = aruco.GridBoard_create(5, 7, markerLength, markerSeparation, aruco_dict)
arucoParams = aruco.DetectorParameters_create()



cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read() # Capture frame-by-frame
    if ret == True:
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # aruco.detectMarkers() requires gray image

        corners, ids, rejectedImgPoints = aruco.detectMarkers(frame_gray, aruco_dict, parameters=arucoParams)  # First, detect markers
        aruco.refineDetectedMarkers(frame_gray, board, corners, ids, rejectedImgPoints)

        if ids is not None: # if there is at least one marker detected
            im_with_aruco_board = aruco.drawDetectedMarkers(frame, corners, ids, (0,255,0))
            retval, rvec, tvec = aruco.estimatePoseBoard(corners, ids, board, camera_matrix, dist_coeffs)  # posture estimation from a aruco board
            if retval != 0:
                im_with_aruco_board = aruco.drawAxis(im_with_aruco_board, camera_matrix, dist_coeffs, rvec, tvec, 100)  # axis length 100 can be changed according to your requirement
        else:
            im_with_aruco_board = frame

        cv2.imshow("arucoboard", im_with_aruco_board)

        if cv2.waitKey(2) & 0xFF == ord('q'):
            break
    else:
        break


cap.release()   # When everything done, release the capture
cv2.destroyAllWindows()