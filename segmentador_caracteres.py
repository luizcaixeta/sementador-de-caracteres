import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

def preprocess_image(image_path, output_folder="caracteres_segmentados", threshold=128, min_char_width=5, min_line_height=10):

    """

    Segmenta os caracteres de uma imagem com múltiplas linhas e os salva individualmente.

    """

    #criar a pasta para salvar os caracteres, se não existir
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    #carrega a imagem em escala de cinza
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        print(f"Erro: Não foi possível carregar a imagem em {image_path}")
        return []
    
    #binarizar a imagem
    _, binary_image = cv2.threshold(image, threshold, 255, cv2.THRESH_BINARY_INV)
    
    #projeção horizontal: soma dos pixels ao longo das linhas
    horizontal_projection = np.sum(binary_image, axis=1)
    
    #plota o gráfico da projeção horizontal
    plt.figure(figsize=(10, 5))
    plt.plot(horizontal_projection, range(len(horizontal_projection)), color='blue')
    plt.title("Projeção Horizontal (Soma dos Pixels por Linha)")
    plt.xlabel("Soma dos Pixels")
    plt.ylabel("Linhas (Y)")
    plt.gca().invert_yaxis()  #inverter o eixo Y para corresponder à imagem
    plt.show()
    
    #encontrar os limites das linhas
    line_indices = np.where(horizontal_projection > 0)[0]
    if len(line_indices) == 0:
        print("Nenhuma linha de texto encontrada.")
        return []
    
    #segmentar as linhas de texto
    lines = []
    start = line_indices[0]
    for i in range(1, len(line_indices)):
        if line_indices[i] - line_indices[i - 1] > 1:  #espaço entre linhas
            end = line_indices[i - 1]
            line_height = end - start + 1
            if line_height >= min_line_height:
                line = binary_image[start:end + 1, :]
                lines.append(line)
            start = line_indices[i]
    end = line_indices[-1]
    line_height = end - start + 1
    if line_height >= min_line_height:
        line = binary_image[start:end + 1, :]
        lines.append(line)
    
    #processar cada linha para segmentar os caracteres
    all_characters = []
    for line_num, line in enumerate(lines):
        # Projeção vertical: soma dos pixels ao longo das colunas
        vertical_projection = np.sum(line, axis=0)
        
        #plotar o gráfico da projeção vertical
        plt.figure(figsize=(10, 5))
        plt.plot(range(len(vertical_projection)), vertical_projection, color='red')
        plt.title(f"Projeção Vertical (Soma dos Pixels por Coluna) - Linha {line_num + 1}")
        plt.xlabel("Colunas (X)")
        plt.ylabel("Soma dos Pixels")
        plt.show()
        
        #encontrar os limites dos caracteres
        character_indices = np.where(vertical_projection > 0)[0]
        if len(character_indices) == 0:
            print(f"Nenhum caractere encontrado na linha {line_num + 1}.")
            continue
        
        #segmentar os caracteres na linha atual
        characters = []
        start = character_indices[0]
        for i in range(1, len(character_indices)):
            if character_indices[i] - character_indices[i - 1] > 1:  #espaço entre caracteres
                end = character_indices[i - 1]
                char_width = end - start + 1
                if char_width >= min_char_width:
                    char = line[:, start:end + 1]
                    characters.append(char)
                start = character_indices[i]
        end = character_indices[-1]
        char_width = end - start + 1
        if char_width >= min_char_width:
            char = line[:, start:end + 1]
            characters.append(char)
        
        #salvar os caracteres da linha atual
        for i, char in enumerate(characters):
            char = cv2.bitwise_not(char)  # Inverter as cores de volta ao original
            char_path = os.path.join(output_folder, f"line_{line_num + 1}_char_{i + 1}.png")
            cv2.imwrite(char_path, char)
            print(f"Caractere {i + 1} da linha {line_num + 1} salvo em {char_path}")
        
        all_characters.extend(characters)
    
    #exibir os caracteres segmentados
    plt.figure(figsize=(15, 5))
    for i, char in enumerate(all_characters):
        plt.subplot(1, len(all_characters), i + 1)
        plt.imshow(char, cmap='gray')
        plt.title(f"Caractere {i + 1}")
        plt.axis('off')
    plt.show()
    
    return all_characters

#testar a função com uma imagem de exemplo
image_path = "teste.jpg"  # Substitua pelo caminho da sua imagem
characters = preprocess_image(image_path, threshold=128, min_char_width=5, min_line_height=10)