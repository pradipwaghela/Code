from pathlib import Path
import pandas as pd
log=Path('log_file.txt').read_text()
print(log)
log[10]
countriesStr.to_csv("logfile1.csv",index=False,sep=" ")