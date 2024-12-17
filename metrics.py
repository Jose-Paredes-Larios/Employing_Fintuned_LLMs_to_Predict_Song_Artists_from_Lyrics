import pandas as pd
from sklearn.metrics import precision_recall_fscore_support

def calculate_metrics(fPath, trueLabels, predicted):
    df = pd.read_csv(fPath, sep="\t")
    true = df[trueLabels].astype(str)
    pred = df[predicted].astype(str)

    precision, recall, f1, _ = precision_recall_fscore_support(true, pred, average="macro")
    print("Overall Metrics:")
    print("     Precision: ")
    print("     "+str(round(precision,3)))
    print("     Recall: ")
    print("     "+str(round(recall,3)))
    print("     F-1 Score: ")
    print("     "+str(round(f1,3))+"\n")

    print("Per-Artist Metrics:")
    labels = sorted(df[trueLabels].unique())
    artistMetrics = precision_recall_fscore_support(true, pred, labels=labels, average=None)
    for i, label in enumerate(labels):
        print("  Artist: "+label)
        print("    Precision: ")
        print("    "+str(round(artistMetrics[0][i],3)))
        print("    Recall: ")
        print("    "+str(round(artistMetrics[1][i],3)))
        print("    F1-Score: ")
        print("    "+str(round(artistMetrics[2][i],3))+"\n")

file_path = "/Users/joseparedes/Desktop/finalPredictions/ensemble1960.txt"
calculate_metrics(file_path, "actual", "predicted")
