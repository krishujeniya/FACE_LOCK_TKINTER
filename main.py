import threading
import tkinter as tk
from tkinter import simpledialog, messagebox
import cv2
import face_recognition
import os
import pyttsx3
import numpy as np
import time
import speech_recognition as sr


class FaceLockSystem(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Face Lock System")
        self.config(bg="gray")
        self.users = {}  # Dictionary to store user face encodings
        self.current_user = None  # Variable to store the current user
        self.add_face_button = tk.Button(self, text="Add Face", command=self.add_face,background="green",foreground="black",activebackground="black",activeforeground="green",font="Helvetica 12 bold")
        self.add_face_button.pack(pady=10)
        self.load_face_data_thread = threading.Thread(target=self.load_face_data)
        self.load_face_data_thread.start()
        # Start the face recognition thread
        self.start_unlock_device_thread()
        self.voice_button = tk.Button(self, text="Start Voice Recognition", command=self.start_voice_recognition,background="green",foreground="black",activebackground="black",activeforeground="green",font="Helvetica 12 bold")
        self.voice_button.pack(pady=10)

        self.mainloop()
    def start_voice_recognition(self):
        r=sr.Recognizer() 
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print("\nLts..")
            r.pause_threshold=1
            audio=r.listen(source)
        try:
            qu=r.recognize_google(audio,language="en-In")
            print("Ok!")
        except Exception as e:
            return ""
        self.speak(qu)



    def start_unlock_device_thread(self):
        self.stop_unlock_device_thread()  # Stop the existing thread if running
        self.face_recognition_thread = threading.Thread(target=self.unlock_device)
        self.face_recognition_thread.start()

    def stop_unlock_device_thread(self):
        if hasattr(self, 'face_recognition_thread') and self.face_recognition_thread.is_alive():
            self.face_recognition_thread.join()  # Wait for the thread to complete

    def add_face(self):
        username = simpledialog.askstring("Input", "Enter your username:")
        if username:
            self.capture_face_data(username)


    def capture_face_data(self, username):
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        cap = cv2.VideoCapture(0)

        face_encodings = []
        while len(face_encodings) < 100:
            ret, frame = cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
            for (x, y, w, h) in faces:
                face_encoding = face_recognition.face_encodings(frame, [(y, x + w, y + h, x)])[0]
                face_encodings.append(face_encoding)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.imshow('Face Data Collection', frame)
            cv2.waitKey(1)

        cap.release()
        cv2.destroyAllWindows()

        # Save face encodings
        os.makedirs("face_data", exist_ok=True)
        encoding_path = f"face_data/{username}_encoding.npy"
        with open(encoding_path, 'wb') as f:
            np.save(f, np.array(face_encodings))

        self.users[username] = encoding_path
        # Restart the unlock device thread after adding a new face
        self.start_unlock_device_thread()
        messagebox.showinfo("Information", f"Face data for {username} captured successfully!")

    def load_face_data(self):
        try:
            for file in os.listdir("face_data"):
                if file.endswith("_encoding.npy"):
                    username = file.split("_")[0]
                    encoding_path = os.path.join("face_data", file)
                    self.users[username] = encoding_path
        except:
            pass

    def unlock_device(self):
        cap = cv2.VideoCapture(0)
        start_time = time.time()  # Record the start time
        

        while True:
            ret, frame = cap.read()
            face_locations = face_recognition.face_locations(frame)
            face_encodings = face_recognition.face_encodings(frame, face_locations)

            for face_encoding in face_encodings:
                for username, encoding_path in self.users.items():
                    with open(encoding_path, 'rb') as f:
                        saved_encodings = np.load(f)
                    matches = face_recognition.compare_faces(saved_encodings, face_encoding)
                    if any(matches):
                        self.current_user = username
                        self.speak(f"Hey {username}!")
                        cap.release()
                        cv2.destroyAllWindows()
                        return

            elapsed_time = time.time() - start_time
            # If 5 seconds have passed and no recognized face is found, speak "Welcome buddy"
            if elapsed_time >= 5:
                self.speak("hey user!")
                cap.release()
                cv2.destroyAllWindows()
                return

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

    def speak(self, text):
        engine = pyttsx3.init()
        # Set properties (you can adjust these according to your preference)
        engine.setProperty('rate', 150)  # Speed of speech
        engine.setProperty('volume', 1)  # Volume (0.0 to 1.0)
        # Set female voice (adjust voice and variant based on your preferences)
        engine.setProperty('voice', 'en+f4')  # Set the desired voice here
        engine.say(text)
        engine.runAndWait()

if __name__ == "__main__":
    FaceLockSystem()
