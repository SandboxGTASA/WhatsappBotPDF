# WhatsappBotPDF
Projeto que desenvolvi com a intenção de automatizar o envio de arquivos PDF via Whatsapp em massa.

Guia basico para rodar o programa após instalar bibliotecas<br>

1   - Insira um arquivo .csv no mesmo diretório do programa (como padrão está sendo utilizado "CLIENTES.csv").<br>
1.1 - O arquivo deve conter somente o nome do arquivo pdf/nome do contato salvo. Os dois serão iguais.
2   - Coloque o chromedriver na pasta path de seu SO (Windows 7)<br>
2.1 - Para encontrar a pasta pressione Windows + R e digite %PATH% no campo para executar<br>
3   - Abra o arquivo bot_whats_pdf.py e altere a variável diretorio<br>
3.1 - Dentro da função "env_boleto_massa" altere a variavel "diretorio" com o caminho para a pasta aonde se encontram os arquivos .pdf que irá enviar.<br>
