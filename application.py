def Voice_rec();
  fs = 48000
  
  # seconds
  duration = 5 
  myrecording = sd.rec(int(duration * fs),
                        samplerate=fs, channels=2)
  sd.wait()
  
  #Save as a FLAC file at the correct sampling rate
  return sf.write('my_audio_file.flac', myrecording, fs)
  
  master = Tk()
  
  label(master, text=" Voice Recorder : "
        ). grid(row=0, sticky=W, rowspan=5)
        
  b = Button(master, text="Start", command=Voice_rec)
  b.grid(row=0, column=2, columnspan=2, rowspan=2, padx=5, pady=5)
  
  mainloop()
