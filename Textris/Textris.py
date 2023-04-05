import pygame
import random
import math
import time
import sys
import os

def resource_path(relative_path):
    try:
    # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


pygame.init()

score = 0
points = 0
pad = 0
storedLetter = ""
lastWord = ""
swapped = 0

pygame.display.set_caption('Textris')

# an array with letters distributed in such a way that the more common ones show up more often, that way you won't get 14 Qs in a row.
alpha = ["E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","E","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","L","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","T","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","I","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","D","U","U","U","U","U","U","U","U","U","U","U","U","U","U","U","U","U","U","U","U","U","U","U","U","U","U","U","U","U","U","U","U","U","U","U","U","U","U","U","U","U","U","U","U","U","U","U","U","U","U","U","U","U","U","U","U","U","U","U","U","P","P","P","P","P","P","P","P","P","P","P","P","P","P","P","P","P","P","P","P","P","P","P","P","P","P","P","P","P","P","P","P","P","P","P","P","P","P","P","P","P","P","P","P","P","P","P","P","P","P","P","P","P","P","P","P","P","M","M","M","M","M","M","M","M","M","M","M","M","M","M","M","M","M","M","M","M","M","M","M","M","M","M","M","M","M","M","M","M","M","M","M","M","M","M","M","M","M","M","M","M","M","M","M","M","M","M","M","M","M","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","C","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","H","B","B","B","B","B","B","B","B","B","B","B","B","B","B","B","B","B","B","B","B","B","B","B","B","B","B","B","B","B","B","B","B","B","B","B","B","B","B","B","B","B","B","B","B","B","K","K","K","K","K","K","K","K","K","K","K","K","K","K","K","K","K","K","K","K","K","K","K","K","K","K","K","K","K","K","K","K","K","K","K","K","K","K","K","K","K","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","G","W","W","W","W","W","W","W","W","W","W","W","W","W","W","W","W","W","W","W","W","W","W","W","W","W","W","W","W","W","W","W","W","W","W","W","W","W","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","F","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","V","V","V","V","V","V","V","V","V","V","V","V","V","V","J","J","J","J","J","J","J","J","J","Z","Z","Z","Z","Z","Z","Z","Z","X","X","X","X","X","Q"]
queue = []
# a dictonary of only 4 letter words to fit with the tetra theme of tetris still. 
words = ["abba", "able", "abut", "aced", "aces", "ache", "acid", "acme", "acne", "acre", "acts", "adds", "afar", "aged", "ages", "agin", "ahem", "ahoy", "aide", "aids", "ails", "aims", "airs", "ajar", "alan", "alas", "alec", "ales", "ally", "alma", "aloe", "also", "alto", "amah", "amen", "amin", "ammo", "anal", "anew", "anna", "anon", "ante", "anti", "ants", "apes", "apex", "aqua", "arch", "area", "aria", "arid", "arms", "army", "arse", "arts", "arty", "asks", "atom", "atop", "auld", "aunt", "aura", "auto", "avid", "away", "awed", "awol", "awry", "axel", "axis", "axle", "baba", "babe", "babu", "baby", "bach", "back", "bags", "bail", "bait", "bake", "bald", "bale", "balk", "ball", "balm", "band", "bane", "bang", "bank", "barb", "bard", "bare", "barf", "bark", "barn", "bars", "base", "bash", 
"bask", "bass", "bath", "bats", "bawl", "bays", "beak", "beam", "bean", "bear", "beat", "beau", "beck", "beds", "beef", "been", "beep", "beer", "bees", "begs", "bell", "belt", "bend", "bene", "bent", "berg", "best", "beta", "beth", "bets", "bias", "bide", "bids", "biff", "bike", "bill", "bind", "bins", "bios", "bird", "bite", "bits", "blab", "blah", "blam", "bled", "blew", "blip", "blob", "bloc", "blot", "blow", "blue", "blur", "boar", "boat", "body", "bogs", "boil", "bold", "bolt", "bomb", "bond", "bone", "bong", "bony", "boob", "book", "boom", "boon", "boot", "bora", "bore", "born", "boss", "both", "bout", "bowl", "bows", "boys", "bozo", "brad", "brag", "bran", "bras", "brat", "bred", "bree", "bren", "brew", "brie", "brig", "brim", "brin", "bris", "brit", "bros", "brow", "buck", "buds", "buff", "bugs", "bulb", "bulk", "bull", "bump", "bums", "bunk", "buns", "bunt", "bura", "burn", "burp", "bury", "bush", "bust", "busy", "buts", "butt", "buys", "buzz", "byes", "cabs", "cafe", "caff", "cage", "cain", "cake", "calf", "call", "calm", "came", "camp", "cams", "cane", "cans", "cant", "cape", "capo", "caps", "carb", "card", "care", "carl", "carp", "carr", "cars", "cart", "casa", "case", "cash", "cast", "cats", "cave", "cell", "cent", "chad", "chap", "chat", "chef", "chew", "chez", "chic", "chin", "chip", "chit", "chop", "chow", "chug", "chum", "ciao", "cite", "city", "clad", "clam", "clan", "clap", "claw", "clay", "clef", "clip", "clod", "clop", "clot", "club", "clue", "coal", "coat", "coax", "cobb", "coca", "cock", "coco", "code", "coed", "coil", "coin", "coke", "cola", 
"cold", "cole", "coma", "comb", "come", "comp", "cone", "conk", "conn", "cons", "cook", "cool", "coon", "coop", "coot", "cope", "cops", "copy", "cord", "core", "cork", "corn", "cory", "cost", "cosy", "cots", "coup", "cove", "cows", "cozy", "crab", "cram", "crap", "crew", "crib", "cris", "croc", "crop", "crow", "crud", "crux", "cube", "cubs", "cued", "cuff", "cult", "aron", "cups", "curb", "curd", "cure", "curl", "curt", "cusp", "cuss", "cute", "cuts", "cyst", "dads", "daft", "dago", "dahl", "dais", "dale", "dame", "damn", "damp", "dang", "dare", "dark", "darn", "dart", "dash", "data", "date", "dato", "davy", "dawn", "days", "daze", "dead", "deaf", "deal", "dean", "dear", "debt", "deck", "deco", "deed", "deem", "deep", "deer", "deft", "defy", "deke", "deli", "dell", "demo", "dent", "deny", "desk", "dewy", "dial", "dibs", "dice", "dick", "died", "dies", "diet", "digs", "dike", "dill", "dime", "dine", "ding", "dink", "dips", "dire", "dirk", "dirt", "disc", "dish", "disk", "ditz", "diva", "dive", "dock", "docs", "doer", "does", "dogs", "dojo", "dole", "doll", "dolt", "dome", "done", "dong", "doom", "door", "dope", "dork", "dorm", "dory", "dose", "dost", "dote", "doth", "dots", "dour", "dove", "down", "doze", "drab", "drag", "draw", "drew", "drip", "drop", "drug", "drum", "dual", "duce", "duck", "duct", "dude", "duds", "duel", "dues", "duet", "duff", "duke", "dull", "duly", "dumb", "dump", "dung", "dunk", "dusk", "dust", "duty", "dyed", "dyer", "dyke", "each", "earl", "earn", "ears", "ease", "east", "easy", "eats", "echo", "eddy", "edge", "edgy", "edit", "eels", "eggs", 
"egos", "elks", "elms", "else", "emit", "ends", "envy", "epic", "ergo", "eros", "euro", "even", "ever", "eves", "evil", "exam", "exes", "exit", "eyed", "eyes", "eyre", "face", "fact", "fade", "fads", "tint", "fail", "fair", "fake", "fall", "fame", "fang", "fans", "fare", "farm", "fart", "fast", "fate", "faun", "faux", "fave", "fear", "feat", "feds", "feed", "feel", "fees", "feet", "fell", "felt", "fend", "fern", "fess", "feta", "feud", "fido", "fife", "file", "fill", "film", "find", "fine", "fink", "fins", "fire", "firm", "firs", "fish", "fist", "fits", "five", "fizz", "flag", "flak", "flan", "flap", "flat", "flaw", "flay", "flea", "fled", "flee", "flew", "flex", "flip", "floe", "flog", "flop", "flow", "flue", "flux", "foal", "foam", "foil", "fold", "folk", "fond", "font", "food", "fool", "foot", "ford", "fore", "fork", "form", "fort", "foul", "four", "fowl", "foxy", "frat", "fray", "free", "fret", "frog", "from", "yeet", "fuel", "fugu", "full", "fund", "funk", "furs", "fury", "fuse", "fuss", "fuzz", "gaby", "gaff", "gaga", "gage", "gags", "gain", "gala", "gale", "gall", "gals", "game", "gams", "gang", "gaps", "garb", "gasp", "gate", "gave", "gawk", "gays", "gaze", "gear", "geek", "gees", "geez", "gels", "gems", "gene", "germ", "gets", "gift", "gigs", "gill", "gimp", "girl", "gist", "give", "glad", "glee", "glen", "glib", "glop", "glow", "glue", "glum", "gnat", "gnaw", "goad", "goal", "goat", "gobs", "gods", "goes", "gold", "golf", "gone", "gong", "good", "goof", "goon", "gore", "gory", "gosh", "gout", "gown", "grab", "grad", "gram", "gran", "gray", "grew", "grey", 
"grid", "grim", "grin", "grip", "grog", "grow", "grub", "guff", "gulf", "gull", "gums", "gunk", "guns", "guru", "gush", "guts", "guys", "gyms", "hack", "hadj", "hags", "haha", "hail", "hair", "hale", "half", "hall", "halo", "halt", "hams", "hand", "hang", "hank", "haps", "hard", "hare", "harm", "harp", "hart", "hash", "hast", "hate", "hath", "hats", "haul", "have", "hawk", "haze", "hazy", "head", "heal", "heap", "hear", "heat", "heck", "heed", "heel", "heft", "heil", "heir", "held", "hell", "helm", "helo", "help", "hemp", "hens", "herb", "herd", "here", "hero", "hers", "hick", "hide", "high", "hike", "hill", "hilt", "hind", "hint", "hips", "hire", "hiss", "hits", "hive", "hoax", "hobo", "hock", "hoes", "hogs", "hold", "hole", "holt", "holy", "home", "homo", "hong", "honk", "hood", "hoof", "hook", "hoop", "hoot", "hope", "hops", "hora", "horn", "hose", "host", "hots", "hour", "howe", "howl", "hows", "huck", "huge", "hugs", "hula", "hulk", "hull", "hump", "hums", "hung", "hunh", "hunk", "huns", "hunt", "hurl", "hurt", "hush", "husk", "huts", "hymn", "hype", "hypo", "iced", "icky", "icon", "idea", "idle", "idly", "idol", "iffy", "ills", "imam", "inch", "info", "into", "ions", "iris", "iron", "itch", "item", "jabs", "jack", "jade", "jags", "jail", "jake", "jams", "jane", "jars", "java", "jaws", "jazz", "jean", "jeep", "jeez", "jefe", "jell", "jerk", "jess", "jest", "jets", "jews", "jiff", "jill", "jinx", "jobs", "jock", "joes", "joey", "john", "join", "joke", "jolt", "josh", "joys", "judo", "jugs", "juke", "jump", "junk", "jury", "just", "kale", "kane", "kaon", "keel", 
"keen", "keep", "kegs", "kelp", "keno", "kent", "kept", "kern", "keys", "khan", "kick", "kids", "kill", "kiln", "kilo", "kilt", "kind", "king", "kink", "kins", "kirk", "kiss", "kite", "kiwi", "knee", "knew", "knit", "knob", "knot", "know", "kobo", "koss", "kris", "labs", "lace", "lack", "lacy", "lads", "lady", "laid", "lair", "lake", "lama", "lamb", "lame", "lamp", "land", "lane", "lang", "laps", "lard", "lark", "lars", "lash", "lass", "last", "late", "lava", "lawn", "laws", "lays", "lazy", "lead", "leaf", "leak", "lean", "leap", "lear", "lech", "left", "legs", "lend", "leno", "lens", "lent", "less", "lest", "lets", "levy", "lewd", "liar", "lice", "lick", "lido", "lids", "lied", "lien", "lier", "lies", "lieu", "life", "lift", "like", "lily", "lima", "limb", "lime", "limo", "limp", "line", "ling", "link", "lint", "lion", "lips", "lira", "list", "lite", "live", "load", "loaf", "loan", "lobe", "loca", "loch", "lock", "loco", "lode", "loft", "logo", "logs", "loin", "lone", "long", "look", "loom", "loon", "loop", "loos", "loot", "lord", "lore", "lose", "loss", "lost", "lots", "loud", "lout", "love", "lowe", "lows", "luau", "lube", "luce", "luck", "luge", "lull", "lulu", "lump", "luna", "lung", "lure", "lurk", "lush", "lust", "lutz", "lynx", "mace", "mach", "mack", "made", "mags", "maid", "mail", "maim", "main", "make", "male", "mall", "malt", "mama", "mano", "many", "maps", "marc", "mare", "mark", "mars", "mart", "mash", "mask", "mass", "mate", "math", "mats", "matt", "maul", "maxi", "maya", "mayo", "maze", "mead", "meal", "mean", "meat", "meet", "melt", "memo", "mend", 
"menu", "meow", "mere", "merl", "mesa", "mesh", "mess", "meta", "meth", "mice", "mick", "mike", "mild", "mile", "milk", "mill", "milo", "milt", "mime", "mina", "mind", "mine", "mini", "mink", "mint", "miss", "mist", "mite", "mitt", "moan", "moat", "mobs", "mock", "mode", "moil", "mojo", "mold", "mole", "moll", "moly", "moms", "monk", "mono", "mood", "moon", "moot", "mope", "mops", "more", "morn", "mort", "moss", "most", "mote", "moth", "move", "much", "muck", "muff", "mugs", "mule", "mums", "muse", "mush", "muss", "must", "mute", "mutt", "myth", "nada", "nail", "name", "nana", "naps", "narc", "nary", "navy", "nazi", "near", "neat", "neck", "need", "neon", "nerd", "ness", "nest", "neve", "news", "newt", "next", "nice", "nick", "nigh", "nine", "nite", "node", "nods", "noel", "noir", "nome", "none", "noon", "nope", "norm", "nose", "nosh", "nosy", "note", "noun", "nous", "nova", "nude", "nuke", "null", "numb", "nuns", "nuts", "oaks", "oars", "oath", "oats", "obey", "oboe", "odds", "odor", "offs", "ogle", "ogre", "oils", "oily", "oink", "okay", "okra", "olds", "omen", "once", "ones", "only", "onto", "oops", "ooze", "opal", "open", "opus", "oral", "orbs", "orgy", "otto", "ouch", "ours", "outs", "oval", "oven", "over", "owed", "owes", "owls", "owns", "oxen", "oyez", "pace", "pack", "pact", "pads", "page", "paid", "pail", "pain", "pair", "pale", "palm", "palp", "pals", "pane", "pans", "pant", "papa", "para", "pare", "park", "part", "pass", "past", "pate", "path", "pave", "pawn", "paws", "pays", "peak", "pear", "peas", "peat", "peck", "pecs", "peed", "peek", "peel", "peep", 
"peer", "pees", "pele", "pelt", "pens", "peon", "perk", "perm", "pest", "pets", "pfft", "phew", "pick", "pied", "pier", "pies", "pigs", "pike", "pile", "pill", "pimp", "pina", "pine", "ping", "pink", "pins", "pint", "pipe", "piss", "pits", "pity", "plan", "play", "plea", "pled", "plop", "plot", "plow", "ploy", "plug", "plum", "plus", "pods", "poem", "poet", "poke", "pole", "poll", "polo", "poly", "pond", "pong", "pony", "poof", "pooh", "pool", "poop", "poor", "pope", "pops", "pore", "pork", "porn", "port", "pose", "post", "pots", "pour", "pout", "pram", "pray", "prep", "prey", "prim", "prod", "prof", "prom", "prop", "pros", "psst", "puce", "puck", "puff", "puke", "pull", "pulp", "pump", "punk", "puns", "punt", "puny", "pure", "purr", "push", "puss", "puts", "pyre", "quad", "quid", "quit", "quiz", "race", "rack", "racy", "raft", "rage", "rags", "raid", "rail", "rain", "rake", "ramp", "rand", "rang", "rank", "rant", "rape", "rare", "rash", "rate", "rath", "rats", "rave", "rays", "read", "real", "ream", "reap", "rear", "redo", "reds", "reed", "reef", "reek", "reel", "rein", "rely", "rent", "reps", "rest", "ribs", "rice", "rich", "rick", "ride", "rife", "riff", "rift", "rigs", "rile", "ring", "rink", "riot", "ripe", "rips", "rise", "risk", "rite", "ritz", "road", "roam", "roar", "robe", "robs", "rock", "rode", "rods", "role", "rolf", "roll", "romp", "roof", "rook", "room", "root", "rope", "rose", "rosy", "roto", "rots", "rows", "rube", "rubs", "ruby", "rude", "ruff", "ruin", "rule", "rump", "rune", "rung", "runs", "runt", "ruse", "rush", "rust", "ruth", "sabe", "sack", 
"sade", "safe", "saga", "sage", "said", "sail", "sake", "saki", "sale", "salt", "same", "sand", "sane", "sang", "sank", "sans", "saps", "sark", "saul", "save", "saws", "says", "scab", "scag", "scam", "scan", "scar", "scat", "scot", "scow", "scry", "scud", "scum", "seal", "seam", "sear", "seas", "seat", "seed", "seek", "seem", "seen", "seep", "seer", "sees", "self", "sell", "semi", "send", "sent", "sera", "sets", "sewn", "sexy", "shad", "shag", "shah", "sham", "shat", "shaw", "shay", "shea", "shed", "shes", "shin", "ship", "shit", "shiv", "shoe", "shoo", "shop", "shot", "show", "shun", "shut", "sick", "side", "sift", "sigh", "sign", "silk", "sill", "simp", "sims", "sine", "sing", "sink", "sins", "sire", "sirs", "site", "sits", "size", "skag", "skid", "skim", "skin", "skip", "skis", "skit", "slam", "slap", "slaw", "slay", "sled", "slew", "slid", "slim", "slip", "slit", "slob", "slop", "slot", "slow", "slug", "slum", "slur", "slut", "smog", "smug", "snag", "snap", "snip", "snit", "snob", "snot", "snow", "snub", "snug", "soak", "soap", "soar", "sobs", "sock", "soda", "sofa", "soft", "soil", "sold", "sole", "solo", "some", "song", "sons", "sook", "soon", "soot", "sore", "sort", "soul", "soup", "sour", "sous", "sown", "span", "spar", "spas", "spat", "spaz", "spew", "spic", "spin", "spit", "spot", "spry", "spud", "spun", "spur", "stab", "stag", "star", "stat", "stay", "stem", "step", "stew", "stir", "stop", "stow", "stub", "stud", "stun", "such", "suck", "suds", "sued", "sues", "suit", "sulk", "sumo", "sump", "sums", "sung", "sunk", "sure", "surf", "suss", "swab", "swam", 
"swan", "swap", "swat", "sway", "swig", "swim", "sync", "syne", "tabs", "tach", "tack", "taco", "tact", "tags", "tail", "take", "tale", "talk", "tall", "tame", "tank", "tape", "tarp", "tart", "task", "tate", "taut", "taxi", "teal", "team", "tear", "teas", "teed", "teen", "tell", "temp", "tend", "tens", "tent", "term", "test", "text", "than", "that", "thaw", "thee", "them", "then", "they", "thin", "this", "thou", "thru", "thug", "thus", "tick", "tide", "tidy", "tied", "tier", "ties", "tiff", "tiki", "tile", "till", "tilt", "time", "ting", "tins", "tiny", "tips", "tire", "tits", "toad", "toby", "toed", "toes", "tofu", "toga", "toke", "told", "toll", "tomb", "tome", "toms", "tone", "tong", "tons", "tony", "took", "tool", "toon", "toot", "tops", "tore", "torn", "toro", "tory", "tosh", "toss", "tote", "tots", "tour", "town", "toys", "tram", "trap", "tray", "tree", "trek", "trey", "trig", "trim", "trio", "trip", "trot", "troy", "true", "tuba", "tube", "tubs", "tuck", "tuna", "tune", "tung", "turd", "turf", "turk", "turn", "tush", "tusk", "tutu", "twas", "twat", "twig", "twin", "twit", "twos", "type", "typo", "tyre", "ugly", "undo", "unit", "unto", "upon", "urge", "urns", "used", "user", "uses", "vail", "vain", "vamp", "vary", "vase", "vast", "veal", "veer", "veil", "vein", "vent", "vera", "very", "vest", "veto", "vets", "vial", "vibe", "vice", "view", "vile", "vill", "vine", "vino", "visa", "viva", "vive", "void", "volt", "vote", "vows", "wack", "wade", "wage", "waif", "wail", "wait", "wake", "walk", "wall", "wand", "want", "ward", "ware", "warm", "warn", "warp", "wars", 
"wart", "wary", "wash", "wasp", "watt", "wave", "wavy", "waxy", "ways", "weak", "wean", "wear", "webs", "weds", "weed", "week", "weep", "weir", "weld", "well", "welt", "went", "wept", "were", "west", "wets", "wham", "what", "whee", "when", "whet", "whew", "whey", "whim", "whip", "whit", "whiz", "whoa", "whom", "whys", "wick", "wide", "wife", "wigs", "wild", "will", "wilt", "wily", "wimp", "wind", "wine", "wing", "wink", "wins", "wipe", "wire", "wise", "wish", "with", "wits", "woes", "woke", "wolf", "womb", "wont", "wood", "woof", "wool", "wops", "word", "wore", "work", "worm", "worn", "wrap", "writ", "wuss", "wynn", "yams", "yang", "yank", "yard", "yarn", "yawn", "yeah", "year", "yech", "yell", "yeti", "yipe", "yoga", "yogi", "yoke", "yolk", "yore", "your", "iota", "yuck", "zany", "zeal", "zero", "zest", "zeta", "zing", "zits", "zone", "zoom"]

width_of_window = 500
height_of_window = 600


itt = 0
for items in alpha:
    letter = alpha[math.floor((random.random()*100000))%1578]
    queue.append(letter)
curLetter = queue[itt] #alpha[math.floor((random.random()*100000))%1579 ]
nextLetter = queue[itt+1]




font = pygame.font.Font('font.ttf', 25)
text = font.render(curLetter, True, (0, 255, 0))
textRect = text.get_rect()

nex = font.render('NEXT:', True, (0, 255, 0))
next = font.render(nextLetter, True, (0, 255, 0))

sco = font.render('SCORE:', True, (0, 255, 0))
scor = font.render(str(points), True, (0+(points/15), 255, 0+(points/15)))

wo = font.render('WORD:', True, (0, 255, 0))
wor = font.render("TEST", True, (0, 255, 0))

sto = font.render('STORE:', True, (0, 255, 0))
stor = font.render("X", True, (0, 255, 0))

nexRect = nex.get_rect()
nextRect = next.get_rect()

scoRect = sco.get_rect()
scorRect = scor.get_rect()

woRect = wo.get_rect()
worRect = wor.get_rect()

stoRect = sto.get_rect()
storRect = stor.get_rect()




window = pygame.display.set_mode((width_of_window,height_of_window))

running  = True

fps = pygame.time.Clock()



board = [[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "] ]


for i in range(20):
    for j in range(10):
        board[i][j] = '?'
                                    

def clearUp(loc, Mode):
    if Mode == 1:
        for i in range(loc):
            board[loc-i] = board[(loc-i)-1]
            board[0] = ["?", "?", "?", "?", "?", "?", "?", "?", "?", "?"]
    if Mode == 2:
        for i in range(20):
            board[i][loc] = '?'
    global score
    score += 1
    if score < 20:
        pygame.time.set_timer(DROP_IT, 500-(score*20))
    else:
        pygame.time.set_timer(DROP_IT, 100)

def drop():
    window.fill((0,0,0))
    for x in range(10):
        for y in range(20):
            rect = pygame.Rect(x * 30, y * 30, 30, 30)
            pygame.draw.rect(window, (255, 255, 255), rect, 1)
            if board[y][x] != '?':
                text = font.render(board[y][x], True, (0, 255, 0))
                rect = pygame.Rect((x * 30) +1, (y * 30)+1, 28, 28)
                #pygame.draw.rect(window, (255, 100, 0), rect)
                textRect.center = ((x*30)+15, (y*30)+15)
                window.blit(text, textRect)     
                
    pygame.display.update()
    #pygame.draw.rect(window, (255,100,0), [(posX*30)+1, (posY*30)+1, 28, 28], 0)
    textRect.center = ((posX*30)+15, (posY*30)+15)
    nextRect.center = (400, 100)
    nexRect.center = (410,70)
    scoRect.center = (410, 170)
    scorRect.center = (400-pad, 200)
    woRect.center = (400, 270)
    worRect.center = (400,300)
    stoRect.center = (400, 370)
    storRect.center = (400,400)

    text = font.render(curLetter, True, (0, 255, 0))
    next = font.render(nextLetter, True, (0, 255, 0))
    scor = font.render(str(points), True, (0+(points/15), 255, 0+(points/15)))
    stor = font.render(storedLetter, True, (0, 255, 0))
    wor = font.render(lastWord, True, (0, 255, 0))
    window.blit(text, textRect)
    window.blit(next, nextRect)
    window.blit(sco, scoRect)
    window.blit(scor, scorRect)
    window.blit(nex, nexRect)
    window.blit(sto, stoRect)
    window.blit(stor, storRect)
    window.blit(wo, woRect)
    window.blit(wor, worRect)
    pygame.display.update()  

def scoreIt(curWord):
    global lastWord
    lastWord = curWord
    curWord = curWord.lower()
    for i in curWord:
        global points
        if i == 'e':
            points += 10
        if i == 'a':
            points += 13
        if i == 'i':
            points += 62
        if i == 'l':
            points += 47
        if i == 'n':
            points += 70
        if i == 'o':
            points += 28
        if i == 'r':
            points += 60
        if i == 's':
            points += 19
        if i == 't':
            points += 59
        if i == 'u':
            points += 86
        if i == 'd':
            points += 83
        if i == 'g':
            points += 106
        if i == 'b':
            points += 101
        if i == 'c':
            points += 95
        if i == 'm':
            points += 93
        if i == 'p':
            points += 89
        if i == 'f':
            points += 109
        if i == 'h':
            points += 96
        if i == 'v':
            points += 132
        if i == 'w':
            points += 109
        if i == 'y':
            points += 115
        if i == 'k':
            points += 105
        if i == 'j':
            points += 137
        if i == 'x':
            points += 141
        if i == 'q':
            points += 145
        if i == 'z':
            points += 138
    global pad
    if points > 100 and pad == 0:
        pad+= 20
    if points > 1000 and pad == 20:
        pad+= 25
    if points > 10000 and pad == 40:
        pad+= 25

def checkIt(x, y):
    if x <= 16:
        curWord = board[x][y] + board[x+1][y] + board[x+2][y] + board[x+3][y]
        for i in words:
            if curWord.lower() == i:
                print(curWord)
                clearUp(y, 2)
                scoreIt(curWord)
                    
            if reverse(curWord.lower()) == i:
                print(curWord)
                clearUp(y, 2)
                scoreIt(reverse(curWord))
    if y < 7:
        curWord = board[x][y] + board[x][y+1] + board[x][y+2] + board[x][y+3]
        for i in words:
            if curWord.lower() == i:
                print(curWord)
                clearUp(x, 1)
                scoreIt(curWord)
            if reverse(curWord.lower()) == i:
                print(curWord)
                clearUp(x, 1)
                scoreIt(reverse(curWord))
    if y > 0 and y < 8:
        curWord = board[x][y-1] + board[x][y] + board[x][y+1] + board[x][y+2]
        for i in words:
            if curWord.lower() == i:
                print(curWord)
                clearUp(x, 1)
                scoreIt(curWord)
            if reverse(curWord.lower()) == i:
                print(curWord)
                clearUp(x, 1)
                scoreIt(reverse(curWord))
    if y > 1 and y < 9:
        curWord = board[x][y-2] + board[x][y-1] + board[x][y] + board[x][y+1]
        for i in words:
            if curWord.lower() == i:
                print(curWord)
                clearUp(x, 1)
                scoreIt(curWord)
            if reverse(curWord.lower()) == i:
                print(curWord)
                clearUp(x, 1)
                scoreIt(reverse(curWord))
    if y > 2:
        curWord = board[x][y-3] + board[x][y-2] + board[x][y-1] + board[x][y]
        for i in words:
            if curWord.lower() == i:
                print(curWord)
                clearUp(x, 1)
                scoreIt(curWord)
            if reverse(curWord.lower()) == i:
                print(curWord)
                clearUp(x, 1)
                scoreIt(reverse(curWord))
            

def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str

DROP_IT = pygame.USEREVENT + 1

pygame.time.set_timer(DROP_IT, 500)

posX = math.floor((random.random()*1000)%10)
posY = 0
dropped = 0

def left():
     
     global posX 
     if posX > 0 and dropped == 0:
        posX = posX-1

def right():
     global posX 
     if posX <9 and dropped == 0:
        posX = posX + 1



def speed():
    pygame.time.set_timer(DROP_IT, 50)
    global dropped
    dropped = 1
def store():
    global posY
    global curLetter
    global nextLetter
    global itt
    global swapped
    global storedLetter
    if storedLetter == "" and swapped == 0:
        storedLetter = curLetter
        posY = 0
        curLetter = queue[itt+1]
        nextLetter = queue[itt+2]
        itt+=1
        swapped = 1

    if storedLetter != "" and swapped == 0:
        temp = storedLetter
        storedLetter = curLetter
        posY = 0
        curLetter = temp
        swapped = 1




pygame.display.update()

while running:  
    
   
 
 for event in pygame.event.get():

    if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                left()
            if event.key == pygame.K_RIGHT:
                right()
            if event.key == pygame.K_DOWN:
                speed()
            if event.key == pygame.K_UP:
                store()

    if event.type == DROP_IT:
            drop()
            if posY <19 and board[posY+1][posX] == '?':
                posY+=1
            else:
                if dropped == 1:
                    dropped = 0
                    if score < 20:
                        pygame.time.set_timer(DROP_IT, 500-(score*20))
                    else:
                        pygame.time.set_timer(DROP_IT, 100)

                board[posY][posX] = curLetter
                checkIt(posY, posX)
                posY=0 
                posX = math.floor((random.random()*1000)%10)
                text = font.render(curLetter, True, (0, 255, 0))
                itt += 1
                curLetter = queue[itt]
                nextLetter = queue[itt+1]
                swapped = 0
                
                

                
                


            
    
    if event.type == pygame.QUIT:  
           running = False


