

def generate_fields():
    MY_FIELDS = ['hero_firstname',
                 'hero_lastname',
                 'hero_gender',
                 'hero_adj',
                 'animal_lowercase',
                 'animal_adj_not_size',
                 'friend_firstname',
                 'friend_lastname',
                 'friend_gender',
                 'friend_relationship',
                 'forest',
                 'favorite_toy',
                 'color',
                 'clothing',
                 'very_healthy_food',
                 'unhealthy_food_1',
                 'unhealthy_food_2',
                 'unhealthy_food_3',
                 'unhealthy_food_4',
                 'unhealthy_food_5']

    return MY_FIELDS

def generate_descriptions():
    MY_DESCRIPTIONS = {
                       'hero_firstname' : 'First name',
                       'hero_lastname' : 'Last name',
                       'hero_gender' : 'Gender',
                       'hero_adj' : 'An adjective to describe your hero (e.g. little, brave)',
                       'animal_lowercase' : 'A type of animal (e.g. bear, pig)',
                       'animal_adj_not_size' : "An adjective (not relating to size) describing the animal(s) (e.g. hairy, scary)",
                       'friend_firstname' : 'First name',
                       'friend_lastname' : 'Last name',
                       'friend_gender' : 'Gender',
                       'friend_relationship' : 'Relationship',
                       'forest' : 'The name of a forest or park nearby (e.g. Sherwood Forest)',
                       'favorite_toy' : "The hero's favourite cuddly toy (e.g. Mr Teddy)",
                       'color' : 'A color (e.g. red, green)',
                       'clothing' : 'An item of clothing, singular (e.g. skirt, dungarees)',
                       'very_healthy_food' : 'A type of healthy vegetable, plural (e.g. carrots, cabbages)',
                       'unhealthy_food_1' : 'Unhealthy food 1',
                       'unhealthy_food_2' : 'Unhealthy food 2',
                       'unhealthy_food_3' : 'Unhealthy food 3',
                       'unhealthy_food_4' : 'Unhealthy food 4',
                       'unhealthy_food_5' : 'Unhealthy food 5',
                       }

    return MY_DESCRIPTIONS

def generate_suggestions():
    MY_SUGGESTIONS = dict()
    MY_SUGGESTIONS['hero'] = [
                              ('Sam', 'Gump', 'male'),
                              ('Bob','Doop', 'male'),
                              ('Jody','Gloop', 'female'),
                              ('Robin','Snozcumber', 'female'),
                              ('Mike', 'Giantbulb', 'male'),
                              ('Alex','Slaughterhouse', 'male'),
                              ('Lee','Lakeman', 'male'),
                              ('Chloe', 'Bogtrotter', 'female'),
                              ('Catherine','Ramsbottom', 'female'),
                           ]

    MY_SUGGESTIONS['sidekick'] = [
                                  ('Tom', 'Goral', 'male', 'friend'),
                                  ('Simon','Loppe', 'male', 'friend'),
                                  ('Jeanny','Lovely', 'female', 'friend'),
                                  ('Charlotte','Obsidian', 'female', 'father'),
                                  ('Tony', 'Starwish', 'male', 'uncle'),
                                  ('Max','Cameron', 'male', 'brother'),
                                  ('Lea','Fisherman', 'female', 'sister'),
                                  ('Sandy', 'Malibu', 'female', 'aunt'),
                                  ('Kate','Thunderburn', 'female', 'mother'),
                                  ]

    MY_SUGGESTIONS['pos_character'] = ['gentle', 'thoughtful', 'modest', 'adorable', 'brave', 'helpful','loving', 'special', 'hopeful', 'optimistic', 'charming','kind', 'grateful', 'gracious', 'delightful', 'patient','generous', 'energetic', 'down to earth', 'admirable', 'friendly','smart', 'considerate','noble', 'articulate', 'caring','intuitive', 'sympathetic','clever', 'daring', 'courageous','hilarious', 'understanding', 'incredible','funny', 'popular', 'virtuous', 'lovable', 'remarkable', 'cute', 'sweet', 'splendid','stable', 'witty', 'admirable', 'giving', 'intelligent', 'brave', 'bold']
    MY_SUGGESTIONS['neg_character'] = ['greedy','callous','selfish','spiteful','mean','cowardly','stupid', 'spiteful', 'scheming','wild','tactless','peculiar','creepy','sinister', 'arrogant', 'proud', 'ruthless', 'cold-blooded', 'smelly', 'vile', 'snotty', 'hungry', 'predatory', 'malicious', 'deranged', 'snooty', 'violent', 'cowardly', 'brutal', 'controlling', 'clumsy', 'forgetful', 'thoughtless', 'stingy', 'rude', 'tight-fisted',]
    MY_SUGGESTIONS['phys_adj'] = ['pink','feathery','sloppy','slimy','spiky','greasy','ginger','brunette','brown', 'blonde', 'red','tall','short','fat','squat','chubby', 'skinny', 'pointy', 'scrawny', 'wobbly', 'wide', 'vast', 'solid', 'fragile', 'fluffy', 'hairy', 'grubby', 'dirty', 'moist', 'ugly', 'pretty', 'charming', 'handsome', 'beautiful', 'sticky', 'curvaceous', 'curvy', 'ample', 'ruddy',]
    MY_SUGGESTIONS['hero_adj']= MY_SUGGESTIONS['pos_character'] + MY_SUGGESTIONS['neg_character'] + MY_SUGGESTIONS['phys_adj']

    MY_SUGGESTIONS['animal_lowercase'] = ['fox','monkey','snake','bear','rat','lizard','owl','badger', 'ostrich','frog']
    MY_SUGGESTIONS['animal_adj_not_size'] = ['hairy', 'fluffy', 'scary', 'spiky', 'cruel', 'kind', 'fierce', 'friendly', 'fuzzy','hysterical','naughty','scruffy',]
    MY_SUGGESTIONS['forest'] = ['Penrose Woods','Central Park','Sherwook Forest','Kennel Vale',	'Idless Woods','St James\'s Park','Kensington Gardens','Gurglebridge','Hyde Park','Hampstead Heath',
    									'New Swamp','Thetford Forest','The Amazon Rainforest','Wyre Forest','Snotchester Forest','Greenwood Forest','Spittleton Woods','Gruesomeside Forest','Grizedale Forest','Dallington Forest','Yuckylake Woods','Stinkville Forest',
    									'Greenton Woods', 'Slipperyham Park', 'Bogstaple Woods', 'Awfulpool Forest']
    MY_SUGGESTIONS['favorite_toy'] = ['Mr Teddy','Miss Piggy','Terrance the Moose','Little Mouse', 'Henry the Hippo','Spike','Daisy','Laura','Rags','Bunny',
                             'George','Blankey','Ted','Hugo','Molly','Dolly','Emma','Piglet','Donkey',]

    MY_SUGGESTIONS['color'] = ['red', 'yellow', 'green', 'blue', 'purple', 'pink']
    MY_SUGGESTIONS['clothing'] = ['top hat', 'bowler hat', 'dungarees', 'pinafore', 'skirt', 't-shirt', 'jumper', 'waistcoat', 'coat', 'jacket']
    MY_SUGGESTIONS['very_healthy_food'] = ['carrots', 'butternut squashes', 'aubergines', 'courgettes', 'cauliflowers', 'cabbages', 'parsnips', 'sprouts', 'turnips',
                          'sweet potatoes', 'swedes','broccoli florets','pumpkins','peppers','onions','runner beans','sugar snap pea','pods of peas','peas','red cabbages','lettuces','cucumbers',]
    MY_SUGGESTIONS['unhealthy_food_1'] = ['crisps', 'sweets', 'biscuits', 'cakes']
    MY_SUGGESTIONS['unhealthy_food_2'] = ['toffees', 'chocolates', 'macarons']
    MY_SUGGESTIONS['unhealthy_food_3'] = ['chips', 'doughnuts', 'pancakes']
    MY_SUGGESTIONS['unhealthy_food_4'] = ['muffins','cupcakes','pizzas']
    MY_SUGGESTIONS['unhealthy_food_5'] = ['lollipops','jelly babies','humbugs','fruit gums']

    return MY_SUGGESTIONS
