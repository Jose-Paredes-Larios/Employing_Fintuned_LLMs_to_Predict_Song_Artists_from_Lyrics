Step 0: Selecting a Dataset

- The Songs Across Numerous Genres and Generations (SANGG) comes in different sizes: standard and mini. The standard size train, validation, and test sets are simply called SANGG{settype}.tsv and include all lyrics from the 27 artists. The mini datasets only include lyrics from artists of a given epoch, totaling 9 artist per miniset.

- Selecting the dataset to use depends on the experiment. However, it should be noted that training models with the standard dataset is tremendously memory intensive and is only feasible on powerful GPUs. The minisets are solid alternatives for those who do not have access to such GPUs. 

- Each set tags lyrics with numbers. These numbers map to artists in the following ways:
	Standard Set:
		 0: Miley Cyrus
		 1: Taylor Swift
		 2: Demi Lovato
		 3: Mariah Carey
		 4: Christina Aguilera
		 5: Britney Spears
		 6: Aretha Franklin
		 7: Etta James
		 8: Nancy Sinatra
		 9: Elvis Presley
		 10: Chuck Berry
		 11: The Beatles
		 12: Green Day
		 13: Pearl Jam
		 14: Blink-182
		 15: Coldplay
		 16: Imagine Dragons
		 17: Foo Fighters
		 18: Johnny Cash
		 19: Dolly Parton
		 20: Glen Campbell
		 21: Shania Twain
		 22: Garth Brooks
		 23: Dixie Chicks
		 24: Carrie Underwood
		 25: Jason Aldean
		 26: Miranda Lambert

	Miniset 2010:
		0: Miley Cyrus
		1: Taylor Swift
		2: Demi Lovato
		3: Coldplay
		4: Imagine Dragons
		5: Foo Fighters
		6: Carrie Underwood
		7: Jason Aldean
		8: Miranda Lambert

	Miniset 1990:
		0: Mariah Carey
		1: Christina Aguilera
		2: Britney Spears
		3: Green Day
		4: Pearl Jam
		5: Blink-182
		6: Shania Twain
		7: Garth Brooks
		8: Dixie Chicks

	Miniset 1960: 
		0: Aretha Franklin
		1: Etta James
		2: Nancy Sinatra
		3: Elvis Presley
		4: Chuck Berry
		5: The Beatles
		6: Johnny Cash
		7: Dolly Parton
		8: Glen Campbell

Step 1: Training the Models

- You will produce X classifiers for each of the models you are evaluating. To do so, you must leverage NLPScholar and run a TextClassification experiment on train mode. There is a sample train config file provided (finalTrain.yaml) that can be closely followed. Use one of the sets from step 0. All you must do is update the directories and labels in the config file. Here is some more detail on the components of the config file:
	- trainfpath: the address of where the train set is stored
	- validfpath: the address of where the validation set is stored
	- modelfpath: where the classifier will be stored. This address will be used in the following step to evaluate it. 

Step 2: Evaluate the Models

- A sample config file has been provided (finalEval.yaml) to evaluate the models. As such, all you have to do is update the directories and labels in the config file. Here is some more detail on the components of the config file:

	- datafpath: the address of where the test set is stored.
	- predfpath: the name of the output and where it will be stored
	- id2label: allows us to link numbers with artists (e.g. 0 corresponds to Taylor Swift)

- Each classifier will output a file containing its predicted artist for a given song. To obtain an ensemble prediction, take the predicted columns of each classifier and place it in a new TSV. From there, the ensemble prediction is simply the majority predicted artists. A script will eventually be released to automate this process.

Step 3: Analyze the Results

- With the ensemble predictions, a confusion matrix can be generated following this link: https://www.nyckel.com/blog/confusion-matrix/. 

- To obtain overall and per artist precision, recall, and f1 scores from the ensemble predictions, use the provided metrics.py script by directing it to the TSV file containing the predicitons. 

- Celebrate your results, and keep up the good work NLPScholar. 
