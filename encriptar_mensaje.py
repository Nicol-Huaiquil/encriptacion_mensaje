from cryptography.fernet import Fernet
import configparser
import base64

def getKeyFrom(configFile):
    config = configparser.ConfigParser()
    config.read(configFile)
    key = config.get('Encryption', 'Key')
    keyBytes = base64.urlsafe_b64decode(key)
    return keyBytes

def encrypt(text, key):
    cipherSuite = Fernet(key)
    encryptedText = cipherSuite.encrypt(text.encode())
    return encryptedText

def decrypt(encryptedText, key):
    cipherSuite = Fernet(key)
    decryptedText = cipherSuite.decrypt(encryptedText)
    return decryptedText.decode()

# Cargar la clave desde el archivo de configuración
configFile = 'key.config'
key = getKeyFrom(configFile)
from cryptography.fernet import Fernet
import configparser
import base64

def getKeyFrom(configFile):
    config = configparser.ConfigParser()
    config.read(configFile)
    key = config.get('Encryption', 'Key')
    keyBytes = base64.urlsafe_b64decode(key)
    return keyBytes

def encrypt(text, key):
    cipherSuite = Fernet(key)
    encryptedText = cipherSuite.encrypt(text.encode())
    return encryptedText

# Cargar la clave desde el archivo de configuración
configFile = 'key.config'
key = getKeyFrom(configFile)

# Mensajes a encriptar
messages = [
'¡Hola a todos los amantes de los videojuegos! ¿Alguien ha probado el nuevo género de juegos de realidad virtual?',
'¡Hola! Sí, he tenido la oportunidad de experimentar algunos juegos de realidad virtual y la inmersión es simplemente increíble.',
'Vaya, eso suena interesante. ¿Cuáles son sus experiencias favoritas con los juegos de realidad virtual?',
'Personalmente, disfruté mucho de un juego de aventuras en realidad virtual en el que exploraba ruinas antiguas y resolvía acertijos. La sensación de estar realmente en ese mundo fue asombrosa.',
'Recuerdo haber jugado un juego de disparos en realidad virtual donde tenía que luchar contra robots gigantes. Fue una experiencia emocionante y desafiante.',
'¡Eso suena genial! Me encantaría probar un juego de carreras en realidad virtual para sentir la velocidad y la adrenalina como si estuviera al volante.',
'Definitivamente recomendaría probar juegos de deportes en realidad virtual. Es increíble cómo puedes sentir que estás participando en un partido de tenis o baloncesto desde la comodidad de tu hogar.',
'Tienes razón. Los juegos de deportes en realidad virtual son una forma divertida de mantenerse activo y desafiarse a uno mismo.',
'¡Estoy emocionado por el futuro de los juegos de realidad virtual! Parece que cada vez hay más opciones y mejoras en la tecnología.',
'Sin duda, la realidad virtual tiene el potencial de transformar por completo la forma en que jugamos y experimentamos los videojuegos.',
'Estoy de acuerdo. Estoy ansioso por ver qué innovaciones nos esperan en los próximos años.',
'¡Mantengamos nuestros visores listos y nuestras mentes abiertas para sumergirnos en nuevas y emocionantes aventuras virtuales!'

]

encrypted_messages = []
for message in messages:
    encrypted_message = encrypt(message, key)
    encrypted_messages.append(encrypted_message)

# Imprimir los mensajes encriptados
for i, encrypted_message in enumerate(encrypted_messages):
    print(f"Mensaje {i+1} encriptado:", encrypted_message.decode())