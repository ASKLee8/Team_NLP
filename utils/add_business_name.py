import pandas as pd



df = pd.read_csv("yelp_academic_dataset_review_mini.csv", index_col=0)
#print(df)
#df['new_column'] = 'some_value'
#df.to_csv('yelp_with_business.csv')
df['business_name'] = 'business_name'
#df2 = pd.read_csv("yelp_with_business.csv")
#print(df2)

business_df = pd.read_json("yelp_academic_dataset_business.json", lines=True)
#print(df3.address)

business_name_array = []

for index, row in df.iterrows():
	business_id = row['business_id']
	#print(business_id)
	business_found = business_df.loc[business_df['business_id'] == business_id]
	#if len(business_found) >= 1:
	#	print(business_found.name.item())
	business_name = "-";
	business_name = business_name.join(business_found.name)
	#print('--------')
	#print(business_name)
	#if len(business_name) >= 0:
	#	df.set_value(index, 'business_name', business_name)
	#else:
	#	df.set_value(index, 'business_name', '00900000000000')
	#df['business_name'] = business_name
	business_name_array.append(business_name)
	#print(business_name)
	#print('--------')


#print(business_name_array)

df['business_name']=business_name_array

df.to_csv('yelp_with_business.csv')
df2 = pd.read_csv("yelp_with_business.csv")
print(df2.business_name)



