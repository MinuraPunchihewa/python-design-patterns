from english import English
from spanish import Spanish
from adapter import Adapter


objs = []

english = English()
spanish = Spanish()

objs.append(Adapter(english, speak=english.speak_english))
objs.append(Adapter(spanish, speak=spanish.speak_spanish))

for obj in objs:
    print("{} says '{}'\n".format(obj.name, obj.speak()))