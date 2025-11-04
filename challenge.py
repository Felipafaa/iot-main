import cv2
import torch
from datetime import datetime
from flask import Flask, render_template, Response
import os
import csv 


app = Flask(__name__)


model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
TARGET_CLASS = 'motorcycle'


VIDEO_SOURCE = 'ssstik.io_@sobrerodasbrofc_1758598609723.mp4' 

def processar_frames():
    cap = cv2.VideoCapture(VIDEO_SOURCE)
    if not cap.isOpened():
        print(f"Erro ao abrir o vídeo: {VIDEO_SOURCE}")
        return
    
    # --- ALTERAÇÃO 1: Caminho do CSV ---
    # Aponta para o disco persistente que será montado no Azure
    arquivo_csv = "/mnt/data/detecoes.csv"
    
    # Garante que o diretório de montagem existe antes de tentar escrever
    os.makedirs(os.path.dirname(arquivo_csv), exist_ok=True)
    
    with open(arquivo_csv, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        
    
        f.seek(0, 2)
        if f.tell() == 0:
            writer.writerow(["Timestamp", "Classe", "Confianca", "Centro_X", "Centro_Y"])
        
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            results = model(frame)
            for *box, conf, cls in results.xyxy[0]:
                class_name = model.names[int(cls)]
                if class_name == TARGET_CLASS and float(conf) > 0.5:
                    x1, y1, x2, y2 = map(int, box)
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.putText(frame, f"{class_name} {conf:.2f}", (x1, y1 - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                    
                    center_x = (x1 + x2) // 2
                    center_y = (y1 + y2) // 2
                    
                    print(f"[BACKEND SIMULADO] Detecção recebida: Timestamp={datetime.now().isoformat()}, X={center_x}, Y={center_y}")

                
                    timestamp = datetime.now().isoformat()
                    writer.writerow([timestamp, class_name, f"{float(conf):.2f}", center_x, center_y])

            (flag, encodedImage) = cv2.imencode(".jpg", frame)
            if not flag:
                continue
            
            yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + 
                  bytearray(encodedImage) + b'\r\n')
    cap.release()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(processar_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    html_template = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Dashboard de Detecção de Motos</title>
        <style>
            body { font-family: Arial, sans-serif; text-align: center; background-color: #f0f0f0; }
            h1 { color: #333; }
            img { border: 2px solid #333; margin-top: 20px; max-width: 80%; }
        </style>
    </head>
    <body>
        <h1>Dashboard - Detecção de Motos em Tempo Real</h1>
        <img src="{{ url_for('video_feed') }}">
    </body>
    </html>
    """
    if not os.path.exists('templates'):
        os.makedirs('templates')
    with open('templates/index.html', 'w', encoding='utf-8') as f:
        f.write(html_template)
    
    # --- ALTERAÇÃO 2: Configuração do Servidor ---
    # 'host=0.0.0.0' é obrigatório para o Azure acessar o app dentro do container
    # 'debug=False' é a prática correta para produção
    app.run(debug=False, host='0.0.0.0', port=5000)
