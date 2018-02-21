from wit import Wit

def RecognizeSpeech(AUDIO_FILENAME,CHUNK_SIZE):
   client = Wit("EGYXBUP5MBO2C3FH67L6IP2JNZ3DLRCW") 
   def wavIterator():
       wav = open(AUDIO_FILENAME, 'rb')
       chunk = wav.read(CHUNK_SIZE)
       while chunk:
           yield chunk
           chunk = wav.read(CHUNK_SIZE)
   resp = client.speech(wavIterator(), None,
           {'Content-Type': 'audio/wav', 'Transfer-encoding':'chunked'})
   print(resp)