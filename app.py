from flask import Flask, render_template, Response, send_from_directory
import cv2

app = Flask(__name__, static_folder='static')
camera = cv2.VideoCapture(0)

def generate_frames():
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cam')
def videostream():
    return render_template('video.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/static/buttons.js')
def serve_js():
    return send_from_directory('static', 'buttons.js')

#Definição da Rota Video Feed   
@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
    #Respose no flask são respostas personalizadas para o Servidor, em Formato HTTP


if __name__ == '__main__':
    app.run(debug=True )
