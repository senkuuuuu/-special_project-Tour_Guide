import asyncio
from modules.functionality.record_audio import *
from modules.functionality.voice_to_text import *
from modules.functionality.text_to_voice import *
from modules.functionality.start_speaking import *
from modules.essentials.character_ai_async import *
from modules.essentials.characters import *
from modules.essentials.dialog_box_tkinter import *
from modules.data_handlers.cleaner import *


class Aurora:
    def __init__(self):
        self.ai_response = '...'
        self.user_input = '...'
        self.dialog_box = DialogBox()
        self.tasks = []
        self.cleaner = clean()
        self.running = True

    async def pygame_event_loop(self, event_queue):
        """Handles Pygame's event loop."""
        while self.running:
            await asyncio.sleep(0)  
            event = pygame.event.poll()
            if event.type != pygame.NOEVENT:
                await event_queue.put(event)
    
    async def handle_events(self, event_queue, character, start_recording):
        button_clicks = 0
        while self.running:
            if not event_queue.empty():
                event = await event_queue.get()
                if event.type == pygame.QUIT:
                    result = self.dialog_box.show_popup('yesno', 'Do you wish to exit the program?')

                    if result == True:
                        self.running = False
                        self.cleaner.terminate_tasks(self.tasks)
                        self.cleaner.terminate_temp()
                        self.cleaner.terminate_lingering_obj(self.__class__)
                    else:
                        pass

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    button_clicks += 1

                    if character.button_clicked(event.pos):
                        if button_clicks%2 == 0:
                            start_recording.set()
                            character.change_mic(0)
                        else:
                            start_recording.clear()
                            character.change_mic(1)
            await asyncio.sleep(0.01) 

    async def idle_animation(self, screen, character, fps, start_idle):
        character_state = 0
        while self.running:
            await start_idle.wait()
            await asyncio.sleep(1 / fps)
            character_state+=1
            character.idle(screen, character_state)
            pygame.display.flip()
    
    async def thinking_animation(self, screen, character, start_thinking, fps):
        while self.running:
            await start_thinking.wait()
            await asyncio.sleep(1 / fps)
            character.thinking(screen)
            pygame.display.flip()
    
    async def talking_animation(self, screen, character, fps, start_ai_speaking):
        character_state = 0
        while self.running:
            await start_ai_speaking.wait()
            await asyncio.sleep(1 / fps)
            character_state+=1
            character.talking(screen, character_state)
            pygame.display.flip()


    async def voice_to_text(self, start_voice_to_text, start_generating_ai_response):
        while self.running:
            await start_voice_to_text.wait()
            self.user_input = asyncio.to_thread(stt().convert())
            print(self.user_input)

            start_voice_to_text.clear()
            start_generating_ai_response.set()

    async def run_character_ai(self, start_generating_ai_response, start_ai_speaking, start_thinking):
        while self.running:
            await start_generating_ai_response.wait()
            start_generating_ai_response.clear() 
            try:
                self.ai_response = await AI(self.user_input).interpret() 
                print("AI Response:", self.ai_response)
                await talk(self.ai_response).run()
            except Exception as e:
                self.dialog_box.show_popup('error', 'Had an error communicating with Makise Kurisu, Please check your internet conection, El Psy Congroo...')
                self.running = False


            start_thinking.clear()
            start_ai_speaking.set()
    
    async def start_ai_speak(self, start_ai_speaking, start_idle):
        while self.running:
            await start_ai_speaking.wait()
            await asyncio.to_thread(speak().begin)

            start_ai_speaking.clear()
            start_idle.set()
            


    async def main(self):
        pygame.init()
        pygame.display.set_caption("Aurora")

        #essentials
        screen = pygame.display.set_mode((550, 700))
        character = Character()
        idle_fps = 1
        talking_fps =4

        #event queue
        event_queue = asyncio.Queue()

        #event handlers
        start_idle = asyncio.Event()
        start_idle.set()

        start_recording = asyncio.Event()

        start_voice_to_text = asyncio.Event()

        start_generating_ai_response = asyncio.Event()

        start_ai_speaking = asyncio.Event()

        start_thinking = asyncio.Event()

        self.tasks = [
            asyncio.create_task(self.pygame_event_loop(event_queue)),
            asyncio.create_task(self.idle_animation(screen, character, idle_fps, start_idle)),
            asyncio.create_task(self.handle_events(event_queue, character, start_recording)),
            asyncio.create_task(Record(start_recording, start_voice_to_text, start_idle, start_thinking).record()),
            asyncio.create_task(self.thinking_animation(screen,character, start_thinking, idle_fps)),
            asyncio.create_task(self.voice_to_text(start_voice_to_text, start_generating_ai_response)),
            asyncio.create_task(self.run_character_ai(start_generating_ai_response, start_ai_speaking, start_thinking)),
            asyncio.create_task(self.start_ai_speak(start_ai_speaking, start_idle)),
            asyncio.create_task(self.talking_animation(screen, character, talking_fps, start_ai_speaking)),

        ]

        try:
            await asyncio.gather(*self.tasks)
        except asyncio.CancelledError:
            pass
        finally:
            pygame.quit()
    
    def __del__(self):
        print(f"Destroyed instance: {self.__class__}")
        
    
    