# CS361PartnerMicroservice

This microservice program will implement a function that can be imported into the main program. The microservice program will contain 3 lists of words: nouns, verbs, and adjectives, as well as a function that can be called in the main program. What the program gives is a strings of words in JSON format. 

Requesting data:
Call the function in the main program with the respective parameters. 

Request parameters:
giveWords(n, v, a)
  where n is the number of nouns you want, v is the number of verbs you want, and a is the number of adjectives you want

For example:
giveWords(2, 3, 5) will give you a JSON-formatted string separated by category. 

Receiving data: 
Import the file and use it in a manner similar to this:
main_output = giveWords(2, 3, 5)

UML:

![UML](https://github.com/sanen03/CS361PartnerMicroservice/blob/main/UML.png)
