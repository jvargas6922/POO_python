import json
from producto import Producto


def main():
    with open('productos.txt') as file:
        for line in file:
            try:
                data = json.loads(line)

                producto = Producto(data.get('nombre'), data.get('precio'))
                print(producto)
            except ValueError as e:
                print(f"Error: {e}")
                with open('error.log', 'a') as error_file:
                    error_file.write(f'Error: {e}\n')
                    error_file.write(f'Line: {line}\n')
                    error_file.write('---\n')
                print(f"Error: {e}")
                print(f"Line: {line}")

if __name__ == '__main__':
    main()