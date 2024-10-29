# The NeverEnding Story

## What is this?

We follow **Dave**, our Programmed Paladin on his adventure!

This is an **self-continuing** story that is **automatically updated 3x a day to this GitHub repository.**
**Enjoy you morning coffee and read where dave is at!** The story is updated at **12:00 AM, 8:00 AM, 4:00 PM Eastern Standard Time**

### [Click Here to Read Dave's Story Below](#the-story-of-dave-the-programmed-paladin)

Built with **Generative Artificial Intelligence** using **Meta's llama3.1 70b Large Language Model**. This project accomplishes these steps:

1. Start a story with an initial story chunk (some paragraphs).
2. Continue writing the next story chunk using the previous story chunk as context.
3. Write the stories to this README.md file with dated entries.
4. Automate the git commands to commit and push to this repository.
5. Cronjob the script to run 24x a day

### Features I found cool when building

#### Groq API

**Using [Groq](https://groq.com/) for LLM's is intuitive and easy.** the syntax and responses received from the model are easily understood and can allow for great debugging. Groq was also chosen over [OpenAI's GPT models](https://openai.com/api/) because Groq is **free** and has **fast-inference's** meaning the story generation is extremely fast.

The fact this model is free (hopefully for a long time) allows for the great learning and exploration of using LLM's to make projects like this that **experiment with how models behave when in a continuous conversation and creating content akin to a writing style and theme.**

As Groq introduces newer models, perhaps the story may become more fluid over time.

#### Algorithms

I had to really design and think about how the story generation will be organized so that the LLM can parse the recent stories. I knew i needed to separate eah story so i separated them by the markdown line `---\n`

In my learning i optimized retrieving the latest story. This was done by sending a pointer to the end of file and use a reading window (buffer) that will expand its memory only when the story separator is not within the window. Once found, the most recent story chunk is retrieved and cleaned to hold the story text to give the LLM context for the next story.

#### Python Packaging

I learned how to properly use `__init__.py` and create sub-packages within the project such as `utils`, `tools`, and `update`

#### Automated git commits and push to GitHub

One very interesting feature i learned is that i can use system calls to send git commands such as `git add`, `git commit`, and `git push origin master`. This proved useful to keep updating the repository as the script runs without human input (apart form setting up SSH keys for secure connections)

The other feature is that cronjobs on Linux are very useful to run the script as a background process, simply requiring a workstation to be online. This can be done by editing the cronjob file with the following command:

```bash
crontab -e
```

**Note:** the cronjobs need to be in the following format (with script running every day at time 16:00)

```bash
00 16 * * * cd /path/to/repository ; source path/to/venv/bin/activate ; path/to/venv/bin/python3 /path/to/repository/main.py
```

This cronjob essentially runs the command to cd to the repository, spin up the python virtual environment, then use that virtual environments python version to execute the main script.

## Now enough of the technical stuff... Lets see how Dave is doing

## The Story of Dave the Programmed Paladin

---

**Date Written:** 2024-10-29 18:37:32

As the sun rose over the rolling hills of the Dragon Coast, a worn leather wagon rattled and creaked its way along the dusty road to Bluestone. Among its passengers was Dave the Paladin, a young and ambitious warrior-monk clad in the simple, yet practical, attire of his order. With his gleaming steel-plated armor, longsword, and the symbol of his faith – a silver holy symbol of Selûne, the Moonmaiden – emblazoned on his chest, Dave cut an imposing figure amidst the peasant travelers. Yet, despite his martial bearing, a palpable sense of restlessness hung about him, like a traveler eager to shake off the tedium of months spent within the cloistered walls of his monastery.

Dave's thoughts were consumed by the whispered tales of adventure and bravery that had long circulated among the brothers of his order. Tales of valiant heroes, of treacherous quests, and of the world beyond the monastery's walls had stirred something deep within him. It was this insatiable hunger for excitement and purpose that had driven him to bid farewell to the familiar, if unfulfilling, routines of his monastic life and set out into the wider world. Bluestone, a humble but bustling town on the northwestern coast of Faerûn, was to be his starting point – a stepping stone into the great unknown.

As the wagon creaked and groaned over a particularly rutted stretch of road, a lanky, freckled youth with a handful of straw-stuffed luggage and a stringy-looking packmule caught Dave's eye. "Hey there! Mind if I slide on in? The missus has a heap of baskets on this side," the youth called out, motioning toward a corner of the wagon, where a stocky countrywoman guarded a veritable forest of woven reed containers. "They're for the market – finest freshwater clams this side of the Coast Way," she explained in a gruff, no-nonsense voice.

Dave motioned graciously for the youth to join him, and they introduced themselves as Eli and his mother, Elara – a long-time seller of fresh seafood in Bluestone. "We've made the trip from Greenhaven these six years now," Elara explained, "though the tales of orcs and bandits along the roads don't make me sleep easy of late." As they spoke, the wagon inched closer to its destination – and the promise of adventure hovered tantalizingly within reach, like the first wisps of morning fog lifting to reveal the unsuspected wonders of the day to come.

---

**Date Written:** 2024-10-29 18:38:25

The air was alive with the sweet scent of wildflowers and the earthy aroma of damp soil as the wagon rounded a bend, affording a breathtaking view of Bluestone in the distance. Nestled between the windswept dunes and the sun-kissed waters of the Dragon's Teeth bay, the town seemed to shimmer and dance in the morning light, its weather-beaten buildings and sail-crowded harbor blending into a tapestry of color and life. A sturdy stone lighthouse stood sentinel over the town's seaside promenade, its watchfires still smoldering from the previous night's vigil.

As the wagon drew closer, the faint sounds of market-day commerce – hawkers calling their wares, haggling merchants, and the constant clucking of poultry – mingled with the creaking of the wagon's wooden frame, drawing Dave's senses into a world of cacophonous delight. He felt his excitement building, like a drumbeat quickening its tempo, and his thoughts began to turn to the many possibilities this bustling town might offer – adventure, danger, or fortune. He knew, deep within, that this place was but the starting point on a grand journey that would see him facing his share of trials and tribulations, all in the name of service to his faith and his unyielding pursuit of justice.

As the wagon approached the town gate, its attendant watchmen cast a practiced eye over the passenger manifest, scrutinizing the new faces in their midst. A dour-faced veteran of the town watch, a portly sergeant named Marcellus with a gruff tone to match, approached the wagon, scanning each passenger with a practiced gaze. His eyes narrowed in inspection as they landed upon the armor-clad paladin, and a half-step closer, he inquired gruffly, "Mind showin' yer credentials, friend? Can't be too careful with all these... incidents 'round the Coast of late." The other riders, Elara in particular, cast inquisitive glances at Dave, sizing up his potential to attract unwanted attention.

The conversation hung, like the uncertain pause between musical phrases, as Dave sought to demonstrate his peaceful intentions while convincingly establishing his, and thus his fellow passengers', legitimacy in the face of curious scrutiny. What manner of resolve would he muster in this time-honored ritual of convincing the vigilant gate sergeant of his integrity, faith unshakeable, and pure heart burning with purpose, only time could tell.

---

**Date Written:** 2024-10-29 18:38:30

As Dave's hand instinctively rose to the engraved silver medallion hanging around his neck, a symbol of his unwavering allegiance to the Order of the Radiant Dawn, a gentle influx of sunlight highlighted the fine lines and delicate filigree that adorned the pendant. His eyes locked onto Sergeant Marcellus's, conveying a sense of sincerity and diligence honed from years of devotion to his faith. In a clear, measured tone, Dave declared, "Greetings, Sergeant. I am Dave, a paladin of the Order of the Radiant Dawn. I come to Bluestone on a mission of peace, with the intention of providing aid to those in need and dispelling the shadows that seek to encroach upon this fair town."

He retrieved a fold of parchment, sealed with the Order's emblem in crimson wax, from a hidden compartment within his armor. The document, penned by the Order's Chancellor herself, attested to Dave's status and mission, carried all the weight of his organization's authority, further underscoring the legitimacy of his claim. Elara's curious gaze also encompassed the parchment as Dave unfolded it, her angular features tilting with interest. The air appeared to thicken momentarily as the watchman scrutinized the seal, weighing the weight of the endorsement and his own seasoned judgment against the perceived risks presented by a battle-hardened paladin.

Sergeant Marcellus deliberated in a state of quiet contemplation, a flicker of intense scrutiny dancing within the depths of his otherwise stony visage, before finally breaking the silence with an economical nod. "Welcome, Paladin Dave. You and your companions may pass. Mind you keep a weather eye on the goings-on around town. Rumors've been circulating... certain unwholesome occurrences disturbing the peace. If you should happen to run into trouble, don't hesitate to reach out to the watch. We'll be keeping an eye out for you." A quiet sigh accompanied the passing of his gaze over the wagon's occupants once more, leaving them to continue onward into the vibrant melee that awaited in Bluestone.

Once the wagon had passed beneath the raised portcullis, the sounds of market-day commerce swelled around them in a joyous surge. The sweet fragrance of exotic spices and freshly baked bread, mingling with the sounds of hammering on metal and clashing steel from the local smithies and armorers, surrounded the wagon as they threaded their way deeper into Bluestone. Vendors selling an assortment of treasures, trinkets, and seemingly vital necessities of oceanic provenance flanked their progress, competing for the attention of passersby and out-of-town merchant travelers in an incessant flurry of motion, eye-catching spectacles, and melodic cajoling.

---

**Date Written:** 2024-10-29 18:38:35

As the wagon navigated through the bustling streets, the cacophony of sounds and vibrant colors enveloped Dave and his companions, creating a sensory overload that was both exhilarating and overwhelming. The warm sunlight danced across the town, casting long shadows behind the colorful stalls and illuminating the dusty cobblestones. Elara's gaze darted from one vendor to the next, her eyes sparkling with curiosity as she took in the kaleidoscope of sights and sounds. She fingered the hilt of her sword, a habitual gesture that betrayed a lingering unease, even as a hint of excitement played on her lips.

To their left, a harried-looking vendor touted his wares, a rainbow of seashells arranged artfully on a velvet-draped board. The vendor's cries of "Crabs, shells, and curios from the farthest reaches!" mingled with the chatter of a nearby performer, a juggler whose whirling clubs created a blur of motion as he effortlessly kept a half-dozen different objects aloft. Further on, the pungent aroma of fresh fish wafted from a food stall, entwining itself with the sweet scent of sugar and spices from a nearby bakery. A cluster of passersby gathered around the baker's stall, sampling her wares and laughing as she traded banter with the juggler.

Dave guided the wagon with a gentle touch, navigating the crowded streets with a practiced ease. His eyes never strayed far from the bustling throng, his paladin's instincts honed to detect even the slightest whisper of unrest or deceit. As they made their way deeper into the heart of Bluestone, the architecture shifted from rough-hewn commercial structures to more refined, ornate dwellings, replete with intricate carvings and coats of arms that told the story of a rich and storied history. The air was alive with the pulse of the town, a fascinating tapestry of sound, color, and scent that seemed to grow more complex, and alluring, with every passing moment.

Ahead, the rooftop of a stately structure dominated the skyline, gleaming a weathered gold in the sunlight. The Bluestone Manor, seat of the town's wealthy patron family, loomed over the surrounding landscape like a gently weathered behemoth. Rumors had circulated among the townspeople about the strange occurrences and mysterious phenomena reported within the manor's hallowed halls, the strange disappearances and inexplicable occurrences said to plague the halls that seemed to defy the understanding of even the wisest scholars. The tales hung in the air like the persistent scent of salt and seaweed, piquing the interest of both the townsfolk and the visitors, as the mysterious allures of the ancient structure seemingly called out like a siren's song, drawing in all who would pause to listen.
