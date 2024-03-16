# Recebe os valores de Red, Green e Blue do usuário
red = int(input("Digite o valor de Red (0-255): "))
green = int(input("Digite o valor de Green (0-255): "))
blue = int(input("Digite o valor de Blue (0-255): "))

def rgb_to_hex(red, green, blue):
    # Converte os valores RGB para hexadecimal
    hex_color = '#{:02x}{:02x}{:02x}'.format(red, green, blue)
    return hex_color
# Verifica se os valores estão dentro do intervalo 0-255
if 0 <= red <= 255 and 0 <= green <= 255 and 0 <= blue <= 255:
    # Obtém o código hexadecimal
    hex_color = rgb_to_hex(red, green, blue)
    # Exibe a cor e o código hexadecima
    print("Código Hexadecimal:", hex_color)
else:
    print("Os valores de Red, Green e Blue devem estar no intervalo de 0 a 255.")
