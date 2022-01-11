ANALYSIS OF PART OF SPEECH TAGS IN LANGUAGE IDENTIFICATION OF CODE MIXED TEXT :

This project was made as a part of my Minor & Major Assignments during my course in B.Tech (Computer Science) in Jamia Millia Islamia University, New Delhi.
A research paper has also been published on it. Link - https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3462976

AIM - The project determines the language of the words given in a sentence. The sentence can be either in English, Hindi or Hinglish (that is Hindi
written in English script).

APPROACH - 
Firstly, we trained the models to identify Enlish words based on a data set where X was (Word, POS) and Y was English.
Secondly, we trained the models to identify Hindi words. We first trans-literated Hindi words (written in Hindi script) to English words and then obtained the final data set where X was (Words, POS (as in Hindi script)) and Y was Hindi.

TEACHNOLOGIES USED - 
NLTK library and Pandas in Python
