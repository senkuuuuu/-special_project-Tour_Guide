import pyaudio
import wave
import asyncio

class Record:
    def __init__(self, start_recording, start_voice_to_text, start_idle, start_thinking):
        self.sample_rate = 44100
        self.start_recording = start_recording
        self.start_voice_to_text = start_voice_to_text
        self.start_idle = start_idle
        self.start_thinking = start_thinking
        self.format = pyaudio.paInt16
        self.channels = 1
        self.chunk = 1024
        self.filename = 'temp_input.wav'
        self.is_recording = False

    async def record(self):
        while True:
            await self.start_recording.wait() # Wait for the event to be set
    
            if self.is_recording:
                continue  # Avoid starting multiple recordings

            self.is_recording = True

            # Initialize PyAudio
            audio = pyaudio.PyAudio()
            stream = audio.open(format=self.format, channels=self.channels, rate=self.sample_rate, input=True, frames_per_buffer=self.chunk)

            print("\nRecording...")
            frames = []

            try:
                while self.start_recording.is_set():
                    data = stream.read(self.chunk, exception_on_overflow=False)
                    frames.append(data)
                    await asyncio.sleep(0)
            except Exception as e:
                print(f"Error during recording: {e}")
            finally:
                # Cleanup resources
                stream.stop_stream()
                stream.close()
                audio.terminate()

                print("Finished recording.")
                with wave.open(self.filename, 'wb') as wf:
                    wf.setnchannels(self.channels)
                    wf.setsampwidth(audio.get_sample_size(self.format))
                    wf.setframerate(self.sample_rate)
                    wf.writeframes(b''.join(frames))

                self.is_recording = False

                self.start_recording.clear()
                self.start_idle.clear()

                self.start_voice_to_text.set()
                self.start_thinking.set()
