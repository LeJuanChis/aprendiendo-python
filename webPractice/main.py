from flask import Flask, render_template
import cv2

vid = cv2.VideoCapture(0)

app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():

    while (True):
        res, frame = vid.read()
        cv2.rectangle(frame, (100, 100), (200, 200), (255, 0, 0), 2)

        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xff == ord('q'):
            break

        vid.release()
        cv2.destroyAllWindows()
    return render_template("index.html")

if __name__ == '__main__':
    app.run(port = 5990, debug=True)
