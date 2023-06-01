# telkomsel-MLE-technical-test
This is a dedicated repository for technical test for Machine Learning Engineer at telkomsel



## Launching the app
As github is not able to hold the model, the model can be reproduced using "Problem-1-Image Classification.ipynb"


### On-Demand classification

Please make sure that you already install streamlit on your python environment.

```
pip install streamlit
```

Once it's installed you can launch the app by firstly open the terminal and go to the direction of the copy of this repo.
Then you can launch the app using this command:
```
streamlit run deployment.py
```

### Batch based classification

Open and execute in the terminal. The default directory is using test dataset from kaggle.

```
python predictBatches.py
```
