import os

def get_professions_options():
    return {
        1: "primitive_iron",
        2: "finest_sea_salt",
        3: "classic_coal",
        4: "bright_copper",
        5: "shadowy_cobalt",
        6: "",
        7: "",
    }


def search_files_from_text(path, text): #, incluir_subcarpetas=True):
    results = []

    for root, dirs, files in os.walk(path):
        for file in files:
            if text in file:
                results.append(os.path.join(root, file))
        #if not incluir_subcarpetas:
        #    break  # solo busca en el directorio principal si se desactiva la recursión

    return results