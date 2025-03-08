# Chatbot Llama 3 com Ollama

Este projeto é um chatbot baseado no modelo **Llama 3**, utilizando **Ollama** como backend para execução local do modelo de IA. A interface foi desenvolvida com **Flask**, permitindo interação via navegador.

## 🚀 Funcionalidades
- Chatbot local com modelo **Llama 3** rodando via **Ollama**.
- Interface web simples para interagir com o chatbot.
- Configuração de API via variáveis de ambiente.
- Suporte a execução local e via Docker.

---

## 📋 Pré-requisitos

Antes de começar, instale os seguintes requisitos no seu sistema:

- **Python 3.10+**
- **pip** (gerenciador de pacotes do Python)
- **Docker** (opcional, caso queira rodar via container)
- **Ollama** (para rodar modelos LLM)

### Instalar Ollama
Se ainda não tiver o **Ollama**, instale-o:
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

Após a instalação, baixe o modelo **Llama 3**:
```bash
ollama pull llama3
```

---

## 📦 Instalação
### 1️⃣ Clonar o repositório
```bash
git clone https://github.com/seu-usuario/chatbot-llama.git
cd chatbot-llama
```

### 2️⃣ Criar e ativar o ambiente virtual
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate  # Windows
```

### 3️⃣ Instalar dependências
```bash
pip install -r requirements.txt
```

### 4️⃣ Configurar a URL da API Ollama
A API do Ollama deve estar rodando na porta padrão `11434`. Você pode definir a variável de ambiente `OLLAMA_API_URL` para apontar para a API do Ollama.

#### 📍 Opção 1: Definir variável de ambiente
```bash
export OLLAMA_API_URL="http://localhost:11434/v1/chat/completions"  # Linux/macOS
set OLLAMA_API_URL="http://localhost:11434/v1/chat/completions"  # Windows
```

#### 📍 Opção 2: Criar um arquivo `.env`
Crie um arquivo chamado **`.env`** na raiz do projeto e adicione:
```env
OLLAMA_API_URL=http://localhost:11434/v1/chat/completions
```

---

## ▶️ Execução do projeto

### Rodando localmente
Certifique-se de que o **Ollama** está rodando e execute:
```bash
python src/app.py
```
O chatbot estará acessível via navegador em: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🐳 Rodando via Docker
### 1️⃣ Construir a imagem Docker
```bash
docker build -t chatbot-llama .
```

### 2️⃣ Rodar o container
```bash
docker run -p 5000:5000 -e OLLAMA_API_URL="http://host.docker.internal:11434/v1/chat/completions" chatbot-llama
```

Acesse no navegador: [http://127.0.0.1:5000](http://127.0.0.1:5000)

⚠️ **Nota:** No Docker, use `http://host.docker.internal:11434/v1/chat/completions` para acessar o Ollama rodando no host.

---

### 🔄 Substituindo localhost pelo IP de um servidor Ollama remoto

Se você já possui um servidor Ollama rodando em outra máquina, basta substituir localhost pelo IP do servidor. Por exemplo:

export OLLAMA_API_URL="http://192.168.1.100:11434/v1/chat/completions"

Ou, se estiver usando Docker:

docker run -p 5000:5000 --env OLLAMA_API_URL="http://192.168.1.100:11434/v1/chat/completions" chatbot-llama

Isso permitirá que o chatbot se conecte a um servidor Ollama remoto, caso seu ambiente local não tenha capacidade suficiente para rodá-lo.

## 📝 Licença
Este projeto é open-source sob a licença MIT.

---

💡 **Autor:** [Marco Gomes](https://github.com/mgsantos89)

