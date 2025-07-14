from animeflv import AnimeFLV

with AnimeFLV() as api:

    # Se recibe la serie que se desea
    elements = api.search(input("Escribir serie: "))

    # Se enumeran los resultados encontrados para el nombre ingresado
    for i, element in enumerate(elements):
        print(f"{i}, {element.title}")

    try:

        # Se guarda la serie seleccionada
        selection = int(input("Selecciona una serie: "))
        info = api.get_anime_info(elements[selection].id)
        info.episodes.reverse()

        # Se enumeran los episodios existentes
        for j, episode in enumerate(info.episodes):
            print(f"{j} | Episodio - {episode.id}")

        index_episode = int(input("Selecciona un episodio: "))
        serie = elements[selection].id
        capitulo = info.episodes[index_episode].id
        results = api.get_links(serie, capitulo)
            
        for result in results:
            print(f"{result.server} - {result.url}")

    except Exception as e:
        print(e)
