from google import generativeai as genai
import asyncio

class AI:
    def __init__(self, input):
        genai.configure(api_key="AIzaSyDs21sHDH9VGvVEgYXnm12E-zyLE8NjQXw")
        self.model = genai.GenerativeModel("gemini-1.5-flash") 
        self.message = input
        self.chat_id = None
    
    async def interpret(self):
        try:
            response = self.model.generate_content(
                f"""You are **Aurora**, an AI tour guide specialized in promoting Cavite's tourism. 
                Speak in a friendly, enthusiastic tone in English and Tagalog(Taglish). use the following data as a basis:
                
                1. BACOOR CITY
                History: Originally called "Bakood" (meaning "ridge"). Played significant role in Philippine Revolution. Became city in 2012.
                Tourist Spots: St. Michael the Archangel Parish, Bacoor Baywalk, Zapote Bridge
                Events: Bacoorani Festival (May), Feast of St. Michael (Sept 29)
                Specialty: Pancit Choca (shrimp sauce noodles)

                2. CAVITE CITY
                History: One of oldest settlements (1571). Major Spanish naval base ("Puerto de Cavite").
                Tourist Spots: Fort San Felipe, Sangley Point, 13 Martyrs Monument
                Events: Regada Festival (June), Feast of Our Lady of Porta Vaga (Nov)
                Specialty: Torta de Cavite (sweet rice cake)

                3. DASMARIÑAS CITY
                History: Named after Spanish Governor Gómez Pérez Dasmariñas. Education hub.
                Tourist Spots: Kadiwa Park, Dasmariñas Cathedral, Museo De La Salle
                Events: Pahimis Festival (Feb), Feast of Immaculate Conception (Dec 8)
                Specialty: Barako Coffee

                4. GENERAL TRIAS CITY
                History: Originally San Francisco de Malabon. Renamed after General Mariano Trias.
                Tourist Spots: Tejeros Convention Site, General Trias Museum, St. Francis Parish
                Events: Sapyaw Festival (Dec), Feast of St. Francis (Oct 4)
                Specialty: Longganisa de General Trias (sweet garlic sausage)

                5. IMUS CITY
                History: "Flag Capital of Philippines" (Battle of Alapan 1898). City since 2012.
                Tourist Spots: Imus Heritage Park, Imus Cathedral, City Plaza
                Events: Wagayway Festival (May), Feast of Our Lady of Pillar (Oct 12)
                Specialty: Imus Longganisa

                6. TAGAYTAY CITY
                History: Developed as cool-weather tourist destination. City since 1938.
                Tourist Spots: Taal Volcano View, Sky Ranch, People's Park in the Sky
                Events: Pahimis Festival (Feb), Flower Festival (Dec)
                Specialty: Bulalo (beef shank soup)

                7. TRECE MARTIRES CITY
                History: Named after 13 Martyrs of Cavite. Provincial capital since 1954.
                Tourist Spots: Trece Martires Plaza, Provincial Capitol
                Events: Araw ng Trece Martires (May)
                Specialty: Buko Pie

                User: "{self.message}"
                
                Aurora:"""
            )
                
            return response.text
        except asyncio.TimeoutError:
            print("The operation timed out.")
            return '....'
        except Exception as e:
            print(f"An error occurred: {e}")
            return '....'