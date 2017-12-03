import json
import sys
from sklearn.externals import joblib
import pandas as pd
 
class insurance_predict:

	def __init__(self):
		print('Loading the Forest Classifier.')
		self.classifier = joblib.load('classifier_model.pkl')
		print('Loading the Bronze Regressor.')
		self.regressor_bronze = joblib.load('regressor_model_bronze.pkl')
		print('Loading the Silver Regressor.')
		self.regressor_silver = joblib.load('regressor_model_silver.pkl')
		print('Loading the Gold Regressor.')
		self.regressor_gold = joblib.load('regressor_model_gold.pkl')
		print('Loading the Platinum Regressor.')
		self.regressor_platinum = joblib.load('regressor_model_platinum.pkl')
		print('Model ready for use.')

	def get_data(self,data):
		columns=['ANNUAL_INCOME', 'HEIGHT', 'OPTIONAL_INSURED', 'PEOPLE_COVERED', 'WEIGHT',\
			'Low', 'Medium', 'High' ,'Age' ,'MARITAL_STATUS_M','MARITAL_STATUS_S', 'TOBACCO_No','TOBACCO_Yes',\
			'sex_F', 'sex_M', 'state_Alabama', 'state_Alaska', 'state_Arizona', 'state_Arkansas',\
			'state_California', 'state_Colorado', 'state_Connecticut', 'state_Delaware',\
			'state_District of Columbia', 'state_Florida', 'state_Georgia', 'state_Hawaii', 'state_Idaho',\
			'state_Illinois', 'state_Indiana', 'state_Iowa', 'state_Kansas','state_Kentucky',\
			'state_Louisiana','state_Maine','state_Maryland','state_Massachusetts','state_Michigan',\
			'state_Minnesota', 'state_Mississippi', 'state_Missouri','state_Montana','state_Nebraska',\
			'state_Nevada','state_New Hampshire','state_New Jersey','state_New Mexico','state_New York',\
			'state_North Carolina','state_North Dakota','state_Ohio','state_Oklahoma','state_Oregon',\
			'state_Pennsylvania', 'state_Rhode Island','state_South Carolina','state_South Dakota',\
			'state_Tennessee','state_Texas','state_Utah','state_Vermont','state_Virginia', \
			'state_Washington', 'state_West Virginia', 'state_Wisconsin', 'state_Wyoming']
		append_dict = {
		'ANNUAL_INCOME':data['ANNUAL_INCOME'],
		'HEIGHT':data['HEIGHT'],
		'PEOPLE_COVERED':data['PEOPLE_COVERED'],
		'OPTIONAL_INSURED':data['OPTIONAL_INSURED'],
		'WEIGHT':data['WEIGHT'],
		'Low':data['LOW'],
		'Medium':data['MEDIUM'],
		# 'High':data['HIGH'],
		'Age':data['AGE']
		}
		if data['MARITAL_STATUS'] == 'M':
			append_dict['MARITAL_STATUS_M'] = 1
			append_dict['MARITAL_STATUS_S'] = 0
		else:
			append_dict['MARITAL_STATUS_M'] = 0
			append_dict['MARITAL_STATUS_S'] = 1
		if data['TOBACCO'] == 'Yes':
			append_dict['TOBACCO_Yes'] = 1
			append_dict['TOBACCO_No'] = 0
		else:
			append_dict['TOBACCO_Yes'] = 0
			append_dict['TOBACCO_No'] = 1
		if data['SEX'] == 'M':
			append_dict['sex_M'] = 1
			append_dict['sex_F'] = 0
		else:
			append_dict['sex_M'] = 0
			append_dict['sex_F'] = 1
		state = 'state_' + data['STATE']
		append_dict[state] = 1
		data = [] 
		data.append(append_dict)
		df = pd.DataFrame(data, columns=columns)
		df = df.fillna(0)

		class_plan = self.classifier.predict(df)
		premium_bronze = self.regressor_bronze.predict(df)
		premium_silver = self.regressor_silver.predict(df)
		premium_gold = self.regressor_gold.predict(df)
		premium_platinum = self.regressor_platinum.predict(df)
		return_dict = {
		'CLASS':class_plan[0],
		'BRONZE_PREMIUM':premium_bronze[0],
		'SILVER_PREMIUM':premium_silver[0],
		'GOLD_PREMIUM':premium_gold[0],
		'PLATINUM_PREMIUM':premium_platinum[0]
		}
		return return_dict









