from itertools import product
import re
'''
https://www.codewars.com/kata/5a3267b2ee1aaead3d000037/train/python


Background
If your phone buttons have letters, then it is easy remember long phone numbers by making words from the substituted digits.

https://en.wikipedia.org/wiki/Phoneword

source: imgur.com
This is common for 1-800 numbers

1-800 number format
This format probably varies for different countries, but for the purpose of this Kata here are my rules:

A 1-800 number is an 11 digit phone number which starts with a 1-800 prefix.

The remaining 7 digits can be written as a combination of 3 or 4 letter words. e.g.

1-800-CODE-WAR
1-800-NEW-KATA
1-800-GOOD-JOB
The - are included just to improve the readability.

Story
A local company has decided they want to reserve a 1-800 number to help with advertising.

They have already chosen what words they want to use, but they are worried that maybe that same phone number could spell out other words as well. Maybe bad words. Maybe embarrassing words.

They need somebody to check for them so they can avoid any accidental PR scandals!

That's where you come in...

Kata Task
There is a preloaded array of lots of 3 and 4 letter (upper-case) words:

For Python it is: WORDS
Given the 1-800 (phone word) number that the company wants to use, you need to check against all known words and return the set of all possible 1-800 numbers which can be formed using those same digits.

Notes
The desired phone-word number provided by the company is formatted properly. No need to check.
All the letters are upper-case. No need to check.
Only words in the list are allowed.
'''

WORDS = ['ACT', 'ADD', 'ALL', 'APE', 'AND', 'ANN', 'ANY', 'ANT', 'ARE', 'ART', 'ASS', 'BAD', 'BAR', 'BAT', 'BAY', 'BEE', 'BIG', 'BIT', 'BOB', 'BOY', 'BUN', 'BUT', 'CAN', 'CAR', 'CAT', 'COT', 'COW', 'CUT', 'DAD', 'DAY', 'DEW', 'DID', 'DIN', 'DOG', 'DON', 'DOT', 'DUD', 'EAR', 'EAT', 'EEL', 'EGG', 'ERR', 'EYE', 'FAG', 'FAR', 'FLY', 'FOR', 'FUN', 'FUR', 'GAY', 'GET', 'GOT', 'GUM', 'GUN', 'GUY', 'GUT', 'GYM', 'HAS', 'HAT', 'HER', 'HEY', 'HIM', 'HIS', 'HIT', 'HOW', 'HUG', 'HUN', 'ICE', 'INK', 'ITS', 'IVE', 'JAN', 'JET', 'JOB', 'JOT', 'JOY', 'KEY', 'LAP', 'LAY', 'LIE', 'LET', 'LOG', 'MAN', 'MAP', 'MAY', 'MEN', 'MOM', 'MUD', 'MUM', 'NAP', 'NEW', 'NOD', 'NOT', 'NOW', 'OAR', 'ODD', 'OFF', 'OLD', 'ONE', 'OUR', 'OUT', 'PAN', 'PAL', 'PAT', 'PAW', 'PEN', 'PET', 'PIG', 'PIT', 'POT', 'PRO', 'PUT', 'QUO', 'RAG', 'RAM', 'RAN', 'RAP', 'RAT', 'RED', 'RIP', 'ROD', 'ROT', 'RUN', 'RUT', 'SAT', 'SAW', 'SAY', 'SEA', 'SEE', 'SEX', 'SHE', 'SOY', 'SUN', 'SUX', 'TAN', 'TAT', 'TEA', 'THE', 'TIN', 'TIP', 'TIT', 'TON', 'TOP', 'TOO', 'TWO', 'URN', 'USE', 'VAN', 'VET', 'VIP', 'WAR', 'WAS', 'WAY', 'WED', 'WHO', 'WHY', 'WIN', 'WON', 'XXX', 'YAK', 'YAM', 'YAP', 'YOU', 'YUM', 'ZAP', 'ZIP', 'ZIT', 'ZOO', 'ABLE', 'ACED', 'AGOG', 'AHEM', 'AHOY', 'ALLY', 'AMEN', 'ANTI', 'ANTS', 'ANUS', 'APES', 'ARMY', 'ARSE', 'ARTY', 'AVID', 'AWED', 'BABY', 'BARS', 'BATS', 'BAYS', 'BEAR', 'BEES', 'BILL', 'BITE', 'BITS', 'BLOW', 'BLUE', 'BOLD', 'BONE', 'BOOB', 'BOOM', 'BOSS', 'BOYS', 'BUFF', 'BUNG', 'BUNS', 'BUMS', 'BURP', 'BUST', 'BUSY', 'BUZZ', 'CANS', 'CANT', 'CARS', 'CART', 'CATS', 'CHAP', 'CHIC', 'CHUM', 'CIAO', 'CLAP', 'COCK', 'CODE', 'COOL', 'COWS', 'COZY', 'CRAB', 'CREW', 'CURE', 'CULT', 'DADS', 'DAFT', 'DAWN', 'DAYS', 'DECK', 'DEED', 'DICK', 'DING', 'DOGS', 'DOTS', 'DOLL', 'DOLT', 'DONG', 'DOPE', 'DOWN', 'DRAW', 'DUCK', 'DUDE', 'DUMB', 'DUTY', 'EARL', 'EARN', 'EARS', 'EASY', 'EATS', 'EDGE', 'EELS', 'EGGS', 'ENVY', 'EPIC', 'EYES', 'FACE', 'FAGS', 'FANG', 'FARM', 'FART', 'FANS', 'FAST', 'FEAT', 'FEET', 'FISH', 'FIVE', 'FIZZ', 'FLAG', 'FLEW', 'FLIP', 'FLOW', 'FOOD', 'FORT', 'FUCK', 'FUND', 'GAIN', 'GEEK', 'GEMS', 'GIFT', 'GIRL', 'GIST', 'GIVE', 'GLEE', 'GLOW', 'GOLD', 'GOOD', 'GOSH', 'GRAB', 'GRIN', 'GRIT', 'GROT', 'GROW', 'GRUB', 'GUNS', 'GUSH', 'GYMS', 'HAIL', 'HAIR', 'HALO', 'HANG', 'HATS', 'HEAD', 'HEAL', 'HEIR', 'HELL', 'HELP', 'HERE', 'HERO', 'HERS', 'HIGH', 'HIRE', 'HITS', 'HOLY', 'HOPE', 'HOST', 'HUNK', 'HUGE', 'HUNG', 'HUNS', 'HURT', 'ICON', 'IDEA', 'IDLE', 'IDOL', 'IOTA', 'JAZZ', 'JERK', 'JESS', 'JETS', 'JINX', 'JOBS', 'JOHN', 'JOKE', 'JUMP', 'JUNE', 'JULY', 'JUNK', 'JUST', 'KATA', 'KEYS', 'KICK', 'KIND', 'KING', 'KISS', 'KONG', 'KNOB', 'KNOW', 'LARK', 'LATE', 'LEAN', 'LICE', 'LICK', 'LIKE', 'LION', 'LIVE', 'LOGS', 'LOCK', 'LONG', 'LOOK', 'LORD', 'LOVE', 'LUCK', 'LUSH', 'MAKE', 'MANY', 'MART', 'MATE', 'MAXI', 'MEEK', 'MIKE', 'MILD', 'MINT', 'MMMM', 'MOMS', 'MOOD', 'MOON', 'MOOT', 'MUCH', 'MUFF', 'MUMS', 'MUTT', 'NAPS', 'NAZI', 'NEAT', 'NECK', 'NEED', 'NEWS', 'NEXT', 'NICE', 'NICK', 'NOON', 'NOSE', 'NOTE', 'OARS', 'OATS', 'ONCE', 'ONLY', 'OPEN', 'ORGY', 'OVAL', 'OVER', 'PANS', 'PALS', 'PART', 'PAST', 'PATS', 'PAWS', 'PEAR', 'PERT', 'PENS', 'PETS', 'PHEW', 'PIPE', 'PIPS', 'PLAN', 'PLUM', 'PLUS', 'POET', 'POOF', 'POOP', 'POSH', 'POTS', 'PROS', 'PSST', 'PUKE', 'PUNK', 'PURE', 'PUSH', 'PUSS', 'QUAD', 'QUAK', 'QUID', 'QUIT', 'RANT', 'RAPE', 'RAPS', 'RAPT', 'RATE', 'RAMS', 'RATS', 'REAP', 'RICK', 'RING', 'RIPE', 'ROOT', 'ROSE', 'ROSY', 'ROTS', 'RUNT', 'RUTS', 'SAFE', 'SAGE', 'SANE', 'SAVE', 'SAWS', 'SEEK', 'SEXY', 'SHAG', 'SHIT', 'SICK', 'SIGH', 'SIRE', 'SLAG', 'SLIT', 'SLUT', 'SNAP', 'SNOG', 'SNUG', 'SOFT', 'SOON', 'SOUL', 'SOUP', 'SPRY', 'STIR', 'STUN', 'SUCK', 'SWAG', 'SWAY', 'TACT', 'TANK', 'TANS', 'THAT', 'THIS', 'TIME', 'TINS', 'TINY', 'TITS', 'TOES', 'TONS', 'TONY', 'TOPS', 'TOYS', 'UBER', 'URNS', 'USED', 'USER', 'USES', 'VAIN', 'VAMP', 'VARY', 'VEIN', 'VENT', 'VERY', 'VEST', 'VIEW', 'VIVA', 'VOLT', 'VOTE', 'WAFT', 'WAGE', 'WAKE', 'WALK', 'WALL', 'WANG', 'WANK', 'WANT', 'WARD', 'WARM', 'WARP', 'WARS', 'WART', 'WASH', 'WAVE', 'WEAR', 'WEDS', 'WEED', 'WEEN', 'WELD', 'WHAT', 'WHEE', 'WHEW', 'WHIP', 'WHIZ', 'WHOA', 'WIFE', 'WILL', 'WIND', 'WING', 'WINK', 'WINS', 'WIRE', 'WISH', 'WITH', 'WORD', 'WORK', 'WRAP', 'XMAN', 'XMEN', 'XRAY', 'XTRA', 'XXXX', 'YANK', 'YAKS', 'YAMS', 'YAPS', 'YARD', 'YARN', 'YELP', 'YERN', 'YOKE', 'YOLK', 'YULE', 'ZANY', 'ZAPS', 'ZIPS', 'ZITS', 'ZERO', 'ZOOM', 'ZOOS']

def get_all_allowed_combinations(string):
    res = []
    code = [
        [], 
        [],
        ["A", "B", "C"],
        ["D", "E", "F"],
        ["G", "H", "I"], 
        ["J", "K", "L"],
        ["M", "N", "O"], 
        ["P", "Q", "R", "S"],
        ["T", "U", "V"],
        ["W", "X", "Y", "Z"]
    ]
    for l,c in product(string, code):
        if l in c:
            res.append(c)
    combinations = list(product(*res))
    result = ["".join(item) for item in combinations if "".join(item) in WORDS]
    return result

def check1800(s: str) -> set:
    ans = set()
    words = re.findall(r'[A-Z]',s)
    first_word, second_word = words[:4], words[4:]
    print(first_word, second_word)
    for k,j in product(get_all_allowed_combinations(first_word), get_all_allowed_combinations(second_word)):
        ans.add(f"1-800-{k}-{j}")
    first_word, second_word = words[:3], words[3:]
    for k,j in product(get_all_allowed_combinations(first_word), get_all_allowed_combinations(second_word)):
        ans.add(f"1-800-{k}-{j}")
    return ans

print(check1800("1-800-CODE-WAR"))
print(check1800("1-800-BOY-ARMY"))
print(check1800("1-800-SAT-SNAP"))