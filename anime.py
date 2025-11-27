from animeflv import AnimeFLV
from tqdm import tqdm
import os
import sys

def clear_screen():
    """Limpia la pantalla de la terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu_principal():
    """Muestra el menú principal de la aplicación"""
    print("=" * 50)
    print("          DESCARGADOR DE ANIME - ANIMEFLV")
    print("=" * 50)
    print("1. Buscar y descargar anime")
    print("2. Salir")
    print("=" * 50)

def buscar_anime(api):
    """Función para buscar anime y seleccionar episodios"""
    clear_screen()
    print("🔍 BUSQUEDA DE ANIME")
    print("-" * 30)
    
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
    print("📺 RESULTADOS DE BUSQUEDA")
    print("-" * 30)
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
            
        mostrar_episodios(api, elements[seleccion_idx])
        
    except (ValueError, IndexError):
        print("❌ Selección inválida.")
        input("Presiona Enter para continuar...")
    except Exception as e:
        print(f"❌ Error: {e}")
        input("Presiona Enter para continuar...")

def mostrar_episodios(api, anime_seleccionado):
    """Muestra los episodios disponibles para un anime"""
    try:
        info = api.get_anime_info(anime_seleccionado.id)
        info.episodes.reverse()  # Mostrar del más reciente al más antiguo
        
        while True:
            clear_screen()
            print(f"🎬 {anime_seleccionado.title}")
            print("-" * 50)
            print(f"📖 Descripción: {getattr(info, 'description', 'No disponible')}")
            print(f"📊 Total de episodios: {len(info.episodes)}")
            print("-" * 50)
            
            # Mostrar primeros y últimos episodios
            if len(info.episodes) > 10:
                print("📋 Episodios (primeros 5 y últimos 5):")
                for j, episode in enumerate(info.episodes[:5]):
                    print(f"   {j + 1}. Episodio {episode.id}")
                print("   ...")
                for j, episode in enumerate(info.episodes[-5:], len(info.episodes) - 4):
                    print(f"   {j}. Episodio {episode.id}")
            else:
                print("📋 Episodios:")
                for j, episode in enumerate(info.episodes):
                    print(f"   {j + 1}. Episodio {episode.id}")
            
            print(f"\n{len(info.episodes) + 1}. 📥 Descargar intervalo de episodios")
            print(f"{len(info.episodes) + 2}. 🔗 Ver enlaces de un episodio")
            print(f"{len(info.episodes) + 3}. 🔙 Volver a búsqueda")
            print(f"{len(info.episodes) + 4}. 🏠 Menú principal")
            
            try:
                seleccion_ep = input("\nSelecciona una opción: ").strip()
                
                if seleccion_ep == str(len(info.episodes) + 1):
                    if descargar_intervalo(api, anime_seleccionado, info.episodes):
                        return True
                elif seleccion_ep == str(len(info.episodes) + 2):
                    if ver_enlaces_episodio(api, anime_seleccionado, info.episodes):
                        return True
                elif seleccion_ep == str(len(info.episodes) + 3):
                    return  # Volver a búsqueda
                elif seleccion_ep == str(len(info.episodes) + 4):
                    return True  # Salir al menú principal
                else:
                    episodio_idx = int(seleccion_ep) - 1
                    if 0 <= episodio_idx < len(info.episodes):
                        if ver_enlaces_episodio_individual(api, anime_seleccionado, info.episodes[episodio_idx]):
                            return True
                    else:
                        print("❌ Opción inválida.")
                        input("Presiona Enter para continuar...")
                        
            except ValueError:
                print("❌ Entrada inválida.")
                input("Presiona Enter para continuar...")
                
    except Exception as e:
        print(f"❌ Error al obtener información del anime: {e}")
        input("Presiona Enter para continuar...")

def descargar_intervalo(api, anime_seleccionado, episodios):
    """Permite seleccionar y descargar un intervalo de episodios"""
    clear_screen()
    print(f"📥 DESCARGAR INTERVALO DE EPISODIOS")
    print("-" * 50)
    print(f"🎬 Anime: {anime_seleccionado.title}")
    print(f"📊 Episodios disponibles: {len(episodios)}")
    print("-" * 50)
    
    try:
        # Mostrar rango de episodios disponibles
        primer_episodio = episodios[-1].id if episodios else "N/A"
        ultimo_episodio = episodios[0].id if episodios else "N/A"
        print(f"📈 Rango disponible: Episodio {primer_episodio} a {ultimo_episodio}")
        
        # Obtener intervalo del usuario
        inicio = input("\nEpisodio inicial: ").strip()
        fin = input("Episodio final: ").strip()
        
        if not inicio or not fin:
            print("❌ Debes ingresar ambos valores.")
            input("Presiona Enter para continuar...")
            return False
        
        # Verificar que los episodios existen
        episodios_a_descargar = []
        for episodio in episodios:
            if inicio <= episodio.id <= fin or fin <= episodio.id <= inicio:
                episodios_a_descargar.append(episodio)
        
        if not episodios_a_descargar:
            print("❌ No se encontraron episodios en el rango especificado.")
            input("Presiona Enter para continuar...")
            return False
        
        # Ordenar episodios
        episodios_a_descargar.sort(key=lambda x: x.id)
        
        print(f"\n📋 Episodios a descargar ({len(episodios_a_descargar)}):")
        for ep in episodios_a_descargar:
            print(f"   - Episodio {ep.id}")
        
        # Confirmar descarga
        confirmar = input(f"\n¿Descargar {len(episodios_a_descargar)} episodios? (s/n): ").strip().lower()
        if confirmar != 's':
            print("❌ Descarga cancelada.")
            input("Presiona Enter para continuar...")
            return False
        
        # Directorio de descarga
        directorio = input("Directorio de descarga (dejar vacío para actual): ").strip()
        if not directorio:
            directorio = "."
        
        # Descargar episodios
        print(f"\n📥 Iniciando descarga de {len(episodios_a_descargar)} episodios...")
        
        for i, episodio in enumerate(tqdm(episodios_a_descargar, desc="Descargando", unit="ep"), 1):
            try:
                print(f"\n⬇️ Descargando episodio {episodio.id} ({i}/{len(episodios_a_descargar)})...")
                download_one(anime_seleccionado.id, episodio.id, directorio)
                print(f"✅ Episodio {episodio.id} descargado correctamente")
            except Exception as e:
                print(f"❌ Error al descargar episodio {episodio.id}: {e}")
                continue
        
        print(f"\n🎉 ¡Descarga completada! {len(episodios_a_descargar)} episodios descargados en '{directorio}'")
        input("Presiona Enter para continuar...")
        
    except Exception as e:
        print(f"❌ Error durante la descarga: {e}")
        input("Presiona Enter para continuar...")
    
    return False

def ver_enlaces_episodio(api, anime_seleccionado, episodios):
    """Permite seleccionar un episodio para ver sus enlaces"""
    clear_screen()
    print(f"🔗 VER ENLACES DE EPISODIO")
    print("-" * 50)
    print(f"🎬 Anime: {anime_seleccionado.title}")
    print("-" * 50)
    
    try:
        # Mostrar episodios numerados
        for j, episode in enumerate(episodios):
            print(f"   {j + 1}. Episodio {episode.id}")
        
        print(f"\n{len(episodios) + 1}. 🔙 Volver")
        
        seleccion = input("\nSelecciona un episodio: ").strip()
        if seleccion == str(len(episodios) + 1):
            return False
        
        episodio_idx = int(seleccion) - 1
        if 0 <= episodio_idx < len(episodios):
            return ver_enlaces_episodio_individual(api, anime_seleccionado, episodios[episodio_idx])
        else:
            print("❌ Episodio inválido.")
            input("Presiona Enter para continuar...")
            
    except ValueError:
        print("❌ Entrada inválida.")
        input("Presiona Enter para continuar...")
    
    return False

def ver_enlaces_episodio_individual(api, anime_seleccionado, episodio):
    """Muestra los enlaces de descarga para un episodio específico"""
    clear_screen()
    print(f"🔗 ENLACES DE DESCARGA")
    print("-" * 50)
    print(f"🎬 Anime: {anime_seleccionado.title}")
    print(f"📺 Episodio: {episodio.id}")
    print("-" * 50)
    
    try:
        results = api.get_links(anime_seleccionado.id, episodio.id)
        
        if not results:
            print("❌ No se encontraron enlaces para este episodio.")
        else:
            print("🌐 Servidores disponibles:")
            for i, result in enumerate(results, 1):
                print(f"   {i}. {result.server} - {result.url}")
        
        print("\n1. 📥 Descargar este episodio")
        print("2. 🔙 Volver a episodios")
        print("3. 🏠 Menú principal")
        
        opcion = input("\nSelecciona una opción: ").strip()
        if opcion == "1":
            directorio = input("Directorio de descarga (dejar vacío para actual): ").strip()
            if not directorio:
                directorio = "."
            
            try:
                print(f"⬇️ Descargando episodio {episodio.id}...")
                download_one(anime_seleccionado.id, episodio.id, directorio)
                print(f"✅ Episodio {episodio.id} descargado correctamente en '{directorio}'")
                input("Presiona Enter para continuar...")
            except Exception as e:
                print(f"❌ Error al descargar: {e}")
                input("Presiona Enter para continuar...")
            return False
        elif opcion == "2":
            return False
        elif opcion == "3":
            return True
        else:
            print("❌ Opción inválida, volviendo a episodios...")
            input("Presiona Enter para continuar...")
            return False
            
    except Exception as e:
        print(f"❌ Error al obtener enlaces: {e}")
        input("Presiona Enter para continuar...")
        return False

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
                    print("👋 ¡Hasta luego!")
                    break
                else:
                    print("❌ Opción inválida. Por favor selecciona 1 o 2.")
                    input("Presiona Enter para continuar...")
                    
    except KeyboardInterrupt:
        print("\n\n👋 ¡Hasta luego!")
    except Exception as e:
        print(f"❌ Error crítico: {e}")
        input("Presiona Enter para salir...")

if __name__ == "__main__":
    main()
