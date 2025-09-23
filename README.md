# Projeto: Detecção de Motocicletas em Tempo Real com YOLOv5

## 📖 Descrição
[cite_start]Este projeto foi desenvolvido para o Challenge da disciplina **DISRUPTIVE ARCHITECTURES: IOT, IOB & GENERATIVE IA** da FIAP[cite: 2]. [cite_start]A solução implementa um sistema de Visão Computacional capaz de detectar motocicletas em um fluxo de vídeo em tempo real[cite: 13]. [cite_start]As detecções são destacadas visualmente na tela e todos os dados relevantes são salvos em um arquivo CSV para persistência e análise posterior[cite: 10, 13].

## 🛠️ Tecnologias Utilizadas
O projeto foi construído utilizando as seguintes tecnologias:

* **Linguagem:** Python 3
* **Modelo de IA:** YOLOv5 (da Ultralytics) para detecção de objetos.
* **Bibliotecas Principais:**
    * **PyTorch:** Framework utilizado para carregar e executar o modelo YOLOv5.
    * **OpenCV (cv2):** Essencial para a manipulação de vídeo, captura de quadros e desenho das detecções na tela.
    * **NumPy:** Utilizada para operações numéricas eficientes.

## 🚀 Instruções de Uso

Siga os passos abaixo para configurar e executar o projeto em seu ambiente local.

**1. Clonar o Repositório**
```bash
# Clone este repositório para a sua máquina local
git clone [https://github.com/Felipafaa/iot-main.git](https://github.com/Felipafaa/iot-main.git)
cd seu-repositorio
```

**2. Instalar as Dependências**
É altamente recomendado criar um ambiente virtual (`venv`) para isolar as dependências do projeto.
```bash
# Crie um ambiente virtual (opcional, mas recomendado)
python -m venv venv
source venv/bin/activate  # No Windows, use: venv\Scripts\activate

# Instale as bibliotecas necessárias a partir do arquivo requirements.txt
pip install -r requirements.txt
```
*Observação: Caso não tenha um arquivo `requirements.txt`, você pode criá-lo com `pip freeze > requirements.txt` após instalar as bibliotecas manualmente (`pip install torch opencv-python numpy`).*

**3. Configurar a Fonte de Vídeo**
Abra o arquivo de script (`detector_motos.py`) e altere a variável `VIDEO_SOURCE` para a fonte desejada:
```python

VIDEO_SOURCE = 'video_exemplo.mp4'  # <-- MUDE AQUI
```

**4. Executar o Script**
Com as dependências instaladas e a fonte de vídeo configurada, execute o script:
```bash
python detector_motos.py
```

## ✅ Resultados Esperados
Ao executar o script, você terá duas saídas, conforme os requisitos do projeto:

1.  [cite_start]**Output Visual em Tempo Real:** Uma janela será aberta, exibindo o vídeo com as motocicletas detectadas sendo destacadas por retângulos verdes e com o ponto central marcado[cite: 13].
2.  **Persistência de Dados:** Um arquivo chamado `detecoes.csv` será criado (ou atualizado) na pasta do projeto. [cite_start]Este arquivo registrará cada detecção com `Timestamp`, `Classe`, `Confiança` e as coordenadas `X` e `Y` do centro do objeto[cite: 10].

![Exemplo de Detecção](https://i.imgur.com/link-para-sua-imagem.png)