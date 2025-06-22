import argparse
from threading import Thread
from sync import sync_from_remotes
from server import app
import time
import os  # 👈 Importación para usar variables de entorno

# ✅ Determina si se debe activar la sincronización automáticamente usando la variable de entorno SYNC
# Se activa si SYNC=true (no distingue mayúsculas/minúsculas)
SYNC_ENV = os.getenv('SYNC', '').lower() == 'true'

# ✅ Determina si se debe iniciar el servidor web usando la variable de entorno SERVER
# Se activa si SERVER=true
SERVER_ENV = os.getenv('SERVER', '').lower() == 'true'

# ✅ Puerto donde se ejecutará el servidor web (por defecto 5000)
# Puede ser configurado mediante la variable de entorno PORT
PORT_ENV = int(os.getenv('PORT', 5000))

# ✅ Intervalo (en minutos) entre ejecuciones automáticas de sincronización
# Puede ser configurado mediante la variable de entorno INTERVAL
INTERVAL_ENV = int(os.getenv('INTERVAL', 5))
def run_sync_interval(interval_minutes):
    """Ejecuta sync_from_remotes en intervalos regulares"""
    while True:
        print(f"\nIniciando sincronización automática (cada {interval_minutes} minutos)...")
        sync_from_remotes()
        print(f"Sincronización completada. Esperando {interval_minutes} minutos...")
        time.sleep(interval_minutes * 60)

def main():
    parser = argparse.ArgumentParser(description='Sistema de sincronización de archivos')
    parser.add_argument('--sync', action='store_true', help='Ejecutar solo la sincronización')
    parser.add_argument('--server', action='store_true', help='Ejecutar solo el servidor')
    parser.add_argument('--port', type=int, default=PORT_ENV, help='Puerto para el servidor')
    parser.add_argument('--interval', type=int, default=INTERVAL_ENV,
                        help='Intervalo en minutos para sincronización automática')
    
    args = parser.parse_args()

    # Usar variables de entorno si no se especifican flags en la línea de comandos
    if not args.sync and not args.server:
        args.sync = SYNC_ENV
        args.server = SERVER_ENV

    if not args.sync and not args.server:
        # Si sigue sin especificarse nada, por defecto ejecuta ambos
        args.sync = True
        args.server = True

    if args.sync and args.server:
        # Ejecutar ambos en threads separados
        sync_thread = Thread(target=run_sync_interval, args=(args.interval,))
        sync_thread.daemon = True
        sync_thread.start()

        print(f"Servidor iniciado en puerto {args.port} con sincronización automática cada {args.interval} minutos")
        app.run(host='0.0.0.0', port=args.port)
    elif args.sync:
        # Solo sincronización
        sync_from_remotes()
    elif args.server:
        # Solo servidor
        print(f"Servidor iniciado en puerto {args.port} (sin sincronización automática)")
        app.run(host='0.0.0.0', port=args.port)

if __name__ == '__main__':
    main()