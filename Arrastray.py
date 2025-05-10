import cv2
import mediapipe as mp
import serial
import time


arduino = serial.Serial('COM3', 9600)  
time.sleep(2)  


mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils


cap = cv2.VideoCapture(0)
prev_finger_count = -1


finger_tips = [4, 8, 12, 16, 20]

def contar_dedos(hand_landmarks):
    dedos = []

    
    if hand_landmarks.landmark[finger_tips[0]].x < hand_landmarks.landmark[finger_tips[0] - 1].x:
        dedos.append(1)
    else:
        dedos.append(0)

    
    for tip in finger_tips[1:]:
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip - 2].y:
            dedos.append(1)
        else:
            dedos.append(0)

    return sum(dedos)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            count = contar_dedos(hand_landmarks)

            
            if count != prev_finger_count:
                print(f"Dedos levantados: {count}")
                arduino.write(str(count).encode())
                prev_finger_count = count

            cv2.putText(frame, f"Dedos: {count}", (10, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 0, 0), 3)

    cv2.imshow("Arrastrar y soltar con una mano", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

arduino.close()
cap.release()
cv2.destroyAllWindows()
