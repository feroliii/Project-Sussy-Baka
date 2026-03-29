# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Aoi")
define m = Character("Me")
define g = Character("Girl")

define cafe = Image('cafe.png')
define airport = Image('airport.jpg')
define campus = Image('campus.png')

# The game starts here.

label start:

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
            jump start_ger

    label start_en:
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
                        jump bad_end

            "Nah bro, look at me! I'm bald and smelly asf :/":
                jump bad_end

    label good_end:
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

            "Better be transparent.":
                jump saying

            "I don't want to hurt her feelings...":
                jump not_saying

    label saying:

        $ preferences.text_cps = 30
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

        a "It's a shame I can't say goodbye in person. I'm in Japan right now. 😭😭"

        m "Haha, it's okay. But I'll miss you. I'll definitely tell you about my new school when I get there!"

        a "Yeah! Don't forget to message me. If you forget I gonna kill you!."

        m "I'd never forget you dummy!"
        
        a "You better not! hmph 😤"

        m "Ahaha see you later Aoi!"
        
        a "See you! Bye bye"

        "The main character moved to a new university. Even though the distance between them grew, they continued to stay in touch."

        "Aoi and the main character became closer over time. Who knows—maybe a bright future awaits them."
        
        return

    label not_saying:

        $ preferences.text_cps = 30
        m "Well, I'm planning to look for internship opportunities. Since third year is when you should start early."

        a "Oh, I see."

        m "What about you?"

        a "I'm not sure yet. Next year will be my second year, so probably the same as this year."

        m "Are you planning to return to Japan after graduation?"

        a "I'm not sure yet if I want to go back or stay here..."

        m "Yeah... It's hard to choose."

        "Final exams came, and I left without Aoi ever knowing."

        a "Where are you? I haven't seen you at all. The new school year is about to start. 😢😢😢"

        m "Aoi… you won't be mad at me for what I'm about to say, right?"

        a "Hmm? Go ahead, I won't be mad."

        m "Actually… I transferred schools. Sorry for not telling you."
        
        m "I didn't want to hurt your feelings."

        "Aoi paused a bit before replying."

        a "Ah haha… it's okay. We can still stay in touch. Just not in person…"

        m "You're really not sad?"

        a "Kinda, but you know... it's your life and if it makes you happy I'm happy too!"

        m "Ohh thank you!! I was just afraid of making you sad. I'm really sorry. 😭😭😭"

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
                        jump bad_end_pt

            "Nem ferrando, olha pra mim! Tô careca e fedido :/":
                jump bad_end_pt

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
                        jump bad_end_es

            "Nah hermano, ¡mírame! Estoy calvo y huelo horrible :/":
                jump bad_end_es

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
                        jump bad_end_ita

            "Nah fratello, guardami! Sono calvo e puzzo da morire :/":
                jump bad_end_ita

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
                        jump bad_end_fr

            "Non mec, regarde-moi ! Je suis chauve et je pue à mort :/":
                jump bad_end_fr

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
        # This shows a character sprite. A placeholder is used, but you can
        # replace it by adding a file named "eileen happy.png" to the images
        # directory.


        # This ends the game.

    return
