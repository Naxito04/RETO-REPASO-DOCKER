import os
import psycopg

url = os.getenv("DATABASE_URL")

try:
    with psycopg.connect(url) as connection:
        with connection.cursor() as cur:
            print("Conexión establecida")
            
            query = """
            INSERT INTO characters (name, status, species, type, gender, origin_name, location_name, image, url) VALUES 
            ('Rick Sanchez', 'Alive', 'Human', '', 'Male', 'Earth (C-137)', 'Earth (Replacement Dimension)', 'https://rickandmortyapi.com/api/character/avatar/1.jpeg', 'https://rickandmortyapi.com/api/character/1'),
            ('Morty Smith', 'Alive', 'Human', '', 'Male', 'Earth (C-137)', 'Earth (Replacement Dimension)', 'https://rickandmortyapi.com/api/character/avatar/2.jpeg', 'https://rickandmortyapi.com/api/character/2'),
            ('Summer Smith', 'Alive', 'Human', '', 'Female', 'Earth (C-137)', 'Earth (Replacement Dimension)', 'https://rickandmortyapi.com/api/character/avatar/3.jpeg', 'https://rickandmortyapi.com/api/character/3'),
            ('Beth Smith', 'Alive', 'Human', '', 'Female', 'Earth (C-137)', 'Earth (Replacement Dimension)', 'https://rickandmortyapi.com/api/character/avatar/4.jpeg', 'https://rickandmortyapi.com/api/character/4'),
            ('Jerry Smith', 'Alive', 'Human', '', 'Male', 'Earth (C-137)', 'Earth (Replacement Dimension)', 'https://rickandmortyapi.com/api/character/avatar/5.jpeg', 'https://rickandmortyapi.com/api/character/5'),
            ('Abadango Cluster Princess', 'Alive', 'Alien', 'Cluster Princess', 'Female', 'Abadango', 'Abadango', 'https://rickandmortyapi.com/api/character/avatar/6.jpeg', 'https://rickandmortyapi.com/api/character/6'),
            ('Abradolf Lincler', 'Unknown', 'Human', 'Genetic experiment', 'Male', 'Earth (C-137)', 'Testicle Monster Dimension', 'https://rickandmortyapi.com/api/character/avatar/7.jpeg', 'https://rickandmortyapi.com/api/character/7'),
            ('Adjudicator Rick', 'Dead', 'Human', '', 'Male', 'unknown', 'Citadel of Ricks', 'https://rickandmortyapi.com/api/character/avatar/8.jpeg', 'https://rickandmortyapi.com/api/character/8'),
            ('Agency Director', 'Dead', 'Human', '', 'Male', 'Earth (Replacement Dimension)', 'Earth (Replacement Dimension)', 'https://rickandmortyapi.com/api/character/avatar/9.jpeg', 'https://rickandmortyapi.com/api/character/9'),
            ('Alan Rails', 'Dead', 'Human', 'Superhuman (Ghost trains power)', 'Male', 'unknown', 'Worldender''s lair', 'https://rickandmortyapi.com/api/character/avatar/10.jpeg', 'https://rickandmortyapi.com/api/character/10'),
            ('Albert Einstein', 'Dead', 'Human', '', 'Male', 'Earth (C-137)', 'Earth (C-137)', 'https://rickandmortyapi.com/api/character/avatar/11.jpeg', 'https://rickandmortyapi.com/api/character/11'),
            ('Alexander', 'Dead', 'Human', '', 'Male', 'Earth (C-137)', 'Anatomy Park', 'https://rickandmortyapi.com/api/character/avatar/12.jpeg', 'https://rickandmortyapi.com/api/character/12'),
            ('Alien Googah', 'Alive', 'Alien', '', 'Female', 'unknown', 'Earth (Replacement Dimension)', 'https://rickandmortyapi.com/api/character/avatar/13.jpeg', 'https://rickandmortyapi.com/api/character/13'),
            ('Alien Morty', 'Alive', 'Alien', '', 'Male', 'unknown', 'Citadel of Ricks', 'https://rickandmortyapi.com/api/character/avatar/14.jpeg', 'https://rickandmortyapi.com/api/character/14'),
            ('Alien Rick', 'Alive', 'Alien', '', 'Male', 'unknown', 'Citadel of Ricks', 'https://rickandmortyapi.com/api/character/avatar/15.jpeg', 'https://rickandmortyapi.com/api/character/15');
            """
            cur.execute("TRUNCATE TABLE characters RESTART IDENTITY CASCADE;")
            connection.commit();
            cur.execute(query)
            connection.commit();

            query2 = "SELECT id, name, species FROM characters ORDER BY id LIMIT 10"
            cur.execute(query2)

            filas = cur.fetchall()
            for fila in filas:
                print(fila)

            query3 = "SELECT COUNT(*) AS total_personajes FROM characters"
            cur.execute(query3)
            count = cur.fetchall()
            print(f"Número de personajes: {count}")

except Exception as e:
    print("Error:", e)
    raise