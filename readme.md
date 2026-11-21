This is a project to understand how [Markov Chain](https://en.wikipedia.org/wiki/Markov_chain) works, and how it can be used to create a word or phrase with convincing pattern.

# How to use
Tweak the constants in [generateDist.py](./generateDist.py) and run it. Then use the `RandomWordGenerator` class in [makeAWord.py](./makeAWord.py) to generate the word based on the given Markov Chain (represented as `.json` file).

# Text Credits
| Text File | Source |
| --- | --- |
| [countries.txt](./texts/countries.txt) | https://gist.github.com/dariusz-wozniak/656f2f9070b4205c5009716f05c94067#file-list-of-countries-txt |
| [first-names.txt](./texts/first-names.txt) | https://github.com/dominictarr/random-name/blob/master/first-names.txt |
| [last-names.txt](./texts/last-names.txt) | https://gist.github.com/craigmartin97/e98a9e2a267c379e47be1191d9431de2 |
| [nama.txt](./texts/nama.txt) | https://gist.github.com/maulvi/e443e22b82a1dc24e14344b47f0a80ea |
| [popular.txt](./texts/popular.txt) & [unix-words.txt](./texts/unix-words.txt) | https://github.com/dolph/dictionary |

[sample.txt](./texts/sample.txt) is sampled from [popular.txt](./texts/popular.txt)