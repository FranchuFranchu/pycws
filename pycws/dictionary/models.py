from django.db import models
from languages.models import Language
from users.models import User

class Dictionary(models.Model):
    language = models.OneToOneField(Language, on_delete=models.CASCADE)
    # word_set = reversed ForeignKey
    # Dictionary fields
    enable_gloss = models.BooleanField(default=False)
    enable_alternate_word = models.BooleanField(default=False)
    enable_class = models.BooleanField(default=False)
    enable_register = models.BooleanField(default=False)
    enable_dialect = models.BooleanField(default=False)
    enable_sampa = models.BooleanField(default=False)
    enable_ipa = models.BooleanField(default=False)
    enable_etymology = models.BooleanField(default=False)
    enable_notes = models.BooleanField(default=False)
    enable_sample = models.BooleanField(default=False)
    enable_image_link = models.BooleanField(default=False)
    # No source language, this is done with etymologies
    # Other settings
    allow_irregular_stems = models.CharField(max_length=4, default='none', choices=[
        ('none', 'Don\'t use these'),
        ('edit', 'Edit word page only'),
        ('both', 'Edit and Add word pages')
    ])
    is_private = models.BooleanField(default=False, choices=[
        (False, 'Public'),
        (True, 'Private')
    ])
    enable_roots = models.BooleanField(default=False, choices=[
        (False, 'No, don\'t'),
        (True, 'Yes, allow it')
    ])
    clear_wordbank = models.CharField(max_length=3, default='yes', choices=[
        ('yes', 'Always'),
        ('no', 'Never'),
        ('ask', 'Ask each time')
    ])
    display_field = models.CharField(max_length=4, default='none', choices=[
        ('hint', 'Hint word'),
        ('note', 'Notes'),
        ('etym', 'Etymology'),
        ('none', 'None')
    ])
    classify_results = models.CharField(max_length=5, default='pos', choices=[
        ('pos', 'Only part of speech'),
        ('class', 'Only class'),
        ('both', 'Part of speech and class')
    ])

class Word(models.Model):
    dictionary = models.ForeignKey(Dictionary, on_delete=models.CASCADE)
    lemma = models.TextField()
    alternative = models.TextField(blank=True)
    gloss = models.TextField(blank=True)
    wordlink = models.ForeignKey('Wordlink', null=True, on_delete=models.SET_NULL)
    PARTS_OF_SPEECH = [
        ('', 'None'),
        ('abbr', 'Abbreviation'),
        ('adj', 'Adjective'),
        ('adp', 'Adposition'),
        ('adv', 'Adverb'),
        ('aff', 'Affix'),
        ('aux', 'Auxiliary'),
        ('conj', 'Conjunction'),
        ('det', 'Determiner'),
        ('intj', 'Interjection'),
        ('noun', 'Noun'),
        ('num', 'Numeral'),
        ('part', 'Particle'),
        ('phrs', 'Phrase'),
        ('prop', 'Proper noun'),
        ('pron', 'Pronoun'),
        ('verb', 'Verb'),
    ]
    pos = models.CharField(max_length=4, default='', choices=PARTS_OF_SPEECH)
    dialects = models.TextField()  # Because we can't know the dialect options
    classes = models.TextField()
    REGISTERS = [
        ('wip', 'wip'),
    ]
    register = models.CharField(max_length=3, default='wip', choices=REGISTERS)
    pronunciation_sampa = models.TextField()
    pronunciation_ipa = models.TextField()
    # No source language, this is done with etymologies
    etymology = models.TextField()
    notes = models.TextField()
    sample = models.TextField()
    image_link = models.URLField()

class Wordlink(models.Model):
    linkname = models.TextField()
    altname = models.TextField(blank=True)
    hint = models.TextField()
    pos = models.CharField(max_length=4, default='', choices=Word.PARTS_OF_SPEECH)  # To be removed
    addedby = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    islocked = models.BooleanField(default=False)
    # word_set = reversed ForeignKey
