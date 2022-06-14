import pandas as pd
log = pd.read_csv("log_file.txt")
data=pd.DataFrame(log)
print(data)
log.to_csv("Logfile.csv",index=False,sep=",")