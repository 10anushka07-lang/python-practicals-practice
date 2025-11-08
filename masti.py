import cv2
from pyzbar import pyzbar

def decode(frame):
    decoded_objects = pyzbar.decode(frame)
    for obj in decoded_objects:
        # Draw rectangle
        cv2.rectangle(frame, (obj.rect.left, obj.rect.top),
                      (obj.rect.left + obj.rect.width, obj.rect.top + obj.rect.height),
                      (0, 255, 0), 2)
        # Display data
        data = obj.data.decode("utf-8")
        type_ = obj.type
        cv2.putText(frame, f'{data} ({type_})', 
                    (obj.rect.left, obj.rect.top - 10), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        print(f'Detected {type_}: {data}')
    return frame

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame = decode(frame)
    cv2.imshow('QR/Barcode Scanner', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
