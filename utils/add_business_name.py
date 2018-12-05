import pandas as pd

# load reviews CSV file
df = pd.read_csv("yelp_academic_dataset_review_mini.csv", index_col=0)
df['business_name'] = 'business_name'

# load business JSON file
business_df = pd.read_json("yelp_academic_dataset_business.json", lines=True)

# this will store business names
business_name_array = []
# this will store category
business_type_array = []

# we will only extract the following categories. All else will be called "Other"
searchStr1 = "Mexican"
searchStr2 = "Italian"
searchStr3 = "Indian"
searchStr4 = "Chinese"
searchStr5 = "Thai"
searchStr6 = "Korean"
searchStr7 = "Japanese"

# Loop through each row in CSV
for index, row in df.iterrows():
	business_id = row['business_id']
	# find the corresponding business ID in JSON file
	business_found = business_df.loc[business_df['business_id'] == business_id]
	# extract business name and store in array
	business_name = str(business_found.name.item())
	business_name_array.append(business_name)

	# extract business category, search string for cuisine and set all to "Other" if no match	
	business_type = str(business_found.categories)
	if business_type.find(searchStr1) >=0:
		business_type = searchStr1
	elif business_type.find(searchStr2) >= 0 :	
		business_type = searchStr2
	elif business_type.find(searchStr3) >= 0:	
		business_type = searchStr3
	elif business_type.find(searchStr4) >= 0:	
		business_type = searchStr4
	elif business_type.find(searchStr5) >= 0:	
		business_type = searchStr5
	elif business_type.find(searchStr6) >= 0:	
		business_type = searchStr6
	elif business_type.find(searchStr7) >= 0:	
		business_type = searchStr7						
	else :
		business_type = "Other"
	# add to array 
	business_type_array.append(business_type)


# copy array to new columns in CSV
df['business_name']=business_name_array
df['business_type']=business_type_array

# save file
df.to_csv('yelp_with_business.csv')


