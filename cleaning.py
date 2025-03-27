import random

s = "illustrations/an.jpg illustrations/Betto.png illustrations/Chairs.png illustrations/Finalgirl.png illustrations/gatoCool.png illustrations/hayloft_I.png illustrations/hayloft_ii.png illustrations/kissing.png illustrations/literally_me.png illustrations/mika_&_moonchild_filter.png illustrations/tv_glow_fixed.png"
def cleanUp(s):
    sp = s.split()
    clean = []

    for item in sp:
        r = random.randint(1,3)
        #clean.append(f"\"{item}\",\n" )
        if (r == 1):
            clean.append(f"<div class=\"card card_small\"><img src=\"{item}\" alt=\"Artwork\"></div>\n")
        if (r == 2):
            clean.append(f"<div class=\"card card_medium\"><img src=\"{item}\" alt=\"Artwork\"></div>\n")
        if (r == 3):
            clean.append(f"<div class=\"card card_large\"><img src=\"{item}\" alt=\"Artwork\"></div>\n")

    return clean

file = open("illustrations.txt", 'a')

ts = (cleanUp(s))

for t in ts:
    file.write(t)


# <!-- <div class="pin_container">
#         <div class="card card_small"><img src="image1.jpg" alt="Artwork 1"></div>
#         <div class="card card_medium"><img src="image2.jpg" alt="Artwork 2"></div>
#         <div class="card card_large"><img src="image3.jpg" alt="Artwork 3"></div>
#         <div class="card card_medium"><img src="image4.jpg" alt="Artwork 4"></div>
#         <div class="card card_small"><img src="image5.jpg" alt="Artwork 5"></div>
#         <div class="card card_large"><img src="image6.jpg" alt="Artwork 6"></div>
#         <div class="card card_medium"><img src="image7.jpg" alt="Artwork 7"></div>
#         <div class="card card_small"><img src="image8.jpg" alt="Artwork 8"></div>
#         <div class="card card_medium"><img src="image9.jpg" alt="Artwork 9"></div>
#     </div> -->



