# Projeto: Dashboard de Detecção de Motocicletas com YOLOv5 e Flask

## 📖 Descrição
1.  Detectar motocicletas em um fluxo de vídeo em tempo real.
2.  Exibir as detecções em um dashboard web amigável.
3.  Simular o envio de dados estruturados para um backend.
4.  Persistir todas as detecções em um arquivo CSV para análise futura.

## ✨ Features
* **Dashboard em Tempo Real:** Interface web construída com Flask que transmite o vídeo processado diretamente para o navegador.
* **Simulação de Backend:** A cada detecção, os dados são impressos no console do servidor, simulando o recebimento por um endpoint de API.
* **Persistência de Dados:** Todas as detecções são salvas de forma estruturada em um arquivo `detecoes.csv`, incluindo timestamp, confiança e coordenadas.
* **Setup Simplificado:** O script gera automaticamente o arquivo HTML necessário para o dashboard, simplificando a configuração.

## 🛠️ Tecnologias Utilizadas
[cite_start]O projeto foi construído utilizando as seguintes tecnologias[cite: 26]:
* **Linguagem:** Python 3
* **Framework Web:** Flask
* [cite_start]**Modelo de IA:** YOLOv5 (da Ultralytics) para detecção de objetos[cite: 13].
* **Bibliotecas Principais:**
    * **OpenCV:** Para manipulação de vídeo e imagens.
    * **PyTorch:** Para carregar e executar o modelo YOLOv5.
    * **CSV:** Para a persistência dos dados.

## 🚀 Instruções de Uso
[cite_start]Siga os passos abaixo para configurar e executar o projeto em seu ambiente local[cite: 26].

**1. Clonar o Repositório**
```bash
# Clone este repositório para a sua máquina local
git clone [https://github.com/Felipafaa/iot-main.git](https://github.com/Felipafaa/iot-main.git)
cd seu-repositorio
```

**2. Instalar as Dependências**
É altamente recomendado criar um ambiente virtual (`venv`). Depois, instale as bibliotecas a partir do arquivo `requirements.txt`.
```bash
# Crie e ative um ambiente virtual (Opcional, mas recomendado)
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate

# Instale as dependências
pip install -r requirements.txt
```
*(Se não tiver o arquivo `requirements.txt`, crie-o com `pip freeze > requirements.txt` após instalar as bibliotecas manualmente: `pip install Flask torch opencv-python numpy`)*

**3. Configurar a Fonte de Vídeo**
Abra o arquivo principal (`app.py` ou `challenge.py`) e altere a variável `VIDEO_SOURCE` para a fonte desejada:
```python
# Use 0 para a webcam ou o caminho para um arquivo de vídeo
VIDEO_SOURCE = 'seu_video.mp4'  # <-- MUDE AQUI
```

**4. Executar a Aplicação**
Com tudo configurado, inicie o servidor Flask:
```bash
python app.py
```

**5. Acessar o Dashboard**
Abra seu navegador e acesse o seguinte endereço:
[http://127.0.0.1:5000](http://127.0.0.1:5000)

## ✅ Resultados Parciais
[cite_start]Ao executar o projeto, você observará três saídas simultâneas, cumprindo todos os requisitos[cite: 26]:

1.  **Dashboard Web:** No seu navegador, o vídeo será exibido com as detecções em tempo real.
2.  **Console (Simulação de Backend):** No terminal onde você executou o script, mensagens estruturadas de cada detecção serão impressas.
3.  **Arquivo `detecoes.csv`:** Na pasta do projeto, o arquivo CSV será criado e populado com os dados de todas as motocicletas detectadas.
