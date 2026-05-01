from cryptography.fernet import Fernet
import os

def cifrar_mensaje():
    print("Iniciando proceso de cifrado simétrico...")
    
    # Generación de  llave
    clave = Fernet.generate_key()
    fernet = Fernet(clave)
    
    # Texto plano a cifrar
    mensaje_original = b"Datos confidenciales del sensor IoT: Temperatura=24C, Estado=Activo"
    mensaje_cifrado = fernet.encrypt(mensaje_original)
    
    # Resultados almacenados en el directorio de trabajo
    with open("clave_secreta.key", "wb") as f_clave:
        f_clave.write(clave)
        
    with open("datos_cifrados.txt", "wb") as f_msg:
        f_msg.write(mensaje_cifrado)
        
    print("Proceso realizado con éxito. Archivos 'clave_secreta.key' y 'datos_cifrados.txt' extraídos al host.")

if __name__ == "__main__":
    cifrar_mensaje()