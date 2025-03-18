## Segmentador de caracteres

Em muitos projetos de visão computacional, é essencial extrair e isolar caracteres específicos de imagens contendo textos. Este repositório tem como objetivo fornecer uma solução para essa tarefa, segmentando caracteres de imagens de maneira eficiente e preparando-os para reconhecimento por modelos de inteligência artificial.

## Funcionalidades

Dado uma imagem de entrada contendo textos, este código realiza a segmentação dos caracteres presentes, gerando imagens individuais para cada um deles. Essas imagens segmentadas podem ser utilizadas como input para modelos de reconhecimento de caracteres (OCR) ou outras aplicações de processamento de imagem.

## Como funciona?

O código utiliza técnicas de processamento de imagem para:

1. Pré-processamento: Ajustes de brilho, contraste e filtragem para melhorar a qualidade da imagem.

2. Detecção de caracteres: Identificação e isolamento dos caracteres presentes na imagem.

3. Segmentação: Geração de imagens individuais para cada caractere detectado.

## Exemplo de funcionamento

Dado o input:

![teste_soma](https://github.com/user-attachments/assets/c70aaec9-c733-4b4f-84b1-de4bae744f70)

São extraídos os seguintes caracteres e salvos isoladamente na pasta 'caracteres_segmentados' da seguinte forma:

+ Primeiro:
![line_1_char_1](https://github.com/user-attachments/assets/15f92909-ffc7-41bc-be5f-5d0dc7ac2d04)

+ Segundo:
![line_1_char_2](https://github.com/user-attachments/assets/7d73a6da-cb3b-47d4-9868-252e5f4ee571)

+Terceiro:
![line_1_char_3](https://github.com/user-attachments/assets/8131eab0-05ee-4dc1-bbcf-739b54d73c7b)

Além disso, o código também é capaz de detectar quebras de linha.

## Aplicações:

+ Reconhecimento óptico de caracteres (OCR).
+ Análise de documentos digitalizados.
+ Automação de processos de extração de texto.

## Como usar

1. Clone este repositório:

```git clone https://github.com/luizcaixeta/sementador-de-caracteres.git```

2. Instale as dependências necessárias:

 ```pip install -r requirements.txt```  

 3. Execute o código com a sua imagem de entrada

 ```python segmentador_caracteres.py```    
   





