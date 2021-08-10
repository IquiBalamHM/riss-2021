from Camera import *

print ("Starting...")
camera = Camera(selection="Intel")
try:
    while True:

        sucess,frame = camera.getFrame()
        if not sucess:
            continue    

        # Show images
        cv2.namedWindow('RealSense', cv2.WINDOW_AUTOSIZE)
        cv2.imshow('RealSense', frame)
        cv2.waitKey(1)

finally:
    # Stop streaming
    camera.stop()    
# loop over the boundaries
print ("Ending...")
