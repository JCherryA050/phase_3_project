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
        pass
        
        
    def create_barplots(self):
            
            functional_cats = self.df_[(self.df_['status_group'] == 'functional') & (self.df_['water_quality'] != 'other')].select_dtypes('object')
            not_functional_cats = self.df_[(self.df_['status_group'] == 'non functional') & (self.df_['water_quality'] != 'other')].select_dtypes('object')
            functional_needs_repair_cats = self.df_[(self.df_['status_group'] == 'functional needs repair') & 
                                              (self.df_['water_quality'] != 'other')].select_dtypes('object')
            
            for col in functional_cats.columns:
                
                # Instantiate the bar plots for EDA
                fig,ax = plt.subplots(figsize=(15,8));
                width = 0.3
                
                
                # TAKE COLUMN THAT ISN"T THE COLUMN IN QUESTION
                n = len(functional_cats.groupby(col).count()['status_group'].index)
                r = np.arange(n)
                
                # MAKE SURE THAT ALL X,Y PAIRS HAS EQUAL AMOUNT OF LABELS
                x_func = functional_cats.groupby(col).count()['status_group'].index
                y_func = functional_cats.groupby(col).count()['status_group'].values
                x_func_rep = functional_needs_repair_cats.groupby(col).count()['status_group'].index
                y_func_rep = functional_needs_repair_cats.groupby(col).count()['status_group'].values
                x_not_func = not_functional_cats.groupby('water_quality').count()['status_group'].index
                y_not_func = not_functional_cats.groupby('water_quality').count()['status_group'].values
                
                ax.bar(r,y_func,width=width,align='edge')
                ax.bar(r-width,y_func_rep,width=width,align='edge')
                ax.bar(r+width,y_not_func,width=width,align='edge')
                plt.xticks(r + width/2,list(functional_cats.groupby(col).count()['status_group'].index))
                ax.set_title('Water Quality vs. Water Point Function')
                ax.set_xlabel('Water Quality')
                ax.set_ylabel('Number of Water Points')
                ax.legend(['functional','non functional','functional needs repair'])
                plt.tight_layout()
                
                fig.savefig('images/{}.png'.format(col));
                self.bar_plots_[col] = (fig,ax)
                
                
                
            pass