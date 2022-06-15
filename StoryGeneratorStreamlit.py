

# TO CORRECT
# BUGs: selectbox (when 0), ...
# avoid to have twice an unhealthy food
# suggest & memorize hero & hero friend
# suggest friend relationship with linked to sex
# suggest for all fields
# use streamlit form insted of my repetitions
# use different files (for the data, for the functions...) to clarify the code
# do copies with git
# do the fairytale generation
# push to Streamlit Cloud
# do the other generations (cf. the website story-generator)
# add variety in hero's trip (based on characteristics of hero & villain + on chance + on state evolution of hero/villain and on intent)


import streamlit as st
import random
import copy

MY_SUGGESTIONS = dict()
# 0 = male; 1 = female
MY_SUGGESTIONS['hero'] = [('Sam', 'Gump', 0),
                       ('Bob','Doop', 0),
                       ('Jody','Gloop', 1),
                       ('Robin','Snozcumber', 1),
                       ('Mike', 'Giantbulb', 0),
                       ('Alex','Slaughterhouse', 0),
                       ('Lee','Lakeman', 0),
                       ('Chloe', 'Bogtrotter', 1),
                       ('Catherine','Ramsbottom', 1),
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
MY_SUGGESTIONS['nb_animals'] = (1,2,3,4,5)

MY_IDs = ['hero_firstname', 'hero_lastname', 'hero_gender', 'hero_adj',
          'animal', 'animal_adj_not_size', 'nb_animals', 'friend_firstname', 'friend_lastname', 'friend_gender', 'friend_relationship',
          'forest', 'toy', 'color', 'clothing',
          'healthy_food', 'unhealthy_food_1', 'unhealthy_food_2', 'unhealthy_food_3', 'unhealthy_food_4', 'unhealthy_food_5']

MY_DESCRIPTIONS = { 'hero_firstname' : '',
                    'hero_lastname' : '',
                    'hero_gender' : '',
                    'hero_adj' : 'An adjective to describe your hero (e.g. little, brave)',
                    'animal' : 'A type of animal (e.g. bear, pig)',
                    'animal_adj_not_size' : "An adjective (not relating to size) describing the animal(s) (e.g. hairy, scary)",
                    'nb_animals' : 'How many of the animals above will be in the story',
                    'friend_firstname' : '',
                    'friend_lastname' : '',
                    'friend_gender' : '',
                    'friend_relationship' : '',
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



# Create a fairy tale
# https://www.plot-generator.org.uk/fairytale/

# FULL WIDTH
# st.set_page_config(layout="wide")

# *******************************
# personalized style
# button
m = st.markdown("""
    <style>
    div.stButton > button:first-child {
        background-color: rgb(200, 200, 200);
    }
    </style>""", unsafe_allow_html=True)
# *******************************

my_columns = dict() # USED FOR SELECTBOX & PEOPLE
MY_VALUES = dict()

for my_id in MY_IDs:
    if my_id not in st.session_state:
        st.session_state[my_id] = ''
    MY_VALUES[my_id] = st.session_state[my_id]

def get_or_suggest_a_piece_of_information(my_id):
    # my_id = str of a number e.g. "5"
    my_value = MY_VALUES[my_id]
    my_suggestions = MY_SUGGESTIONS[my_id]
    my_description = MY_DESCRIPTIONS[my_id]
    my_id_key = my_id + '_key'
    col_1, col_2 = st.columns([1,1])
    with col_1:
        placeholder = st.empty()
        my_value = placeholder.text_input(my_description, value=my_value, key=my_id_key)
        st.session_state[my_id] = my_value
    with col_2:
        st.write('')
        st.write('')
        click_suggest = st.button('Suggest', key=my_id_key)
        if click_suggest:
            #my_value = random.choice(my_suggestions)
            #placeholder.text_input(my_description, value=my_value)
            #st.session_state[my_id] = my_value
            st.session_state[my_id] = random.choice(my_suggestions)

def get_or_suggest_a_person(my_id, my_description):
    # my_id = str of a number e.g. "5"
    my_suggestions = MY_SUGGESTIONS['hero']
    my_value_firstname = MY_VALUES['hero_firstname']
    my_value_lastname = MY_VALUES['hero_lastname']
    my_value_gender = MY_VALUES['hero_gender']
    st.write(my_description)
    placeholder_firstname = st.empty()
    placeholder_lastname = st.empty()
    placeholder_gender = st.empty()
    my_value_firstname = placeholder_firstname.text_input('First name', value=my_value_firstname, key='hero_firstname_key')
    my_value_lastname = placeholder_lastname.text_input('Last name', value=my_value_lastname, key='hero_lastname_key')
    #my_value_gender = placeholder_gender.radio('Gender', ('male', 'female'), index=my_value_gender, key="hero_sex_key")
    st.write(my_value_gender)
    click_suggest = st.button('Suggest', key='my_id')
    if click_suggest:
        my_value_suggested = random.choice(my_suggestions)
        my_value_firstname = my_value_suggested[0]
        my_value_lastname = my_value_suggested[1]
        my_value_gender = my_value_suggested[2]
        #placeholder_firstname.text_input('First name', value=my_value_firstname)
        placeholder_lastname.text_input('Last name', value=my_value_lastname)
        placeholder_gender.radio('Gender', ('male', 'female'), index= my_value_gender)
    st.session_state['hero_firstname'] = my_value_firstname
    st.session_state['hero_lastname'] = my_value_lastname
    st.session_state['hero_gender'] = my_value_gender

def get_or_suggest_selectbox(my_id):
    # my_id = str of a number e.g. "5"
    my_value = MY_VALUES[my_id]
    my_suggestions = MY_SUGGESTIONS[my_id]
    my_description = MY_DESCRIPTIONS[my_id]
    my_id_key = my_id + '_key'
    col_1, col_2 = st.columns([1,1])
    with col_1:
        placeholder = st.empty()
        placeholder.selectbox(my_description, my_suggestions, key=my_id_key)
    with col_2:
        st.write('')
        st.write('')
        click_suggest = st.button('Suggest', key=my_id_key)
        if click_suggest:
            my_value = random.choice(my_suggestions) - 1 # minus one since selectbox index starts from 0
            placeholder.selectbox(my_description, options=my_suggestions, index=my_value, key=my_id_key)
            st.session_state[my_id] = my_value


# *******************************
# TITLES & UPPER PART
st.title('Story Generator - Fairytale')
'Please keep your input family friendly.'

# RANDOM FILL
st.subheader('Need a prompt? Go random! ')
if st.button('Fill entire form with random ideas'):
    'FillAll function'
else:
    'Fill the form yourself'


# *******************************
# FORM
st.header('Fill in the form.')

# HERO
st.subheader("The hero (a child)")

# TODO
get_or_suggest_a_person('hero', '')
# FIN TODO

get_or_suggest_a_piece_of_information('hero_adj')
get_or_suggest_a_piece_of_information('toy')

# VILLAIN (animals)
st.subheader("The villain")
get_or_suggest_a_piece_of_information('animal')
get_or_suggest_selectbox ('nb_animals')
get_or_suggest_a_piece_of_information('animal_adj_not_size')

# ADDITIONAL INFORMATION
st.subheader("Additional information")
# TODO
#get_or_suggest_a_person('6', 'A friend or family member of the hero')
#get_or_suggest_a_piece_of_information('7', 'His or her relationship to the hero')
# FIN TODO
get_or_suggest_a_piece_of_information('forest')
get_or_suggest_a_piece_of_information('color')
get_or_suggest_a_piece_of_information('clothing')
get_or_suggest_a_piece_of_information('healthy_food')
"Five unhealthy foods, plural (e.g. biscuits, crisps)"
get_or_suggest_a_piece_of_information('unhealthy_food_1')
get_or_suggest_a_piece_of_information('unhealthy_food_2')
get_or_suggest_a_piece_of_information('unhealthy_food_3')
get_or_suggest_a_piece_of_information('unhealthy_food_4')
get_or_suggest_a_piece_of_information('unhealthy_food_5')

for key in st.session_state:
    if 'key' not in key and st.session_state[key]:
        st.write(key, ':', st.session_state[key])
