# CS361PartnerMicroservice

This microservice program will implement a function that can be imported into the main program. The microservice program will contain 3 lists of words: nouns, verbs, and adjectives, as well as a function that can be called in the main program. What the program gives is a strings of words in JSON format. 

Requesting data:
Run the program. It runs in its own process, and will ask you inputs for how many nouns, verbs, and adjectives you want.

Request parameters:
Enter a positive integer respective to the word type you want when prompted.

For example:
How many nouns do you want? 2
How many verbs do you want? 3
How many adjectives do you want? 4

Receiving data: 
It will write the JSON object to a file called output.txt

UML:

![UML](https://github.com/sanen03/CS361PartnerMicroservice/blob/main/UML.png)
