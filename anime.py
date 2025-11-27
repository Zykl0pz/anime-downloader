from animeflv import AnimeFLV
from tqdm import tqdm
import os
import sys
import json
import time
from datetime import datetime

def clear_screen():
    """Limpia la pantalla de la terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu_principal():
    """Muestra el menú principal de la aplicación"""
    print("=" * 50)
    print("          DESCARGADOR DE ANIME - ANIMEFLV")
    print("=" * 50)
    print("1. Buscar y descargar anime")
    print("2. Extraer todos los enlaces de un anime")
    print("3. Salir")
    print("=" * 50)

def buscar_anime(api):
    """Función para buscar y descargar un anime específico"""
    clear_screen()
    print("🔍 BÚSQUEDA Y DESCARGA DE ANIME")
    print("=" * 50)
    
    # Buscar anime
    query = input("Escribir nombre del anime: ").strip()
    if not query:
        print("❌ Debes ingresar un nombre para buscar.")
        input("Presiona Enter para continuar...")
        return
    
    try:
        elements = api.search(query)
    except Exception as e:
        print(f"❌ Error al buscar: {e}")
        input("Presiona Enter para continuar...")
        return
    
    if not elements:
        print("❌ No se encontraron resultados para tu búsqueda.")
        input("Presiona Enter para continuar...")
        return
    
    # Mostrar resultados
    clear_screen()
    print("📺 SELECCIONA UN ANIME")
    print("=" * 50)
    for i, element in enumerate(elements):
        print(f"{i + 1}. {element.title}")
    
    print(f"{len(elements) + 1}. 🔙 Volver al menú principal")
    
    try:
        seleccion = input("\nSelecciona una opción: ").strip()
        if seleccion == str(len(elements) + 1):
            return
        
        seleccion_idx = int(seleccion) - 1
        if seleccion_idx < 0 or seleccion_idx >= len(elements):
            print("❌ Selección inválida.")
            input("Presiona Enter para continuar...")
            return
            
        anime_seleccionado = elements[seleccion_idx]
        
        # Obtener información del anime
        clear_screen()
        print("🔄 OBTENIENDO INFORMACIÓN DEL ANIME...")
        print(f"🎬 Anime: {anime_seleccionado.title}")
        print("=" * 50)
        
        info = api.get_anime_info(anime_seleccionado.id)
        total_episodios = len(info.episodes)
        
        if total_episodios == 0:
            print("❌ No se encontraron episodios para este anime.")
            input("Presiona Enter para continuar...")
            return
        
        print(f"📊 Total de episodios encontrados: {total_episodios}")
        
        # Mostrar episodios
        clear_screen()
        print(f"📋 EPISODIOS DE {anime_seleccionado.title.upper()}")
        print("=" * 50)
        
        info.episodes.reverse()
        
        for i, episodio in enumerate(info.episodes):
            print(f"{i + 1}. Episodio {episodio.id}")
        
        print(f"{len(info.episodes) + 1}. 🔙 Volver al menú principal")
        
        ep_seleccion = input("\nSelecciona un episodio: ").strip()
        if ep_seleccion == str(len(info.episodes) + 1):
            return
        
        ep_idx = int(ep_seleccion) - 1
        if ep_idx < 0 or ep_idx >= len(info.episodes):
            print("❌ Selección inválida.")
            input("Presiona Enter para continuar...")
            return
        
        episodio_seleccionado = info.episodes[ep_idx]
        
        # Obtener enlaces del episodio
        clear_screen()
        print("🔗 OBTENIENDO ENLACES DE DESCARGA...")
        print(f"🎬 Anime: {anime_seleccionado.title}")
        print(f"📺 Episodio: {episodio_seleccionado.id}")
        print("=" * 50)
        
        enlaces = api.get_links(anime_seleccionado.id, episodio_seleccionado.id)
        
        if not enlaces:
            print("❌ No se encontraron enlaces para este episodio.")
            input("Presiona Enter para continuar...")
            return
        
        print(f"📊 Se encontraron {len(enlaces)} enlaces:")
        for i, enlace in enumerate(enlaces):
            print(f"{i + 1}. Servidor: {enlace.server}")
            print(f"   URL: {enlace.url}")
            print(f"   Calidad: {getattr(enlace, 'quality', 'Desconocida')}")
            print()
        
        input("Presiona Enter para continuar...")
        
    except (ValueError, IndexError):
        print("❌ Selección inválida.")
        input("Presiona Enter para continuar...")
    except Exception as e:
        print(f"❌ Error: {e}")
        input("Presiona Enter para continuar...")

def extraer_todos_enlaces(api):
    """Función principal para extraer todos los enlaces de un anime"""
    clear_screen()
    print("🔗 EXTRACCIÓN AUTOMÁTICA DE ENLACES")
    print("=" * 50)
    
    # Buscar anime
    query = input("Escribir nombre del anime: ").strip()
    if not query:
        print("❌ Debes ingresar un nombre para buscar.")
        input("Presiona Enter para continuar...")
        return
    
    try:
        elements = api.search(query)
    except Exception as e:
        print(f"❌ Error al buscar: {e}")
        input("Presiona Enter para continuar...")
        return
    
    if not elements:
        print("❌ No se encontraron resultados para tu búsqueda.")
        input("Presiona Enter para continuar...")
        return
    
    # Mostrar resultados
    clear_screen()
    print("📺 SELECCIONA UN ANIME PARA EXTRAER ENLACES")
    print("=" * 50)
    for i, element in enumerate(elements):
        print(f"{i + 1}. {element.title}")
    
    print(f"{len(elements) + 1}. 🔙 Volver al menú principal")
    
    try:
        seleccion = input("\nSelecciona una opción: ").strip()
        if seleccion == str(len(elements) + 1):
            return
        
        seleccion_idx = int(seleccion) - 1
        if seleccion_idx < 0 or seleccion_idx >= len(elements):
            print("❌ Selección inválida.")
            input("Presiona Enter para continuar...")
            return
            
        anime_seleccionado = elements[seleccion_idx]
        procesar_extraccion_enlaces(api, anime_seleccionado)
        
    except (ValueError, IndexError):
        print("❌ Selección inválida.")
        input("Presiona Enter para continuar...")
    except Exception as e:
        print(f"❌ Error: {e}")
        input("Presiona Enter para continuar...")

def procesar_extraccion_enlaces(api, anime_seleccionado):
    """Procesa la extracción de todos los enlaces del anime seleccionado"""
    clear_screen()
    print("🔄 OBTENIENDO INFORMACIÓN DEL ANIME...")
    print(f"🎬 Anime: {anime_seleccionado.title}")
    print("=" * 50)
    
    try:
        # Obtener información completa del anime
        info = api.get_anime_info(anime_seleccionado.id)
        total_episodios = len(info.episodes)
        
        if total_episodios == 0:
            print("❌ No se encontraron episodios para este anime.")
            input("Presiona Enter para continuar...")
            return
        
        print(f"📊 Total de episodios encontrados: {total_episodios}")
        print("🔄 Comenzando extracción de enlaces...")
        print("=" * 50)
        
        # Seleccionar formato de salida
        print("\n📁 FORMATO DE SALIDA:")
        print("1. JSON (recomendado para uso programático)")
        print("2. TXT (formato legible)")
        
        formato = input("\nSelecciona el formato (1-2): ").strip()
        if formato not in ['1', '2']:
            print("❌ Formato inválido, usando JSON por defecto.")
            formato = '1'
        
        # Extraer enlaces de todos los episodios
        resultados = {}
        episodios_procesados = 0
        episodios_con_error = 0
        
        info.episodes.reverse()
        
        with tqdm(total=total_episodios, desc="Extrayendo enlaces", unit="ep") as pbar:
            for episodio in info.episodes:
                try:
                    # Obtener enlaces del episodio
                    enlaces = api.get_links(anime_seleccionado.id, episodio.id)
                    
                    # Almacenar resultados
                    resultados[episodio.id] = {
                        'episodio': episodio.id,
                        'enlaces': []
                    }
                    
                    for enlace in enlaces:
                        resultados[episodio.id]['enlaces'].append({
                            'servidor': enlace.server,
                            'url': enlace.url,
                            'calidad': getattr(enlace, 'quality', 'Desconocida')
                        })
                    
                    episodios_procesados += 1
                    time.sleep(0.5)  # Pequeña pausa para no saturar el servidor
                    
                except Exception as e:
                    print(f"\n⚠️ Error en episodio {episodio.id}: {e}")
                    resultados[episodio.id] = {
                        'episodio': episodio.id,
                        'error': str(e),
                        'enlaces': []
                    }
                    episodios_con_error += 1
                
                pbar.update(1)
        
        # Guardar resultados en archivo
        guardar_resultados(anime_seleccionado, resultados, formato, 
                          episodios_procesados, episodios_con_error, total_episodios)
        
    except Exception as e:
        print(f"❌ Error crítico: {e}")
        input("Presiona Enter para continuar...")

def guardar_resultados(anime, resultados, formato, exitosos, con_error, total):
    """Guarda los resultados en el formato seleccionado"""
    clear_screen()
    print("💾 GUARDANDO RESULTADOS")
    print("=" * 50)
    
    # Crear nombre de archivo seguro
    nombre_archivo = "".join(c for c in anime.title if c.isalnum() or c in (' ', '-', '_')).rstrip()
    nombre_archivo = nombre_archivo.replace(' ', '_')
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    try:
        if formato == '1':  # JSON
            archivo_salida = f"{nombre_archivo}_enlaces_{timestamp}.json"
            
            # CORRECCIÓN APLICADA AQUÍ
            episodios_ordenados = dict(sorted(resultados.items(), key=lambda x: int(x[0]) if isinstance(x[0], str) and x[0].isdigit() else x[0]))
            
            # Estructura de datos para JSON
            datos_exportar = {
                'anime': anime.title,
                'anime_id': anime.id,
                'fecha_extraccion': datetime.now().isoformat(),
                'estadisticas': {
                    'total_episodios': total,
                    'episodios_exitosos': exitosos,
                    'episodios_con_error': con_error
                },
                'episodios': episodios_ordenados
            }
            
            with open(archivo_salida, 'w', encoding='utf-8') as f:
                json.dump(datos_exportar, f, ensure_ascii=False, indent=2)
                
        else:  # TXT
            archivo_salida = f"{nombre_archivo}_enlaces_{timestamp}.txt"
            
            with open(archivo_salida, 'w', encoding='utf-8') as f:
                f.write("=" * 60 + "\n")
                f.write(f"ENLACES DE DESCARGA - {anime.title}\n")
                f.write("=" * 60 + "\n")
                f.write(f"Anime: {anime.title}\n")
                f.write(f"ID: {anime.id}\n")
                f.write(f"Fecha de extracción: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f"Total episodios: {total} | Exitosos: {exitosos} | Errores: {con_error}\n")
                f.write("=" * 60 + "\n\n")
                
                # CORRECCIÓN APLICADA AQUÍ
                episodios_ordenados = sorted(resultados.items(), key=lambda x: int(x[0]) if isinstance(x[0], str) and x[0].isdigit() else x[0])
                
                for ep_num, datos_ep in episodios_ordenados:
                    f.write(f"EPISODIO {datos_ep['episodio']}\n")
                    f.write("-" * 40 + "\n")
                    
                    if 'error' in datos_ep:
                        f.write(f"❌ ERROR: {datos_ep['error']}\n")
                    elif not datos_ep['enlaces']:
                        f.write("⚠️ No se encontraron enlaces\n")
                    else:
                        for i, enlace in enumerate(datos_ep['enlaces'], 1):
                            f.write(f"{i}. Servidor: {enlace['servidor']}\n")
                            f.write(f"   Calidad: {enlace['calidad']}\n")
                            f.write(f"   URL: {enlace['url']}\n")
                    
                    f.write("\n")
        
        # Mostrar resumen
        print(f"✅ EXTRACCIÓN COMPLETADA")
        print("=" * 50)
        print(f"📁 Archivo guardado: {archivo_salida}")
        print(f"🎬 Anime: {anime.title}")
        print(f"📊 Estadísticas:")
        print(f"   • Total de episodios: {total}")
        print(f"   • Episodios procesados: {exitosos}")
        print(f"   • Episodios con error: {con_error}")
        print(f"   • Tasa de éxito: {(exitosos/total)*100:.1f}%")
        print("=" * 50)
        
        input("\nPresiona Enter para continuar...")
        
    except Exception as e:
        print(f"❌ Error al guardar archivo: {e}")
        input("Presiona Enter para continuar...")

def main():
    """Función principal de la aplicación"""
    try:
        with AnimeFLV() as api:
            while True:
                clear_screen()
                mostrar_menu_principal()
                
                opcion = input("\nSelecciona una opción: ").strip()
                
                if opcion == "1":
                    buscar_anime(api)
                elif opcion == "2":
                    extraer_todos_enlaces(api)
                elif opcion == "3":
                    print("👋 ¡Hasta luego!")
                    break
                else:
                    print("❌ Opción inválida. Por favor selecciona 1, 2 o 3.")
                    input("Presiona Enter para continuar...")
                    
    except KeyboardInterrupt:
        print("\n\n👋 ¡Hasta luego!")
    except Exception as e:
        print(f"❌ Error crítico: {e}")
        input("Presiona Enter para salir...")

if __name__ == "__main__":
    main()