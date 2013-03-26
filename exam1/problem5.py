story = 'The ravenous zombies started attacking yesterday'
listOfAdjs = ['ravenous']
listOfNouns = ['zombies', 'humans', 'yesterday']
listOfVerbs = ['attacking', 'attacks']

madForm = 'The [ADJ] [NOUN] started [VERB] [NOUN]'

def generateForm(story, listOfAdjs, listOfNouns, listOfVerbs):
    """ 
    story: a string containing sentences
    listOfAdjs: a list of valid adjectives
    listOfNouns: a list of valid nouns
    listOfVerbs: a list of valid verbs
    
    For each word in story that is in one of the lists,
    * replace it with the string '[ADJ]' if the word is in listOfAdjs
    * replace it with the string '[VERB]' if the word is in listOfVerbs
    * replace it with the string '[NOUN]' if the word is in listOfNouns
    
    returns: string, A Mad-Libs form of the story. 
    """

    wordlist = story.rsplit(' ')

    #determine type of word
    def wordType(word):
        if word in listOfAdjs:
            return '[ADJ]'
        elif word in listOfNouns:
            return '[NOUN]'
        elif word in listOfVerbs:
            return '[VERB]'
        else:
            return None

    new_story = ''
    for word in wordlist:
        if wordType(word) != None:
            new_story += wordType(word) + ' '
        else:
            new_story += word + ' '

    return new_story[:-1]

def generateTemplates(madLibsForm):
    """ 
    madLibsForm: string, in a Mad-Lib form. See output of `generateForm`

    returns: a list of '[ADJ]', '[VERB]', and '[NOUN]' strings, in
    the order they appear in the madLibsForm.
    """
    
    template_list = []
    string = madLibsForm

    while string.find('[') != -1:
        start = string.find('[')
        end = string.find(']')
        template_list += [string[start:end + 1]]
        string = string[end + 1:]

    return template_list

def verifyWord(userWord, madTemplate, listOfAdjs, listOfNouns, listOfVerbs):
    """ 
    userWord: a string, the word the user inputted
    madTemplate: string, the type of word the user was supposed to input
    listOfAdjs: a list of valid adjectives
    listOfNouns: a list of valid nouns
    listOfVerbs: a list of valid verbs):

    returns: Boolean, whether or not the word is valid
    """
    templates_d = {'[ADJ]': listOfAdjs,
                   '[NOUN]': listOfNouns,
                   '[VERB]': listOfVerbs}

    return userWord in templates_d[madTemplate]

print verifyWord('bullshit', '[ADJ]', listOfAdjs, listOfNouns, listOfVerbs)
