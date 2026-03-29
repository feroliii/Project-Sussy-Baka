# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Aoi")
define m = Character("Me")
define g = Character("Girl")

define a_jp = Character("Aoi",  what_font="NotoSansJP.ttf")
define m_jp = Character("Me", what_font="NotoSansJP.ttf")
define g_jp = Character("Girl", what_font="NotoSansJP.ttf")
define na_jp = Character(" ", what_font="NotoSansJP.ttf")
define na_jp_sec = Character(" ", what_font="NotoSansJP.ttf")
define na_jp_third = Character(" ", what_font="NotoSansJP.ttf")

define cafe = Image('cafe.png')
define airport = Image('airport.jpg')
define campus = Image('campus.png')
define sky = Image('sky.jpg')
define sakura = Image('sakura.jpg')

#These are copyright music that I found on the Internet, I will change all of them as soon as I done working on them. These does not belong to me just to be  clear.
define audio.lecarrousel = "assets/ost/Le-Carrousel.ogg"
define audio.newhome = "assets/ost/New-Home.ogg"
define audio.wind = "assets/ost/Wind.ogg"
define audio.lol = "assets/ost/legend-nver-die.ogg"
define audio.driftaway = "assets/ost/Drifting-away.ogg"
define audio.ballerina = "assets/ost/Ballerina.ogg"
define audio.bleached = "assets/ost/Bleached.ogg"
define audio.onceupon = "assets/ost/once-upon-a-time.ogg"

# The game starts here.

label start:

    stop music fadeout 2.0

    play music lecarrousel

    menu:
        "Language menu"

        "English":
            jump start_en

        "Português":
            jump inicio_pt
        
        "Español":
            jump start_es

        "Italiano":
            jump start_ita

        "Français":
            jump start_fr

        "Deutsch":
            jump start_german

        "Tiếng Việt":
            jump start_vi

        "日本語":
            jump start_jp
        


    label start_en:

        stop music fadeout 1.0

        play music newhome volume 0.6

        scene cafe

        "I will never forget the image of that girl. The one who perhaps made my cold heart tremble once again."

        "But it seems that the poetic scenes I dreamed of will never become reality."

        "All I can do is stand and watch her from afar, unable to do anything."

        "“It's not possible.” “We don't even know each other—how could you talk to her?”"

        "Those voices kept echoing in my mind. I truly didn't know what to do anymore."

        "Today is like every other day. The same familiar cafeteria, the same familiar seat. She's sitting there again. And me, as always, just watching from afar."

        "My final year here before transferring somewhere completely different."

        "AAAAA! This could be that “moment”—when the boy and girl leads accidentally meet. Too bad I'm just a side character."

        "Damn it. Should I approach her?"

        $ preferences.text_cps = 0

        menu:
            "Damn it. Should I approach her?" 

            "Of course, dumbass!":
                menu:
                    "Are you sure? You have never approached a girl before."

                    "Yes! I'm sure!":
                        jump good_end

                    "For real, let's go home and play league (I'm bronze).":
                        jump league_end

            "Nah bro, look at me! I'm bald and smelly asf :/":
                jump bad_end

    label league_end:

        stop music fadeout 1.0

        play music lol volume 0.5 

        scene sky

        $ preferences.text_cps = 30

        m "PUSH THE WAVE SHIT EZREAL"

        "30 min later..."

        m "GET THE BARON!! SMITE SMITE!"

        "5 matches later..."

        m "Fuck... I'm iron now..."

        m "..."

        m "What happened?"
        
        m "..."

        m "That was way better than talking to a girl 🔥🔥🔥"

        return

    label good_end:
        stop music fadeout 1.0

        play music wind volume 0.7

        $ preferences.text_cps = 30
        "Gathering all my courage, I stood up and walked toward her."

        "I've endured the feeling of just watching without doing anything long enough. Now, get rid of this embarrassment."

        "As I got closer, my heartbeat felt like it tripled. Nervousness and a flood of not-so-good memories from past conversations with girls came crashing in like a tsunami."

        "Whatever, it's all or nothing, I told myself."

        m "Hey... excuse me."

        "I forced the words out."

        "She looked up at me. Oh! It felt like I could just… die and ascend right there."

        "Or at least that's what I thought. Maybe it's a bit weird to bother her while she's eating?"

        "In a very gentle, slightly bothered tone, she replied:"

        g "Who are you? I don't think we know each other?"

        "Damn..."
        "Let's push a bit further."

        m "Well, I've seen you around a few times. I think you're cute! So..."
        
        "Fuck..." 
        "What should I ask? I need to keep the conversation alive..."

        m "Are you american?"

        g "No, actually I'm an international student."

        m "Oh!"

        m "Me too! I'm asian. What about you?"

        g "Really?? I'm asian too!"

        m "Ni hao fine shyt"

        g "..."
        
        m "haha..." 
        
        m "My bad, trash joke..."

        m "By the way I'm from Vietnam"

        g "I'm japanese"

        m "No waaay!!! You will not believe but I'm learning japanese."

        g "That's nice! And who is it going?"

        m "To be honest, kinda good but I don't anyone to practice with."

        m "Hey! Could you help me? With practicing the japanese."
        
        g "Hmm... I'm eating right now so... It's not a good time you know?"

        m "Oh... I don't want to bother you... Sorry."

        m "Well... nice to meet you."

        "I turned back to my usual table."

        "But before I could sit down, she said:"

        g "Wait!! It's not that disgusting that a foreigner is interested in my language. I'll help you. Do you use any social media? IG? Line?"

        m "Oh, I have Line, just never really used it. No one uses Line in the U.S. anyway. I also have IG. Let's go with IG."

        g "Ok ok."

        m "Ahh... shit..."

        g "What?"

        m "My phone just died..."

        g "Hahaha It's fine!"

        g "Where, put your search for your user and follow for me."

        "She gave me her iPhone and typed my IG really quick."

        m "Alright, here's my IG."

        g "Okay. Did you request to follow?"

        m "Yeah! Thank you so much. I'll charge my phone as soon as possible."

        g "Haha, no problem."

        m "I'll let you finish your lunch. I have to head to class. See you later."

        g "Yeah! See you!"

        m "Oh I forgot to say it but my name is Brandon!"

        g "Hahaha my name is Aoi!"

        m "Nice to meet you Aoi!"

        a "Nice to meet you too!"

        "That entire afternoon, my mind felt like it was exploding. I did it. Amazing."
        "Sheeesh my legs are shaking."

        jump after_cof

    label bad_end:
        
        stop music fadeout 1.0

        play music driftaway volume 0.6

        scene sky

        $ preferences.text_cps = 30
        
        m "Yeah, what am I thinking?"
        m "I didn't approach her before and today will not be different..."

        "And just like that, I kept watching from afar. March, April, then May passed."

        "The end of my second year approached."

        "I transferred to a new university, carrying an indescribable sadness."

        "Maybe I was just too cowardly. I kept blaming myself."

        "What a regret."

        return

    label after_cof:

        stop music fadeout 1.0

        play music bleached volume 0.6

        scene campus
        "Since that conversation, my days have been replaced with happier, more lively ones."

        "At the same time, I could comfortably start conversations with her without fearing being seen as disgusting like before."

        "Whenever I walked to the cafeteria, I always hoped she would be sitting near the usual window spot." 
        
        "Then we would talk about things we experienced during the day."

        "At first, the topics were a bit dry. But gradually, more interesting things came up."

        "Thinking about it..." 
        
        "It's actually pretty interesting that I became friends with a Japanese person."

        "I always thought someone like me—a Vietnamese—would have a hard time getting close to a Japanese person, especially a girl."

        "Maybe I just tend to overthink things."

        "Then one day in mid-April—"

        "Aoi suddenly asked me:"
        
        a "Brandon, what are you planning to do next year?"

        "Her question caught me off guard. Because I might be transferring next year."

        "The atmosphere became slightly awkward."

        "Should I tell her?"

        $ preferences.text_cps = 0

        menu:
            "Should I tell her?"

            "Better tell the truth.":
                jump saying

            "I don't want to hurt her feelings...":
                jump not_saying

    label saying:

        $ preferences.text_cps = 30

        stop music fadeout 1.0

        play music ballerina volume 0.6


        m "Aoi, there's something I want to tell you. I just don't know if it'll make you sad."

        a "Hmm? Go ahead. It should be fine."

        "I felt nervous but continued anyway. I thought being honest would be better."

        m "Unfortunately, I won't be here next year. I'll be transferring to a university in another state."

        a "Wait, why transfer? I think this school isn't that bad."

        "Aoi looked slightly sad as she spoke."

        m "Of course it's not bad! But you know... I got a better scholarschip there so I couldn't decline it..."

        a "That's a shame... It would've been nice if you stayed and we could keep meeting like this..."

        a "But HEYYY!!! CONGRATS!!! THAT'S REALLY GOOD!!!"

        m "Thank you so much!!"

        a "..."

        m "..."

        a "Hey we can enjoy the time we have left while you're still here, okay?"

        m "Yeah of course! We have a lot of time!"

        "After that conversation, although Aoi felt a bit sad whenever it came up, the two of us actually grew closer."

        "Eventually, the inevitable came. Final exams passed. The second year ended. And I had to leave."


        scene airport

        "On the day of departure, she messages me:"

        a "So today's the day you leave, right?"

        m "Yeah..."

        a "It's a shame I can't say goodbye in person. I'm in Japan right now. (━┳━ _ ━┳━)"

        m "Haha, it's okay. But I'll miss you. I'll definitely tell you about my new school when I get there!"

        a "Yeah! Don't forget to message me. If you forget I gonna kill you!."

        m "I'd never forget you dummy!"
        
        a "You better not! hmph ╰(⸝⸝⸝´꒳`⸝⸝⸝)╯"

        m "Ahaha see you later Aoi!"
        
        a "See you! Bye bye"

        "The main character moved to a new university. Even though the distance between them grew, they continued to stay in touch."

        "Aoi and the main character became closer over time. Who knows—maybe a bright future awaits them."
        
        return

    label not_saying:

        stop music fadeout 1.0

        play music onceupon volume 0.5

        $ preferences.text_cps = 30
        m "Well, I'm planning to look for internship opportunities. Since third year is when you should start early."

        a "Oh, I see."

        m "What about you?"

        a "I'm not sure yet. Next year will be my second year, so probably the same as this year."

        m "Are you planning to return to Japan after graduation?"

        a "I'm not sure yet if I want to go back or stay here..."

        m "Yeah... It's hard to choose."

        "Final exams came, and I left without Aoi ever knowing."

        "On the begin of the next year, Aoi texts me."

        a "Where are you? I haven't seen you at all. The new school year is about to start. (┳◇┳)"

        m "Aoi… you won't be mad at me for what I'm about to say, right?"

        a "Hmm? Go ahead, I won't be mad."

        m "Actually… I transferred schools. Sorry for not telling you."
        
        m "I didn't want to hurt your feelings."

        "Aoi paused a bit before replying."

        a "Ah haha… it's okay. We can still stay in touch. Just not in person…"

        m "You're really not sad?"

        a "Kinda, but you know... it's your life and if it makes you happy I'm happy too!"

        m "Ohh thank you!! I was just afraid of making you sad. I'm really sorry. (╯_╰)"

        "But in reality, Aoi was very sad that he wasn't honest with her."

        "Even though they stayed in contact, their closeness could never grow further due to the distance."

        "In the end, he did gain a Japanese friend. But it felt bittersweet because he wasn't honest."

        return



    label inicio_pt:

        scene cafe

        "Eu nunca vou esquecer a imagem daquela garota. Aquela que talvez fez meu coração frio tremer mais uma vez."

        "Mas parece que as cenas poéticas que eu sonhei nunca vão se tornar realidade."

        "Tudo que posso fazer é ficar parado e observar ela de longe, sem conseguir fazer nada."

        "“Não é possível.” “A gente nem se conhece—como você vai falar com ela?”"

        "Essas vozes continuavam ecoando na minha mente. Eu realmente não sabia mais o que fazer."

        "Hoje é como qualquer outro dia. A mesma cafeteria de sempre, o mesmo lugar de sempre. Ela está sentada lá de novo. E eu, como sempre, só observando de longe."

        "Meu último ano aqui antes de me transferir para um lugar completamente diferente."

        "AAAAA! Esse poderia ser aquele “momento”—quando o protagonista e a garota se encontram por acaso. Pena que eu sou só um personagem secundário."

        "Droga. Será que eu vou falar com ela?"

        $ preferences.text_cps = 0

        menu:
            "Droga. Será que eu vou falar com ela?"

            "Claro, idiota!":
                menu:
                    "Tem certeza? Você nunca chegou em uma garota antes."

                    "Sim! Tenho certeza!":
                        jump good_end_pt

                    "Ah, melhor ir pra casa jogar League (sou bronze).":
                        jump league_end_pt

            "Nem ferrando, olha pra mim! Tô careca e fedido :/":
                jump bad_end_pt

    label league_end_pt:
        $ preferences.text_cps = 30

        m "EMPURRA A ONDA EZREAL MERDA"

        "30 minutos depois..."

        m "PEGUE O BARÃO!! SMITE SMITE!"

        "5 partidas depois..."

        m "Merda... virei ferro agora..."

        m "..."

        m "O que aconteceu?"
        
        m "..."
        
        m "Isso foi muito melhor do que conversar com uma garota 🔥🔥🔥"

        return

    label good_end_pt:
        $ preferences.text_cps = 30

        "Juntando toda a minha coragem, eu levantei e fui até ela."

        "Eu aguentei tempo demais só olhando sem fazer nada. Agora chega dessa vergonha."

        "À medida que eu me aproximava, parecia que meu coração estava batendo três vezes mais rápido. Nervosismo e várias memórias ruins de conversas passadas vieram como um tsunami."

        "Tanto faz, é tudo ou nada, eu disse pra mim mesmo."

        m "Oi... com licença."

        "Eu forcei as palavras a saírem."

        "Ela olhou pra mim. Nossa! Parecia que eu podia simplesmente… morrer ali mesmo."

        "Ou pelo menos foi o que eu pensei. Talvez seja meio estranho incomodar ela enquanto está comendo?"

        "Com um tom gentil, mas levemente incomodado, ela respondeu:"

        g "Quem é você? Acho que a gente não se conhece?"

        "Droga..."
        "Vamos insistir um pouco mais."

        m "Bom, eu já te vi algumas vezes por aqui. Acho você bonita! Então..."

        "Merda..."
        "O que eu pergunto? Preciso manter a conversa viva..."

        m "Você é americana?"

        g "Não, na verdade eu sou uma estudante internacional."

        m "Ah!"

        m "Eu também! Sou asiático. E você?"

        g "Sério?? Eu também sou asiática!"

        m "Ni hao fine shyt"

        g "..."

        m "haha..."

        m "Foi mal, piada ruim..."

        m "Aliás, eu sou do Vietnã"

        g "Eu sou japonesa"

        m "Sério??? Você não vai acreditar, mas eu tô aprendendo japonês."

        g "Que legal! E como está indo?"

        m "Pra ser sincero, até que bem, mas eu não tenho ninguém pra praticar."

        m "Ei! Você poderia me ajudar? A praticar japonês."

        g "Hmm... eu tô comendo agora então... não é um bom momento, sabe?"

        m "Ah... não quero te incomodar... desculpa."

        m "Bom... prazer em te conhecer."

        "Eu voltei para a minha mesa de sempre."

        "Mas antes de eu sentar, ela disse:"

        g "Espera!! Não é nada estranho um estrangeiro se interessar pela minha língua. Eu te ajudo. Você usa alguma rede social? IG? Line?"

        m "Ah, eu tenho Line, mas nunca usei muito. Ninguém usa isso aqui nos EUA. Também tenho IG. Vamos de IG."

        g "Ok ok."

        m "Ahh... droga..."

        g "O que foi?"

        m "Meu celular morreu..."

        g "Hahaha, tudo bem!"

        g "Aqui, coloca seu usuário que eu te sigo."

        "Ela me deu o iPhone dela e digitou meu IG rapidinho."

        m "Pronto, esse é meu IG."

        g "Ok. Você já pediu pra seguir?"

        m "Sim! Muito obrigado mesmo. Vou carregar meu celular assim que puder."

        g "Haha, tranquilo."

        m "Vou deixar você terminar de comer. Tenho que ir pra aula. Até mais."

        g "Sim! Até!"

        m "Ah, esqueci de falar, meu nome é Brandon!"

        g "Hahaha meu nome é Aoi!"

        m "Prazer em te conhecer, Aoi!"

        a "Prazer!"

        "Naquela tarde inteira, minha mente parecia explodir. Eu consegui. Incrível."

        "Caramba... minhas pernas estão tremendo."

        jump after_cof_pt

    label bad_end_pt:
        $ preferences.text_cps = 30

        m "É... o que eu tava pensando?"

        m "Eu nunca falei com ela antes e hoje não vai ser diferente..."

        "E assim, eu continuei só observando de longe. Março, abril, depois maio passaram."

        "O fim do meu segundo ano chegou."

        "Eu me transferi para outra universidade, carregando uma tristeza indescritível."

        "Talvez eu só tenha sido covarde demais. Continuei me culpando."

        "Que arrependimento."

        return

    label after_cof_pt:

        scene campus

        "Desde aquela conversa, meus dias ficaram mais felizes e animados."

        "Ao mesmo tempo, eu conseguia conversar com ela sem medo de parecer estranho como antes."

        "Sempre que eu ia para a cafeteria, eu torcia para ela estar sentada perto da janela."

        "Então a gente conversava sobre o dia."

        "No começo, os assuntos eram meio sem graça. Mas aos poucos foram ficando mais interessantes."

        "Pensando bem..."

        "É até interessante que eu fiz amizade com uma japonesa."

        "Eu sempre achei que alguém como eu—um vietnamita—teria dificuldade em se aproximar de uma japonesa, ainda mais sendo uma garota."

        "Talvez eu pense demais."

        "Até que um dia, em abril—"

        "Aoi me perguntou:"

        a "Brandon, o que você pretende fazer ano que vem?"

        "A pergunta me pegou de surpresa. Porque talvez eu vá me transferir."

        "O clima ficou meio estranho."

        "Eu devo contar pra ela?"

        $ preferences.text_cps = 0

        menu:
            "Devo contar pra ela?"

            "Melhor ser sincero.":
                jump saying_pt

            "Não quero magoar ela...":
                jump not_saying_pt

        label saying_pt:

        $ preferences.text_cps = 30

        m "Aoi, tem algo que eu quero te contar. Só não sei se vai te deixar triste."

        a "Hmm? Pode falar. Acho que tudo bem."

        "Eu fiquei nervoso, mas continuei mesmo assim. Achei que ser honesto seria melhor."

        m "Infelizmente, eu não vou estar aqui ano que vem. Vou me transferir para uma universidade em outro estado."

        a "Espera, por que transferir? Eu acho que essa faculdade nem é tão ruim."

        "Aoi parecia um pouco triste enquanto falava."

        m "Claro que não é ruim! Mas sabe como é... eu consegui uma bolsa melhor lá, então não pude recusar..."

        a "Que pena... teria sido legal se você ficasse e a gente pudesse continuar se encontrando assim..."

        a "MAS EIIII!!! PARABÉNS!!! ISSO É MUITO BOM!!!"

        m "Muito obrigado!!"

        a "..."

        m "..."

        a "Ei, a gente ainda pode aproveitar o tempo que resta enquanto você está aqui, ok?"

        m "Sim, claro! Ainda temos bastante tempo!"

        "Depois dessa conversa, apesar da Aoi ficar um pouco triste quando o assunto surgia, nós dois acabamos nos aproximando ainda mais."

        "Eventualmente, o inevitável chegou. As provas finais passaram. O segundo ano acabou. E eu tive que ir embora."

        scene airport

        "No dia da partida, ela me manda mensagem:"

        a "Então hoje é o dia que você vai embora, né?"

        m "É..."

        a "Que pena que não posso me despedir pessoalmente. Estou no Japão agora 😭😭"

        m "Haha, tudo bem. Mas vou sentir sua falta. Com certeza vou te contar sobre minha nova faculdade quando chegar lá!"

        a "Sim! Não esquece de me mandar mensagem. Se esquecer eu te mato!."

        m "Eu nunca esqueceria você, sua boba!"

        a "É bom mesmo! hmph 😤"

        m "Ahaha, até mais Aoi!"

        a "Até! Tchau tchau"

        "O protagonista se mudou para uma nova universidade. Mesmo com a distância entre eles aumentando, continuaram mantendo contato."

        "Aoi e o protagonista ficaram mais próximos com o tempo. Quem sabe—talvez um futuro brilhante os espere."

        return


    label not_saying_pt:

        $ preferences.text_cps = 30

        m "Bom, eu estou pensando em procurar estágios. Já que no terceiro ano é quando você deve começar mais cedo."

        a "Ah, entendi."

        m "E você?"

        a "Ainda não sei. Ano que vem vai ser meu segundo ano, então provavelmente igual a esse."

        m "Você pretende voltar pro Japão depois de se formar?"

        a "Não sei ainda se quero voltar ou ficar aqui..."

        m "É... é difícil escolher."

        "As provas finais chegaram, e eu fui embora sem que a Aoi soubesse."

        a "Onde você está? Não te vi mais. O novo ano letivo está prestes a começar 😢😢😢"

        m "Aoi… você não vai ficar brava comigo pelo que eu vou dizer, né?"

        a "Hmm? Pode falar, não vou ficar brava."

        m "Na verdade… eu me transferi de faculdade. Desculpa por não ter te contado."

        m "Eu não queria machucar seus sentimentos."

        "Aoi demorou um pouco antes de responder."

        a "Ah haha… tudo bem. A gente ainda pode manter contato. Só não pessoalmente…"

        m "Você realmente não ficou triste?"

        a "Um pouco, mas sabe... é a sua vida, e se isso te faz feliz, eu também fico feliz!"

        m "Ahh obrigado!! Eu só estava com medo de te deixar triste. Me desculpa mesmo 😭😭😭"

        "Mas na verdade, Aoi ficou muito triste por ele não ter sido honesto."

        "Mesmo continuando em contato, a proximidade entre eles nunca mais pôde crescer por causa da distância."

        "No fim, ele até ganhou uma amiga japonesa. Mas ficou um gosto agridoce, porque ele não foi sincero."

        return


    label start_es:
        scene cafe

        "Nunca olvidaré la imagen de esa chica. La que quizás hizo que mi corazón frío temblara una vez más."

        "Pero parece que las escenas poéticas con las que soñé nunca se harán realidad."

        "Todo lo que puedo hacer es quedarme y observarla desde lejos, sin poder hacer nada."

        "“No es posible.” “Ni siquiera nos conocemos, ¿cómo podrías hablarle?”"

        "Esas voces seguían resonando en mi mente. Realmente no sabía qué hacer ya."

        "Hoy es como cualquier otro día. La misma cafetería familiar, el mismo asiento familiar. Ella está sentada allí otra vez. Y yo, como siempre, solo observando desde lejos."

        "Mi último año aquí antes de transferirme a un lugar completamente diferente."

        "¡AAAA! Este podría ser ese “momento”—cuando el chico y la chica protagonistas se encuentran accidentalmente. Qué pena que solo soy un personaje secundario."

        "Maldita sea. ¿Debería acercarme a ella?"
        $ preferences.text_cps = 0
        menu:
            "Maldita sea. ¿Debería acercarme a ella?" 

            "¡Claro que sí, idiota!":
                menu:
                    "¿Estás seguro? Nunca te has acercado a una chica antes."

                    "¡Sí! ¡Estoy seguro!":
                        jump good_end_es

                    "En serio, mejor vamos a casa a jugar League (soy bronce).":
                        jump league_end_es

            "Nah hermano, ¡mírame! Estoy calvo y huelo horrible :/":
                jump bad_end_es


    label league_end_es:
            $ preferences.text_cps = 30

            m "¡EMPUJA LA OLA EZREAL MIERDA"

            "30 minutos después..."

            m "¡TOMA EL BARÓN!! ¡SMITE SMITE!"

            "5 partidas después..."

            m "Mierda... ahora soy hierro..."

            m "..."

            m "¿Qué pasó?"
            
            m "..."
            
            m "Eso fue mucho mejor que hablar con una chica 🔥🔥🔥"

            return

    label good_end_es:
        $ preferences.text_cps = 30
        "Reuniendo todo mi valor, me levanté y caminé hacia ella."

        "He soportado demasiado tiempo la sensación de solo observar sin hacer nada. Ahora, deshazte de esta vergüenza."

        "Al acercarme, mi corazón parecía triplicarse. Los nervios y una avalancha de recuerdos no tan buenos de conversaciones pasadas con chicas me embargaron como un tsunami."

        "Sea lo que sea, es todo o nada, me dije."

        m "Hola… disculpa."

        "Forcé las palabras a salir."

        "Ella me miró. ¡Oh! Sentí que podría… morir y ascender justo allí."

        "O al menos eso pensé. Tal vez sea un poco raro molestarla mientras come."

        "Con un tono muy gentil, ligeramente molesta, respondió:"

        g "¿Quién eres? Creo que no nos conocemos."

        "Maldición..."
        "Vamos a arriesgarnos un poco más."

        m "Bueno, te he visto por ahí unas cuantas veces. ¡Creo que eres linda! Así que…"
        
        "Maldita sea..." 
        "¿Qué debería preguntar? Necesito mantener la conversación..."

        m "¿Eres estadounidense?"

        g "No, en realidad soy estudiante internacional."

        m "¡Oh!"

        m "¡Yo también! Soy asiático. ¿Y tú?"

        g "¿De verdad?? ¡Yo también soy asiática!"

        m "Ni hao fine shyt"

        g "…"
        
        m "jaja..." 
        
        m "Perdón, mal chiste…"

        m "Por cierto, soy de Vietnam"

        g "Soy japonesa"

        m "¡No puede ser! No lo vas a creer, pero estoy aprendiendo japonés."

        g "¡Qué bien! ¿Y cómo va eso?"

        m "Para ser honesto, bastante bien, pero no tengo con quién practicar."

        m "¡Oye! ¿Podrías ayudarme? Con el japonés."
        
        g "Hmm… estoy comiendo ahora, así que… no es un buen momento, ¿sabes?"

        m "Oh… no quiero molestarte… lo siento."

        m "Bueno… un gusto conocerte."

        "Volví a mi mesa habitual."

        "Pero antes de que pudiera sentarme, ella dijo:"

        g "¡Espera! No es tan desagradable que un extranjero se interese en mi idioma. Te ayudaré. ¿Usas alguna red social? ¿IG? ¿Line?"

        m "Oh, tengo Line, solo que nunca la he usado realmente. Nadie usa Line en EE.UU. de todos modos. También tengo IG. Mejor usemos IG."

        g "Ok, ok."

        m "Ahh… mierda…"

        g "¿Qué?"

        m "Mi teléfono se apagó…"

        g "Jajaja ¡Está bien!"

        g "Mira, busca mi usuario y sígueme."

        "Me dio su iPhone y escribió mi IG rápidamente."

        m "Listo, aquí está mi IG."

        g "Está bien. ¿Solicitaste seguirme?"

        m "¡Sí! Muchas gracias. Cargaré mi teléfono lo antes posible."

        g "Jaja, no hay problema."

        m "Te dejaré terminar tu almuerzo. Tengo que ir a clase. Hasta luego."

        g "¡Sí! ¡Nos vemos!"

        m "Oh, olvidé decirlo, ¡mi nombre es Brandon!"

        g "¡Jajaja, yo soy Aoi!"

        m "¡Un gusto conocerte Aoi!"

        a "¡Igualmente!"

        "Toda esa tarde, sentí que mi mente explotaba. Lo hice. Increíble."
        "Mis piernas están temblando."

        jump after_cof_es

    label bad_end_es:
        $ preferences.text_cps = 30
        
        m "Sí, ¿en qué estaba pensando?"
        m "No me acerqué a ella antes y hoy no será diferente..."

        "Y así, seguí observando desde lejos. Pasaron marzo, abril y mayo."

        "Se acercaba el fin de mi segundo año."

        "Me transferí a una nueva universidad, cargando una tristeza indescriptible."

        "Quizás fui demasiado cobarde. Me seguí culpando."

        "Qué arrepentimiento."

        return

    label after_cof_es:

        scene campus
        "Desde esa conversación, mis días se llenaron de más felicidad y vitalidad."

        "Al mismo tiempo, podía empezar conversaciones con ella sin temer ser visto como desagradable como antes."

        "Cada vez que caminaba hacia la cafetería, esperaba que ella estuviera sentada cerca del lugar habitual junto a la ventana."
        
        "Luego hablábamos sobre cosas que habíamos vivido durante el día."

        "Al principio, los temas eran un poco secos. Pero gradualmente surgieron cosas más interesantes."

        "Pensándolo bien..." 
        
        "Es realmente interesante que haya hecho amistad con una persona japonesa."

        "Siempre pensé que alguien como yo—un vietnamita—tendría dificultades para acercarse a una persona japonesa, especialmente una chica."

        "Quizás tiendo a pensar demasiado."

        "Entonces un día a mediados de abril—"

        "Aoi de repente me preguntó:"
        
        a "Brandon, ¿qué planes tienes para el próximo año?"

        "Su pregunta me tomó por sorpresa. Podría transferirme el próximo año."

        "El ambiente se volvió ligeramente incómodo."

        "¿Debería decirle?"

        $ preferences.text_cps = 0

        menu:
            "¿Debería decirle?"

            "Mejor ser transparente.":
                jump saying_es

            "No quiero herir sus sentimientos...":
                jump not_saying_es

    label saying_es:

        $ preferences.text_cps = 30
        m "Aoi, hay algo que quiero decirte. Solo que no sé si te entristecerá."

        a "Hmm? Adelante. Debería estar bien."

        "Me sentí nervioso, pero continué. Pensé que ser honesto sería mejor."

        m "Desafortunadamente, el próximo año no estaré aquí. Me transferiré a una universidad en otro estado."

        a "Espera, ¿por qué transferirte? Creo que esta escuela no está tan mal."

        "Aoi se veía un poco triste mientras hablaba."

        m "¡Claro que no está mal! Pero ya sabes… obtuve una mejor beca allí, así que no podía rechazarla…"

        a "Qué lástima… hubiera sido agradable que te quedaras y pudiéramos seguir viéndonos así…"

        a "¡Pero HEYYY!!! ¡FELICIDADES!!! ¡ESO ES INCREÍBLE!!!"

        m "¡Muchísimas gracias!"

        a "…"

        m "…"

        a "Oye, podemos disfrutar el tiempo que nos queda mientras aún estás aquí, ¿ok?"

        m "¡Sí, por supuesto! ¡Tenemos mucho tiempo!"

        "Después de esa conversación, aunque Aoi se sentía un poco triste cada vez que surgía el tema, los dos nos acercamos más."

        "Eventualmente, lo inevitable llegó. Pasaron los exámenes finales. Terminó el segundo año. Y tuve que irme."

        scene airport

        "El día de la partida, ella me envió un mensaje:"

        a "Así que hoy es el día que te vas, ¿verdad?"

        m "Sí…"

        a "Qué pena que no pueda despedirme en persona. Estoy en Japón ahora. 😭😭"

        m "Jaja, está bien. Pero te extrañaré. ¡Te contaré todo sobre mi nueva escuela cuando llegue!"

        a "¡Sí! No olvides enviarme un mensaje. Si lo olvidas, ¡te mataré!."

        m "¡Nunca te olvidaría, tonta!"
        
        a "¡Más te vale! hmph 😤"

        m "¡Jaja, nos vemos luego Aoi!"
        
        a "¡Nos vemos! Adiós"

        "El personaje principal se mudó a una nueva universidad. Aunque la distancia creció entre ellos, continuaron en contacto."

        "Aoi y el protagonista se hicieron más cercanos con el tiempo. Quién sabe—tal vez un futuro brillante les espere."
        
        return

    label not_saying_es:

        $ preferences.text_cps = 30
        m "Bueno, estoy planeando buscar oportunidades de prácticas. Ya que el tercer año es cuando uno debería comenzar temprano."

        a "Ah, entiendo."

        m "¿Y tú?"

        a "Todavía no estoy segura. El próximo año será mi segundo año, así que probablemente igual que este."

        m "¿Planeas volver a Japón después de graduarte?"

        a "No estoy segura si quiero volver o quedarme aquí…"

        m "Sí… es difícil elegir."

        "Llegaron los exámenes finales, y me fui sin que Aoi lo supiera."

        a "¿Dónde estás? No te he visto en absoluto. El nuevo año escolar está a punto de comenzar. 😢😢😢"

        m "Aoi… no te enojarás por lo que voy a decir, ¿verdad?"

        a "Hmm? Adelante, no me enojaré."

        m "En realidad… me transferí de escuela. Perdón por no decirte."
        
        m "No quería herirte."

        "Aoi hizo una pausa antes de responder."

        a "Ah jaja… está bien. Podemos seguir en contacto. Solo que no en persona…"

        m "¿De verdad no estás triste?"

        a "Un poco, pero sabes… es tu vida y si te hace feliz, ¡yo también estoy feliz!"

        m "¡Oh, gracias!! Solo tenía miedo de entristecerte. Lo siento mucho. 😭😭😭"

        "Pero en realidad, Aoi estaba muy triste porque no fui honesto con ella."

        "Aunque mantuvieron contacto, su cercanía nunca pudo crecer más debido a la distancia."

        "Al final, sí ganó una amiga japonesa. Pero fue agridulce porque no fui honesto."

        return
    

    label start_ita:

        scene cafe

        "Non dimenticherò mai l'immagine di quella ragazza. Quella che forse ha fatto tremare di nuovo il mio cuore freddo."

        "Ma sembra che le scene poetiche che sognavo non diventeranno mai realtà."

        "Tutto quello che posso fare è stare lì a guardarla da lontano, incapace di fare qualsiasi cosa."

        "“Non è possibile.” “Non ci conosciamo nemmeno—come potresti parlarle?”"

        "Quelle voci continuavano a rimbombare nella mia mente. Davvero non sapevo più cosa fare."

        "Oggi è come ogni altro giorno. La stessa mensa familiare, lo stesso posto familiare. Lei è seduta lì di nuovo. E io, come sempre, solo a guardare da lontano."

        "Il mio ultimo anno qui prima di trasferirmi da qualche altra parte completamente diversa."

        "AAAA! Questo potrebbe essere quel “momento”—quando il ragazzo e la ragazza protagonisti si incontrano per caso. Peccato che io sia solo un personaggio secondario."

        "Dannazione. Dovrei avvicinarmi a lei?"
        $ preferences.text_cps = 0
        menu:
            "Dannazione. Dovrei avvicinarmi a lei?" 

            "Certo, idiota!":
                menu:
                    "Sei sicuro? Non ti sei mai avvicinato a una ragazza prima."

                    "Sì! Sono sicuro!":
                        jump good_end_ita

                    "Davvero, torniamo a casa a giocare a League (sono bronzo).":
                        jump league_end_ita

            "Nah fratello, guardami! Sono calvo e puzzo da morire :/":
                jump bad_end_ita

    label league_end_ita:
        $ preferences.text_cps = 30

        m "SPINGI L'ONDA MERDA EZREAL"

        "30 minuti dopo..."

        m "PRENDIAMO IL BARONE!! SMITE SMITE!"

        "Dopo 5 partite..."

        m "Cazzo... ora sono ferro..."

        m "..."

        m "Che è successo?"

        m "..."

        m "È stato molto meglio che parlare con una ragazza 🔥🔥🔥"

    return

    label good_end_ita:
        $ preferences.text_cps = 30
        "Radunando tutto il mio coraggio, mi alzai e mi avvicinai a lei."

        "Ho sopportato abbastanza la sensazione di guardare senza fare nulla. Ora, liberati di questa vergogna."

        "Avvicinandomi, il mio cuore sembrava triplicare. Nervosismo e una valanga di ricordi non troppo piacevoli di conversazioni passate con ragazze mi travolsero come uno tsunami."

        "Va bene, tutto o niente, mi dissi."

        m "Ciao… scusa."

        "Forzai le parole a uscire."

        "Lei alzò lo sguardo verso di me. Oh! Sembrava che potessi… morire e ascendere lì stesso."

        "O almeno questo pensavo. Forse è un po' strano disturbarla mentre mangia?"

        "Con un tono molto gentile, leggermente infastidita, rispose:"

        g "Chi sei? Non credo che ci conosciamo."

        "Dannazione..."
        "Proviamo ad andare un po' più avanti."

        m "Beh, ti ho visto qualche volta in giro. Penso che tu sia carina! Quindi…"
        
        "Cazzo..." 
        "Cosa dovrei chiedere? Devo mantenere viva la conversazione..."

        m "Sei americana?"

        g "No, in realtà sono una studentessa internazionale."

        m "Oh!"

        m "Anch'io! Sono asiatico. E tu?"

        g "Davvero?? Anch'io sono asiatica!"

        m "Ni hao fine shyt"

        g "…"
        
        m "Haha..." 
        
        m "Scusa, pessima battuta…"

        m "A proposito, vengo dal Vietnam"

        g "Sono giapponese"

        m "No waaay!!! Non ci crederai, ma sto imparando il giapponese."

        g "Che bello! E come va?"

        m "Ad essere onesto, abbastanza bene, ma non ho nessuno con cui praticare."

        m "Ehi! Potresti aiutarmi? Con il giapponese."
        
        g "Hmm… sto mangiando adesso, quindi… non è un buon momento, sai?"

        m "Oh… non voglio disturbarti… scusa."

        m "Comunque… piacere di conoscerti."

        "Tornai al mio solito tavolo."

        "Ma prima che potessi sedermi, disse:"

        g "Aspetta!! Non è così disgustoso che uno straniero sia interessato alla mia lingua. Ti aiuterò. Usi qualche social? IG? Line?"

        m "Oh, ho Line, ma non l'ho mai usato seriamente. Nessuno usa Line negli Stati Uniti comunque. Ho anche IG. Meglio usare IG."

        g "Ok, ok."

        m "Ahh… cazzo…"

        g "Cosa?"

        m "Il mio telefono si è spento…"

        g "Hahaha va bene!"

        g "Guarda, cerca il mio utente e seguimi."

        "Mi diede il suo iPhone e scrisse il mio IG velocemente."

        m "Ecco, il mio IG."

        g "Ok. Hai richiesto di seguirmi?"

        m "Sì! Grazie mille. Caricherò il telefono il prima possibile."

        g "Haha, nessun problema."

        m "Ti lascio finire il pranzo. Devo andare a lezione. Ci vediamo dopo."

        g "Sì! Ci vediamo!"

        m "Oh, mi sono dimenticato di dirlo, mi chiamo Brandon!"

        g "Haha, io sono Aoi!"

        m "Piacere di conoscerti Aoi!"

        a "Piacere mio!"

        "Quel pomeriggio, la mia mente sembrava esplodere. Ce l'ho fatta. Fantastico."
        "Le gambe mi tremano."

        jump after_cof_ita

    label bad_end_ita:
        $ preferences.text_cps = 30
        
        m "Sì, cosa stavo pensando?"
        m "Non mi sono avvicinato a lei prima e oggi non sarà diverso..."

        "E così, continuai a guardare da lontano. Passarono marzo, aprile e maggio."

        "Si avvicinava la fine del mio secondo anno."

        "Mi trasferii in una nuova università, portando con me una tristezza indescrivibile."

        "Forse ero troppo codardo. Continuavo a incolparmi."

        "Che rimpianto."

        return

    label after_cof_ita:

        scene campus
        "Da quella conversazione, i miei giorni sono diventati più felici e vivaci."

        "Allo stesso tempo, potevo iniziare conversazioni con lei senza temere di sembrare disgustoso come prima."

        "Ogni volta che andavo in mensa, speravo sempre che lei fosse seduta vicino al solito posto vicino alla finestra."
        
        "Poi parlavamo delle cose che avevamo vissuto durante il giorno."

        "All'inizio, gli argomenti erano un po' secchi. Ma gradualmente sono emerse cose più interessanti."

        "A pensarci bene..." 
        
        "È davvero interessante che io abbia fatto amicizia con una persona giapponese."

        "Ho sempre pensato che qualcuno come me—un vietnamita—avrebbe avuto difficoltà ad avvicinarsi a una persona giapponese, soprattutto una ragazza."

        "Forse tendo a pensare troppo."

        "Poi un giorno a metà aprile—"

        "Aoi improvvisamente mi chiese:"
        
        a "Brandon, cosa prevedi di fare l'anno prossimo?"

        "La sua domanda mi colse di sorpresa. Potrei trasferirmi l'anno prossimo."

        "L'atmosfera diventò leggermente imbarazzante."

        "Dovrei dirglielo?"

        $ preferences.text_cps = 0

        menu:
            "Dovrei dirglielo?"

            "Meglio essere trasparente.":
                jump saying_ita

            "Non voglio ferire i suoi sentimenti...":
                jump not_saying_ita

    label saying_ita:

        $ preferences.text_cps = 30
        m "Aoi, c'è qualcosa che voglio dirti. Solo che non so se ti rattristerà."

        a "Hmm? Vai avanti. Dovrebbe andare bene."

        "Ero nervoso, ma continuai. Pensavo che essere onesti sarebbe stato meglio."

        m "Sfortunatamente, il prossimo anno non sarò qui. Mi trasferirò in un'università in un altro stato."

        a "Aspetta, perché trasferirti? Penso che questa scuola non sia così male."

        "Aoi sembrava un po' triste mentre parlava."

        m "Certo che non è male! Ma sai… ho ottenuto una borsa di studio migliore lì, quindi non potevo rifiutarla…"

        a "Che peccato… sarebbe stato bello se fossi rimasto e ci saremmo potuti vedere ancora così…"

        a "Ma HEYYY!!! CONGRATULAZIONI!!! È DAVVERO FANTASTICO!!!"

        m "Grazie mille!!"

        a "…"

        m "…"

        a "Ehi, possiamo goderci il tempo che ci resta mentre sei ancora qui, ok?"

        m "Sì, certo! Abbiamo molto tempo!"

        "Dopo quella conversazione, anche se Aoi era un po' triste ogni volta che se ne parlava, in realtà ci avvicinammo di più."

        "Alla fine, l'inevitabile arrivò. Gli esami finali passarono. Il secondo anno finì. E dovetti andare via."

        scene airport

        "Il giorno della partenza, mi scrisse un messaggio:"

        a "Quindi oggi è il giorno in cui te ne vai, giusto?"

        m "Sì…"

        a "Peccato che non possa salutarti di persona. Sono in Giappone adesso. 😭😭"

        m "Haha, va bene. Ma mi mancherai. Ti racconterò tutto sulla mia nuova scuola quando arriverò!"

        a "Sì! Non dimenticare di scrivermi. Se dimentichi, ti ucciderò!."

        m "Non ti dimenticherei mai, sciocca!"
        
        a "Meglio per te! hmph 😤"

        m "Ahaha ci vediamo dopo Aoi!"
        
        a "Ci vediamo! Ciao"

        "Il protagonista si trasferì in una nuova università. Anche se la distanza tra loro crebbe, continuarono a rimanere in contatto."

        "Aoi e il protagonista diventarono più vicini col tempo. Chissà—forse li aspetta un futuro luminoso."
        
        return

    label not_saying_ita:

        $ preferences.text_cps = 30
        m "Beh, sto pianificando di cercare opportunità di tirocinio. Poiché il terzo anno è quando dovresti iniziare presto."

        a "Ah, capisco."

        m "E tu?"

        a "Non sono ancora sicura. Il prossimo anno sarà il mio secondo anno, quindi probabilmente uguale a questo."

        m "Hai intenzione di tornare in Giappone dopo la laurea?"

        a "Non sono sicura se voglio tornare o restare qui…"

        m "Sì… è difficile scegliere."

        "Arrivarono gli esami finali, e me ne andai senza che Aoi lo sapesse."

        a "Dove sei? Non ti ho visto affatto. Il nuovo anno scolastico sta per iniziare. 😢😢😢"

        m "Aoi… non ti arrabbierai per quello che sto per dire, vero?"

        a "Hmm? Vai avanti, non mi arrabbierò."

        m "In realtà… mi sono trasferito di scuola. Scusa per non avertelo detto."
        
        m "Non volevo ferirti."

        "Aoi fece una pausa prima di rispondere."

        a "Ah haha… va bene. Possiamo rimanere in contatto. Solo che non di persona…"

        m "Davvero non sei triste?"

        a "Un po', ma sai… è la tua vita e se ti rende felice, sono felice anch'io!"

        m "Oh, grazie!! Avevo solo paura di renderti triste. Mi dispiace davvero. 😭😭😭"

        "Ma in realtà, Aoi era molto triste che non fossi stato onesto con lei."

        "Anche se rimasero in contatto, la loro vicinanza non poté crescere ulteriormente a causa della distanza."

        "Alla fine, guadagnò un'amica giapponese. Ma fu agrodolce perché non fui onesto."

        return

    label start_fr:
            
        scene cafe

        "Je n'oublierai jamais l'image de cette fille. Celle qui, peut-être, a fait trembler mon cœur froid une fois de plus."

        "Mais il semble que les scènes poétiques dont je rêvais ne deviendront jamais réalité."

        "Tout ce que je peux faire, c'est rester là à l'observer de loin, incapable de faire quoi que ce soit."

        "« Ce n'est pas possible. » « Nous ne nous connaissons même pas — comment pourrais-tu lui parler ? »"

        "Ces voix résonnaient sans cesse dans ma tête. Je ne savais vraiment plus quoi faire."

        "Aujourd'hui est comme tous les autres jours. La même cafétéria familière, la même place familière. Elle est assise là encore. Et moi, comme toujours, je regarde juste de loin."

        "Ma dernière année ici avant de me transférer ailleurs complètement différent."

        "AAAA ! Ça pourrait être ce “moment”—quand le garçon et la fille principaux se rencontrent par hasard. Dommage que je ne sois qu'un personnage secondaire."

        "Merde. Devrais-je aller lui parler ?"
        $ preferences.text_cps = 0
        menu:
            "Merde. Devrais-je aller lui parler ?" 

            "Bien sûr, espèce d'idiot !":
                menu:
                    "Tu es sûr ? Tu ne t'es jamais approché d'une fille avant."

                    "Oui ! Je suis sûr !":
                        jump good_end_fr

                    "Sérieusement, rentrons à la maison et jouons à League (je suis bronze).":
                        jump league_end_fr

            "Non mec, regarde-moi ! Je suis chauve et je pue à mort :/":
                jump bad_end_fr

    label league_end_fr:
        $ preferences.text_cps = 30

        m "POUSSE LA VAGUE MERDE EZREAL"

        "30 minutes plus tard..."

        m "PRENONS LE BARON !! SMITE SMITE !"

        "Après 5 parties..."

        m "Merde... je suis maintenant en fer..."

        m "..."

        m "Que s'est-il passé ?"

        m "..."

        m "C'était bien mieux que de parler à une fille 🔥🔥🔥"

    return
    label good_end_fr:
        $ preferences.text_cps = 30
        "Rassemblant tout mon courage, je me levai et m'avançai vers elle."

        "J'ai assez supporté le sentiment de simplement regarder sans rien faire. Maintenant, débarrassons-nous de cette gêne."

        "En m'approchant, mon cœur semblait tripler. La nervosité et une avalanche de souvenirs pas très agréables de conversations passées avec des filles me submergèrent comme un tsunami."

        "Quoi qu'il en soit, c'est tout ou rien, me dis-je."

        m "Salut… excuse-moi."

        "Je forçai les mots à sortir."

        "Elle leva les yeux vers moi. Oh ! J'avais l'impression de pouvoir… mourir et m'élever juste là."

        "Ou du moins, c'est ce que je pensais. Peut-être que c'est un peu étrange de la déranger pendant qu'elle mange ?"

        "D'une voix très douce, légèrement contrariée, elle répondit :"

        g "Qui es-tu ? Je ne crois pas que nous nous connaissions."

        "Merde..."
        "Allons un peu plus loin."

        m "Eh bien, je t'ai vue quelques fois dans les parages. Je pense que tu es mignonne ! Donc…"
        
        "Merde..." 
        "Que devrais-je demander ? Je dois maintenir la conversation vivante..."

        m "Es-tu américaine ?"

        g "Non, en fait je suis une étudiante internationale."

        m "Oh !"

        m "Moi aussi ! Je suis asiatique. Et toi ?"

        g "Vraiment ?? Moi aussi je suis asiatique !"

        m "Ni hao fine shyt"

        g "…"
        
        m "Haha..." 
        
        m "Désolé, mauvaise blague…"

        m "Au fait, je viens du Vietnam"

        g "Je suis japonaise"

        m "No waaay !!! Tu ne vas pas le croire, mais j'apprends le japonais."

        g "C'est super ! Et comment ça se passe ?"

        m "Pour être honnête, plutôt bien, mais je n'ai personne avec qui pratiquer."

        m "Hé ! Tu pourrais m'aider ? Pour pratiquer le japonais."
        
        g "Hmm… je mange en ce moment, donc… ce n'est pas un bon moment, tu sais ?"

        m "Oh… je ne veux pas te déranger… désolé."

        m "Bon… enchanté."

        "Je retournai à ma table habituelle."

        "Mais avant que je puisse m'asseoir, elle dit :"

        g "Attends !! Ce n'est pas dégoûtant qu'un étranger s'intéresse à ma langue. Je vais t'aider. Tu utilises un réseau social ? IG ? Line ?"

        m "Oh, j'ai Line, mais je ne l'ai jamais vraiment utilisé. Personne n'utilise Line aux États-Unis de toute façon. J'ai aussi IG. Allons-y avec IG."

        g "Ok, ok."

        m "Ahh… merde…"

        g "Quoi ?"

        m "Mon téléphone vient de mourir…"

        g "Hahaha c'est bon !"

        g "Regarde, cherche mon nom d'utilisateur et suis-moi."

        "Elle me donna son iPhone et écrivit mon IG rapidement."

        m "Voilà, mon IG."

        g "Ok. As-tu demandé à me suivre ?"

        m "Oui ! Merci beaucoup. Je chargerai mon téléphone dès que possible."

        g "Haha, pas de problème."

        m "Je te laisse finir ton déjeuner. Je dois aller en cours. À plus tard."

        g "Oui ! À plus tard !"

        m "Oh, j'ai oublié de le dire mais je m'appelle Brandon !"

        g "Haha, moi c'est Aoi !"

        m "Enchanté Aoi !"

        a "Enchantée !"

        "Cet après-midi-là, mon esprit semblait exploser. Je l'ai fait. Incroyable."
        "Mes jambes tremblent."

        jump after_cof_fr

    label bad_end_fr:
        $ preferences.text_cps = 30
        
        m "Oui, à quoi pensais-je ?"
        m "Je ne me suis pas approché d'elle avant et aujourd'hui ne sera pas différent…"

        "Et ainsi, je continuai à observer de loin. Mars, avril, puis mai passèrent."

        "La fin de ma deuxième année approchait."

        "Je me suis transféré dans une nouvelle université, portant une tristesse indescriptible."

        "Peut-être que j'étais juste trop lâche. Je continuais à me blâmer."

        "Quel regret."

        return

    label after_cof_fr:

        scene campus
        "Depuis cette conversation, mes journées sont devenues plus joyeuses et animées."

        "En même temps, je pouvais commencer des conversations avec elle sans craindre d’être perçu comme dégoûtant comme avant."

        "Chaque fois que j'allais à la cafétéria, j'espérais toujours qu'elle soit assise près de la place habituelle à côté de la fenêtre."
        
        "Puis nous parlions des choses que nous avions vécues dans la journée."

        "Au début, les sujets étaient un peu secs. Mais progressivement, des choses plus intéressantes apparaissaient."

        "À y réfléchir..." 
        
        "C'est plutôt intéressant que je sois devenu ami avec une Japonaise."

        "J'ai toujours pensé que quelqu'un comme moi — un Vietnamien — aurait du mal à se rapprocher d'une Japonaise, surtout une fille."

        "Peut-être que je réfléchis trop."

        "Puis un jour, à la mi-avril—"

        "Aoi me demanda soudain :"
        
        a "Brandon, que comptes-tu faire l'année prochaine ?"

        "Sa question me prit au dépourvu. Car je pourrais me transférer l'année prochaine."

        "L'atmosphère devint légèrement gênante."

        "Devrais-je le lui dire ?"

        $ preferences.text_cps = 0

        menu:
            "Devrais-je le lui dire ?"

            "Mieux vaut être transparent.":
                jump saying_fr

            "Je ne veux pas lui faire de la peine…":
                jump not_saying_fr

    label saying_fr:

        $ preferences.text_cps = 30
        m "Aoi, il y a quelque chose que je veux te dire. Je ne sais pas si ça va te rendre triste."

        a "Hmm ? Vas-y. Ça devrait aller."

        "J'étais nerveux mais je continuai. Je pensais qu'être honnête serait mieux."

        m "Malheureusement, je ne serai pas ici l'année prochaine. Je vais me transférer dans une université dans un autre état."

        a "Attends, pourquoi te transférer ? Je pense que cette école n'est pas si mal."

        "Aoi semblait un peu triste en parlant."

        m "Bien sûr que ce n'est pas mal ! Mais tu sais… j'ai obtenu une meilleure bourse là-bas donc je ne pouvais pas refuser…"

        a "Quel dommage… ça aurait été bien si tu étais resté et que nous pouvions continuer à nous voir comme ça…"

        a "Mais HEYYY !!! FÉLICITATIONS !!! C'EST VRAIMENT BIEN !!!"

        m "Merci beaucoup !!"

        a "…"

        m "…"

        a "Hé, nous pouvons profiter du temps qu'il nous reste tant que tu es encore là, d'accord ?"

        m "Oui bien sûr ! Nous avons beaucoup de temps !"

        "Après cette conversation, même si Aoi était un peu triste chaque fois que le sujet revenait, nous nous sommes en fait rapprochés."

        "Finalement, l'inévitable arriva. Les examens finaux passèrent. La deuxième année se termina. Et je dus partir."

        scene airport

        "Le jour du départ, elle m'envoya un message :"

        a "Alors aujourd'hui, c'est le jour où tu pars, n'est-ce pas ?"

        m "Oui…"

        a "Dommage que je ne puisse pas te dire au revoir en personne. Je suis au Japon maintenant. 😭😭"

        m "Haha, ça va. Mais tu vas me manquer. Je te raconterai tout sur ma nouvelle école quand j'arriverai !"

        a "Oui ! N'oublie pas de m'envoyer un message. Si tu oublies, je vais te tuer !."

        m "Je ne t'oublierai jamais, idiote !"
        
        a "Tu ferais mieux de ne pas ! hmph 😤"

        m "Ahaha, à plus tard Aoi !"
        
        a "À plus tard ! Bye bye"

        "Le protagoniste déménagea dans une nouvelle université. Même si la distance entre eux augmenta, ils restèrent en contact."

        "Aoi et le protagoniste se rapprochèrent avec le temps. Qui sait — peut-être qu'un avenir radieux les attend."
        
        return

    label not_saying_fr:

        $ preferences.text_cps = 30
        m "Eh bien, je prévois de chercher des opportunités de stage. Puisque la troisième année est le moment où il faut commencer tôt."

        a "Oh, je vois."

        m "Et toi ?"

        a "Je ne sais pas encore. L'année prochaine sera ma deuxième année, donc probablement pareil que cette année."

        m "As-tu l'intention de retourner au Japon après l'obtention du diplôme ?"

        a "Je ne sais pas encore si je veux revenir ou rester ici…"

        m "Oui… c'est difficile de choisir."

        "Les examens finaux arrivèrent, et je partis sans qu'Aoi le sache."

        a "Où es-tu ? Je ne t'ai pas du tout vu. La nouvelle année scolaire est sur le point de commencer. 😢😢😢"

        m "Aoi… tu ne seras pas fâchée par ce que je vais dire, n'est-ce pas ?"

        a "Hmm ? Vas-y, je ne me fâcherai pas."

        m "En fait… je me suis transféré dans une autre école. Désolé de ne pas te l'avoir dit."
        
        m "Je ne voulais pas te blesser."

        "Aoi fit une pause avant de répondre."

        a "Ah haha… ça va. Nous pouvons rester en contact. Juste pas en personne…"

        m "Tu n'es vraiment pas triste ?"

        a "Un peu, mais tu sais… c'est ta vie et si ça te rend heureux, je suis heureuse aussi !"

        m "Oh merci !! J'avais juste peur de te rendre triste. Je suis vraiment désolé. 😭😭😭"

        "Mais en réalité, Aoi était très triste que je n'aie pas été honnête avec elle."

        "Même s'ils restèrent en contact, leur proximité ne put jamais s'approfondir à cause de la distance."

        "Finalement, il eut une amie japonaise. Mais ce fut doux-amer car il n'avait pas été honnête."

        return



    label start_german:
            
        scene cafe

        "Ich werde das Bild dieses Mädchens nie vergessen. Diejenige, die vielleicht mein kaltes Herz noch einmal zum Beben gebracht hat."

        "Aber es scheint, dass die poetischen Szenen, von denen ich träumte, niemals Wirklichkeit werden."

        "Alles, was ich tun kann, ist, von weitem zuzusehen, unfähig, etwas zu unternehmen."

        "„Es ist nicht möglich.“ „Wir kennen uns doch gar nicht – wie könntest du mit ihr sprechen?“"

        "Diese Stimmen hallten immer wieder in meinem Kopf wider. Ich wusste wirklich nicht mehr, was ich tun sollte."

        "Heute ist wie jeder andere Tag. Dieselbe vertraute Cafeteria, derselbe vertraute Platz. Sie sitzt wieder dort. Und ich, wie immer, nur zuschauend aus der Ferne."

        "Mein letztes Jahr hier, bevor ich irgendwohin ganz anders wechsle."

        "AAAAA! Das könnte dieser „Moment“ sein – wenn der Junge und das Mädchen zufällig aufeinandertreffen. Schade, dass ich nur eine Nebenfigur bin."

        "Verdammt. Soll ich auf sie zugehen?"
        $ preferences.text_cps = 0
        menu:
            "Verdammt. Soll ich auf sie zugehen?" 

            "Natürlich, du Trottel!":
                menu:
                    "Bist du sicher? Du hast noch nie ein Mädchen angesprochen."

                    "Ja! Ich bin sicher!":
                        jump good_end_german

                    "Echt, lass uns nach Hause gehen und League spielen (ich bin Bronze).":
                        jump league_end_german

            "Nee Mann, schau mich an! Ich bin kahl und stinkig :/":
                jump bad_end_german

    label league_end_german:
        $ preferences.text_cps = 30

        m "SCHIEB DIE WELLE VERDAMMT EZREAL"

        "30 Minuten später..."

        m "HOLT DEN BARON!! SMITE SMITE!"

        "Nach 5 Spielen..."

        m "Scheiße... ich bin jetzt Eisen..."

        m "..."

        m "Was ist passiert?"

        m "..."

        m "Das war viel besser als mit einem Mädchen zu reden 🔥🔥🔥"

        return

    label good_end_german:
        $ preferences.text_cps = 30
        "Mit all meinem Mut stand ich auf und ging auf sie zu."

        "Ich habe das Gefühl, nur zuzusehen und nichts zu tun, lange genug ertragen. Jetzt, weg mit dieser Verlegenheit."

        "Als ich näher kam, fühlte sich mein Herzschlag wie verdreifacht an. Nervosität und eine Flut nicht so guter Erinnerungen an frühere Gespräche mit Mädchen stürzten auf mich ein wie ein Tsunami."

        "Egal, alles oder nichts, sagte ich mir."

        m "Hey... entschuldige."

        "Ich zwang die Worte heraus."

        "Sie sah mich an. Oh! Es fühlte sich an, als könnte ich einfach… hier sterben und aufsteigen."

        "Oder zumindest dachte ich das. Vielleicht ist es ein bisschen seltsam, sie zu stören, während sie isst?"

        "In einem sehr sanften, leicht genervten Ton antwortete sie:"

        g "Wer bist du? Ich glaube, wir kennen uns nicht?"

        "Verdammt..."
        "Lass uns ein bisschen weiter gehen."

        m "Nun, ich habe dich ein paar Mal gesehen. Ich finde dich süß! Also..."

        "Scheiße..." 
        "Was soll ich fragen? Ich muss das Gespräch am Laufen halten..."

        m "Bist du Amerikanerin?"

        g "Nein, eigentlich bin ich internationale Studentin."

        m "Oh!"

        m "Ich auch! Ich bin asiatisch. Und du?"

        g "Echt?? Ich bin auch asiatisch!"

        m "Ni hao, fine shyt"

        g "..."

        m "Haha..." 

        m "Mein Fehler, schlechter Witz..."

        m "Übrigens, ich komme aus Vietnam"

        g "Ich bin Japanerin"

        m "Nein waaay!!! Du wirst es nicht glauben, aber ich lerne Japanisch."

        g "Das ist schön! Und wie läuft es?"

        m "Ehrlich gesagt, ganz gut, aber ich habe niemanden zum Üben."

        m "Hey! Kannst du mir helfen? Beim Japanisch üben."

        g "Hmm... Ich esse gerade, also... ist gerade keine gute Zeit, weißt du?"

        m "Oh... ich will dich nicht stören... Entschuldigung."

        m "Na ja... schön, dich kennenzulernen."

        "Ich drehte mich zurück zu meinem üblichen Tisch."

        "Aber bevor ich mich setzen konnte, sagte sie:"

        g "Warte!! Es ist nicht eklig, dass sich ein Ausländer für meine Sprache interessiert. Ich helfe dir. Benutzt du Social Media? IG? Line?"

        m "Oh, ich habe Line, habe es aber nie wirklich benutzt. In den USA benutzt sowieso niemand Line. Ich habe auch IG. Dann nehmen wir IG."

        g "Ok ok."

        m "Ahh... Scheiße..."

        g "Was?"

        m "Mein Handy ist gerade ausgegangen..."

        g "Hahaha, ist schon ok!"

        g "Gib mir deinen Usernamen, ich folge dir."

        "Sie gab mir ihr iPhone und tippte meinen IG-Account sehr schnell ein."

        m "Alles klar, hier ist mein IG."

        g "Okay. Hast du die Anfrage geschickt?"

        m "Ja! Vielen Dank. Ich lade mein Handy so schnell wie möglich auf."

        g "Haha, kein Problem."

        m "Ich lasse dich dein Mittagessen beenden. Ich muss zum Unterricht. Bis später."

        g "Ja! Bis dann!"

        m "Oh, ich habe vergessen zu sagen, mein Name ist Brandon!"

        g "Hahaha, mein Name ist Aoi!"

        m "Schön, dich kennenzulernen, Aoi!"

        a "Schön, dich auch kennenzulernen!"

        "Den ganzen Nachmittag fühlte sich mein Kopf an, als würde er explodieren. Ich hab es geschafft. Unglaublich."
        "Mann, meine Beine zittern."

        jump after_cof_german

    label bad_end_german:
        $ preferences.text_cps = 30
        
        m "Ja, was denke ich mir nur?"
        m "Ich habe sie vorher nicht angesprochen, und heute wird es nicht anders sein..."

        "Und so sah ich weiter aus der Ferne zu. März, April, dann Mai vergingen."

        "Das Ende meines zweiten Jahres rückte näher."

        "Ich wechselte zu einer neuen Universität, mit einem unbeschreiblichen Gefühl der Traurigkeit."

        "Vielleicht war ich einfach zu feige. Ich gab mir selbst die Schuld."

        "Was für ein Bedauern."

        return

    label after_cof_german:

        scene campus
        "Seit diesem Gespräch wurden meine Tage glücklicher und lebendiger."

        "Gleichzeitig konnte ich nun problemlos Gespräche mit ihr beginnen, ohne Angst zu haben, wie zuvor ekelhaft wahrgenommen zu werden."

        "Wann immer ich zur Cafeteria ging, hoffte ich immer, dass sie an ihrem üblichen Platz am Fenster sitzen würde."

        "Dann unterhielten wir uns über Dinge, die wir tagsüber erlebt hatten."

        "Anfangs waren die Themen etwas trocken. Aber nach und nach kamen interessantere Dinge auf."

        "Wenn ich darüber nachdenke..."

        "Es ist tatsächlich ziemlich interessant, dass ich mit einer Japanerin befreundet bin."

        "Ich dachte immer, jemand wie ich – ein Vietnamese – hätte es schwer, einem japanischen Mädchen näherzukommen."

        "Vielleicht neige ich einfach dazu, zu viel nachzudenken."

        "Dann, eines Tages Mitte April—"

        "Fragte Aoi mich plötzlich:"

        a "Brandon, was hast du nächstes Jahr vor?"

        "Ihre Frage überraschte mich, da ich vielleicht nächstes Jahr wechseln würde."

        "Die Atmosphäre wurde etwas unangenehm."

        "Soll ich es ihr sagen?"

        $ preferences.text_cps = 0

        menu:
            "Soll ich es ihr sagen?"

            "Besser ehrlich sein.":
                jump saying_german

            "Ich will ihre Gefühle nicht verletzen...":
                jump not_saying_german

    label saying_german:

        $ preferences.text_cps = 30
        m "Aoi, es gibt etwas, das ich dir sagen möchte. Ich weiß nur nicht, ob es dich traurig macht."

        a "Hmm? Sag es ruhig. Es sollte in Ordnung sein."

        "Ich fühlte mich nervös, aber sprach trotzdem weiter. Ich dachte, es wäre besser, ehrlich zu sein."

        m "Leider werde ich nächstes Jahr nicht hier sein. Ich werde zu einer Universität in einem anderen Bundesstaat wechseln."

        a "Warte, warum wechseln? Ich denke, diese Schule ist nicht so schlecht."

        "Aoi sah dabei etwas traurig aus."

        m "Natürlich ist sie nicht schlecht! Aber weißt du... Ich bekam dort ein besseres Stipendium, also konnte ich nicht ablehnen..."

        a "Das ist schade... Es wäre schön gewesen, wenn du geblieben wärst und wir uns weiterhin so treffen könnten..."

        a "Aber HEYYY!!! HERZLICHEN GLÜCKWUNSCH!!! DAS IST WIRKLICH GUT!!!"

        m "Vielen Dank!!"

        a "..."

        m "..."

        a "Hey, wir können die Zeit, die wir noch haben, genießen, solange du noch hier bist, okay?"

        m "Ja, natürlich! Wir haben viel Zeit!"

        "Nach diesem Gespräch, obwohl Aoi sich manchmal etwas traurig fühlte, wuchsen wir tatsächlich näher zusammen."

        "Schließlich kam das Unvermeidliche. Die Abschlussprüfungen bestanden. Das zweite Jahr endete. Und ich musste gehen."

        scene airport

        "Am Tag der Abreise schrieb sie mir:"

        a "Also, heute ist der Tag, an dem du gehst, richtig?"

        m "Ja..."

        a "Schade, dass ich mich nicht persönlich verabschieden kann. Ich bin gerade in Japan. 😭😭"

        m "Haha, ist schon okay. Aber ich werde dich vermissen. Ich werde dir definitiv von meiner neuen Schule erzählen, wenn ich dort ankomme!"

        a "Ja! Vergiss nicht mir zu schreiben. Wenn du es vergisst, bringe ich dich um!."

        m "Ich würde dich nie vergessen, Dummkopf!"

        a "Du besser nicht! Hmpf 😤"

        m "Ahaha, bis später, Aoi!"

        a "Bis dann! Tschüss"

        "Der Hauptcharakter zog an eine neue Universität. Auch wenn die Entfernung zwischen ihnen wuchs, blieben sie in Kontakt."

        "Aoi und der Hauptcharakter wurden mit der Zeit enger. Wer weiß – vielleicht erwartet sie eine strahlende Zukunft."

        return

    label not_saying_german:

        $ preferences.text_cps = 30
        m "Nun, ich plane, nach Praktikumsmöglichkeiten zu suchen. Im dritten Jahr sollte man früh anfangen."

        a "Oh, verstehe."

        m "Und du?"

        a "Ich bin mir noch nicht sicher. Nächstes Jahr wird mein zweites Jahr sein, also wahrscheinlich dasselbe wie dieses Jahr."

        m "Planst du nach dem Abschluss nach Japan zurückzukehren?"

        a "Ich bin mir noch nicht sicher, ob ich zurück will oder hier bleiben..."

        m "Ja... schwer zu entscheiden."

        "Die Abschlussprüfungen kamen, und ich ging, ohne dass Aoi es wusste."

        a "Wo bist du? Ich habe dich überhaupt nicht gesehen. Das neue Schuljahr beginnt bald. 😢😢😢"

        m "Aoi… du wirst mir nicht böse sein für das, was ich jetzt sage, oder?"

        a "Hmm? Sag ruhig, ich werde nicht böse sein."

        m "Eigentlich… ich habe die Schule gewechselt. Tut mir leid, dass ich es dir nicht gesagt habe."

        m "Ich wollte deine Gefühle nicht verletzen."

        "Aoi machte eine kurze Pause, bevor sie antwortete."

        a "Ah haha… es ist okay. Wir können trotzdem in Kontakt bleiben. Nur nicht persönlich…"

        m "Du bist wirklich nicht traurig?"

        a "Ein bisschen, aber weißt du... es ist dein Leben, und wenn es dich glücklich macht, bin ich auch glücklich!"

        m "Ohh danke!! Ich hatte nur Angst, dich traurig zu machen. Es tut mir wirklich leid. 😭😭😭"

        "Aber in Wirklichkeit war Aoi sehr traurig, dass er nicht ehrlich zu ihr war."

        "Auch wenn sie in Kontakt blieben, konnte ihre Nähe aufgrund der Entfernung nie weiter wachsen."

        "Am Ende gewann er eine japanische Freundin. Aber es fühlte sich bittersüß an, weil er nicht ehrlich war."

        return

    label start_vi:
        scene cafe

        "Tôi sẽ không bao giờ quên hình ảnh của cô gái đó. Người mà có lẽ đã khiến trái tim lạnh lùng của tôi rung động một lần nữa."

        "Nhưng có vẻ như những cảnh thơ mộng mà tôi mơ sẽ không bao giờ trở thành hiện thực."

        "Tất cả những gì tôi có thể làm là đứng nhìn cô ấy từ xa, không thể làm gì cả."

        "“Không thể được.” “Chúng ta còn chưa biết nhau—làm sao mà cậu dám nói chuyện với cô ấy?”"

        "Những tiếng nói đó cứ vang lên trong đầu tôi. Tôi thực sự không biết phải làm gì nữa."

        "Hôm nay cũng giống như mọi ngày khác. Căn tin quen thuộc, chỗ ngồi quen thuộc. Cô ấy lại ngồi đó. Và tôi, như mọi khi, chỉ nhìn từ xa."

        "Năm cuối cùng của tôi trước khi chuyển đến một nơi hoàn toàn khác."

        "AAAAA! Đây có thể là “khoảnh khắc”—khi nam chính và nữ chính vô tình gặp nhau. Tiếc là tôi chỉ là nhân vật phụ."

        "Chết tiệt. Tôi có nên tiến đến gần cô ấy không?"

        $ preferences.text_cps = 0

        menu:
            "Chết tiệt. Tôi có nên tiến đến gần cô ấy không?" 

            "Tất nhiên rồi, đồ ngốc!":
                menu:
                    "Mày chắc chứ? Chưa bao giờ mà mày thực sự tiếp cận một cô gái và nói chuyện với cổ trước giờ luôn á nha."

                    "Ừ! Tao chắc chắn là tao sẽ làm đưuọc cái gì đó bự lần này!":
                        jump good_end_vi

                    "À vậy à, về nhà chơi Liên Minh luôn (đồng đoàn thẳng tiến).":
                        jump league_end_vi

            "Không đâu, nhìn bản thân của mày kìa! Đúng chất thằng hôi lông :/":
                jump bad_end_vi

    label league_end_vi:
            $ preferences.text_cps = 30

            m "Đẩy wave lính đi Ezreal, dễ ẹc à sao mày ngo thế con!"

            "30 phút sau..."

            m "LẤY BARON!! SMITE SMITE!!"

            "5 trận sau..."

            m "Chết tiệt... giờ thành sắt đoàn mẹ rồi..."

            m "..."

            m "Chuyện gì vừa xảy ra vậy?"
            
            m "..."

            m "Bruh tính ra chơi Liên Minh vẫn vui chán."

            m "Vui hơn hẳn là nói chuyện với cô ta, hẹ hẹ hẹ."

            return

    label good_end_vi:
            $ preferences.text_cps = 30
            "Tập hết can đảm, tôi đứng dậy và tiến về phía cô ấy."

            "Tôi đã chịu đựng cảm giác chỉ nhìn mà không làm gì quá lâu rồi. Giờ thì xóa bỏ sự xấu hổ này."

            "Khi tiến gần, tim tôi đập như gấp ba lần. Sự lo lắng và những kỷ niệm không mấy tốt đẹp từ các cuộc trò chuyện trước đây ùa về như sóng thần."

            "Thôi được, tất cả hoặc không gì cả, tôi tự nhủ."

            m "Chào... xin lỗi."

            "Tôi gắng gượng nói ra câu đó."

            "Cô ấy ngẩng lên nhìn tôi. Ôi! Cảm giác như tôi có thể chết và lên thiên đường ngay tại chỗ."

            "Ít nhất đó là cảm giác của tôi. Có lẽ hơi lạ khi làm phiền cô ấy khi cô ấy đang ăn?"

            "Với giọng nhẹ nhàng, hơi khó chịu, cô ấy trả lời:"

            g "Bạn là ai? Mình nghĩ chúng ta chưa quen biết gì nhau hết á?"

            "Chết tiệt..."
            "Tiếp tục một chút."

            m "À, tôi đã thấy bạn vài lần. Tôi nghĩ bạn dễ thương! Vậy nên..."

            "Chết tiệt..." 
            "Tôi nên hỏi gì đây? Tôi cần giữ cuộc trò chuyện sống động..."

            m "Bạn là người Mỹ phải không?"

            g "Không, thực ra tôi là sinh viên quốc tế."

            m "Ồ!"

            m "Tôi cũng vậy!"

            g "Thật sao??"

            m "Ni hao fine shyt"

            g "..."

            "Bỏ mẹ. Đùa ngo quá. Chết con rồi. AAAAAA."

            m "Haha..." 

            m "Xin lỗi nha, mình nhạt vl..."

            m "Nhân tiện mình là người Việt"

            g "Tôi là người Nhật"

            m "Không thể tin được!!! Nhưng tôi đang học tiếng Nhật á."

            g "Hay quá! Và tiến triển thế nào rồi?"

            m "Thành thật mà nói, cũng khá tốt nhưng tôi không có ai để luyện cùng."

            m "Này! Bạn có thể giúp tôi không?"
            
            g "Hmm... tôi đang ăn, nên... không phải lúc tốt đâu."

            m "Ồ... tôi không muốn làm phiền bạn... Xin lỗi."

            m "Chà... thật vui khi gặp bạn."

            "Tôi quay về bàn quen thuộc của mình."

            "Nhưng trước khi tôi kịp ngồi xuống, cô ấy nói:"

            g "Đợi!! Không đến mức ghê tởm khi một người nước ngoài quan tâm đến ngôn ngữ của tôi đâu. Tôi sẽ giúp bạn. Bạn có dùng mạng xã hội không? IG? Line?"

            m "Ồ, tôi có Line nhưng chưa dùng bao giờ. Ở Mỹ cũng ít người dùng Line. Tôi cũng có IG. Vậy dùng IG nhé."

            g "Ok ok."

            m "Ahh... chết tiệt..."

            g "Gì vậy?"

            m "Điện thoại tôi vừa hết pin..."

            g "Hahaha không sao đâu!"

            g "Đưa tôi tìm tên người dùng của bạn và follow nhé."

            "Cô ấy đưa tôi iPhone và nhanh chóng gõ IG của tôi."

            m "Được rồi, đây là IG của tôi."

            g "Ok. Đã gửi yêu cầu follow chưa?"

            m "Rồi! Cảm ơn bạn rất nhiều. Tôi sẽ sạc điện thoại ngay lập tức."

            g "Haha, không sao đâu."

            m "Tôi sẽ để bạn ăn tiếp. Tôi phải đi học. Hẹn gặp lại nhé."

            g "Ừ! Hẹn gặp lại!"

            m "Ồ, tôi quên nói tên mình là Brandon!"

            g "Haha, tôi tên là Aoi!"

            m "Rất vui được gặp bạn Aoi!"

            a "Rất vui được gặp bạn nữa!"

            "Suốt cả buổi chiều, tâm trí tôi như nổ tung. Tôi đã làm được. Tuyệt vời."
            "Chân tôi run rẩy."

            jump after_cof_vi

    label bad_end_vi:
            $ preferences.text_cps = 30
            
            m "Ừ, tôi đang nghĩ gì vậy?"
            m "Tôi chưa từng tiếp cận cô ấy và hôm nay cũng vậy..."

            "Và cứ như thế, tôi chỉ nhìn từ xa. Tháng Ba, tháng Tư, rồi tháng Năm trôi qua."

            "Cuối năm thứ hai cũng đến."

            "Tôi chuyển đến trường mới, mang theo nỗi buồn không thể diễn tả."

            "Có lẽ tôi quá nhút nhát. Tôi cứ tự trách bản thân."

            "Thật hối tiếc."

            return

    label after_cof_vi:

    scene campus
    "Kể từ cuộc trò chuyện đó, những ngày của tôi trở nên hạnh phúc và sống động hơn."

    "Đồng thời, tôi có thể bắt đầu trò chuyện với cô ấy mà không sợ bị coi là khó chịu như trước."

    "Mỗi khi tôi đi đến căn tin, tôi luôn hy vọng cô ấy sẽ ngồi gần cửa sổ quen thuộc." 
    
    "Rồi chúng tôi trò chuyện về những điều xảy ra trong ngày."

    "Lúc đầu, chủ đề hơi khô khan. Nhưng dần dần, những chuyện thú vị hơn xuất hiện."

    "Nhìn lại..." 
    
    "Thật thú vị khi tôi đã trở thành bạn với một người Nhật."

    "Tôi luôn nghĩ người như tôi — một người Việt — sẽ khó gần gũi với một người Nhật, đặc biệt là con gái."

    "Có lẽ tôi chỉ hay suy nghĩ quá nhiều."

    "Rồi một ngày giữa tháng Tư —"

    "Aoi bất ngờ hỏi tôi:"
    
    a "Brandon, năm tới cậu định làm gì?"

    "Câu hỏi của cô ấy khiến tôi bất ngờ. Bởi vì có thể tôi sẽ chuyển trường năm tới."

    "Không khí trở nên hơi ngượng ngùng."

    "Tôi có nên nói thật không?"

    $ preferences.text_cps = 0

    menu:
        "Tôi có nên nói thật không?"

        "Nên thành thật.":
            jump saying_vi

        "Tôi không muốn làm cô ấy buồn...":
            jump not_saying_vi

    label saying_vi:

        $ preferences.text_cps = 30
        m "Aoi, có chuyện tôi muốn nói với cậu. Tôi chỉ không biết nó sẽ làm cậu buồn không."

        a "Hmm? Nói đi. Không sao đâu."

        "Tôi cảm thấy lo lắng nhưng vẫn tiếp tục. Tôi nghĩ thành thật là tốt hơn."

        m "Thật không may, tôi sẽ không ở đây năm tới. Tôi sẽ chuyển đến một trường đại học khác."

        a "Chờ đã, sao lại chuyển? Tôi nghĩ trường này cũng không tệ."

        "Aoi hơi buồn khi nói vậy."

        m "Dĩ nhiên trường này không tệ! Nhưng cậu biết đấy... tôi nhận được học bổng tốt hơn nên không thể từ chối..."

        a "Thật tiếc... Sẽ thật tuyệt nếu cậu ở lại và chúng ta vẫn gặp nhau như này..."

        a "Nhưng HEYYY!!! CHÚC MỪNG!!! THẬT TUYỆT VỜI!!!"

        m "Cảm ơn cậu rất nhiều!!"

        a "..."

        m "..."

        a "Này, chúng ta hãy tận hưởng thời gian còn lại khi cậu vẫn còn ở đây nhé!"

        m "Ừ tất nhiên! Chúng ta còn nhiều thời gian!"

        "Sau cuộc trò chuyện đó, dù Aoi hơi buồn khi nhắc lại, hai chúng tôi thực sự trở nên gần gũi hơn."

        "Cuối cùng, điều không thể tránh khỏi đã đến. Kỳ thi kết thúc. Năm thứ hai kết thúc. Và tôi phải đi."

        scene airport

        "Ngày ra đi, cô ấy nhắn tin cho tôi:"

        a "Hôm nay là ngày cậu đi phải không?"

        m "Ừ..."

        a "Thật tiếc là tôi không thể nói lời tạm biệt trực tiếp. Tôi đang ở Nhật. 😭😭"

        m "Haha, không sao đâu. Nhưng tôi sẽ nhớ cậu. Tôi sẽ kể cho cậu về trường mới khi đến đó!"

        a "Ừ! Đừng quên nhắn tin nhé. Nếu quên thì tôi sẽ giết cậu!"

        m "Tôi sẽ không bao giờ quên cậu đâu, đồ ngốc!"

        a "Cậu tốt nhất đấy! hmph 😤"

        m "Ahaha, hẹn gặp lại Aoi!"

        a "Hẹn gặp lại! Tạm biệt"

        "Nhân vật chính chuyển đến một trường đại học mới. Dù khoảng cách giữa họ lớn hơn, họ vẫn giữ liên lạc."

        "Aoi và nhân vật chính trở nên gần gũi hơn theo thời gian. Ai mà biết—có thể tương lai tươi sáng đang chờ đợi họ."

        return

    label not_saying_vi:

        $ preferences.text_cps = 30
        m "À, tôi đang định tìm cơ hội thực tập. Vì năm ba là lúc nên bắt đầu sớm."

        a "Ồ, tôi hiểu rồi."

        m "Còn cậu thì sao?"

        a "Tôi chưa chắc. Năm tới sẽ là năm hai của tôi, nên có lẽ cũng giống năm nay."

        m "Cậu có định về Nhật sau khi tốt nghiệp không?"

        a "Tôi chưa chắc là muốn về hay ở lại..."

        m "Ừ... Thật khó để quyết định."

        "Kỳ thi kết thúc, và tôi rời đi mà Aoi không hề biết."

        a "Cậu đâu rồi? Tôi chẳng thấy cậu đâu cả. Năm học mới sắp bắt đầu. 😢😢😢"

        m "Aoi… cậu sẽ không giận tôi về chuyện sắp nói chứ?"

        a "Hmm? Nói đi, tôi sẽ không giận đâu."

        m "Thực ra… tôi đã chuyển trường. Xin lỗi vì không nói với cậu."

        m "Tôi không muốn làm cậu buồn."

        "Aoi dừng lại một chút trước khi trả lời."

        a "Ah haha… không sao đâu. Chúng ta vẫn có thể giữ liên lạc. Chỉ là không gặp trực tiếp thôi…"

        m "Cậu thật sự không buồn sao?"

        a "Hơi buồn chút, nhưng cậu biết đấy… nếu điều đó làm cậu vui, tôi cũng vui theo!"

        m "Cảm ơn cậu!! Tôi chỉ sợ làm cậu buồn thôi. Tôi thật sự xin lỗi. 😭😭😭"

        "Nhưng thực tế, Aoi rất buồn vì tôi không thành thật với cô ấy."

        "Dù họ vẫn giữ liên lạc, sự gần gũi giữa họ không bao giờ phát triển hơn vì khoảng cách."

        "Cuối cùng, tôi đã có một người bạn Nhật. Nhưng cảm giác vẫn đắng ngắt vì tôi không thành thật."

        return


    label start_jp:

        scene cafe

        na_jp "あの女の子の姿は決して忘れられない。たぶん、彼女が僕の冷たい心を再び揺さぶったのだろう。"

        na_jp_sec "でも、僕が夢見た詩的なシーンは現実になることはなさそうだ。"

        na_jp_third "僕にできることは、遠くから見つめることだけで、何もできない。"

        na_jp "「無理だ」「お互い知らないのに、どうやって話せる？」"

        na_jp_sec "その声が頭の中で響き続け、僕はもうどうしたらいいのか分からなかった。"

        na_jp_third "今日もいつもと同じ日。馴染みのカフェテリア、馴染みの席。彼女はまたそこに座っている。そして僕は、いつものように遠くから見ているだけ。"

        na_jp "転校する前の最後の一年だ。"

        na_jp_sec "あああ！これが「瞬間」かもしれない——少年と少女が偶然出会う瞬間。でも僕はただの脇役。"

        na_jp_third "くそ。声をかけるべきか？"
        $ preferences.text_cps = 0
        menu:
            "くそ。声をかけるべきか？" 

            "もちろん、バカ！":
                menu:
                    "本気か？今まで女の子に話しかけたことないだろう。"
                    
                    "うん！本気だ！":
                        jump good_end_jp

                    "マジか、じゃあ家に帰ってリーグやろう（俺ブロンズ）。":
                        jump league_end_jp

            "無理、俺見て！ハゲで臭い :/":
                jump bad_end_jp

    label league_end_jp:
        $ preferences.text_cps = 30

        m_jp "レーン押せ、EZREAL !"

        na_jp "30分後…"

        m_jp "バロン行け！！スマイトスマイト！"

        na_jp_sec "5試合後…"

        m_jp "くそ…俺、アイアンになった…"

        m_jp "…"

        m_jp "何が起きた？"

        m_jp "…"

        m_jp "女の子と話すよりずっと良かった 🔥🔥🔥"

        return
    
    label good_end_jp:
        $ preferences.text_cps = 30
        na_jp_third "勇気を振り絞って立ち上がり、彼女の方へ歩いた。"

        na_jp "何もせず見ているだけの時間が長すぎた。今こそ恥ずかしさを振り払う時だ。"

        na_jp_sec "近づくにつれ、心拍数は三倍になった。緊張と、過去の女の子との会話のあまり良くない記憶が津波のように押し寄せてきた。"

        na_jp_third "まあとにかく、全部かけるしかない、と自分に言い聞かせた。"

        m_jp "えっと…すみません。"

        na_jp "言葉を無理やり絞り出した。"

        na_jp_sec "彼女は顔を上げた。ああ！その場で死んで天に昇れる気分だった。"

        na_jp_third "少なくともそう思った。食事中に声をかけるのは少し変かも？"

        na_jp "彼女はとても優しく、少し困った様子で答えた："

        g_jp "あなたは誰ですか？私たちは知らないと思うけど？"

        na_jp_sec"くそ..."
        na_jp_third "もう少し踏み込もう。"

        m_jp "えっと、何回か見かけたことがあります。可愛いと思いました！だから…"

        na_jp "くそ…" 
        na_jp_sec "何を聞こう？会話を続けなきゃ…"

        m_jp "アメリカ人ですか？"

        g_jp "いいえ、実は私は留学生です。"

        m_jp "ああ！"

        m_jp "僕も！アジア人です。あなたは？"

        g_jp "本当？？私もアジア人！"

        m_jp "こんにちは、fine shyt"

        g_jp "…"

        m_jp "はは…"

        m_jp "ごめん、くだらない冗談…"

        m_jp "ちなみに僕はベトナム出身です。"

        g_jp "私は日本人です。"

        m_jp "ええ！？信じられない！実は日本語を勉強しているんです。"

        g_jp "素敵！進み具合はどうですか？"

        m_jp "正直まあまあだけど、練習する相手がいなくて。"

        m_jp "ねえ！手伝ってくれませんか？日本語の練習。"

        g_jp "うーん…今食事中だから…いいタイミングじゃないかも。"

        m_jp "あ…邪魔したくない…ごめん。"

        m_jp "では…よろしくお願いします。"

        na_jp_third "席に戻ろうとしたが、彼女は言った："

        g_jp "待って ! ! 外国人が私の言語に興味を持つのは別に変じゃないよ。手伝うね。SNS使う?IG?Line?"

        m_jp "ああ、Lineはあるけどほとんど使ってない。アメリカでは誰もLine使わないし。IGもあるから、IGで。"

        g_jp "オッケーオッケー。"

        m_jp "ああ…しまった…"

        g_jp "どうしたの？"

        m_jp "スマホが切れた…"

        g_jp "はは、大丈夫！"

        g_jp "ユーザー名教えて、フォローするね。"

        na_jp "彼女はiPhoneを渡して、私のIGをすぐに入力した。"

        m_jp "よし、これが僕のIG。"

        g_jp "オッケー。フォローリクエスト送った？"

        m_jp "送った！ありがとう。すぐに充電するよ。"

        g_jp "はは、大丈夫。"

        m_jp "じゃあ先にランチを楽しんでね。授業に行くから。またね。"

        g_jp "うん！またね！"

        m_jp "あ、自己紹介忘れたけど、僕はブランドン！"

        g_jp "はは、私は葵！"

        m_jp "よろしく、葵！"

        a_jp "こちらこそ！"

        na_jp_sec "その午後、頭が爆発しそうだった。やった。すごい。"
        na_jp_third "足が震えてる。"

        jump after_cof_jp

    label bad_end_jp:
        $ preferences.text_cps = 30
        
        m_jp "そうだ、僕は何を考えているんだ？"
        m_jp "以前も声をかけなかったし、今日も同じだ…"

        na_jp "そして、ただ遠くから見つめ続けた。3月、4月、そして5月が過ぎた。"

        na_jp_sec "二年目の終わりが近づいた。"

        na_jp_third "新しい大学に転校し、言葉にできない悲しみを抱えた。"

        na_jp "多分、僕は臆病すぎた。自分を責め続けた。"

        na_jp_sec "後悔だ。"

        return

    label after_cof_jp:

        scene campus
        na_jp "あの会話以来、日々はより楽しく、生き生きとしたものになった。"

        na_jp_sec "同時に、以前のように気持ち悪いと思われるのを恐れず、彼女と気楽に会話できるようになった。"

        na_jp_third "カフェテリアに歩くたびに、いつも彼女がいつもの窓際に座っていることを願った。"

        na_jp "そして、その日の出来事について話した。"

        na_jp_sec "最初は話題が少し退屈だった。しかし徐々に、より面白い話題が出てきた。"

        na_jp_third "考えてみると…"

        na_jp "日本人の友達ができるなんて、なかなか面白い。"

        na_jp_sec "僕のようなベトナム人が日本人、特に女の子と仲良くなるのは難しいと思っていた。"

        na_jp_third "多分、考えすぎなんだろう。"

        na_jp "そして、4月中旬のある日——"

        na_jp_sec "葵が突然聞いてきた："

        a_jp "ブランドン、来年は何をするつもり？"

        na_jp_third "その質問に驚いた。来年、転校するかもしれなかったから。"

        na_jp "雰囲気が少し気まずくなった。"

        na_jp_sec "言うべきか？"

        $ preferences.text_cps = 0

        menu:
            "言うべきか？"

            "正直に話すべき。":
                jump saying_jp

            "気持ちを傷つけたくない…":
                jump not_saying_jp

    label saying_jp:

        $ preferences.text_cps = 30
        m_jp "葵、伝えたいことがある。悲しませるかもしれないけど…"

        a_jp "ん？話して。大丈夫だと思う。"

        na_jp_third "緊張したが、続けた。正直に話す方がいいと思った。"

        m_jp "残念だけど、来年ここにはいない。別の州の大学に転校する。"

        a_jp "えっ、なんで転校？この学校悪くないと思うけど。"

        na_jp "葵は少し悲しそうだった。"

        m_jp "もちろん悪くない！でも…もっと良い奨学金をもらったから断れなかったんだ…"

        a_jp "残念…もし残っていたら、こうして会い続けられたのに…"

        a_jp "でもヘイ！！！おめでとう！！！すごい！！！"

        m_jp "ありがとう！！"

        a_jp "…"

        m_jp "…"

        a_jp "残りの時間を楽しもう、いい？"

        m_jp "もちろん！まだたくさん時間がある！"

        na_jp_sec "その会話の後、葵は少し悲しんだ時もあったが、二人は確実に親しくなった。"

        na_jp_third "そして避けられない出来事が起きた。期末試験が終わり、二年目が終わり、僕は去らなければならなかった。"

        scene airport

        na_jp "出発の日、彼女がメッセージを送ってきた："

        a_jp "今日が出発の日だよね？"

        m_jp "うん…"

        a_jp "直接お別れできなくて残念。今日本にいる 😭😭"

        m_jp "はは、大丈夫。でも寂しくなるよ。着いたら新しい学校のこと教える！"

        a_jp "うん！忘れずにメッセージしてね。忘れたら殺すよ！"

        m_jp "絶対忘れないよ、バカ！"

        a_jp "忘れちゃダメだよ！ふん 😤"

        m_jp "はは、じゃあまたね、葵！"

        a_jp "またね！バイバイ"

        na_jp_sec "主人公は新しい大学に移った。距離が離れても連絡は続いた。"

        na_jp_third "時間が経つにつれ、葵と主人公はより親しくなった。もしかすると、明るい未来が待っているかもしれない。"

        return

    label not_saying_jp:

        $ preferences.text_cps = 30
        m_jp "僕はインターンシップを探すつもり。三年生は早く始めるべきだから。"

        a_jp "ああ、なるほど。"

        m_jp "君は？"

        a_jp "まだ分からない。来年は二年生だから、多分今年と同じかな。"

        m_jp "卒業後は日本に戻る予定？"

        a_jp "戻るか、ここに残るかまだ決めてない…"

        m_jp "うん…選ぶのは難しいね。"

        na_jp "期末試験が来て、僕は葵に知られることなく去った。"

        a_jp "どこ？全然会わなかった。新学期が始まる 😢😢😢"

        m_jp "葵…僕が言おうとしていることで怒らないよね？"

        a_jp "ん？話して。怒らない。"

        m_jp "実は…転校したんだ。言わなくてごめん。"

        m_jp "君を悲しませたくなかった。"

        na_jp_sec "葵は少し間を置いて答えた。"

        a_jp "あはは…大丈夫。連絡は続けられる。ただ、会えないけど…"

        m_jp "本当に悲しくないの？"

        a_jp "少しはあるけど…でも君の人生だから、君が幸せなら私も幸せ！"

        m_jp "ありがとう！！悲しませるかと思って心配だった。本当にごめん 😭😭😭"

        na_jp_third"でも実際、葵は彼が正直でなかったことにとても悲しんでいた。"

        na_jp "連絡は続いたが、距離のせいで親密さはこれ以上深まらなかった。"

        na_jp_sec "結局、日本人の友達はできた。でも正直でなかったため、甘く切ない感じだった。"
 
        $ gui.text_font = gui_text_font_backup
        return


        # This shows a character sprite. A placeholder is used, but you can
        # replace it by adding a file named "eileen happy.png" to the images
        # directory.


        # This ends the game.

    return
