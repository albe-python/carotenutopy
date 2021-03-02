import json

libri={
    "Libro1": '{ "nome": "Guerra e pace", "autore": "Lev Nikolaevic Tolstoj", "genere": "romanzo storico"}',

    "Libro2": '{ "nome": "Il processo", "autore": "Franz Kafka", "genere": "narrativa filosofica"}',

    "Libro3": '{ "nome": "Il barone rampante", "autore": "Italo Calvino", "genere": "romanzo"}',

    "Libro4":  '{ "nome": "Moby Dick", "autore": "Herman Melville", "genere": "avventura"}',

    "Libro5":  '{ "nome": "Delitto e castigo", "autore": "Fedor Michajlovic Dostoevskij", "genere": "romanzo"}',

    "Libro6":  '{ "nome": "Il deserto dei Tartari", "autore": "Dino Buzzati", "genere": "romanzo"}',

    "Libro7":  '{ "nome": "La montagna incantata", "autore": "Thomas Mann", "genere": "romanzo"}',

    "Libro8":  '{ "nome": "Memorie di Adriano", "autore": "Marguerite Yourcenar", "genere": "romanzo storico"}',
    
    "Libro9":  '{ "nome": "Alla ricerca del tempo perduto", "autore": "Marcel Proust", "genere": "romanzo"}',

    "Libro10":  '{ "nome": "Cecità", "autore": "Josè Saramago", "genere": "Fantascienza Apocalittica e post-apocalittica"}'
    }

y = json.loads(libri["Libro1"])


print(y["genere"])
