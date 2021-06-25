import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

class EdaPlots():
    def init(self,df=None):
        self.df_ = df
        self.bar_plots_ = {}
        self.geo_plots_ = {}
        pass
    def clean (self):
        
        # Fill NaN values
        self.df_['funder'].fillna(value='other',inplace =True)
        self.df_['installer'].fillna(value='other',inplace=True)
        self.df_['subvillage'].fillna(value='none',inplace=True)
        self.df_['public_meeting'].fillna(value=False,inplace=True)
        self.df_['scheme_management'].fillna(value='None',inplace=True)
        self.df_['scheme_name'].fillna(value='None',inplace=True)
        
        # Convert the date items to date-time type
        self.df_['date_recorded'] = pd.to_datetime(self.df_['date_recorded'])
        
        # Drop all geographic outliers
        self.df_ = self.df_[(self.df_['longitude'] != 0)]
        
        
        # Create a Age feature binned by 5 years
        self.df_['age_at_recording'] = pd.DatetimeIndex(self.df_['date_recorded']).year - self.df_['construction_year']
        self.df_.loc[self.df_['age_at_recording'] > 53,'age_at_recording'] = 0
        self.df_.loc[self.df_['age_at_recording'] < 0,'age_at_recording'] = 0
        a = list(range(1,60,5))
        cut_bins = [-1]
        cut_bins.extend(a)
        cut_labels = ['missing','0-5','6-10','11-15','16-20','21-25','26-30','31-35','36-40','41-45','46-50','51-55']
        self.df_.loc[:, 'age_at_recording_bin'] = pd.cut(self.df_['age_at_recording'], bins = cut_bins, labels = cut_labels)
        
        
        # Find top 10 categories for categorical features w/ more than 50 classes and assign 'other' to the rest
        cat = self.df_.select_dtypes('object')
        cols = cat.columns
        self.df_[cols] = self.df_[cols].where(self.df_[cols].apply(lambda x: x.map(x.value_counts())) >= 50, 'other')
        
        # Dropping unnecessary columns
        self.df_.drop(['date_recorded','construction_year','age_at_recording','id'],axis=1,inplace=True)
        
        # Convert the boolian columsn to string 
        self.df_['permit'] = self.df_['permit'].astype(str)
        self.df_['public_meeting'] = self.df_['public_meeting'].astype(str)

        pass