# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define narrator = Character(callback = name_callback, cb_name = None)
define thom = Character("Mr Thomlinson")
define king = Character("Kingshuk Hossain", callback = name_callback, cb_name = "kingshuk")
define ish = Character("Ishmam Ahbab", callback = name_callback, cb_name = "ishmam")
define rich = Character("Richard Carter", callback = name_callback, cb_name = "richard")
define paarth = Character("Paarth Bansal", callback = name_callback, cb_name = "paarth")
define cf = Character("Charles Fenton Tun")
define ff = Character("Frederick Fenton Tun")
define friel = Character("Ms Friel")
define jones = Character("Mrs Jones")
define ager = Character("Mr Ager")
define rager = Character("Mr Rager")
define cole = Character("Mr Cole")
define seed = Character("Mr Seed", callback = name_callback, cb_name = "mrseed")
define sam = Character("Sam Quaye")
define bridge = Character("Bridget")
define hemanth = Character("Hemanth")
define dharan = Character("Dharan")
define laksh = Character("Lakshya Dave")
define best = Character("Johnathon Best")
define stm = Character("Site team member", callback = name_callback, cb_name = "site")

image black = Solid((0, 0, 0, 255))
image kingshuk normal = At('kingshuk_normal', sprite_highlight('kingshuk'))
image kingshuk close = At('kingshuk_close', sprite_highlight('kingshuk'))
image kingshuk look = At('kingshuk_look', sprite_highlight('kingshuk'))
image kingshuk think = At('kingshuk_think', sprite_highlight('kingshuk'))

image ishmam normal = At('ishmam_normal', sprite_highlight('ishmam'))
image ishmam close = At('ishmam_close', sprite_highlight('ishmam'))
image ishmam look = At('ishmam_look', sprite_highlight('ishmam'))
image ishmam frown = At('ishmam_frown', sprite_highlight('ishmam'))
image ishmam closefrown = At('ishmam_closefrown', sprite_highlight('ishmam'))

image richard normal = At('richard_normal', sprite_highlight('richard'))
image richard close = At('richard_close', sprite_highlight('richard'))
image richard look = At('richard_look', sprite_highlight('richard'))

image paarth approve = At('paarth_approve', sprite_highlight('paarth'))
image paarth normal = At('paarth_normal', sprite_highlight('paarth'))
image paarth close = At('paarth_close', sprite_highlight('paarth'))
image paarth look = At('paarth_look', sprite_highlight('paarth'))

image nobody m = At('nobody_m', sprite_highlight('site'))
image nobody m = At('nobody_m', sprite_highlight('mrseed'))

transform scene1:
  xalign 0.5
  #yalign 0.2
  zoom 1.0

transform doing:
    zoom 0.35
    xalign 0.6 yalign 1.0
    linear 0.25 xalign 0.5 yalign 1.0
    linear 0.25 xalign 0.6 yalign 1.0
    repeat

transform stab:
    zoom 0.35
    xalign 0.6 yalign 1.0
    linear 0.25 xalign 0.5 yalign 1.0
    linear 0.25 xalign 0.6 yalign 1.0


transform masonLaunch:
    zoom 0.35
    xalign 0.3 yalign 0.0
    linear 1.0 yalign 1.0

transform throb:
    # banquo throbs
    # banquo ghost: bleurghhh!!!
    # banquo: I'm really feeling it ~ Ngghhh~~~
    zoom 0.35
    xalign 0.5
    yalign 1.0
    linear 0.25 zoom 1.0
    linear 0.25 zoom 1.25
    repeat

transform walkinright:
    zoom 0.35
    xalign 1.0 yalign 1.0
    easein 0.5 xalign 0.85 yalign 1.0

transform slam:
    zoom 0.35
    xalign 0.5 yalign 1.0
    linear 0.15 yalign 2.0
    easein 0.75 xalign 0.5 yalign 1.0

transform midleft4:
    zoom 0.35
    xalign 0.1
    yalign 1.0

transform midcenterleft4:
    zoom 0.35
    xalign 0.3
    yalign 1.0

transform midcenterright4:
    zoom 0.35
    xalign 0.7
    yalign 1.0

transform midright4:
    zoom 0.35
    xalign 0.9
    yalign 1.0



transform midleft3:
    zoom 0.35
    xalign 0.15
    yalign 1.0

transform midcenter3:
    zoom 0.35
    xalign 0.5
    yalign 1.0

transform midright3:
    zoom 0.35
    xalign 0.85
    yalign 1.0

transform midleft2:
    zoom 0.35
    xalign 0.2
    yalign 1.0

transform midright2:
    zoom 0.35
    xalign 0.8
    yalign 1.0

# The game starts here.

label start:

    show black
    stop music fadeout 2.0
    #play music "stories of afternoon.mp3" volume 1.0 loop
    play music "ambience and clock.mp3" volume 0.5 loop

    "Foreword by Mr Thomlinson, FRHistS, Head of History at KEGS"
    "On the Tragedy of Bedford Bog"
    #show mr thomlinson at kegs, probably a scene bg
    #mr thomlinson looks like old neil
    thom "It is with great academic reluctance, that I take up the pen to reflect upon the regrettable incident at Bedford Bog."
    thom "The events that transpired there were not merely the result of circumstance"
    thom "but the slow aggregation of neglect, administrative hubris,"
    play sound "snoring.mp3" volume 1.0 loop
    thom "and a poor grasp of pa- *snore*"
    thom "*snore*"
    thom "..."
    stop sound fadeout 1.0
    thom "This job can be painful at times."
    thom "Historical analysis provides a crystal clear perspective on our faults"
    thom "and it can be difficult, to take ownership of your mistakes."
    "..."
    thom "Yes the bog."
    thom "It began, innocently enough, with a field trip."
    thom "A time-honoured educational tradition designed to break the spirit of the more rebellious Year 10s."
    thom "In there, Kingshuk - who styled himself Heathcliff in a move both literary and deeply concerning"
    thom "became a figure of myth, a martyr and terrifying charisma."
    "..."
    thom "I have drawn several diagrams on the whiteboard, if you'll look here - "
    play sound "<from 5>snoring.mp3" volume 1.0 loop
    thom "*snore*"
    thom "*snore*"
    stop sound fadeout 1.0
    thom "- huh, oh dear, harrumph, they appear to have been wiped clean by the PE department, who needed to revise for a sit up-based assessment."
    thom "A tragedy in its own right."
    thom "And so we must remember, as all historians must,"
    stop music fadeout 1.0
    thom "that when power is left unexamined, and children unheard, even the most civilised of communities may find itself.."
    play sound "<from 10>snoring.mp3" volume 1.0 loop
    thom "*snore*"
    thom "..."
    thom ".."


    #show desert tent
    scene bg felstedfront at scene1 with fade
    stop sound fadeout 1.0
    play music "strange territory.mp3" volume 1.0 loop

    "11:20 AM Weather/Dry 43°C"
    "Felsted Front - Day 6"
    "..."
    "They had left KEGS as students, eager and naïve,"
    "excited for their school trip to the deserts of the Felsted Front, where they would assist Médecins Sans Frontières."
    "Under their guidance, they were to learn about medicine, aid in humanitarian efforts, and perhaps, make a difference."

    scene bg medicaltent at scene1 with fade

    "A man lies on the cot, his leg almost fully torn off above the knee."
    "Doctor Hindre" "Quickly now! Hold the tourniquet a little tighter. I need more time!"
    show kingshuk normal at midcenter3 with dissolve
    "Kingshuk is wrenching the cord with all of his might. Ishmam stands on the other side of the cot apprehensively."
    king ".."
    hide kingshuk with dissolve
    "They had expected hardship."
    "They were not prepared for war."
    show kingshuk normal at midleft2
    show ishmam normal at midright2
    with dissolve
    "Ishmam leans in close, muttering sweet words to the old soldier's ears with tears a mixture of desperation and exhaustion."
    ish "Live. Stay. Stay here."
    king "You've been learning Arabic?"
    ish "I only started a week before the trip. I'm only really doing it for my family but in a sense it's part of my identity."
    ish "It's something I ought to do really. As a muslim."
    king "You still haven't been to Mecca?"
    ish "No I.."
    #narrator ""
    "Old Soldier" "..."
    "The patient shifts uncomfortably as the adrenaline ebbs away, throbbing pain to replace it. The old soldier winces as he rubs his leg against the operating table."
    ish "No, no, careful. Don't exert yourself."
    "He pauses, as he tries to puzzle the correct words in Arabic."
    #narrator ""
    "Doctor Hindre" "Oh dear. Hmm. We may have to do without painkillers for this one."
    "The old soldier looks unfortunate. Hearing these words, he sits up in alarm."
    "The two students however, are unfazed. This is a common occurrence."
    "They hold him down as he struggles desperately to get free."

    scene bg felstedfront at scene1 with fade
    play music "mild tension.mp3" volume 1.0 loop

    show kingshuk normal at midleft2
    show ishmam normal at midright2
    with dissolve
    king "At least we get to leave at lunch."
    ish "The doctor was still going at it as well."
    ish "Y'know, in the future, I wanted to own my own GP one day, I suppose I.."
    king "I don't think a literal warzone and a GP in Ilford are really comparable on the same level. It certainly lacks this intensity."
    narrator "Kingshuk is ragged of breath as they run across the sandy grasses. "
    show richard normal at midcenter3
    show kingshuk normal at midleft3
    show ishmam normal at midright3
    with dissolve
    rich "Yo guys, you're finally back. What took so long? The food is nearly gone."
    king "We just got out of a surgery. Slashed his thigh off, caught in razor wire."
    narrator "Richard winces."
    king "He should make it but the surgeon let us go before it was over because it was overrunning so much."
    rich "While you guys were gone there was another attack. On the south side."
    king "How many times does that make it now? 4 times? Good grief, we're charity aid for heavens sake!"
    ish "Is it really possible to remain non-combatants when we are forcibly brought into combat time and time again?"
    stop music fadeout 1.0
    play audio "machine guns distant.wav" volume 2.0
    narrator "Gunshots ring out from the residential camps."
    rich "Oh dear."
    play sound "crowd.mp3" volume 0.6 loop fadein 0.5
    hide kingshuk
    hide ishmam
    with dissolve
    show richard look at midcenter3
    narrator "His head turns towards the camp. People are fleeing from the tents, dragging children, stumbling over the hard and sandy ground."
    play audio "explosion.wav" volume 0.8
    play audio "whinny.wav" volume 0.8
    narrator "A horse whinnys as an explosion collapses one of the tents."
    play music "on the battlefield.mp3" volume 1.0 loop
    hide richard
    show kingshuk look at midcenter3
    with dissolve
    "Kingshuk looks round. Hesitating." (cb_name = "kingshuk")
    play audio "bullet whizz.wav" volume 2.0
    show kingshuk normal at midcenter3
    narrator "The threat of death loomed close. A stray bullet whizzed past, breaking them out of their trance."
    show richard normal at midleft3
    rich "Run! Holy crap. Twice in a day!"
    show ishmam look at midright3
    with dissolve
    "Ishmam's eyes are wide. His pulse is racing. He struggles to swallow down the lump in his throat as he sprints." #(cb_name = "ishmam")
    play audio "explosion.wav" volume 0.8
    show ishmam closefrown at midright3
    show kingshuk close at midcenter3
    show richard close at midleft3
    "A wall of sand and smoke shoot up beyond the camp's fences."
    "The residential tents collapse as shrapnel rains like knives."
    show ishmam frown at midright3
    show kingshuk normal at midcenter3
    show richard normal at midleft3
    "Kingshuk stumbled to his feet, coughing out grit. Richard grabbed his arm, steadying him." (cb_name = "kingshuk")
    hide ishmam
    show kingshuk normal at midleft2
    show richard normal at midright2
    with dissolve
    narrator "Through the smoke, they heard a woman's shrill, frantic, broken."
    "A mother staggered into view, dragging a boy by the shoulders. He was limp, his chest and abdomen slick with blood."
    "Mother" "Help! Please! Somebody help! My boy!"
    show richard look at midright2
    "Richard looks back, distracted by their cries for help."
    "He looks to Kingshuk."
    show kingshuk look at midleft2
    "Kingshuks face is wide. Spooked. Yet when Richard turns heel, he follows without missing a beat." (cb_name = "kingshuk")
    hide kingshuk
    hide richard
    with dissolve
    show ishmam look at midcenter3
    ish "Hey! What, where are you guys going!? King?"
    show ishmam frown at midcenter3
    hide ishmam with dissolve
    show kingshuk normal at midleft2
    show richard normal at midright2
    with dissolve
    "Kingshuk drops to the ground, clutching the boy's tiny wrist, cradling him in his arms."
    narrator "Richard throws his blazer down, pressing it to the wounds."
    king "He's bleeding out Richard! Press harder!"
    rich "Got it! He's still alive, breathing. Barely."
    hide kingshuk
    hide richard
    show ishmam frown at midcenter3
    with dissolve
    "Ishmam stands back, feet stumbling to a stop." (cb_name = "ishmam")
    show ishmam closefrown at midcenter3
    $renpy.music.set_volume(0.2, channel='music')
    $renpy.music.set_volume(0.5, channel='sound')
    "Nothing is right. The world goes quiet as Ishmam's heart hammers."
    "Just metres from him, people are dying."
    "In fact, he could die. Standing still is certain death."
    "Should he go help them?"
    "Or are they doomed?"
    "Ishmam's chest tightened. Every instinct screamed to stay put. His legs slowly stumbled."
    show ishmam look at midcenter3
    "He looks back again. The family cradling the boy." (cb_name = "ishmam")
    show ishmam normal at midcenter3
    ish "Right. Of course."
    show ishmam frown at midcenter3
    $renpy.music.set_volume(1.0, channel='music')
    $renpy.music.set_volume(1.0, channel='sound')
    
    hide ishmam
    show richard normal at midcenter3
    show kingshuk normal at midleft3
    with dissolve
    narrator "He scrambles. Bolting for where Richard and Kingshuk lay with the boy, wasting precious seconds."
    show ishmam frown at walkinright
    ish "We have no time. It doesn't matter what first aid we do here."
    narrator "He hefts the boy onto his shoulders."
    ish "We've got to live first! Quickly!"
    king "Ish.."
    "He looks up."
    king "Right."
    narrator "The dust rolled heavier. The sound of gunfire rattled closer. Still they worked, three students scrambling out of the dirt, clutching at the life of a child in a war that refused to let them rest."
    stop music fadeout 1.0
    stop sound fadeout 1.0

    scene bg medicaltent at scene1 with fade
    play music "enduring.mp3" volume 1.0 loop

    show paarth normal at midcenter3 with dissolve
    narrator "Paarth helped them drag him in through the flap of the tent. A child, limp, dust caked in his hair."
    hide paarth with dissolve
    narrator "His chest was torn open by the blast, blood soaking through the blazer pressed against it."
    play sound "sobbing.mp3" volume 0.4 loop
    narrator "His mother clutched him, crying out in Arabic, begging."
    "His father dropped to his knees, clutching at Doctor Hindre's coat."
    "Father" "Please! Save him! Help Ahmed! I beg of you!"
    "Father" "Anything! I would do anything for my boy!"
    "Doctor Hindre" "I.. There's not much we can do. The damage is catastrophic."
    #hide doctor
    show kingshuk normal at midleft3
    show ishmam frown at midright3
    show paarth look at midcenter3
    with dissolve
    "He looked over the boy, then at the students - Kingshuk, Ishmam, Paarth - their young faces pale with shock at the battlefield of wounds the boy endures.."
    hide kingshuk
    hide ishmam
    hide paarth
    with dissolve
    "Doctor Hindre" "Even if I operate, he may not live past the hour. Resources are scarce. I..."
    narrator "He falters. The tent is filled with sobbing, shouting. The mother falls against the cot, whispering prayers into her son's ear."
    show kingshuk normal at midleft3
    show ishmam frown at midright3
    with dissolve
    king "Many are injured. With what we have, we may have to triage."
    narrator "Ishmam's hands are trembling as he grips the boy's arm. His voice shakes, but his words are firm."
    ish "He's a child. Please. We have to try. We will save every life. Remember?"
    narrator "Doctor Hindre stares at them, lips tight, eyes hollow with exhaustion. For a moment, he seems to harden."
    stop sound fadeout 1.5
    play audio "yakuza desk slam.wav" volume 0.8
    "Then he slams the tray of instruments onto the table. Crumbling under the weight of his empathy."
    "Doctor Hindre" "We should be getting a resupply soon. We do keep quite the stockpile despite my abstinence to use them."
    "Doctor Hindre" "But I suppose if there's ever any time to use them, it is now."
    "Doctor Hindre" "..."
    "Doctor Hindre" "Fine! Hold him steady. Don't you dare falter!"
    "Doctor Hindre" "This will be quite the gauntlet. Children are always difficult."
    narrator "Kingshuk cleans the wound as Ishmam strokes the boy's hair, blissfully high on adrenaline - whispering in Arabic."
    ish "Stay. Do not sleep, little one. Please."
    stop music fadeout 1.0
    hide kingshuk
    hide ishmam
    with dissolve
    narrator "The scalpel descends. The surgery begins."

    play music "sarcophagus.mp3" volume 1.0 loop

    #show doctor
    show kingshuk normal at midleft3
    show ishmam frown at midright3
    with dissolve
    narrator "Ishmam swallowed hard, sweat dripping down his brow."
    "Doctor Hindre hesitated, scalpel hovering over the boy's bloodied skin."
    show paarth normal at midright3
    hide ishmam with dissolve
    "Doctor Hindre" "Kingshuk, Paarth, get ready to pin him down. He's going to thrash when the scalpel goes in. The anesthesia's completely numbed the pain but he will still be conscious."
    hide kingshuk
    hide paarth
    show ishmam frown at midcenter3
    with dissolve
    ish "Huh? What? Why aren't we using general anesthetic?"
    "Doctor Hindre" "A stray bullet hit the ventilator we use to keep patients breathing while under general anaesthesia. We're making do."
    show kingshuk normal at midleft3
    show ishmam frown at midright3
    with dissolve
    narrator "Kingshuk nodded, leaning over the cot, locking his arms against the boy's shoulders."
    "Doctor Hindre" "On my count. One.. two -"
    narrator "The scalpel sliced into torn flesh. The boy jerked violently, a choked cry breaking from his lips."
    narrator "He thrashed, legs kicking weakly against the cot."
    narrator "Kingshuk and Paarth held firm, teeth gritted, as Dr Hindre worked deeper into the wound, searching for shrapnel."
    hide kingshuk
    hide ishmam
    with dissolve
    "Mother" "Ahmed! My son-!"
    "Father" "O Allah, You are the Creator, the Originator, the Afflicter, the Healer and the Restorer. O Allah I ask by Your most beautiful names and Your exalted attributes."
    "Father" "O You who holds affliction and healing and remedy. I ask You, O Allah, to grant him healing. There is no harm except what You allow, and no benefit except from You..."
    show kingshuk normal at midleft3
    show ishmam frown at midright3
    with dissolve
    "Doctor Hindre" "Clamp! Clamp now!"
    narrator "Kingshuk's hands darted to the instrument, slipping once before gripping it hard, his fingers slick with blood."
    narrator "He handed it over, chest heaving."
    "Doctor Hindre" "Pulse?"
    ish "…Still there, but fading!"
    "Ishmam bent lower, whispering in Arabic through clenched teeth, words trembling like a prayer."
    ish "Stay, little one. Stay with us. Do not go. Ahmed."
    scene bg medicaltentnight at scene1 with fade
    show kingshuk normal at midleft3
    show ishmam frown at midright3
    with dissolve
    narrator "Day turns to night. They work for hours, fighting for his every breath."
    narrator "The cot rattled under the boy's suppressed convulsions, his small chest shuddering with every gasped breath."
    narrator "The light above flickered violently as though it, too, were about to fail."
    "Doctor Hindre" "Almost - almost-!"
    narrator "He yanked a jagged shard of shrapnel free, blood sprayed across the sheet."
    narrator "The boy's body arched, then sagged heavily."
    paarth "Pulse?!"
    ish "...It's - fading-"
    narrator "He pressed harder, holding the arteries, panic rising in his throat."
    ish "Come on, don't let go, don't-!"
    "Doctor Hindre" "Stitches now. Now! Don't freeze - move!"
    narrator "Kingshuk's vision blurred from the heat, the noise, the mother's sobbing beside him. His hands trembled but he forced them steady."
    narrator "The boy gasped raggedly, then sputtered weakly. A breath. Still alive."
    narrator "His blistered eyelids open again, his burns scarred but grafted."
    narrator "This is what they're fighting for."
    narrator "They all froze for a second, listening to that fragile sound."
    narrator "The tightrope between life and death."
    narrator "Doctor Hindre exhaled, his face pale behind the mask, drenched in sweat."
    narrator "He sews the wound closed."
    stop music fadeout 2.0
    show ishmam normal at midright3
    "Doctor Hindre" "..We've bought him time. That's all I can promise."

    play music "serene.mp3" volume 1.0 loop

    hide kingshuk
    hide ishmam
    with dissolve
    narrator "The parents fell to their knees, clutching each other, murmuring prayers of relief."
    play sound "sobbing.mp3" volume 0.4 loop
    narrator "The mother kisses her son's forehead, tears streaming down her face."
    show kingshuk normal at midleft3
    show ishmam normal at midright3
    with dissolve
    narrator "Paarth collapsed back against the wall, his arms shaking uncontrollably. Kingshuk exhales, his body shaking as if for the first time all day."
    narrator "Ishmam still knelt by the cot, whispering broken words, more to himself than to the boy."
    narrator "The boy's chest rose again, shallow but steady. For now, he lived."
    narrator "The tent door is open. For the first time, they feel the cool wind blustering."
    narrator "Outside, the desert sun has hidden away. But the war does not pause."
    stop sound fadeout 2.0

    scene bg felstedfrontnight at scene1 with fade

    narrator "..."
    show kingshuk normal at midleft3
    show ishmam normal at midright3
    with dissolve
    king "I could have never imagined that this was what I was signing up for when they announced this trip during assembly."
    show richard look at midcenter3
    with dissolve
    rich "The war."
    hide richard with dissolve
    king "This, and the visceral nature of reality. The fragility of human life."
    king "There's no soul after death. When one dies within your arms, they're really gone."
    king "No matter how important they are."
    king "Like, it's not a TV show or a book."
    king "There's no purpose, rhyme or reason."
    ish "It really is nothing like class."
    ish "I don't think I could have ever called myself a doctor.."
    ish "a practitioner, had I not come here."
    show paarth normal at midcenter3
    with dissolve
    paarth "I suppose this is what Platos meant."
    show paarth look at midcenter3
    king "This is what medicine truly means."
    show paarth normal at midcenter3
    narrator "Kingshuk shivers."
    king "I'd hate to live like this."
    king "Suffering.."
    paarth "We're helping, arent we?"
    paarth "Without us, most of these people would already be dead."
    hide paarth with dissolve
    king "And without us, some of them wouldn't have to live like this."
    king "Stitched back together, just to suffer longer."
    king "Can you really call that living?"
    ish "..."
    ish "Don't say that. You sound like Charles."
    ish "If we stop believing it matters, then what's the point of being here?"
    "The air goes silent by the tent. Only the flies and the steady beep of a monitor inside."

    scene bg felstedfront at scene1 with fade
    play music "good morning.mp3" volume 0.8 loop

    narrator "8:20 AM Weather/Dry 46°C"
    narrator "Felsted Front - Day 8"
    narrator "..."
    play sound "restaurant.mp3" volume 1.5 loop fadein 1.0
    cf "Two more days."
    show richard look at midcenter3
    with dissolve
    rich "Oh, don't remind me.."
    show richard normal at midcenter3
    rich "We're short on everything now. That last attack, we used all we had to keep everyone alive."
    show kingshuk normal at midleft3
    show ishmam normal at midright3
    with dissolve
    ish "It was worth it though."
    
    rich "Oh most definitely. Without that, we'd.."
    narrator "He cradles his head in his arms."
    
    rich "God, I can't believe I even went on this trip."
    king "Don't we all.."
    hide kingshuk
    hide ishmam
    with dissolve
    stop music fadeout 1.0
    rich "No I mean, I don't even do medicine!"
    rich "I.."
    show ishmam normal at midright3
    with dissolve
    ish "You don't have to keep it in."
    rich "Just because the stupid world challenge trip was full.."
    stop sound fadeout 1.0
    hide kingshuk
    hide ishmam
    with dissolve
    show richard normal at slam
    play audio "yakuza desk slam.wav" volume 0.8
    narrator "He slams the table. Standing up tall, yet looking down."
    rich "Playing around in Romania.."
    rich "I hate this."
    show richard close at midcenter3
    narrator "Tears he didn't realise he was holding back drop onto the table."
    show richard look at midcenter3
    rich "I'm falling apart."
    show richard normal at midcenter3
    rich "I'm not sure how much longer I can take this."
    rich "Damn."
    play sound "restaurant.mp3" volume 1.0 loop fadein 0.5
    narrator "Richard composes himself slowly, but his hands still shake around his mug."
    rich "Do you even care? You've been cold ever since we arrived."
    show kingshuk normal at midleft3
    show ishmam frown at midright3
    with dissolve
    narrator "He looks up at Kingshuk."
    ish "That's not fair. King's trying to keep his head above the water same as you."
    king "Caring doesn't stop the fighting. Every day I get too invested and it hurts when it all ends unhappily."
    
    paarth "But we must care. For who else will? Caring is what performs medical miracles on lost causes. Caring is what sends money to help those suffering in countries far removed."
    ish "A false hope is better than dying hopeless. For otherwise, what have we lived for?"
    ish "What it needs, {w}is kindness."
    narrator "Richard nods. He understands what the point of it all is."
    hide kingshuk
    hide ishmam
    with dissolve
    "He seems to brighten a little." (cb_name = "ishmam")
    paarth "Perhaps there was a reason why your father had wanted you to come here."
    "Richard smiles."
    rich "Right. But of course."
    
    narrator "He glows a little more."
    hide richard with dissolve
    narrator "The sands beyond are still between blades of grass as men work distantly, rebuilding anew upon the wreckages of the residential camps."
    narrator "Children run about the ground as the sun beams overhead."
    narrator "..."
    narrator "A faint shuffling, sand crunches under small feet."
    narrator "They turn."
    narrator "A small cloaked figure limps into view - the boy they saved. Alive. Walking."
    narrator "Relief spreads across Ishmam's face. He rises to greet him."
    show ishmam normal at midcenter3
    with dissolve
    ish "Ahmed..You're awake. Thank goodness."
    ish "How have your parents been? They doing alright?"
    show ishmam close at midcenter3
    paarth "Come here, sit. You shouldn't be walking after -"
    stop sound fadeout 1.0
    show ishmam frown at midcenter3
    narrator "He freezes."
    narrator "The boy looks at them blankly. His lips tremble. He is crying."
    hide ishmam
    show kingshuk normal at midcenter3
    with dissolve
    king "No..."
    hide kingshuk
    show ishmam frown at midcenter3
    with dissolve
    ish "Oh shit."
    narrator "The child's shirt is bulging."
    hide ishmam with dissolve
    narrator "The family's voices echo in their memory. His parents had begged them to let him live."
    play sound "crowd.mp3" volume 0.6 loop fadein 0.5
    narrator "And now, here he is. Sent back, by the regime that owns him."
    narrator "The soldiers shout in alarm. Guns raise."
    $renpy.music.set_volume(0.2, channel='music')
    $renpy.music.set_volume(0.3, channel='sound')
    narrator "The boy steps forward, tears spilling down his cheeks."
    narrator "He does not want this. But he has no choice."
    narrator "Who could know what he is thinking, death approaching."
    narrator "His people were cruel and life was crueller."
    show ishmam frown at midcenter3 with dissolve
    narrator "Ishmam dives for cover, Richard and Paarth clamber under the table."
    show ishmam closefrown at midcenter3
    hide ishmam with dissolve
    show kingshuk normal at midcenter3 with dissolve
    narrator "Kingshuk, a few tables away watches, crouching with his hands holding his head."
    hide kingshuk with dissolve
    narrator "But not all were so lucky."
    $renpy.music.set_volume(0.0, channel='music')
    $renpy.music.set_volume(0.0, channel='sound')
    show black
    play audio "explosion.wav"
    narrator "There was no bright light. The area around the boy disintegrates."
    narrator "People running. People too close by. Those who had not noticed."
    narrator "The ground shook. A fire takes hold in the kitchen."
    narrator "There is a stunned silence as the world catches up to those who live in it."
    rich "Am I alive?"
    rich "Did we all make it?"
    narrator "..."
    $renpy.music.set_volume(0.2, channel='music')
    $renpy.music.set_volume(0.3, channel='sound')
    hide black with fade
    narrator "He listens as his hearing begins to return."
    narrator "Paarth is huddling beside him under the table."
    show ishmam closefrown at midcenter3 with dissolve
    "Ishmam too, is fine."
    hide ishmam with dissolve
    "Dr Hindre.."
    show kingshuk close at midcenter3 with dissolve
    king "Ahh.."
    show kingshuk normal at midcenter3
    king "Of course there can't be a happy ending."
    $renpy.music.set_volume(1.0, channel='music')
    $renpy.music.set_volume(1.0, channel='sound')
    hide kingshuk with dissolve
    "..."
    "The war was unforgiving to all."
    stop sound fadeout 1.0
    scene bg felstedfrontnight at scene1 with fade
    play music "burning.mp3" volume 0.6 loop
    play sound "mourning.mp3" volume 0.8 loop
    "Men fight the fire. The blaze roars but with distance it quietens."
    "A radio plays disjointedly, its volume similarly distant and disconcerting."
    show kingshuk normal at midleft3
    show ishmam frown at midright3
    with dissolve
    king "Do you ever wonder if we're ever actually saving anyone?"
    king "Or just.. delaying the inevitable."
    king "Fighting day and night just so that man may kill each other more."
    narrator "Kingshuk stares at the horizon. Fire crackles."
    show kingshuk normal at midleft3
    show ishmam frown at midcenter3
    show paarth normal at walkinright
    with dissolve
    narrator "Paarth sits beside them on his pack, listening in wordlessly."
    ish "Every minute matters.. Yet I too cannot shake this feeling of dread and somber."
    ish "..."
    ish "It never leaves my mind."
    paarth "Ahmed.."
    narrator "They sit in silence."
    paarth "Only two more days left to go."
    paarth "Two.."
    narrator "They chew on that information, gritty and hard to swallow, like a ball of lard that refuses to go down."
    hide paarth
    with dissolve
    narrator "..."
    narrator "There is a faint shuffling behind them. The wind has gone quiet and sand buffets at their shoes."
    narrator "A familiar face looks at them hunched over and now carrying a crutch."
    show ishmam normal at midright3
    with dissolve
    ish "Ah, the old soldier. You got discharged? You feeling alright then?"
    narrator "The man doesn't answer them. He hobbles over while beckoning them."
    narrator "Ishmam cranes his neck downwards to hear the mans words"
    "Old Soldier" "..."
    show ishmam closefrown at midright3
    narrator "The man murmurs quietly in Arabic. Ishmam's forehead creases as he puzzles the words, desperately keeping the sounds in his mind as he parses them."
    king "What is he saying?"
    show ishmam close at midright3
    ish "I.."
    show ishmam normal at midright3
    ish "We remind him of his sons..."
    king "..."
    king "Let's hope they're still alive."
    narrator "..."
    ish "It's nearly time to go."
    ish "I won't miss this place."
    ish "Yet it will forever be a part of me."
    ish "Was it worth it?"
    ish "..."
    ish "..I'd say it was."
    king "..."
    show kingshuk normal at midleft2
    show ishmam normal at midright2
    with dissolve
    narrator "Their hands brush over the cot. Neither pulls away."
    hide ishmam
    hide kingshuk
    show richard normal at midcenter3
    with dissolve
    narrator "The sun sets on the barren lands of Felsted front. Richard looks to the sky with a quiet relief."
    show richard close at midcenter3
    narrator "The last strands of the biology students' sanity, held together by the promise of a better place."
    hide richard with dissolve
    narrator "The place where they belonged."
    narrator "..."

    show black with dissolve
    stop music fadeout 2.0
    stop sound fadeout 2.0

    play audio "takeoff.mp3" volume 1.0
    narrator "The flight home was silent. No one spoke about what they had seen."
    narrator "No one dared."
    narrator "All were relieved to finally be home. A safe place they belonged to."
    narrator "..."
    play audio "trainhorn.wav" volume 1.0
    narrator "The train pulls into Chelmsford station."

    #scene bg chelmsford high street

    "6:20 AM Weather/Cool 23°C"
    "Chelmsford - Monday"
    "..."
    show kingshuk think at midcenter3 with dissolve
    king "You know you've been away for too long when you pull up to East Anglia rail and are disgusted by the prices."
    show paarth_close at midleft3
    show richard_normal at midright3
    with dissolve
    paarth "uuuuuuuuuuugh.."
    rich "Come on Paarth, we're nearly there now, just push through the jetlag."
    cf "You should have slept on the plane. Like I did."
    friel "Alright everyone, gather up. We need to do the last headcount before we arrive back."

    
    scene bg kegs at scene1 with fade
    play music "woodland.mp3" volume 0.8
    

    narrator "The familiar spires of KEGS peered around the corner."
    show kingshuk normal at midcenter3 with dissolve
    king "Heh, we're finally here."
    narrator "They are hit by a wave of nostalgia. {w} The red bricks.{w} The gate.{w} The short wall that ran around it."
    narrator "*Rattling chains*"
    hide kingshuk with dissolve
    friel "The gate to the staff car park is locked. {w}We'll probably have to go through the main entrance."
    show ishmam normal at midright3 with dissolve
    ish "These chains.."
    show ishmam frown
    ish "..."
    show ishmam look
    narrator "He looks quizically at the gate bound by the chains."
    show ishmam frown
    ish "King? {w}Look at this."
    show kingshuk normal at midcenter3 with dissolve
    king "?"
    ish "When you lock a gate with a chain.."
    hide kingshuk
    hide ishmam
    show paarth normal at midleft2
    show richard normal at midcenter3
    with dissolve

    narrator "The crowd of students have left them behind."
    narrator "The road outside Kegs is quiet. {w}Even Mr Torrie would hesitate before berating you for crossing the road on a red light."
    hide paarth
    hide richard
    show ishmam closefrown at midleft2
    show kingshuk look at midcenter3
    with dissolve
    ish "..."
    show ishmam frown at midleft2
    ish "..wouldn't you use a padlock?"
    show kingshuk think at midcenter3
    king "..."
    hide kingshuk
    hide ishmam
    with dissolve
    #change scene kegs main gate
    narrator "At the front gate"
    friel "Hey! Can you open the gates? They're locked."
    narrator "She shouts towards the site team who stand outside the reception."
    narrator "One of them looks to the other before walking over."
    show nobody m at midcenter3 with dissolve
    stm "Please state your business."
    friel "What do you mean state your business? {w}I work here."
    friel "We're back from the school trip to Felsted front."
    narrator "The site team member eyes Ms Friel carefully."
    ager "Allow me."
    narrator "He speaks to them out of earshot."
    show richard look at midleft2
    with dissolve
    rich "Whats going on? Aren't we going to go home first?"
    cf "Do they really expect us to attend class today?"
    cf "I may be fine but Paarth and my brother very much aren't."
    hide richard 
    show nobody m at midleft3
    with dissolve
    narrator "The site team member seems satisfied with Mr Ager."
    narrator "He steps back, producing some bolt cutters from behind him."
    "Yaseen" "What.."
    narrator "Only from this angle, do the students see."
    narrator "The rifles slung to the side of each site team member."
    play audio "unlock.wav" volume 1.0
    narrator "The gates open, the cut chain crumpling to the ground."
    paarth "Finally.."
    narrator "The students surge forward."
    narrator "Yet they stop when the site team shout."
    play audio "Referee whistle.wav" volume 1.0
    stm "HALT!"
    show paarth normal at midcenter3
    paarth "!.."
    hide paarth
    show kingshuk normal at midcenter3
    king "..."
    hide kingshuk
    show richard normal at midcenter3
    rich "!?.."
    show kingshuk normal at midleft3
    show kingshuk normal at midright3
    narrator "They look up in stunned silence."
    stm "Only authorised personnel from here."
    hide paarth
    hide richard
    hide kingshuk
    with dissolve
    narrator "The teachers walked forward unimpeded."
    narrator "Ms Friel, the one who organised this trip."
    narrator "Mr Ager, Mr Cole, Ms Jones.."
    narrator "They turned, solemnly."
    show nobody m at midcenter3 with dissolve
    stm "You are no longer students here.{w} Your names are not on the register."
    play audio "unlock.wav" volume 0.8
    narrator "The gates close. The students are too compliant to resist the armed site team."
    narrator "The students watch as 2 site team members escort the teachers into the building."
    hide nobody
    show richard normal at midcenter3 
    with dissolve
    rich "What on earth happened while we were away?"
    rich "I couldn't imagine what."
    #change scene aerial view students
    scene bg kegsabove with fade
    narrator "The students lay abandoned, trapped in the staff car park besides the Sixth form centre."
    narrator "Unable to enter. {w}Unable to leave."
    scene bg kegsinside with fade
    #change scene to inside kegs
    play music "tension.mp3" volume 1.0 loop
    "8:35 AM Weather/Cool 23°C"
    "The Darwin Centre - Monday"
    "..."

    narrator "The council chamber of KEGS was dark, lit only by the pale gleam of the skylight."
    show nobody m at midcenter3 with dissolve
    narrator "Mr Seed sat at the long table, his hands folded neatly on the polished wood."
    narrator "He didn't blink."
    play sound "sobbing.mp3" volume 0.8
    narrator "Ms Friel lay collapsed on her knees before him. Sobbing"
    friel "Please! Please, we beg of you. {w}They are children.{w} They're our students!"
    friel "They've been through enough!"
    narrator "Behind her, Ms Jones wrung her hands, her face whiter with fear than ever. {w}Mr Cole kept a hand on her shoulder, steadying her as her voice broke."
    jones "Their names may not be of your concern, but they belong here. No matter what happened while we were away. You can't shut them out. That's just not how it works."
    narrator "Mr Seed regarded them with a strange, thin smile, subtle, yet wide across his face."
    $renpy.music.set_volume(0.4, channel='sound')
    seed "You misunderstand."
    seed "You remain staff of this institution."
    seed "KEGS values its faculty."
    $renpy.music.set_volume(1.0, channel='sound')
    stop sound fadeout 2.0
    narrator "Ms Jones turned, giving Mr Cole a strange look."
    narrator "His gaze shifted, sharp as glass."
    seed "But those children? They are no longer students. Not here."
    seed "Their names are no longer on the register."
    narrator "Mr Cole sweated."
    seed "I have no use for them here."
    narrator "Ms Friel clutched the hem of the table, desperation clawing at her voice."
    friel "Th-then by law - by the contract of their field trip.. We have a legal responsibility for their safety!"
    friel "You cannot simply cast them away! We are bound to their wellbeing!"
    narrator "For the first time, Mr Seed leaned back in his chair, considering. Then slowly, his grin widened."
    seed "Very well. By your own words, you are legally bound. The duty lies with you. Those who organised the trip.. You will take care of them."
    stop music fadeout 2.0
    narrator "A stunned silence fell. Ms Friel's eyes went wide."
    friel "No...no, that isn't what I -"
    seed "The matter is settled. The students won't remain here."
    narrator "He tapped his finger twice on the table."
    seed "They have to go. I have plans for this place. I have no need for ideals or morals."
    play audio "paper.wav" volume 1.0
    narrator "He leisurely flicked through a few of the papers on the desk."
    seed "Yes, yes. That'll do. What a wonderful coincidence."
    narrator "He eyed the letters on the page and waved his hand."
    seed "They'll go to {w}Bedford bog!"
    play music "enduring.mp3" volume 1.0
    #play sound "sobbing.mp3" volume 0.3
    narrator "Ms Friel collapsed, aghast, stuttering and sobbing openly, her wails echoing down the chamber."
    narrator "Mr Cole bent to hold Ms Jones as she buried her face in his chest, whispering through tears."
    jones "He'll be alone, I'll be alone - he's still out there. My husband -"
    cole "Shhh. He trusts you. He trusts all of us. If Mr Seed is sending us..{w} them there, then they'll endure."
    narrator "His voice falters, his throat tightening."
    cole "Even if it's...{w}..Bedford bog."
    narrator "He shuddered."
    narrator "..."
    narrator "Mr Seed turned in his chair, the back facing them all."
    narrator "He turned his head back towards the shadows in the door. Mr Ager stood there, still as stone, his hands clasped behind his back."
    narrator "His eyes betrayed nothing."
    seed "Perhaps, Mr Ager, you could finish that project in the bog?"
    narrator "A pause. Mr Ager lowered his head."
    ager "...It is possible. But only if I have the necessary help and materials."
    narrator "Mr Seed chuckled, the sound hollow and sharp."
    seed "Oh don't concern yourself. That won't be a problem."
    seed "Besides, you'll have Mr Cole here to help you."
    play audio "seed laugh.wav" volume 1.0
    narrator "His laughter echoed long after the decision was made, bouncing through the dark corridors of KEGS, while the teachers held each other, sobbing quietly."
    narrator "Ms Friel lay on the floor, defeated."

    #change scene to aerial view students
    #or perhaps skip this part and go straight to bedford bog
    stop sound fadeout 2.0
    stop music fadeout 2.0
    scene bg kegs with fade

    play music "coming storm.mp3" volume 0.6
    narrator "The students huddle in the centre of the staff car park when they hear engines."
    show kingshuk look at midright2 
    show paarth normal at midleft2
    with dissolve
    king "!.."
    rich "Something's not right guys."
    show kingshuk normal at midright2 
    paarth "Should we run? Guys?"
    show kingshuk look at midright3 
    show paarth normal at midleft3
    show nobody m at midcenter3
    with dissolve
    narrator "The site team turn, seemingly recieving orders."
    narrator "They unholster their firearms as several school minibuses pull into the lot."
    #change scene to council room
    scene bg kegsinside with fade
    show nobody m at midcenter3 with dissolve
    narrator "Mr Seed stands at the top of the steps, hands behind his back. His tone is measured, almost bored."
    seed "They are no longer children of this house. They are no longer ours to shelter."
    seed "I won't let them disturb the school's metamorphasis."
    narrator "He turns away."
    narrator "The shadows lengthen across his face, shrouding his expression, hiding his glee."
    #change scene to aerial view students
    scene bg kegsabove with fade

    narrator "The guards pull open the minibuses' barred doors." 
    narrator "The children resist as the site team bundle them through the doors."
    narrator "That is until a student manages to break free of the encirclement."
    play audio "gunshot.mp3" volume 1.0
    stm "..."
    narrator "They turn, now unfazed by the students' protests."
    narrator "A stunned silence. The students' resistance grows limp."
    stm "In. {w}Now."
    narrator "A chill passes through the students as they are shoved inside one by one."
    #change scene to council room
    scene bg kegsinside with fade
    show nobody m at midcenter3 with dissolve
    seed "It's poetic really."
    seed "Soon I will begin my expansion, {w}and to think that my enemies {w}will conquer it for me!"
    narrator "He laughs heartily."
    seed "Two birds {w}with one stone."
    narrator "The sun shines brightly onto the moss infested roof tiles of KEGS. Yet there is no happiness left in this place."
    narrator "The reception door remains locked, its purpose redundant."
    narrator "When KEGS failed to put the brakes on Mr Seed's campaign, failed to keep him in check.."
    narrator "..The last embers of Mr Carter's gift of glory to the school burnt out alongside him."

    show black with fade

    narrator "Kingshuk stares at the barred window. The landscape begins to change outside - houses thinning into hedgerows, hedgerows into dark trees."
    show kingshuk look at midcenter3 with dissolve
    king "I can't see the city anymore."
    show richard normal at midleft3 
    show ishmam closefrown at midright3 
    with dissolve
    show kingshuk normal at midcenter3
    rich "We'll come back. We have to. KEGS can't just..{w} shut us out forever, right?"
    show ishmam frown at midright3 
    ish "..."
    ish "Don't fool yourself."

    #show bedfordbogplains
    scene bg bog with fade

    narrator "The van jolts to a stop. Chains rattle. The back doors open and the stench of wet earth hits them."
    narrator "A site team member shouts something gutteral and one by one, the students dismount the minibuses."
    narrator "Bsgs are shoved into the mud as if their presence violated the purity of the buses."
    show kingshuk normal at midcenter3 with dissolve
    king "..."
    narrator "The minibuses rev, turn and vanish into the mist, leaving only silence."
    play music "ghosthunter.mp3" volume 0.8
    narrator "The bog stretches out before them. An expanse of swaying reeds dead tres jutted out from the blackened mus, its roots like skeltal fingers."
    narrator "The mist never quite lifted even when then sun burned overhead."
    "Raymond" "Is this..{w} Bedford bog?"
    "Raymond" "Its completely unrecognisable."
    show paarth look at midleft3 with dissolve
    paarth "I guess this is why they didnt let us go too far during the cross countries."
    show paarth close at midleft3 
    paarth "Restricted us to the track."
    show paarth normal at midleft3 
    paarth "God I hated cross country."
    king "I'm saying like.."
    king "I'm so glad we stopped it in year 7.."
    show paarth look at midleft3 
    paarth ".."
    show ishmam look at midright3 with dissolve
    ish "We're probably the last year group to have visited Bedford bog now that I think about it."
    show ishmam normal at midright3 
    ish "I suppose we should explore, the others have already run off ahead."
    king "Right."
    #change scene bedfordbog2

    scene bg river with fade
    "Ezzah" "Careful where you step. It's wet up here."
    "Raymond" "Damn alright."
    narrator "They step carefully through the sodden ground."
    "Raymond" "Come! Look."
    sam "What?"
    narrator "Sam and Ezzah catch up to Raymond who has climbed a small hill."
    "Raymond" "It's a river."
    narrator "The waters simmered with an oily sheen."
    sam "It's completely still."
    narrator "Sam throws a stick into the water."
    narrator "The stick disappears into the water without a sound, barely affected in its fall."
    "Ezzah" "Judging from the banks of the river it probably floods at parts of the year."
    "Ezzah" "There's none of the boggy grass for meters off the bank."
    narrator "She adjusts her glasses."
    "Raymond" "In that case we should build away from here, preferably on higher ground."
    narrator "Ezzah touches the soil, coming away wet and black, clinging like tar."
    "Ezzah" "It's peat."
    narrator "Sam looks to the carpet of reeds as Ezzah creeps along the bank examining the river. The stalks swayed in the deep water."
    sam "We should find shelter soon. Who knows when it will rain out here and besides, it gets dark here earlier than felsted front."
    "Raymond" "We should find the others then. We don't have any tents."
    "Ezzah (Distantly)" "Past a certain point the water gets remarkably deep."
    "Raymond" "You think there's anyone interested in this kind of thing? Somebody who could help?."
    sam "Maybe..Charles Fenton Tun?"
    sam "He seems the sort. And Lakshya."
    play audio "plunge.wav" volume 1.0
    #Ezzah falls into the water, use a trandform and a water plopping sound effect
    sam "I've never had faith in those sort of survivalist shelters though."
    sam "Like how can those twigs and leaves actually keep you warm and dry."
    "Raymond" "..."
    sam "Surely it can't."
    "Raymond" "Maybe it won't keep you comfortable, but it may help keep at least some warmth in?"
    sam "hmm.."
    sam "Ezzah?.."
    narrator "Sam calls out but recieves no answer."
    sam "Ezzah?"
    narrator "Raymond looks around. Ezzah is nowhere to be seen."
    sam "Did she walk off? I thought she was still with us."
    "Raymond" "Same."
    narrator "Raymond peers about the bushes to no avail."
    narrator "Sam. meanwhile, parts the reeds, careful to keep on land."
    narrator "The still surface of the water occasionally broke with a sluggish ripple."
    sam "Where did she go?"
    "Raymond" "I'm not seeing anything."
    sam ".."
    sam "She must be with the others."
    sam "Odd how she managaed to slink by us unnoticed."
    "Raymond" "..."

    #change scene beford bog 3
    scene bg bog with fade

    narrator "The violet heath flutters in the wind, vibrant patches of colour upon the desaturated landscape."
    narrator "The many students had scattered, exploring the land and the forest." 
    narrator "Despite the bleak circumstance, curiousity finds a way."
    show ishmam normal at midright2 
    show richard normal at midleft2 
    with dissolve
    ish "It's so melancholy out here."
    ish "The wide plains and boggy marsh.. Ican't help but feel profound."
    rich "Large empty spaces do seem to do that. I.."
    rich "I still can't come to terms with how quickly it went down."
    narrator "Richard is struggling within some thorned bushes, picking out berries."
    rich "(chewing) They do taste alright. Certainly as well as wild berries can taste."
    ish "What are you doing?! You can't just eat wild things."
    rich "Eh.. I'll live. I have a strong constitution."
    rich "They're not mushrooms."
    narrator "Ishmam begins to calm down. As a medicine student, wild foods were explicitly off the menu by his parents' teaching."
    hide ishmam
    hide richard
    with dissolve
    narrator "Time passes as they forage. The dew dries a little as the morning turns to midday."
    show ishmam normal at midright2 
    show richard normal at midleft2 
    with dissolve
    ish "It's surprising how many fruits there are in Bedford."
    rich "Probably due to flat terrain, it's easy to find food due to the bright colours."
    rich "I think this is about enough."
    ish "You sure? Alright."
    ish "You still feeling okay? I suppose I shouldn't think anything of it then."
    rich "Yeah, I'm good."
    narrator "Returning to the clearing, only a few remained within eyeshot."
    narrator "The clouds had settled overhead, filtering the light into a drab grey."
    ish "Everyone's left.."
    rich "They must have gone exploring the the forest."
    narrator "He looks around, the wind blowing past his hair."
    rich "We should prbably set up camp here. We don't have too much time."
    ish "Right."
    narrator "Ishmam puts down the berries as Raymond and Sam arrive slowly."
    rich "Oh, hi Sam.. Oh, and Raymond."
    rich "You doing alright? We're just starting to make shelters."
    sam "Oh great! We were just about to ask about that. Speaking of."
    "Raymond" "Have you seen Ezzah?"
    ish "No, haven't seen anything. Sorry."
    "Raymond" "No it's alright."
    "Raymond" "Damn it."
    narrator "Raymond sits on a damp log, staring blankly into the bog mist."
    sam "Come on Raymond. We've got shelters to build."
    "Raymond" "True."
    narrator "A pile of branches and leaves starts to build up."
    narrator "Ishmam files down the sticks into usable shapes using a broken piece of metal."
    hide ishmam
    show richard normal at midcenter3 
    with dissolve
    
    laksh "You guys up to something?"
    rich "Yeah. We're making shelters."
    laksh "Sick. What do we do with all this?"
    rich "Come look. Like this."
    narrator "The sound of snapping branches and muffled voices filled the clearing. A rhythm. Organisation. Almost like a heartbeat returning to the group."
    narrator "The commotion attracted people. Assuredness. Direction."
    narrator "The students naturally followed a certain purpose."
    narrator "One by one, they gathered. Not because Richard commanded it. But because he worked. Because he knew what needed to be done."
    narrator "Richard glowed. His blood ran hot, his ancestry flowing through every part of his body, determination warming him where a fire couldn't"
    narrator "In his heart."
    narrator "The swamp still loomed, its river whispering, its trees groaning-but for the first time since their exile, they moved as one."
    #scene bg bedford bog night
    scene bg bognight with fade
    play music "desert night.mp3" volume 0.8
    play sound "burning.mp3" volume 0.8
    #campfire crackle
    show richard normal at midleft2 with dissolve
    "Hemanth" "Is it alright if I take one of these."
    rich "Yeah. we're trying to get one for everyone but I don't know if there will be enough in time."
    rich "Speaking of.."
    narrator "Richard looks off into the black of the wooded forest."
    narrator "His face drops with worry."
    show richard look at midleft2 
    rich "Ishmam."
    show ishmam frown at midright2 with dissolve
    ish "I know. They're still not back yet.."
    narrator "Ishmam shares his pained look."
    ish "We said we'd meet back up here."
    rich "They're probably lost."
    rich "We've done what we can do. The bonfire will be maintained through the night."
    narrator "They sit by the fire. Its hot embers tumble out of the sticks."
    narrator "They hear hurried footsteps. Heavy breathing. Richard stands up."
    #show kingshuk
    show richard normal at slam
    show ishmam normal at midleft3
    show kingshuk normal at midright3
    with dissolve
    narrator "The fire cracked as Kingshuk and a few others slumped into the clearing, their clothes ripped, mud plastered to their legs."
    narrator "Everyone turned to them, faces lit by the orange glow. The night was heavy with expectation."
    rich "Oh my god! You guys okay?"
    #show johnathon
    best "Yeah.."
    best "It was hellish."
    rich "What on earth happened? This isn't everyone is it?"
    king "It is. Just earlier.."
    best "From the beginning Kingshuk."
    king "Right, right.."
    narrator "The students leaned in closer. Kingshuk held his breath for a second, then exhaled sharply."

    #change scene
    hide richard
    hide ishmam
    show kingshuk look at midcenter3 
    with dissolve

    king "We headed in the direction of the forest, east from here. Exploring for landmarks, shelters, paths."
    king "But the trees.. Our path was twisted, half the time we'd find ourselves looping back on ourselves I swear."
    narrator "A murmur spread through the circle."
    king "A lot of people got lost. Archie, Paarth, Samaksh."
    best "Ajay.."
    king "We left directions for them just in case but.."
    king "I don't have much hope."
    narrator "He looks folorn."
    best "The worst part were the bears"
    king "Or whatever those were."
    best "They were about the size of bears anyway. We weren't close enough to see anything but they sounded heavy."
    king "They made these snuffling noises."
    king "And there was this clearing absolutely covered in this awful smelling phlegm."
    #change scene to bedford night
    narrator "..."
    king "We were also looking for food but uh."
    king "Yaseen ate something wrong so he's not doing too well."
    rich "Dang.."
    hide kingshuk with dissolve

    narrator "The night was silent except for the crackling fire."
    narrator "The shelters were finished to a workable degree."
    narrator "A few students stumbled back from the plains and the forest during the night, attracted by the fire."
    narrator "Richard turns in his sleep, slapping away a mosquito as he stares at the first night shift that he organised."
    narrator "He was cold."
    narrator "And hungry."
    narrator "The stars twinkled in the reflection of his tears as slept."
    narrator "They were no longer KEGS students."
    narrator "Just innocents, caught up in the tides of change."
    narrator "Worthless and discarded."

    #change scene bedford forest.
    scene bg rivernight with fade

    #paarth time

    play sound "heavy breathing.mp3" volume 0.4
    narrator "Under the moonlight, through the branches he tumbles."
    show paarth close at midcenter3 with dissolve
    narrator "Paarth Bansal was running for his life."
    
    #show nobody m at midleft2 
    show paarth close at midcenter3
    with dissolve
    narrator "A large shadow chased after him."
    narrator "He had broken off from the group a while ago while investigating a tree with pear-like fruit but when he turned around to share his findings.."
    narrator "His friends were nowhere to be seen."
    narrator "It was getting dark and he was growing afraid when he was spooked by a loud noise."
    show paarth normal at slam
    narrator "He jumped and narrowly dodged a large beast that had been charging at him."
    narrator"Next thing he knew, he was running."
    narrator "Not anywhere, but away."
    paarth "hnggh!"
    narrator "His breath hurt."
    narrator "His chest ached and his fatgue was rapidly outweighing his fear."
    show paarth look at midcenter3
    narrator "He looks behind him as he crashes through a bush."
    show paarth close at midcenter3
    paarth "Aagh!"
    show paarth normal at midcenter3
    paarth "Shit."
    narrator "He scrambles through the undergrowth."
    paarth "Shit. Where do I even go?"
    paarth "I hate this, man."
    show paarth close at midcenter3
    narrator "He closes his eyes as he focuses his efforts in his legs."
    paarth "No. I can't.."
    narrator "He tries to ignore the all encompassing pain in his body."
    show paarth normal at midcenter3
    paarth "I want to live."
    narrator "His foot catches on an exposed root and he falls, tumbling down."
    show paarth close at slam with vpunch
    narrator "Head over heels."
    show paarth close at slam with vpunch
    narrator "His body hits the ground before he even registers his foot catching."
    show paarth close at slam with vpunch
    paarth "!!"
    show paarth close at slam with vpunch
    narrator "He rolls down the hill, hitting trees and crashing through shrubbery with speed."
    show paarth close at slam with vpunch
    narrator "Each bump into a tree knocked the air out of him."
    stop sound fadeout 2.0
    hide paarth with vpunch
    narrator "Then he woke up"

    #change scene looking up at tree and sky
    scene bg sky with fade
    play sound "woodland.mp3" volume 0.8
    paarth "......."

    narrator "The sun was shining."
    scene bg blackfield with fade
    show paarth normal at midcenter3 with dissolve
    narrator "..."
    show paarth approve at midcenter3
    play audio "squeak.wav" volume 0.8
    paarth "Huh!"
    narrator "Paarth bolts upright but he regrets it."
    show paarth normal at midcenter3
    
    narrator "Laying back down, a tree swaying above him.."
    narrator "All was quiet."
    narrator "An open field lay before him, black shapes dotted in the distance."
    scene bg sky with fade
    narrator "He laid his head down to rest."
    paarth "It will be {w}okay"
    narrator "..."
    show black with fade

    #change scene looking up at tree and sky
    narrator "..."
    scene bg sky with fade
    play music "peace.mp3" volume 0.8
    
    narrator "Many hours later he woke again."
    narrator "His muscles still hurt but now he had the energy to resist. He leaned against the tree and looked around."
    #change scene peaceful field of black roots
    scene bg blackfield with fade
    show paarth normal at midcenter3
    with dissolve
    paarth "What a strange place. So serene."
    show paarth close at midcenter3
    narrator "He relaxed with relief. He may be safe here."
    show paarth normal at midcenter3
    narrator "The sky above was clear, painted with soft blue hues."
    narrator "He blocks the sun overhead with his hand."
    narrator "His hand brushes against the dried blood on his forehead."
    paarth "What's that in the distance?"
    narrator "Black shapes roamed the fields far away."
    paarth "Cows maybe?"
    paarth "Hm."
    paarth "Wait, where's my compass?"
    show paarth look at midcenter3
    narrator "Paarth fumble around, searching his pockets, turning them inside out."
    show paarth normal at midcenter3
    paarth "Oh it was there. Right I remember."
    narrator "He fishes out a slightly dull brass compass."
    show paarth look at midcenter3
    narrator "It flickers, pointing north."
    show paarth normal at midcenter3
    paarth "Hm."
    paarth "I came from roughly over there in the forest and that's south after the bend again so.."
    narrator "He looks up, wincing as he slowly gets up from where he lay."
    paarth "I guess I'll head more or less north."
    paarth "There's nothing else to do really, so I just have to pray."
    show paarth close at midcenter3
    paarth "Nngh!"
    narrator "He cries out as his bruises and sores scream at him."
    narrator "Muscle ache in his thighs."
    narrator "His eyes are tightly pressed together, as if they eased the pain."
    show paarth normal at midcenter3
    narrator "Paarth exhaled, his breath shaky but steadying."
    narrator "He began to walk through the wide expanse of long grass."
    narrator "They swayed in the wind as they yellowed in the distance."
    narrator "Limping through the bruises and muscle ache he had endured, he travelled north."
    paarth "Shit. It's not like I have anything else I can do."
    narrator "He grumbles through the pain."
    play sound "fly.wav" volume 0.8
    "Fly" "...."
    stop sound fadeout 2.0
    narrator "A fly buzzes, following Paarth, attracted by the smell of drying blood."
    narrator "He couldn't call anyone. His phone had no signal, not in the wastes of Bedford Bog."
    narrator "He stopped for a moment and considered. Was this place even Bedford?"
    narrator "He laughed to himself. This wasn’t the good place. It wouldn't hurt so much."
    #scene change black roots
    narrator "He had walked a while and the black shapes had grown closer."
    paarth "They're plants?"
    narrator "Dark silhouettes, motionless against the pale grass."
    narrator "Some were tall, hunched figures, their outlines resembling twisted arms frozen in place."
    narrator "Others lay low to the ground, tangled into the earth like melted roots."
    narrator "hey did not sway with the wind."
    narrator "They did not move at all."
    play sound "fly.wav" volume 0.8
    "Fly" "............"
    "Fly" "...."
    "Fly" "........"
    stop sound fadeout 2.0
    paarth "(Thinking) Something's wrong."
    narrator "He watched as a small rabbit noiselessly jumped between the roots. He felt silly for having such dramatic thoughts."
    narrator "The rabbit left silently as he moved from where he was crouched." 
    play sound "fly.wav" volume 0.8
    "Fly" "........"
    stop sound fadeout 2.0
    narrator "The fly finally leaves, distracted by something else. It flies among the dark tendrils of the plants."
    #play audio ripping and tear
    play audio "roar.mp3" volume 0.8
    show paarth normal at slam with hpunch

    narrator "The ground erupts, dark tendrils piercing from the ground."
    narrator "The roots encapsulate the fly with a sickening crunch of chitin cracking against chitin." 
    show paarth normal at slam
    narrator "Earth falls out of the sky, thudding behind Paarth as he crouches down in shock."
    narrator "The wall of blackened roots suspend in mid air for a second as they slowly, silently retreat back to the ground."
    narrator "His heart sat in his throat as he watched, choking on fear."
    narrator "He was fragile, vulnerable. To make a sound was to die."
    paarth "..."
    show paarth close at midcenter3
    narrator "Slowly, he covered his mouth, sealing it so not a sound could escape."
    show paarth normal at midcenter3
    narrator "Not even his grunts of pain as his sores tormented him as he tried to stand up."
    paarth "!..."
    narrator "Carefully, he walked past."

    stop sound fadeout 2.0
    stop music fadeout 2.0
    #change scene bedford bog field
    scene bg bog with fade

    #play audio car engine
    play sound "trainhorn.wav" volume 0.8

    narrator "The students awoke to the sound of car engines."
    narrator "The grass was wet and dewey, the clouds grey and unforgiving."
    show richard close at midcenter3
    rich "They're back?"
    show richard normal at midcenter3
    narrator "His heart flutters for a moment."
    narrator "But as he watches the school minibuses pull away, he steels himself against losing hope."
    narrator "For it was the second best thing that had occured."
    narrator "He approaches the figures left by the tiremarks."
    rich "You came back.."
    #reveal the people
    friel "Of course."
    narrator "She hesitates."
    friel "We couldn’t leave you completely on your own."
    narrator "She tried to smile, but faltered."
    ager "We've brought supplies."
    narrator "There was a flicker of relief until the students saw what he meant."
    narrator "The supplies were high quality, but scarce. Instant meals and canned food, water purifiers, a first aid kit."
    narrator "They crowded around the bag."
    narrator " A person could live in the wild for weeks in relative comfort."
    narrator " Indeed. {w}A small group."
    narrator "It wasn’t enough, not even close to enough for all the students."
    narrator "It was clear that this was never meant for them."
    sam "Th..that's it?"
    narrator "Sam stepped forward, rifling through the bag."
    narrator "Behind, Ishmam nudged Richard, whispering."
    ish "If we share equally, it won’t be enough."
    friel "We'll try to divide what we can. You're still our responsibility."
    narrator "Her voice faltered. Even the younger students could hear it: her words were too thin to stand on."  
    narrator "Richard exhaled through his nose, slow. His brow furrowed. His voice cut through the unease."  
    rich "We won't rely on this alone."  
    rich "We’ll need to find our own food. Build shelters. Organise." 
    narrator "The crowd quietened. They hadn't seen Richard like this before until now. His tone had weight, heavier, impactful."
    #scene quiet clearing
    narrator "The teachers and Richard stepped away from the crowd. The students watched, but no one followed. It was already understood: this was leadership."  
    rich "First: shelters. Not just makeshift ones. Something that will last."  
    rich "Second: we’ll need proper exploration teams. Mapping, food sources, materials. The bog is more dangerous than we thought."
    rich "Many of the students have already gone missing. They're probably lost."
    rich "We should try to find a way to signal to them, perhaps a smoke signal or using the flares."  
    rich "And a perimeter. Rumours or not, no one sleeps without someone on watch. If there are beasts out there, we need to act fast."  
    friel "We’ll need a place for teachers too. Somewhere to keep the supplies safe. A base."  
    rich "True. Then it’s decided."  
    narrator "They didn’t shake hands. That wasn't the nature of their relationship. The weight of the bog hung over them all, but for the first time, the fear felt contained."  
    narrator "Barely."  
    narrator "Behind them, the students whispered, watching Richard with something like hope. The bog whispered too, reeds rustling over hidden waters. It waited, patient."  

    #scene bg bedford_bog 

    


    





    






    return
