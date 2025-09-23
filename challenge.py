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

            # Desenha retângulo e centro
            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.circle(image, (center_x, center_y), 5, (0, 0, 255), -1)
            cv2.putText(image, f"Moto ({center_x}, {center_y})", (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

    return image, motorcycles


def salvar_deteccoes(motos, results, arquivo="detecoes.csv"):
   
    with open(arquivo, mode="a", newline="") as f:
        writer = csv.writer(f)
        for *box, conf, cls in results.xyxy[0]:
            class_name = model.names[int(cls)]
            if class_name == TARGET_CLASS:
                x1, y1, x2, y2 = map(int, box)
                center_x = (x1 + x2) // 2
                center_y = (y1 + y2) // 2
                writer.writerow([datetime.now(), class_name, float(conf), center_x, center_y])

image_path = 'patio.jpg'   
image = cv2.imread(image_path)
results = model(image)
output_image, motos_posicoes = draw_motorcycles(image, results)

salvar_deteccoes(motos_posicoes, results)
print("Detecções salvas em detecoes.csv")
cv2.imshow("Deteccao de Motos", output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
