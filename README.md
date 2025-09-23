# Detector de Motocicletas

Felipe Rosa Peres rm 557636
Vinicius de Souza Santanna rm 556841
Pedro Henrique de Souza rm 555533

Este projeto utiliza YOLOv5 para detectar motocicletas em imagens e mostrar suas posições na tela.

## Requisitos

- Python 3.7 ou superior
- PyTorch
- OpenCV (cv2)
- NumPy

## Instalação

1. Clone este repositório ou baixe os arquivos

2. Instale as dependências necessárias:
```bash
python -m pip install --upgrade pip
python -m pip install torch torchvision torchaudio
python -m pip install opencv-python matplotlib
pip install numpy
```

## Como faz pra utilizar a aplicação

1. Certifique-se de que você tem uma imagem para testar (por padrão, o código procura por 'motos2.jpg' no mesmo diretório)

2. Execute o script principal:
no terminal utilize 

```
python challenge.py
```

3.Verifique se o caminho da imagem está correto 

```
#exemplo

image_path = 'patio.jpg'
image = cv2.imread(image_path)
```

## Funcionalidades

- Detecta motocicletas em imagens
- Desenha retângulos verdes ao redor das motocicletas detectadas
- Marca o centro de cada motocicleta com um círculo vermelho
- Mostra as coordenadas (x,y) de cada motocicleta detectada
- Exibe a imagem com as detecções em uma janela
- Imprime as posições das motocicletas no console

## Observações

- O modelo YOLOv5 será baixado automaticamente na primeira execução
- Para fechar a janela de visualização, pressione qualquer tecla
- Para usar uma imagem diferente, modifique o caminho da imagem no código (`image_path`) 