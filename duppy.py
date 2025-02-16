import os
import difPy  # Importa search directamente para evitar problemas


def main():
    folder_path = input('Introduce el path de la carpeta: ')
    dif = difPy.build(folder_path, similarity="similar")
    search = difPy.search(dif)
    print("Hay", len(search.result), "coincidencias")
    for i in search.result.keys():
        print("\nLa imagen en la ruta:", i, "\nCoincide con la imagen en la ruta:", search.result[i][0][0])
        with open("resultados.txt", "a+") as f:
            f.write(i + "\t=\t" + str(search.result[i][0][0]) + "\n")
            f.close()
    with open("resultados.txt", "a+") as f:
        f.write("\n")
        f.close()
    os.system("PAUSE")


if __name__ == '__main__':
    main()  # Llama a la función principal solo una vez
