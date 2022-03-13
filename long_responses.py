import random

R_EATING = 'I don\'t know how to eat, because i\'m a bot.'

def unknown():
    response = ['Could you please rephrase that?',
    '...',
    'I\'m sorry, I don\'t understand.',
    'I\'m afraid I don\'t understand.',
    'I\'m afraid I don\'t understand. Could you rephrase that?',
    'What does that mean?'][random.randrange(6)]
    return response