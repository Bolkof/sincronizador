import argparse
from threading import Thread
from sync import sync_from_remotes
from server import app
import time

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
    parser.add_argument('--port', type=int, default=5000, help='Puerto para el servidor')
    parser.add_argument('--interval', type=int, default=5, 
                       help='Intervalo en minutos para sincronización automática')
    
    args = parser.parse_args()

    if not args.sync and not args.server:
        # Por defecto ejecuta ambos
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