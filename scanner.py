import os
import sys
import cv2
import numpy as np
from pyzbar.pyzbar import decode
import contextlib

# Hide ZBar warning messages
@contextlib.contextmanager
def hide_warnings():
    with open(os.devnull, 'w') as f:
        old = sys.stderr
        sys.stderr = f
        try:
            yield
        finally:
            sys.stderr = old

cap = cv2.VideoCapture(0)
print("📸 QR Scanner Started. Press 'q' to quit.")

while True:
    success, frame = cap.read()

    if not success:
        print("❌ Can't access webcam.")
        break

    with hide_warnings():  # Hide ZBar warnings
        codes = decode(frame)

    for code in codes:
        data = code.data.decode('utf-8')
        print("✅ QR Code Found:", data)

        points = code.polygon
        if points:
            pts = [(point.x, point.y) for point in points]
            cv2.polylines(frame, [np.array(pts, dtype=np.int32)], True, (0, 255, 0), 2)

    cv2.imshow("QR Scanner", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()            # where to put the code