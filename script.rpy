define David = Character("You")
define bff = Character("Claire")
define j = Character("Joshua")
define r = Character("Rachel")
define guard = Character("Unit 15489204")
define unknown = Character("Unknown Human")

image joshua = "boy.png"
image joshuaAngry = "boyangry.png"
image joshuaConfused = "boyconfused.png"
image joshuaScared = "boyscared.png"

image claire = "claire.png"
image claireDisappointed = "clairedisappointed.png"
image claireHappy = "clairehappy.png"
image claireNervous = "clairenervous.png"
image claireStabbed = "claireStabbed.png"
image claireStabbed2 = "claireStabbed2.png"

image rachel = "girl.png"
image rachelHappy = "girlhappy.png"
image rachelScared = "girlscared.png"

image david = "mike.png"
image davidAngry = "mikeAngry.png"
image davidSad = "mikeSad.png"
image davidBloody = "mikeBloody.png"

image cop1 = "robotcop.png"
image cop2 = "robotcop2.png"
image cop3 = "robotcopgirl.png"

image claireCop = "claire+Police.png"

image hideout = "hideout.jpg"
image city = "Cityscape.jpg"
image city2 = "Cityscape2.jpg"
image waste = "Wasteland.jpg"
image museum = "Museum.jpg"
image walmart = "Walmart2.jpg"
image checkpoint = "Checkpoint.jpg"
image night = "night.jpg"
image black = "black.jpg"

define audio.shot = "audio/Gun+Silencer.mp3"
define audio.stab = "audio/Stab.mp3"
define audio.unstab = "audio/Unstab.mp3"
define audio.fall = "audio/Fall.mp3"
define audio.stall = "audio/HovercraftStall.mp3"
define audio.fire = "audio/FIRE!!!.mp3"
define audio.radio = "audio/Radio.mp3"
define audio.crate = "audio/Crate.mp3"
define audio.paper = "audio/Paper.mp3"

define audio.wasteland = "music/scene3,4.mp3"
define audio.fallsApart = "music/scene5.5,7,9,10.mp3"
define audio.museum = "music/scene5.mp3"
define audio.walmart = "music/scene6.mp3"
define audio.safe = "music/scene8.mp3"
define audio.police = "music/scene2.mp3"

# The game starts here.
label start:
    scene city
    "It is the year 2754. Robots have taken over the planet, exterminating almost all of human life in the process."
    "You survived by hiding in the cellar of the machine shop you used to work in with Claire, your friend since childhood. Since then, you’ve endeavored to stay alive by remaining hidden as much as you can."
    "From what you gathered, you live in the bubble 375, a nearly perfect city separated from the outside by a large dome."
    "You’ve never been outside, and you don’t care to change that. You both live comfortably where you are."
    scene city2 with dissolve
    show text "{size=50}Steel Souls{/size}\n\n{size=18}Click to continue{/size}" at truecenter
    with dissolve
    pause
    hide text
    with dissolve

label Scene1:
    scene hideout with fade
    stop music fadeout 3.0

    "You are sitting in your hideout with Claire, listening to your homemade radio. As you scan the channels, the static suddenly resolves into words."

    play sound radio loop

    "Radio" "BREAKING NEWS: SIGNS OF LIFE WERE DISCOVERED TO THE NORTH OF THE DOME. THE HUMANS APPEAR TO HAVE USED THE DEFUNCT ‘BLACK MUSEUM’ AS A DOMICILE FOR A BRIEF SPAN."
    "Radio" "SECURITY PATROLS HAVE BEEN DISPATCHED TO SWEEP THE AREA. WE WILL REPORT ANY FURTHER INFORMATION AS IT COMES IN."

    stop sound fadeout 1.0

    "As the signal dissolves back to static, Claire turns to you."

    show claireNervous
    bff "They’ll be killed if they get found!"
    hide claireNervous
    show david
    David "Yeah. What do you care?"
    hide david
    show claire
    bff "Well, what if we found them first?"
    hide claire
    show david
    David "And what would that do except get us killed?"
    hide david
    show claireDisappointed
    bff "Are you kidding me? We could warn them."
    hide claireDisappointed
    show claireHappy
    bff "And besides, we could meet others who are just like us."
    hide claireHappy
    show davidAngry
    David "To hell with that, I’d rather stay safe here. I don’t care what happens to them."
    hide davidAngry
    show claireDisappointed
    bff "Please, David. You can’t just leave them to die."
    bff "Besides, they might be useful allies."
    hide claireDisappointed
    stop sound
    menu:
        "Go with Claire to find the humans":
            show david
            David "I guess it wouldn’t hurt to try to find them..."
            hide david
            show claireHappy
            bff "Great! Grab your stuff and let’s go!"
            hide claireHappy
            show david
            David "How do you propose we get out of the dome?"
            play music police fadein 2.0
            hide david
            show claire
            bff "About that. I have an idea, and I don’t think you’ll like it..."
            hide claire
            jump Scene2
        "Stay put":
            show david
            David "Still no. We have enough trouble as it is."
            hide david
            show claire
            bff "I thought you might say that. You’re coming with me, even if I have to drag you."
            hide claire
            show davidAngry
            David "Fine. I’ll go get my stuff."
            hide david angry
            show david
            play music police
            David "How do you propose we get out of the dome?"
            play music police fadein 2.0
            hide david
            show claire
            bff "About that. I have an idea, and I don’t think you’ll like it..."
            hide claire
            jump Scene2
label Scene2:
    scene black
    "Claire was right. You hate this plan."
    "You are curled up in a crate on the back of a stolen hovercraft. Your legs ache from the single position and you are worried that your teeth are chipped from clacking together over every bump."
    "Just when you are fed up enough to jump out of the craft and finally stretch, you feel it slow and stop. Though it’s muffled, you can hear Claire’s voice."

    bff "Good evening, unit 15489204. Unit 13426 requesting permission to pass."
    guard "Denied. You are not registered as an approved craft. You cannot exit the dome. Please turn back."
    bff "Sir? I’m certain I got my registration approved before I left."

    play sound paper
    "You hear rustling."

    bff "Here’s my paper copy."
    guard "This is expired. Permission denied. Turn back or face termination."

    "It sounds like Claire is in trouble. You consider the knife at your belt. If you were fast enough, you might manage to disable the guard before he could kill you both."
    "Of course, he could also raise an alarm, and then you’d both be killed almost immediately."
    stop sound
    menu:
        "Jump up and stab the guard":
            scene checkpoint
            play sound crate
            show davidAngry
            "You can’t just let Claire die. You shove the lid of the crate off and stand, only to stumble as your legs fail to wake up."
            hide davidAngry
            show cop1
            play sound shot
            scene black with fade
            queue sound fall
            stop music fadeout 3.0
            "Before you hit the ground, the guard has put a machine gun round through your head."
            "GAME OVER"
            return
        "Stay put and hope":
            "You decide to sit tight in the hopes that Claire will pull through, or at the very least you’ll survive."

            bff "Please, Unit 15489204. I need to dump this refuse. If I return to the shop with the package, I’ll be scrapped for sure. Could you please let me through this once? I promise it won’t happen again."
            guard "Fine. Just this once. Unit 13426 cleared for transit."
            stop music fadeout 2.0
            "Your faith paid off. You hear a beep and suddenly the craft is speeding off again through the checkpoint and out of the dome."

            jump Scene3
label Scene3:
    "A couple of hours and multiple more nerve wracking checkpoints later, and the two of you have escaped the dome. You’re stunned that Claire made it through them all."
    play sound crate
    scene waste
    play music "<from 2>music/scene3,4.mp3" loop
    "You feel the speeder halt and harsh sunlight floods in as Claire lifts the lid of your crate."
    "It’s a few moments before you can see where you are. You aren’t sure what you were expecting, but it sure wasn’t this. As far as the eye can see, the world is a completely barren desert."
    "A couple of crumbling buildings still stand along the horizon, straining to stay up. Some of the deeper depressions sport a few scraggly blades of grass, but they appear to be the only life."

    show david
    David "This is what Earth looks like? What the hell did the humans do?"
    hide david
    show claire
    bff "You’re human too, you know. Don’t get too high and mighty."
    hide claire
    show david
    David "That doesn’t answer the question."
    hide david
    show claireDisappointed
    bff "Why should I know? You’re the smart one. We probably poisoned the water with chemical byproducts or something."
    hide claireDisappointed
    show davidAngry
    David "It’d be just like them to destroy the whole planet with their recklessness. I bet they built the robots too."
    hide davidAngry
    show claireDisappointed
    bff "Probably. But what does that matter now? We need to get moving again. Come on."
    hide claireDisappointed
    stop sound
label Scene4:
    scene night with fade
    play sound "<from 0 to 3>audio/HovercraftStall.mp3"
    "You and Claire drive until the sun sets and your hovercraft sputters and dies. A quick inspection reveals it overheated. Your craft needs to cool at least a few hours, and probably longer, so you decide to camp for the night."
    "Claire looks annoyed at the delay. She hops off the craft and kicks it."

    show claireDisappointed
    bff "Stupid thing!"
    hide claireDisappointed
    show david
    David "Calm down! It’ll be working by tomorrow, at least if you don’t break it."
    hide david
    show claireNervous
    bff "The police are looking for the other survivors! We need to warn them. We don’t have time for our hovercraft to be dead."
    hide claireNervous
    show davidAngry
    David "Then how do you propose we get to your humans? Fly? Don’t answer that, it was rhetorical."
    hide davidAngry
    show david
    David "Seriously though, help me unpack. We’re not going anywhere. Trust me, I used to fix the things for a living."
    hide david
    show claire
    bff "Want me to help start the fire?"
    hide claire
    show david
    David "No. We can’t light a fire; it’d give us away."
    hide david
    show claire
    bff "It will also help keep us from freezing"
    hide claire
    "She has a point; the temperature is dropping. But you still would prefer not to wake up to the muzzle of a machine gun."
    menu:
        "Light the fire and hope you don't get found":
            show davidAngry
            David "Fine."
            play sound fire loop fadein 1.0
            hide davidAngry
            "You toss her the book of matches in your bag and she goes to work. Before long you are forced to admit she was right. It is much more comfortable with the heat."
            show cop2
            stop sound fadeout 1.0
            play sound shot
            scene black with fade
            queue sound fall
            "Unfortunately, you were also right. A little past midnight, you’re both awakened by the lights of a police patrol. Even Claire can’t lie her way out of this. Your campfire lasts longer than her pleas do."
            "GAME OVER"
            return
        "Tough it out without a fire":
            show davidAngry
            David "Again, that’s a terrible idea, unless you’re trying to get us caught. No."
            hide davidAngry
            show claireDisappointed
            bff "Fine."
            hide claireDisappointed
            "She spends the rest of the night complaining, but you make it morning without incident. When you wake, you find the hovercraft functional and ready to go. You hop back on and continue onwards."
label Scene5:
    scene waste with fade
    "It’s a few hours until you spot the museum on the horizon, and by the time you reach it, the sunset is starting to gild the rocky waste."
    stop music fadeout 4.0
    "Both you and Claire hop off the hovercraft and approach the building. You go first, knife at the ready, just in case the patrols arrived first."
    scene museum with fade
    play music "<from 2.7>music/scene5.mp3" fadein 2.0
    "You wrench open the old, rusted doors to reveal a gallery the size of an airplane hanger, filled to the brim with old paintings. The air is thick with whirling dust and the massive windows are cracked."
    "You walk up to the first dusty painting and blow across it. Claire coughs as a cloud billows around you, but you are spellbound by the canvas. You’ve never seen so much raw emotion as is in these old paintings."

    show claireHappy
    bff "Here’s something only we can make. They can’t."
    hide claireHappy

    "You nod. There’s something in these halls that is completely gone from the dome. You walk between painting after painting, trying to understand exactly how these artists created such work."
    "You’re so caught up in your own world that you nearly miss the teddy bear. You pick it up and dust off its care-worn fur. You flip it over and reveal the tag."
    "'Wal*Mart,' it reads."

    show claireDisappointed
    bff "What’s that?"
    hide claireDisappointed
    show david
    David "I think I know where they went. We passed a shop with a similar sign earlier today."
    hide david
    show claireHappy
    bff "Great! Let's go."
    hide claireHappy
    show david
    David "Right now? Why do you want to go so badly?"
    hide david
    show claireDisappointed
    bff "We need to warn them! The police patrols are after them."
    hide claireDisappointed
    show davidAngry
    stop music fadeout 3.0
    David "Claire, if we go galavanting off in the dark, we’re just going to get captured. This is like your stupid idea with the fire. It’s almost like you want us to get caught..."
    hide davidAngry
    play music fallsApart loop
    "You’re struck by a thought: what if she does want to get caught? How would you tell if she were truly a robot?"

    show davidSad
    David "Claire, are you a robot?"
    hide davidSad
    show claireNervous
    bff "I-"
    bff "I just-"
    bff "I mean-"
    bff "...Why do you think that?"
    hide claireNervous
    show davidAngry
    David "You didn’t answer the question. Yes or no, Claire."
    hide davidAngry
    show claireNervous
    bff "..."
    bff "...No"
    hide claireNervous
    menu:
        "Believe Claire":
            stop music fadeout 3.0
            show david
            David "Great. Then you have no reason to go out now and get us killed. We can leave tomorrow."
            hide david
            show claireDisappointed
            bff "Fine."
            hide claireDisappointed
            jump Scene6
        "Decide Claire is a robot":
            "Claire must be a robot. What else would explain her desperate desire to find the humans, other than being programmed to do so? That’s why she wanted the fire, just to get you found out."
            "That’s also why she was so unsurprised by the waste. She’s been here before. And you certainly know she’s good enough at lying to pull it off."
            "You can’t stay with her; she’ll probably turn you in. You’re still holding your knife. You know enough about robots to know where the battery pack is. If you could get a direct hit..."
            show claireNervous
            play sound stab
            "You close the distance between the two of you and slide the knife into her."
            hide claireNervous
            show claireStabbed
            play sound unstab
            queue sound fall
            "As you pull it free, red blood leaks out of the wound. She lets out a cry and falls on the floor. No sparks. No oil. Just so much blood."
            hide claireStabbed
            jump Scene9
label Scene6:
    scene waste with fade
    "Now well-rested, you both set out for Wal*Mart. This time it’s only a few hours. Claire gets more and more eager the closer you get. Upon arriving, she immediately jumps off the hovercraft and runs to the doors."

    show davidAngry
    David "Claire! Wait!"
    hide davidAngry

    "Claire pays you no heed and instead throws the doors wide open."

    scene walmart with fade
    "Inside, two people huddle around a small, smokey fire. They’ve collected supplies from the store, at least enough to make a serviceable camp."
    show joshuaAngry
    "The older one gets up and walks over to the two of you."

    unknown "Who the hell are you?"
    hide joshuaAngry
    show claireHappy
    bff "I’m Claire, this is David and we come in peace. We’re also humans and we’ve been looking for you."
    hide claireHappy
    show joshuaAngry
    unknown "And why should I believe that load of baloney? Get out before I cut your wires."
    hide joshuaAngry
    show david
    David "Okay, okay, we’re leaving."
    David "One thing first: I think this is yours."
    hide david

    "You pass him the bear and then turn to leave."
    show joshua
    play music walmart fadein 3.0
    "His frown quickly changes into a softer expression. He stares at the bear."

    unknown "Wait!"
    hide joshua

    "You pause and turn around."

    show joshuaConfused
    unknown "How did you find this?"
    hide joshuaConfused
    show david
    David "I saw it when I passed by the abandoned art museum a couple of hours from here. I thought you might’ve wanted it."
    hide david
    show joshua

    "He stares at you for a second before speaking."

    j "I’m Joshua. That’s Rachel. You’re welcome to stay."
    hide joshua

    "You’re a bit surprised that he’s letting you, but you take a seat next to Rachel."
    show joshua

    j "Rachel! Look what he brought."

    "He passes her the bear."
    hide joshua
    show rachelHappy
    "Rachel turns to you and hugs you."

    r "Thank you. That bear was my little sister’s. Her name was Emily."
    hide rachelHappy
    show david
    David "You have a sister? How is she?"
    hide david
    show rachelScared
    r "They killed her when we got caught."
    hide rachelScared
    show davidSad
    David "Oh."
    David "I'm sorry."
    hide davidSad
    show rachel
    r "Oh, don’t be. Here, do you want dinner?"
    hide rachel
    stop music fadeout 3.0
    "You accept the food and let her change the subject. You stay up late talking to them. Claire is nowhere to be found, but you think nothing of it. You go to bed happy and full."
label Scene7:
    play music fallsApart
    "You wake up to garish red light flooding the store. The police are here!"
    "You force yourself up and grab your knife. Maybe you can take enough of them down to escape. You wake the other two and ready to fight."
    "You still can’t find Claire. Where is she? Then you spot her."
    show claireCop
    "She’s with the police."
    hide claireCop

    show davidAngry
    David "Claire! Why?"
    hide davidAngry
    show claireCop
    bff "Stand down and you’ll be safe."

    "That’s a lie and you know it."
    hide claireCop
    show claireNervous
    "You’re not about to go down without a fight. There’s two robots and Claire. The three of you can handle it. You pull your knife and charge."
    "You hear clangs as the robots go down, but you’re focused on Claire."
    "You trusted her."
    "You believed her."
    "And she did this?"
    show claireStabbed2
    play sound stab
    queue sound unstab
    "It’s easier than you expected to slide the knife between her ribs. She falls without a sound."
    "In the dark, her blood looks like oil."
    hide claireStabbed2
    scene walmart
    show davidBloody
    "How do you forgive her for this? Can you?"
    hide davidBloody
    menu:
        "Forgive her. It doesn't matter. She's dead now":
            stop music fadeout 1.0
            "She’s dead. It’s over, and everyone’s safe. You help Joshua drag the police-bots out, then you turn to Claire. She seems so small, so insignificant."
            play music safe
            "She was your best friend."
            "She nearly killed you."
            "She brought you to see the museum. She brought you here"
            "She turned you in."
            "You close her eyes. You lift her body and bring her out. She’s so light."
            "You go back to the Wal*Mart and find a shovel. You’re not sure what she deserves, but you at least owe her this."
            scene waste
            "You dig her grave and leave her to rust into the desert soil."
            jump Scene8
        "Never forget. She's a traitor.":
            jump Scene10
label Scene8:
    "Joshua decides the Wal*Mart is no longer safe. If the police bots sent a signal before dying, there could be several units converging on the store right now. You decide he’s probably right."
    show rachelHappy
    r "You could come with us, if you want."
    hide rachelHappy
    show david
    David "Really?"
    hide david
    show rachelHappy
    r "Sure. You fought your friend for us. Plus, you brought me Emily’s bear."
    hide rachelHappy
    show rachel
    r "It’s not a comfortable life, but it’s better than nothing."
    hide rachel
    show david
    David "I don’t really know what to say..."
    hide david
    menu:
        "Go with Rachel and Joshua":
            show david
            David "I'd love to."
            hide david
            show rachelHappy
            r "I guess you should go help Joshua load up, then."
            hide rachelHappy

            "Rachel’s right. It’s not a comfortable life, but it sure beats living alone in the basement of your shop. They never replace Claire, but you learn to love them just the same."
            scene black
            stop music fadeout 3.0
            "GAME OVER"
            return
        "Go back to the dome":
            show david
            David "I think I’d rather go home."
            hide david
            show rachel
            r "Too bad. Well, you’re welcome anytime."
            hide rachel
            show david
            David "Thanks."
            hide david

            scene waste
            "You leave and head back towards the dome. It’s hard to manage without Claire’s knack for subterfuge, but you successfully sneak back in and go back to your now-empty shop basement."
            "You spend your days scavenging for food and your nights completely alone, trying to forget Claire’s face. It’s not a comfortable life, but at least you’re alive."
            stop music fadeout 3.0
            "GAME OVER"
            return
label Scene9:
    "You stare at her body for a long while before you can force yourself to move. How can you trust yourself after what you did? Where do you go next?"
    scene night
    "You leave the building with no plan in mind, just trying to get as far as possible from her empty eyes. You’re still covered in her blood but you don’t care. You just run."
    "Time seems to fade as you run. You could have been traveling for a few minutes, or maybe a century. The desert is slowly getting dimmer around you. You fall to your knees, unable to get back up."
    "The last thing you see is your hands, still soaked in blood, with wires running under the skin."
    stop music fadeout 3.0
    scene black with fade
    "GAME OVER"
    return
label Scene10:
    "She’s dead. It’s over, and everyone’s safe. You help Joshua drag the police-bots out, then you turn to Claire. She seems so small, so insignificant."
    "She was your best friend."
    "She nearly killed you."
    "She brought you to see the museum. She brought you here."
    "She turned you in."
    "This is all their fault. If they hadn’t gotten caught at the museum, you’d still be at home with her."
    "Part of you knows this is irrational, but the rest of you doesn’t care. You can’t forgive her, and you can’t forgive them. You grab your knife."
    show davidBloody
    "Rachel pleads. Joshua fights. Neither of them live. You can’t see past the pounding anger."
    "Your arm hurts from where Joshua stabbed it. You look at the dark stain spreading across your sleeve. Through the gash, you can swear you see wires. You realize that you’re glad."
    stop music fadeout 3.0
    scene black with fade
    "GAME OVER"
    return
