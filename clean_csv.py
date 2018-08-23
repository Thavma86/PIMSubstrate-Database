import pandas as pd
headers = ["Subject","Subject_type","Object","Object_type"]
df = pd.read_csv('cider_db_remove_empty_cells.csv', names=headers, encoding = "ISO-8859-1")
#df=df.replace('\?','_',regex=True).astype(float)
df['Subject']=df['Subject'].str.replace("?","_")
df['Object']=df['Object'].str.replace("?","_")
df.to_csv('clean_interactions.csv')
