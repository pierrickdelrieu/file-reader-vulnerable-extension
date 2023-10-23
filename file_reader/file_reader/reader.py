# file_reader/reader.py

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return "Le fichier n'a pas été trouvé."
    except Exception as e:
        return f"Une erreur s'est produite : {str(e)}"
