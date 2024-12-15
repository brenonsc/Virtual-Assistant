# Virtual Assistant

Este projeto é um assistente de voz simples desenvolvido em Python que utiliza reconhecimento de fala para interpretar comandos do usuário e responder com ações específicas, como buscar no YouTube ou Wikipedia, informar a hora atual ou encerrar a aplicação.
<br><br>

## Funcionalidades

- **Reconhecimento de voz**: Escuta comandos do usuário e processa utilizando a API do Google Speech Recognition.
- **Síntese de fala**: Responde ao usuário por meio de áudio gerado pela biblioteca gTTS.
- **Integração com YouTube**: Pesquisa vídeos no YouTube com base em comandos de voz.
- **Consulta à Wikipedia**: Busca informações na Wikipedia e retorna um resumo falado.
- **Informação de horário**: Responde com o horário atual.
- **Saída do programa**: Encerra a execução do assistente com o comando "exit".
<br>

## Pré-requisitos

- Python 3.6 ou superior
- Microfone conectado ao sistema
- Bibliotecas Python necessárias:
  - `speech_recognition`
  - `gTTS`
  - `playsound`
  - `wikipedia`
  - `pyaudio`
  - `webbrowser` (módulo padrão do Python)
<br>

## Instalação

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/brenonsc/Virtual-Assistant.git
   cd Virtual-Assistant
   ```

2. **Ative o seu Virtual Environment**

3. **Instale as dependências:**
   Certifique-se de ter o `pip` instalado e execute:

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure permissões para o microfone:**
   Garanta que o sistema tenha acesso ao microfone e que ele esteja funcionando corretamente.
<br>

## Uso

1. **Execute o script:**

   ```bash
   python3 virtual_assistant.py
   ```

2. **Diga um comando de voz:**

   - **"YouTube"**: O assistente solicitará o termo a ser pesquisado e abrirá os resultados no YouTube.
   - **"Wikipedia"**: O assistente solicitará o termo e lerá um resumo das informações obtidas na Wikipedia.
   - **"Que horas são"**: O assistente informará o horário atual.
   - **"Exit"**: Encerra o programa.
<br>

## Arquitetura

- **`get_audio()`**: Captura o áudio do microfone e converte em texto utilizando a API do Google Speech Recognition.
- **`speak(text)`**: Converte texto em áudio utilizando a biblioteca gTTS.
- **`respond(text)`**: Processa os comandos de voz e executa ações específicas, como abrir sites ou responder perguntas.
- **Laço principal**: Mantém o assistente ativo aguardando comandos do usuário.
<br>

## Exemplos

1. **Buscar no YouTube:**

   - Usuário: "YouTube"
   - Assistente: "O que gostaria de pesquisar?"
   - Usuário: "Gatos engraçados"
   - (Abre resultados no YouTube para "Gatos engraçados")

2. **Consultar Wikipedia:**

   - Usuário: "Wikipedia"
   - Assistente: "O que deseja buscar na Wikipedia?"
   - Usuário: "Inteligência Artificial"
   - Assistente: (Resumo falado sobre Inteligência Artificial)
<br>

## Observações

- **Erro de reconhecimento:** Caso a fala do usuário não seja entendida, o assistente responderá "Desculpe, não entendi".
- **Problemas de conexão:** Se a API de reconhecimento não estiver disponível, o assistente notificará o usuário.
- **Requisitos de idioma:** Atualmente, o assistente responde apenas em português.
