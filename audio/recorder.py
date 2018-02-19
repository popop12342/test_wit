import pyaudio
import wave
from wit import Wit

def recReturnWavIterator(RECORD_SECONDS, CHUNK_SIZE, client):

    #--------- SETTING PARAMS FOR OUR AUDIO FILE ------------#
    FORMAT = pyaudio.paInt16    # format of wave
    CHANNELS = 2                # no. of audio channels
    RATE = 44100                # frame rate
    CHUNK = CHUNK_SIZE          # frames per audio sample
    #--------------------------------------------------------#
 
    # creating PyAudio object
    audio = pyaudio.PyAudio()
 
    # open a new stream for microphone
    # It creates a PortAudio Stream Wrapper class object
    stream = audio.open(format=FORMAT,channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)
    print("Listening") 
    for i in range(int(RATE / CHUNK * RECORD_SECONDS)):
        # read audio stream from microphone
        data = stream.read(CHUNK)
        yield data
    print("Finished recording")

def RecognizeSpeech(CHUNK_SIZE):
    client = Wit('EGYXBUP5MBO2C3FH67L6IP2JNZ3DLRCW')
    resp = client.speech(recReturnWavIterator(5,CHUNK_SIZE,client),None,{'Content-Type': 'audio/wav', 'Transfer-encoding': 'chunked'})
    print('Yay, got Wit.ai response: ' + str(resp))