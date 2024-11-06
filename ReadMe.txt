Step 0: Generating the Data Sets

- Before we begin anything involving the models, we must first create datasets to train and evaluate the models. While searching for datasets to refine, we noticed that none provided the information. We were looking for. Thus, we will have to create the data sets from scratch. To do so, we have to webscrape https://github.com/johnwmillr/LyricsGenius and collect a list of songs and label them with their associated artist. 

- Note that you should map artists to numbers and label the songs with numbers. For example, we would tag song X with a 0, which corresponds to artist Y. 

- The result of web scraping is a large data set with thousands of songs. We must now split this data into train, validate, and test sets. We recommend doing an 80%, 10%, 10% split.

Step 1: Training the Models

- We will produce X classifiers for each of the models we are evaluating. To do so, we leverage NLPScholar and run a TextClassification experiment on train mode. There is a sample train config file provided that can be closely followed. Use the sets generated in step 0; a sample train and validate set has been provided. Thus, all we must do is update the directories in the config file. Here is some more detail on the components of the config file:
	- trainfpath: the address of where the train set is stored
	- validfpath: the address of where the validation set is stored
	- modelfpath: where the classifier will be stored. This address will be used in the following step to evaluate it. 

Step 2: Evaluate the Models

- Here we will use NLPScholar and run a TextClassification experiment on evaluate mode. A sample config file and test data set has been provided. As such, all we have to do is update the directories in the config file. Here is some more detail on the components of the config file:

	- datafpath: the address of where the test set is stored.
	- predfpath: the name of the output and where it will be stored
	- id2label: allows us to link numbers with artists (e.g. 0 corresponds to Taylor Swift). To add more artists the model can label lyrics with, add more number artist pairs.

- Because we have to evaluate each classifier for every model, we are going to be running lots of evaluations, which can be onerous. Thus, enumerate your outputs for classifier starting from 1 to n (do this in predfpath). In other words, follow a similar naming scheme: robertaOuput1, robertaOutput2, ...., robertaOutputn. Following this naming convention will allow you to run MCC.py and Ensemble.py, which will quickly calculate MCC and ensemble for us, respectively. 

- There is a provided file call expressEval.py that will produce X classifiers for you in one go that follow the ideal naming convention. Using this file is recommended, for you won't have to continuously run your eval file; you are free to do something else while all classifiers for a model are evaluated. Run this file in your NLPScholar directory. Lastly, make sure to alter the directories in the generate_config_file() function in expressEval.

Step 3: Analyze the Results

- We should now have MCC and ensemble values to work with. To be more specific, each classifier will have an associated MCC value and each model will have an overall MCC (you can use Excel to calculate this) and ensemble value. 

- Use Excel to plot these values and create a bar graph that will help us visualize the data. 