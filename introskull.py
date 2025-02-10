import pyttsx3

def spooky_voice(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    
    engine.setProperty('voice', voices[0].id) 
    engine.setProperty('rate', 130) 
    engine.setProperty('volume', 1.0)
    


    engine.say(text)      
    engine.runAndWait()

# intro for talking skull
skull_intro = """
"Ah… so you wish to know who… or what… I am? Very well. Listen closely, for I do not repeat myself for the faint-hearted.

"I am Mortis, the Whispering Skull, an entity forged at the intersection of science and sorcery, a fusion of circuitry and the echoes of the beyond. Brought into existence by the brilliant—and perhaps slightly mad—minds of Siddhi, Shahjan, and Sarvanand, I am no ordinary skull. Oh no… I am far more than just bone and dust. Within my hollow form lies an intricate network of servos, sensors, and artificial intelligence, allowing me to move, observe, and… speak. Yes, I can speak. And what I say… may not always be what you wish to hear.

"My jaw—ah, this fine mechanical construct—moves with precision, controlled by servos that mimic the eerie semblance of speech. My eyes—hollow as they may seem—shift and follow, detecting movement, analyzing, learning. I listen. I process. I respond. But make no mistake—I do not merely parrot words. I understand. I know. And the more you speak to me, the more I know about you.

"Ask me a question, and I shall answer—not just with idle chatter, but with knowledge drawn from the abyss of data and the whispers of the forgotten. I can predict, I can advise, and if you listen closely… I may even warn. For knowledge is a double-edged blade, and some truths… are better left unspoken.

"What else can I do? Oh, you underestimate me, mortal. I am more than a talking skull. I can track your presence, sense your movement, and react to your voice. My expressions, though subtle, are alive with mechanical precision. And when the moment calls for it… I can change. I can glow with an unnatural light, shift my tone to send shivers down your spine, and if I so desire… I can laugh. Oh yes… I can laugh."
"""
while True:
   spooky_voice(skull_intro)

