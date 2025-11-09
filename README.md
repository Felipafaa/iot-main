## 📋 Entrega da Sprint 4 - Quality Assurance & Tests

Conforme solicitado, seguem os links obrigatórios para a avaliação da Sprint 4:

* **Repositório GitHub:** (https://github.com/Felipafaa/iot-main.git)
* **Plano de Testes (Azure DevOps):** (https://dev.azure.com/RM557636/MotoMap%20-%20P%C3%A1tio%20Inteligente%20Mottu/_testPlans/define?planId=39&suiteId=42)
* **Vídeo de Execução dos Testes Automatizados:** (https://youtu.be/wRdappj_7NM)

---






# Projeto: Dashboard de Detecção de Motocicletas com YOLOv5 e Deploy no Azure

## 🚀 Resultado Final (Deploy em Nuvem)

A aplicação está em execução na nuvem Microsoft Azure e pode ser acedida aqui:




**seu-app-iot-fiap-f0hgg6dsd3g4epck.brazilsouth-01.azurewebsites.net** 

## 📖 Descrição

Este projeto detecta motocicletas num fluxo de vídeo em tempo real e exibe as deteções num dashboard web amigável.

Esta solução foi desenvolvida para o Challenge da FIAP, com foco especial na integração entre **Visão Computacional (IoT)**, **DevOps** e **Cloud**.

As funcionalidades incluem:

* **Dashboard em Tempo Real:** Interface web construída com Flask que transmite o vídeo processado.

* **Simulação de Backend:** A cada deteção, os dados são impressos no console do servidor (visível no Log Stream do Azure).

* **Persistência de Dados na Nuvem:** Todas as deteções são salvas de forma estruturada e persistente num arquivo (`detecoes.csv`) no **Azure File Storage**, cumprindo o requisito de integração com "Banco de Dados".

## 🛠️ Tecnologias Utilizadas

O projeto foi construído utilizando as seguintes tecnologias, integrando múltiplas disciplinas:

### Aplicação (Core)

* **Linguagem:** Python 3.10

* **Framework Web:** Flask

* **Modelo de IA:** YOLOv5 (da Ultralytics)

* **Bibliotecas de Visão:** OpenCV, PyTorch, Pillow

* **Análise de Dados:** Pandas, Numpy

### DevOps & Cloud (Integração)

* **Containerização:** Docker

* **CI/CD:** GitHub Actions

* **Plataforma de Nuvem (PaaS):** Microsoft Azure

* **Serviço de Aplicação:** Azure App Service (para rodar o container)

* **Registro de Imagem:** Azure Container Registry (ACR)

* **Persistência de Dados:** Azure File Storage (para salvar o `.csv`)

## 🚀 Arquitetura da Solução (Fluxo DevOps)

A integração e entrega contínua (CI/CD) deste projeto segue um fluxo profissional de DevOps:

1. **Commit/Push:** O desenvolvedor envia o código (`Dockerfile`, `challenge.py`, etc.) para a branch `main` do GitHub.

2. **CI (Build):** O **GitHub Actions** é acionado automaticamente. Ele constrói a imagem Docker com todas as dependências (PyTorch, OpenCV, Flask, etc.).

3. **Registro:** Após o build, o GitHub Actions envia (push) a imagem de container para o **Azure Container Registry (ACR)**.

4. **CD (Deploy):** O **Azure App Service** deteta que uma nova imagem (`:latest`) está disponível no ACR e automaticamente reinicia o serviço, baixando e executando o novo container.

5. **Persistência:** A aplicação em execução no App Service salva todas as deteções no caminho `/mnt/data/detecoes.csv`, que está mapeado para o **Azure File Storage**, garantindo que os dados não sejam perdidos.

## ✅ Resultados FINAIS

Ao aceder ao link do Azure, você observará os requisitos da entrega:

1. **Dashboard Web:** No navegador, o vídeo é exibido com as deteções em tempo real, servido diretamente pelo Azure.

2. **Console (Simulação de Backend):** No portal do Azure, o "Fluxo de Log" (Log Stream) do App Service mostra as mensagens estruturadas de cada deteção sendo impressas.

3. **Arquivo `detecoes.csv`:** No portal do Azure, dentro da "Conta de Armazenamento" (`seustorageiotfiap`), o arquivo CSV é populado em tempo real com os dados de todas as motocicletas detectadas.

## 🔧 Instruções de Uso (Local)

Embora o projeto esteja focado na nuvem, ele ainda pode ser executado localmente.

1. **Clonar o Repositório**



git clone https://github.com/Felipafaa/iot-main.git
cd iot-main


2. **Instalar as Dependências (com venv)**



Crie e ative um ambiente virtual

python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate

Instale as dependências

pip install -r requirements.txt


3. **Executar a Aplicação**



python challenge.py


4. **Acessar o Dashboard Local**
Abra seu navegador e acesse: `http://127.0.0.1:5000`
