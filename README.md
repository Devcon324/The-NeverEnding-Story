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
5. Cronjob the script to run 3x a day at 00:00, 08:00, and 16:00.

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

**Date Written:** 2024-10-13 13:28:39

The sun was setting over the rolling hills of Faerûn as a worn wagon rattled along the dusty road. Inside, a mix of tired peasants huddled together, their faces etched with the weariness of travel. Amidst them sat Dave, a young paladin with a sense of restlessness that seemed to grow by the day. Clad in simple, unadorned armor, his blond hair tied back in a ponytail, he gazed out at the horizon, his eyes fixed on the faint outline of the StarMountains in the distance. His fellow travelers, all folk who had never ventured far from their humble beginnings, watched him with curiosity and suspicion. This was, after all, a paladin leaving the safety of a monastery to traverse the unpredictable roads of Faerûn.

"Where are ye headed, lad?" asked a gruff old fellow to Dave's left. His name was Grimbold Ironfist, a sturdy blacksmith from a small village to the north. Grimbold had lost an arm in battle and sported a gleaming mechanical replacement that creaked as he shifted on the wooden bench.

"I'm headed to Bluestone," Dave replied, his voice firm but laced with a hint of trepidation. "I've heard the town is seeking brave adventurers to... aid in the protection of its citizens."

A hooded figure near the back of the wagon leaned forward, eyes glinting with curiosity. "Protection from what, exactly?" she asked, her voice husky and mysterious.

Dave's hand instinctively went to the hilt of his sword, an unadorned steel blade he had been given by the monks at the monastery. "I've heard rumors of strange happenings in the nearby forests – whispers of goblins and wild beasts. Bluestone needs someone to investigate."

The peasants exchanged uneasy glances, no doubt thinking about the perils that lay ahead. As for Dave, he felt a thrill of excitement course through his veins, the prospect of adventure igniting a fire within him.

"You're either brave or crazy," Grimbold chuckled, eyeing Dave's unwavering determination. "I reckon it's a bit of both."

The wagon rumbled onward, the travelers subsiding into silence as night began to fall. The stars twinkled above, casting a magical glow over the landscape, as the passengers drifted off to sleep, their dreams filled with the promise of the unknown adventures that lay ahead.

---

**Date Written:** 2024-10-13 13:29:15

As the night deepened, the air grew cooler, filled with the scent of damp earth and the distant calls of nocturnal creatures. The wagon continued to rattle along the road, the rhythmic thud of its wooden wheels on the dusty terrain lulling the travelers into fitful slumber. Dave, however, remained wide awake, his eyes fixed on the starry expanse above, the beam of a pale moonlight casting an ethereal glow across the rolling hills.

As the hours crept by, a silence fell over the wagon, broken only by the occasional snore or creak of the wheels. The hooded figure near the back of the wagon, her face hidden behind a veil of shadows, seemed to be watching Dave with an intensity that made the hairs on the back of his neck stand on end. Her eyes gleamed like two sapphires in the moonlight, an air of mystery surrounding her that was both captivating and unnerving.

Just as the night seemed to be at its darkest, the wagon listed to one side, its wheels grating on a patch of rough terrain. The peasants stirred, their sleep-addled eyes blinking in confusion as the wagon creaked and groaned, threatening to topple over. Grimbold Ironfist coughed loudly, his mechanical arm creaking in protest as he jerked upright.

"What in the seven heavens?" he exclaimed, rubbing his bleary eyes.

Dave leapt to his feet, his hand instinctively going to the hilt of his sword. "We seem to have encountered a spot of rough ground," he said, peering out into the darkness.

As the wagon corrected its balance and continued to rumble forward, the driver – a stubby-nosed man named Jepson – grunted a hasty apology over his shoulder. "Sorry about the jolt, friends," he said, his breath misting in the cool air. "Just a bit of rough road ahead."

As the wagon trundled on, its passengers slowly settled back into their slumber. The hooded figure remained awake, her eyes fixed intently on Dave as the wagon rattled into the darkness. Her features seemed to shift in the flickering moonlight, taking on a subtle yet unsettling aspect that made Dave feel like a mouse beneath the gaze of a hawk.

As the first light of dawn crept over the horizon, the wagon rounded a bend in the road, revealing a silhouette etched against the rising sun: the sleepy village of Ashfall, its wooden rooftops and thatched haystacks stark against the growing light. The air was heavy with the smell of woodsmoke and damp earth, a hearty scent that stirred the travelers from their slumber.

"Well, we're making good time," Grimbold said with a grin, rubbing his one arm over his chest. "Bluestone won't be far now."

As the villagers began to stir, the wagon drew closer to the heart of Ashfall. Dave spotted figures gathered near the village gate, their eyes watching the wagon's approach. Something in their demeanor seemed wary, even hostile, an air of unease that clung to the village like a shroud.

"Welcome to Ashfall, traveler," one of them growled, stepping forward with a mixture of curiosity and suspicion. "But don't be thinkin' of stayin' too long. We've got trouble brewin' in these parts."

---

**Date Written:** 2024-10-13 13:29:31

The villager's words hung in the air, casting a somber mood over the group as they disembarked from the wagon. The sun continued to rise, casting a warm glow over the village, but the atmosphere remained chilly. The peasants on the wagon eyed the villager warily, exchanging nervous glances as they gathered their belongings. Jepson, the wagon driver, merely shrugged and hopped off the wagon, stretching his short legs as he surveyed the village.

Dave's gaze lingered on the villager, a man with a weathered face and a thick beard that seemed to hold a lifetime of secrets. The villager's eyes darted towards the hooded figure, who had stepped off the wagon with an air of quiet confidence. For a moment, the two locked gazes, their faces expressionless. Dave sensed a spark of tension between them, an unspoken connection that spoke of shared knowledge and hidden meanings.

The villager turned back to the wagon driver, his voice brusque. "You're the supply wagon from Harvesthale, ain't ya?" He nodded at the stack of goods lashed to the wagon's bed.

Jepson nodded in affirmation. "Aye, that's right. Bringing in goods for the villagers here."

The villager's expression grew more serious, his brow furrowing in concern. "Well, we'll be glad of the supplies, but like I said, we've got... issues here. Bandits been raiding nearby farms, and our folk are spooked." He eyed the hooded figure warily, his voice dropping to a whisper. "And there's other rumors. Things that the wind carries, of troubles deeper than thieves and rascals."

Grimbold snorted, rubbing his mechanical arm over his chest. "Sounds like any village out in the Boar Downs, eh?" His chuckle was awkward, tinged with a touch of unease. The hooded figure merely listened, her eyes narrowing as she absorbed the villager's words.

A figure emerged from the heart of the village, her face marked by creases of worry and exhaustion. "Elleren," the villager called out to her, as she approached the wagon. She drew up beside the villager, eyeing the wagon and its occupants with a wary intensity.

"I'm Cador," the villager said, pointing to himself. "This is Elleren, the village elder. She's the one you'll want to talk to, if you're looking to do business or rest for a spell." He nodded towards the figure beside him, her silver hair twisted into neat braids that hung down her back like tangles of vines.

Elleren's gaze swept over the wagon's occupants, her eyes lingering on Dave with a concerned expression. She hesitated, then spoke in a voice marked by its deep conviction. "Ah, travelers. I see you've arrived in Ashfall. We've been expecting... well, perhaps not exactly you, but visitors." Her eyes seemed to hold secrets and curiosity in equal measure.

"We've got news of troubles brewing in the hills," Grimbold chimed in, recalling a mixture of excitement and trepidation in his voice. "Dark forces stirring in the lands to the north."

Elleren nodded solemnly, her eyes betraying the depth of the fear that hung in the air. "Yes. We've heard the stories too. These lands, here in Ashfall, know plenty about fear. We've felt the change in the air, long before it spread throughout the lands."

---

**Date Written:** 2024-10-13 16:00:04

As Elleren's words hung in the morning air, a light breeze rustled the leaves of the nearby trees, casting dappled shadows on the ground below. The village elder's eyes seemed to cloud over, as if memories were stirring, memories that she had long hoped to forget. Cador stood tall beside her, his face set in a determined expression, as if he would shield her from the trials that lay ahead.

Elleren turned her gaze back to the wagon's occupants, a sense of resignation etched on her face. "Come," she said finally, her voice a little stronger. "We'll talk in the village hall, away from prying ears and curious eyes. We've much to discuss, and time's not on our side."

As Elleren led the way through the village, the group passed by small cottages with smoke drifting lazily from their chimneys. The residents who caught sight of the group couldn't help but pause in their daily activities, their faces turned towards the visitors with a mixture of curiosity and suspicion.

The village hall itself stood in the heart of Ashfall, an ancient structure with wooden beams weathered to a silvery grey. Elleren pushed open the door, its wooden frame adorned with intricate carvings of various leaves and flowers that danced across its surface. The air inside was heavy with the scent of burning wood and a faint hint of herbs.

As the group settled into their seats around the large wooden table that occupied the center of the hall, a fire crackled to life in the hearth, casting flickering shadows on the walls. Cador took a seat at the far end of the table, his back straight as he listened intently to the conversation that was about to unfold.

Elleren began, her voice steady, as she recounted the troubles that had plagued the village. Dark creatures roamed the hills and forests surrounding Ashfall, creatures that seemed to have no eyes for the villagers' livestock but preyed on anything else that crossed their path. It was as if, she whispered, something had awakened a terror that the villagers had only heard about in fireside tales and distant legends.

Elleren leaned forward, her voice barely above a whisper. "We believe that something – and we don't know what – has risen deep in the forest. A terror that the old gods themselves couldn't have imagined. Our people are leaving their homes to find safety elsewhere. Ashfall's dwindling, dying... and there's no one left to tell us what's happening or how to stop it."

In the pause that followed, the group's collective gaze swung towards the hooded figure, who seemed to be watching the flames dance in the hearth with a mixture of quiet contemplation and hidden understanding.

---

**Date Written:** 2024-10-14 00:00:03

The hooded figure slowly rose from their seat, as if drawn by an unseen force, their movements fluid and calculated. The other occupants of the wagon cast them curious glances, sensing an air of mystery surrounding the enigmatic figure. As they approached the fire, the flickering flames danced with eerie intensity, casting shadows that seemed to stretch and writhe like living things.

Their hood turned towards Elleren, the shadows cast by the cowl deepening the lines of their face, rendering their features almost indistinguishable. The air seemed to vibrate with anticipation as the figure slowly raised its gaze to meet Elleren's. "Tell me," the hooded figure began, their voice low and husky, yet tinged with a quiet authority, "what signs have you seen that point to the nature of this terror? Are there markings, symbols, or tokens that might hint at its origins or essence?"

Elleren hesitated, as if choosing her words carefully. The elderly woman glanced at Cador, who gave her a reassuring nod, before turning back to the hooded figure. "There have been... gruesome finds," she whispered, her voice trembling slightly. "Skulls, some animal, others that I'd swear were human. Carved with strange runes and markings, unlike anything we've ever seen. We've had no seers or scholars among us for nigh on a decade, so we can't decipher their meaning."

The hooded figure leaned in closer, their face still obscured, yet their gaze piercing in its intensity. "I see," they murmured, their words barely audible over the crackling flames. "Perhaps, then, we should begin at the heart of the matter: the forest. It is there that we will discover the source of your troubles, and maybe, just maybe, find a way to dispel the darkness that has descended upon Ashfall."

As the hooded figure's words hung in the air, an expectant silence enveloped the gathering, the shadows on the walls seeming to deepen, as if darkness itself was waiting to see what the future held for the embattled village.

---

**Date Written:** 2024-10-14 08:00:05

The fire crackled in response, as if acknowledging the hooded figure's words, sending a sprig of sparks dancing up into the night air. Elleren's eyes, heavy with concern, darted to the figure's hood, her gaze probing for a glimpse of their face. But the shadows remained resolute, holding their secrets close. She shivered, a frisson of unease running down her spine, as the hooded figure's words seemed to conjure an image of the dark forest, its twisted boughs reaching out like skeletal fingers.

Beyond the fire, the encroaching darkness seemed to loom larger, as if the very trees themselves were listening in on the conversation. A hooting owl, its mournful cry carrying on the evening breeze, seemed to punctuate the hooded figure's declaration. In that moment, the assembled villagers felt the weight of their shared uncertainty settle around them once more. They knew they stood at the cusp of a perilous journey, one that might demand more courage and strength than they could muster.

As the weighty silence continued to hang heavy in the air, Cador leaned forward, his eyes squinting into the flickering flames. "The forest's boundaries have always been treacherous," he said, his deep voice resonating with experience. "But in recent times, the tales have grown too unsettling to ignore. If the origins of the darkness reside within, we'll require a stalwart companion to stand by our side." His words carried an air of expectation, as his gaze settled on the hooded figure.

The figure itself remained quiet, yet their shoulders slightly inclined, as if pondering Cador's offer. With deliberation, they raised a gloved hand, allowing the firelight to catch on the buckles and leather stitched into its length. As the hooded figure parted the darkness enveloping them, a glimpse of skin at the wrist was briefly visible – a smooth, pale epidermis, devoid of any prominent veins or markings. Such an odd sight only deepened the air of intrigue, leavingElleren to ponder what kind of enigmatic being might have emerged from the shadows to possibly alter their village's fate.

---

**Date Written:** 2024-10-14 16:00:02

All the assembled villagers awaited.
