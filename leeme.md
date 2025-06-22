
# Sistema de Sincronización de Archivos Distribuido

Un sistema para sincronizar archivos entre múltiples servidores, con resolución de conflictos basada en fechas de modificación y hashing de contenido.

## Estructura del Proyecto

```
files/                  # Archivos compartidos
├── file1.txt           # Ejemplo de archivo
├── folderA/            # Ejemplo de directorio
└── Sync/               # Configuración y metadatos
    ├── metadata.db     # Base de datos de metadatos (SQLite)
    ├── metadata.csv    # Exportación de metadatos
    ├── servers.txt     # Lista de servidores remotos
    ├── server.py       # Servidor web para compartir archivos
    ├── sync_logic.py   # Lógica de sincronización
    └── sync_client.py  # Cliente para sincronización remota
```

## Configuración de Git (.gitignore)

Para proyectos con seguimiento Git, se recomienda ignorar los siguientes archivos:

1. **Ignorar toda la carpeta Sync** (recomendado para clientes):
   ```
   Sync/
   ```

2. **Ignorar solo archivos específicos** (recomendado para servidores):
   ```
   server.txt
   metadata.csv
   metadata.db
   ```

Ejemplo completo de `.gitignore`:
```
# Ignorar toda la carpeta Sync (descomentar para clientes)
# Sync/

# Ignorar archivos específicos (descomentar para servidores)

# server.txt
#  metadata.csv
#  metadata.db
# Python
__pycache__/
*.py[cod]
*$py.class
```

## Instalación

1. Clona el repositorio:
   ```bash
   https://github.com/Bolkof/sincronizador.git
   ```

2. Instala las dependencias:
   ```bash
   pip install flask requests
   ```

## Uso

### Ejecución básica (servidor + sincronización automática):
```bash
python main.py
```

### Opciones disponibles:
| Comando                | Descripción                                      |
|------------------------|--------------------------------------------------|
| `--sync`              | Ejecutar solo la sincronización                  |
| `--server`            | Ejecutar solo el servidor                        |
| `--port 8080`         | Especificar puerto del servidor (default: 5000)  |
| `--interval 10`       | Intervalo de sincronización en minutos (default: 5) |

### Ejemplos:
1. Servidor en puerto 8080 con sincronización cada 10 minutos:
   ```bash
   python main.py --port 8080 --interval 10
   ```

2. Solo sincronización (una ejecución):
   ```bash
   python main.py --sync
   ```

## Características

- ✅ Sincronización bidireccional
- ✅ Resolución de conflictos por fecha de modificación
- ✅ Hash de contenido (MD5) para verificación
- ✅ Soporte para múltiples servidores remotos
- ✅ Sincronización periódica automática
- ✅ Eliminación segura de archivos borrados remotamente

## Configuración de Servidores

Edita `Sync/servers.txt` para agregar URLs de servidores remotos:
```
http://server1.com/Sync/metadata.csv
http://server2.com/Sync/metadata.csv
```

## Notas importantes

1. Para servidores: No ignores `Sync/metadata.csv` ya que debe ser compartido.
2. Para clientes: Puedes ignorar toda la carpeta `Sync/` si no necesitas versionar la configuración local.
3. Los archivos `*.db` y `*.txt` generalmente no deben versionarse ya que contienen información local específica.