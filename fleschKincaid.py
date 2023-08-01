def fleschKincaid(totWords, totSentences, totSyllables):
    avgWords = totWords / totSentences
    avgSyllables = totSyllables / totWords
    score = 0.39 * avgWords + 11.8 * avgSyllables - 15.59
    score = round(score, 4)
    return score

def wordCount(docString):
    spaces = docString.count(" ")
    if spaces == 0:
        return 1
    else: 
        return spaces

def sentenceCount(docString):
    periods = docString.count(".")
    questionMarks = docString.count("?")
    exclamationMarks = docString.count("!")
    return periods + questionMarks + exclamationMarks

def syllableCount(docString):
    listOfDoc = docString.split(" ")
    syllables = 0
    for x in listOfDoc:
        syllables += syllablesInWord(x.casefold())
    return syllables

def filterString(string):
    if (string.isalpha()):
        return string
    else:
        filtered = string
        punctuation = ['"', '/', "~", "!", "@", "#", "$", "%", "^", "&", "*",\
                       "()", "_", "+","`", "1", "2", "3", "4", "5", "6", "7",\
                       "8", "9", "0", "-", "=", "{", "}", "|", "[", "]", ";",\
                       "'", ":", ",", ".", "<", ">", "?"]
        for x in filtered:
            if x in punctuation:
                filtered = filtered.replace(x, "")
        return filtered

def syllablesInWord(unfiltered):
    string = filterString(unfiltered)
    syllables = 0;
    vowels = ['a', 'e', 'i', 'o', 'u']
    if (len(string) == 0):
        return 0
    else:
        if (string[0] in vowels):
            syllables = 1;
        for x in range(1, len(string)):
            # get rid of diphthongs and triphthongs
            # WARNING: could get rid of some instances
            # that are not diphthongs and triphthongs
            if string[x - 1] not in vowels and string[x] in vowels:
                syllables += 1
        if string.endswith('e'):
            # get rid of common silent vowels
            syllables -= 1
        if (len(string) >= 3):
            if (string.endswith('le') and string[-3] not in vowels):
                # adds back some miscounted syllables
                # ex. saddle, triple, etc.
                syllables += 1
            if (string.find('y') != -1):
                syllables += yAsVowelOccurrences(string, 0)
        if syllables == 0:
            syllables = 1
        return syllables

def yAsVowelOccurrences(string, num):
    occurrences = num
    vowels = ['a', 'e', 'i', 'o', 'u']
    if string.rfind('y') == -1:
        return occurrences
    else:
        index = string.rfind('y')
        subString = string[0: index]
        if (index == len(string) - 1):
            occurrences += 1
        else:
            if (string[index - 1] not in vowels
                and string[index + 1] not in vowels):
                occurrences += 1
        return yAsVowelOccurrences(subString, occurrences)

def fileToScore(filepath):
    data = open(filepath)
    docString = data.read()
    totWords = wordCount(docString)
    totSentences = sentenceCount(docString)
    totSyllables = syllableCount(docString)
    return str(fleschKincaid(totWords, totSentences, totSyllables))

def main():
    from tkinter import Tk     # from tkinter import Tk for Python 3.x
    from tkinter.filedialog import askopenfilename
    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
    return "The Flesch Kincaid grade level score of the file you selected is " \
           + fileToScore(filename)
