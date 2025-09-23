import cv2
import torch
import numpy as np
import csv
from datetime import datetime

model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
TARGET_CLASS = 'motorcycle'
def draw_motorcycles(image, results):
    motorcycles = []

    for *box, conf, cls in results.xyxy[0]:
        class_name = model.names[int(cls)]
        if class_name == TARGET_CLASS:
            x1, y1, x2, y2 = map(int, box)
            center_x = (x1 + x2) // 2
            center_y = (y1 + y2) // 2

            motorcycles.append((center_x, center_y))

            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.circle(image, (center_x, center_y), 5, (0, 0, 255), -1)
            cv2.putText(image, f"Moto ({center_x}, {center_y})", (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

    return image, motorcycles


def salvar_deteccoes_frame(csv_writer, results, target_class_name):
    """
    Itera sobre os resultados e escreve as detecções de motos no CSV.
    """
    for *box, conf, cls in results.xyxy[0]:
        class_name = model.names[int(cls)]
        if class_name == target_class_name:
            x1, y1, x2, y2 = map(int, box)
            center_x = (x1 + x2) // 2
            center_y = (y1 + y2) // 2
            
            
            csv_writer.writerow([datetime.now(), class_name, float(conf), center_x, center_y])


VIDEO_SOURCE = 'ssstik.io_@sobrerodasbrofc_1758598609723.mp4'
cap = cv2.VideoCapture(VIDEO_SOURCE)

if not cap.isOpened():
    print(f"Erro ao abrir o vídeo: {VIDEO_SOURCE}")
    exit()

arquivo_csv = "detecoes.csv"

with open(arquivo_csv, mode="a", newline="", encoding="utf-8") as f:
    
    writer = csv.writer(f)
    f.seek(0, 2)
    if f.tell() == 0:
        writer.writerow(["Timestamp", "Classe", "Confianca", "Centro_X", "Centro_Y"])

    print("Processando vídeo... Pressione 'q' na janela para sair.") 
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Fim do vídeo ou erro na captura.")
            break
        results = model(frame)
       
        output_image, motos_posicoes = draw_motorcycles(frame, results)
        
    
        salvar_deteccoes_frame(writer, results, TARGET_CLASS)
    
        cv2.imshow("Deteccao de Motos em Tempo Real", output_image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()
print(f"Processamento concluído. Detecções salvas em {arquivo_csv}")