import cv2

# histogram equalization
def histogram_equalization(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    equalized = cv2.equalizeHist(gray)
    return cv2.cvtColor(equalized, cv2.COLOR_GRAY2BGR)

# smooth_filter
def smooth_filter(frame):
    #smooth = cv2.blur(frame, (5,5))
    smooth = cv2.GaussianBlur(frame, (5,5), 0)
    return smooth

# 5x5 unsharp filter
def unsharp_filter(frame):
    blurred = cv2.GaussianBlur(frame, (5,5), 0)
    return cv2.addWeighted(frame, 1.5, blurred, -0.5, 0)

# edge detector filter
def edge_detector(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 200)
    return cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

# initialize video capture
cap = cv2.VideoCapture(0)

# create windows
cv2.namedWindow('Original Frame', cv2.WINDOW_NORMAL)
cv2.namedWindow('Filtered Frame', cv2.WINDOW_NORMAL)

# set initial filter to None
current_filter = None

while True:
    # rread a frame from the video feed
    ret, frame = cap.read()

    # check if frame was successfully read
    if not ret:
        break

    # apply the filter
    if current_filter == 'h':
        filtered_frame = histogram_equalization(frame)
    elif current_filter == 's':
        filtered_frame = smooth_filter(frame)
    elif current_filter == 'u':
        filtered_frame = unsharp_filter(frame)
    elif current_filter == 'e':
        filtered_frame = edge_detector(frame)
    else:
        filtered_frame = frame

    # display frames
    combined_frame = cv2.hconcat([frame, filtered_frame])
    cv2.imshow('Original Frame', combined_frame)

    # take in character input
    key = cv2.waitKey(1)
    if key == ord('h'):
        current_filter = 'h'
    elif key == ord('s'):
        current_filter = 's'
    elif key == ord('u'):
        current_filter = 'u'
    elif key == ord('e'):
        current_filter = 'e'
    elif key == ord('q'):
        break

# release video capture and close windows
cap.release()
cv2.destroyAllWindows()