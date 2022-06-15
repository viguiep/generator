# Story generator in Streamlit with form

import streamlit as st
import random


# ******************************************
# VARIABLES
# ******************************************
MY_FIELDS = ['hero_firstname', 'hero_lastname', 'hero_gender', 'hero_adj',
          'animal', 'animal_adj_not_size', 'nb_animals', 'friend_firstname', 'friend_lastname', 'friend_gender', 'friend_relationship',
          'forest', 'toy', 'color', 'clothing',
          'healthy_food', 'unhealthy_food_1', 'unhealthy_food_2', 'unhealthy_food_3', 'unhealthy_food_4', 'unhealthy_food_5']

MY_DESCRIPTIONS = { 'hero_firstname' : 'First name',
                    'hero_lastname' : 'Last name',
                    'hero_gender' : 'Gender',
                    'hero_adj' : 'An adjective to describe your hero (e.g. little, brave)',
                    'animal' : 'A type of animal (e.g. bear, pig)',
                    'animal_adj_not_size' : "An adjective (not relating to size) describing the animal(s) (e.g. hairy, scary)",
                    'nb_animals' : 'How many of the animals above will be in the story',
                    'friend_firstname' : 'First name',
                    'friend_lastname' : 'Last name',
                    'friend_gender' : 'Gender',
                    'friend_relationship' : 'Relationship',
                    'forest' : 'The name of a forest or park nearby (e.g. Sherwood Forest)',
                    'toy' : "The hero's favourite cuddly toy (e.g. Mr Teddy)",
                    'color' : 'A color (e.g. red, green)',
                    'clothing' : 'An item of clothing, singular (e.g. skirt, dungarees)',
                    'healthy_food' : 'A type of healthy vegetable, plural (e.g. carrots, cabbages)',
                    'unhealthy_food_1' : 'Unhealthy food 1',
                    'unhealthy_food_2' : 'Unhealthy food 2',
                    'unhealthy_food_3' : 'Unhealthy food 3',
                    'unhealthy_food_4' : 'Unhealthy food 4',
                    'unhealthy_food_5' : 'Unhealthy food 5'}

MY_SUGGESTIONS = dict()
# 0 = male; 1 = female
MY_SUGGESTIONS['hero'] = [('Sam', 'Gump', 'male'),
                       ('Bob','Doop', 'male'),
                       ('Jody','Gloop', 'female'),
                       ('Robin','Snozcumber', 'female'),
                       ('Mike', 'Giantbulb', 'male'),
                       ('Alex','Slaughterhouse', 'male'),
                       ('Lee','Lakeman', 'male'),
                       ('Chloe', 'Bogtrotter', 'female'),
                       ('Catherine','Ramsbottom', 'female'),
                       ]

MY_SUGGESTIONS['sidekick'] = [('Tom', 'Goral', 'male', 'friend'),
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

MY_SUGGESTIONS['animal'] = ['fox','monkey','snake','bear','rat','lizard','owl','badger', 'ostrich','frog']
MY_SUGGESTIONS['animal_adj_not_size'] = ['hairy', 'fluffy', 'scary', 'spiky', 'cruel', 'kind', 'fierce', 'friendly', 'fuzzy','hysterical','naughty','scruffy',]
MY_SUGGESTIONS['forest'] = ['Penrose Woods','Central Park','Sherwook Forest','Kennel Vale',	'Idless Woods','St James\'s Park','Kensington Gardens','Gurglebridge','Hyde Park','Hampstead Heath',
									'New Swamp','Thetford Forest','The Amazon Rainforest','Wyre Forest','Snotchester Forest','Greenwood Forest','Spittleton Woods','Gruesomeside Forest','Grizedale Forest','Dallington Forest','Yuckylake Woods','Stinkville Forest',
									'Greenton Woods', 'Slipperyham Park', 'Bogstaple Woods', 'Awfulpool Forest']
MY_SUGGESTIONS['toy'] = ['Mr Teddy','Miss Piggy','Terrance the Moose','Little Mouse', 'Henry the Hippo','Spike','Daisy','Laura','Rags','Bunny',
                         'George','Blankey','Ted','Hugo','Molly','Dolly','Emma','Piglet','Donkey',]

MY_SUGGESTIONS['color'] = ['red', 'yellow', 'green', 'blue', 'purple', 'pink']
MY_SUGGESTIONS['clothing'] = ['top hat', 'bowler hat', 'dungarees', 'pinafore', 'skirt', 't-shirt', 'jumper', 'waistcoat', 'coat', 'jacket']
MY_SUGGESTIONS['healthy_food'] = ['carrots', 'butternut squashes', 'aubergines', 'courgettes', 'cauliflowers', 'cabbages', 'parsnips', 'sprouts', 'turnips',
                      'sweet potatoes', 'swedes','broccoli florets','pumpkins','peppers','onions','runner beans','sugar snap pea','pods of peas','peas','red cabbages','lettuces','cucumbers',]
MY_SUGGESTIONS['unhealthy_food_1'] = ['crisps', 'sweets', 'biscuits', 'cakes']
MY_SUGGESTIONS['unhealthy_food_2'] = ['toffees', 'chocolates', 'macarons']
MY_SUGGESTIONS['unhealthy_food_3'] = ['chips', 'doughnuts', 'pancakes']
MY_SUGGESTIONS['unhealthy_food_4'] = ['muffins','cupcakes','pizzas']
MY_SUGGESTIONS['unhealthy_food_5'] = ['lollipops','jelly babies','humbugs','fruit gums']
MY_SUGGESTIONS['nb_animals'] = ['1','2','3','4','5']

# ******************************************
# BEGINNING
# ******************************************
st.title('Story generator (Fairytale)')

"""
Principle:
- enter the data with a FORM
- you can generate all the data (changing the default value)
- then the full app is run
"""

# ******************************************
# SIDEBAR
# ******************************************


MY_VALUES = dict()


for my_field in MY_FIELDS:
    if my_field not in st.session_state:
        st.session_state[my_field] = ''
    MY_VALUES[my_field] = st.session_state[my_field]

def get_info(my_field):
    my_description = MY_DESCRIPTIONS[my_field]
    col_1, col_2 = st.columns([1,1])
    with col_1:
        st.write('')
        st.write('')
        st.write(my_description)
    with col_2:
        my_value = st.text_input('', key=my_field, value=st.session_state[my_field])

st.sidebar.title('Informations')

MY_SUGGESTED_FIELDS = ['hero_adj', 'animal', 'animal_adj_not_size', 'nb_animals', 'forest', 'toy', 'color', 'clothing',
          'healthy_food', 'unhealthy_food_1', 'unhealthy_food_2', 'unhealthy_food_3', 'unhealthy_food_4', 'unhealthy_food_5']

with st.sidebar:

    if st.button('SUGGEST FIELDS'):
        my_suggestions = MY_SUGGESTIONS['hero']
        my_value_suggested = random.choice(my_suggestions)
        st.session_state['hero_firstname'] = my_value_suggested[0]
        st.session_state['hero_lastname'] = my_value_suggested[1]
        st.session_state['hero_gender'] = my_value_suggested[2]
        my_suggestions = MY_SUGGESTIONS['sidekick']
        my_value_suggested = random.choice(my_suggestions)
        st.session_state['friend_firstname'] = my_value_suggested[0]
        st.session_state['friend_lastname'] = my_value_suggested[1]
        st.session_state['friend_gender'] = my_value_suggested[2]
        st.session_state['friend_relationship'] = my_value_suggested[3]
        for my_field in MY_SUGGESTED_FIELDS:
            st.session_state[my_field] =random.choice(MY_SUGGESTIONS[my_field])

    st.subheader('The hero')
    THE_HERO = ['hero_firstname', 'hero_lastname', 'hero_gender', 'hero_adj', 'toy', 'color', 'clothing']
    for my_field in THE_HERO:
        get_info(my_field)

    st.subheader('The villain')
    THE_VILLAIN = ['animal', 'animal_adj_not_size', 'nb_animals']
    for my_field in THE_VILLAIN:
        get_info(my_field)
    st.subheader('The sidekick')

    THE_SIDEKICK = ['friend_firstname', 'friend_lastname', 'friend_gender', 'friend_relationship']
    for my_field in THE_SIDEKICK:
        get_info(my_field)

    st.subheader('Other info')
    THE_OTHER_INFO = ['forest', 'healthy_food', 'unhealthy_food_1', 'unhealthy_food_2','unhealthy_food_3','unhealthy_food_4', 'unhealthy_food_5']
    for my_field in THE_OTHER_INFO:
        get_info(my_field)
