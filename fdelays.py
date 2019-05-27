#!/usr/bin/env python3
import pandas as pd
df= pd.read_csv("flightdelays.csv.1")
print(df[(df["Origin"]=="SFO")]["ArrDelay"].head(3))
print(df["Dest"].value_counts().head(3))
print("Simardeep")
