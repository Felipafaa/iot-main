# 1. Imagem Base: Começamos com uma imagem Python oficial
FROM python:3.10-slim

# 2. Instalar Dependências do Sistema
# O OpenCV precisa de algumas bibliotecas do Linux para funcionar
# *** ALTERAÇÃO AQUI: Trocamos 'libgl1-mesa-glx' por 'libgl1' ***
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# 3. Preparar o Ambiente
WORKDIR /app
COPY requirements.txt .

# 4. Instalar Dependências Python
# Usamos --no-cache-dir para manter a imagem menor
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copiar seu Código
# Copia tudo (app.py, seu_video.mp4, etc.) para dentro do container
COPY . .

# 6. Expor a Porta
# Informa ao Docker que a aplicação roda na porta 5000 (padrão do Flask)
EXPOSE 5000

# 7. Comando para Rodar
# Inicia sua aplicação. 
# O '--host=0.0.0.0' é OBRIGATÓRIO para que o Flask seja acessível
# fora do container.
CMD ["python", "challenge.py"]
