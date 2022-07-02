import numpy as np
import matplotlib.pyplot  as plt
import seaborn as sns
import pandas as pd
import streamlit as st

def trim_pollutantavg():
    st.write(sns.set_style('darkgrid'))
    air_data=pd.read_csv(r"Air_Quality.csv")
    st.write(air_data.head())
    td_0=air_data
    st.image('polavgboxplot.png')
    #finding the quartiles for avg
    IQR=td_0['pollutant_avg'].quantile(0.75)-td_0['pollutant_avg'].quantile(0.25)
    lower_pollutant_avg_limit=td_0['pollutant_avg'].quantile(0.25)-(IQR*1.5)
    upper_pollutant_avg_limit=td_0['pollutant_avg'].quantile(0.75)+(IQR*1.5)
    st.write('lower_pollutant_avg_limit:',lower_pollutant_avg_limit)
    st.write('upper_pollutant_avg_limit:',upper_pollutant_avg_limit)
    st.write('After removing outlier-')
    st.image('pollutantavgoutlier.png')

def trim_pollutantmin():
    st.write(sns.set_style('darkgrid'))
    air_data=pd.read_csv(r"Air_Quality.csv")
    st.write(air_data.head())
    td_0=air_data
    st.image('polminboxplot.png')
    #finding the quartiles for min
    IQR=td_0['pollutant_min'].quantile(0.75)-td_0['pollutant_min'].quantile(0.25)
    lower_pollutant_min_limit=td_0['pollutant_min'].quantile(0.25)-(IQR*1.5)
    upper_pollutant_min_limit=td_0['pollutant_min'].quantile(0.75)+(IQR*1.5)
    st.write(('lower_pollutant_min_limit:',lower_pollutant_min_limit))
    st.write(('upper_pollutant_min_limit:',upper_pollutant_min_limit))
    st.write('After removing outlier-')
    st.image('pollutantminoutlier.png')

def trim_pollutantmax():
    st.write(sns.set_style('darkgrid'))
    air_data=pd.read_csv(r"Air_Quality.csv")
    st.write(air_data.head())
    td_0=air_data
    st.image('polmaxboxplot.png')
    #finding the quartiles for max
    IQR=td_0['pollutant_max'].quantile(0.75)-td_0['pollutant_max'].quantile(0.25)
    lower_pollutant_max_limit=td_0['pollutant_max'].quantile(0.25)-(IQR*1.5)
    upper_pollutant_max_limit=td_0['pollutant_max'].quantile(0.75)+(IQR*1.5)
    st.write(('lower_pollutant_max_limit:',lower_pollutant_max_limit))
    st.write(('upper_pollutant_max_limit:',upper_pollutant_max_limit))
    st.write('After removing outlier-')
    st.image('pollutantmaxoutlier.png')

def iqr_polavg():
    st.write(sns.set_style('darkgrid'))
    air_data=pd.read_csv(r"Air_Quality.csv")
    st.write(air_data.head())
    td_0=air_data
    st.write('Boxplot-')
    st.image('polavgcap.png')
    st.write('Distplot-')
    st.image('poldistavgcap.png')
    IQR = td_0["pollutant_avg"].quantile (0.75) - td_0["pollutant_avg"].quantile(0.25) 
    lower_pollutant_limit= td_0["pollutant_avg"].quantile (0.25)- (IQR *1.5)
    upper_pollutant_limit = td_0["pollutant_avg"].quantile (0.75) +(IQR *1.5)
    st.write(('lower_pollutant_avg_limit:',lower_pollutant_limit))
    st.write(('upper_pollutant_avg_limit:',upper_pollutant_limit))
    st.write('After removing outlier-')
    st.image('polboxavgaftercap.png')

def iqr_polmin():
    st.write(sns.set_style('darkgrid'))
    air_data=pd.read_csv(r"Air_Quality.csv")
    st.write(air_data.head())
    td_0=air_data
    st.write('Boxplot-')
    st.image('polmincap.png')
    st.write('Distplot-')
    st.image('poldistmincap.png')
    IQR = td_0["pollutant_min"].quantile (0.75) - td_0["pollutant_min"].quantile(0.25) 
    lower_pollutant_min_limit= td_0["pollutant_min"].quantile (0.25)- (IQR *1.5)
    upper_pollutant_min_limit = td_0["pollutant_min"].quantile (0.75) +(IQR *1.5)
    st.write(('lower_pollutant_min_limit:',lower_pollutant_min_limit))
    st.write(('upper_pollutant_min_limit:',upper_pollutant_min_limit))
    st.write('After removing outlier-')
    st.image('polboxminaftercap.png')

def iqr_polmax():
    st.write(sns.set_style('darkgrid'))
    air_data=pd.read_csv(r"Air_Quality.csv")
    st.write(air_data.head())
    td_0=air_data
    st.write('Boxplot-')
    st.image('polmaxcap.png')
    st.write('Distplot-')
    st.image('poldistmaxcap.png')
    IQR = td_0["pollutant_max"].quantile (0.75) - td_0["pollutant_max"].quantile(0.25) 
    lower_pollutant_max_limit= td_0["pollutant_max"].quantile (0.25)- (IQR *1.5)
    upper_pollutant_max_limit = td_0["pollutant_max"].quantile (0.75) +(IQR *1.5)
    st.write(('lower_pollutant_max_limit:',lower_pollutant_max_limit))
    st.write(('upper_pollutant_max_limit:',upper_pollutant_max_limit))
    st.write('After removing outlier-')
    st.image('polboxmaxaftercap.png')

def ms_polavg():
    st.write(sns.set_style('darkgrid'))
    air_data=pd.read_csv(r"Air_Quality.csv")
    st.write(air_data.head())
    td_0=air_data
    lower_pollutant_avg_limit= td_0["pollutant_avg"].mean()-(3 *td_0["pollutant_avg"].std()) 
    upper_pollutant_avg_limit= td_0["pollutant_avg"].mean() + (3 *td_0["pollutant_avg"].std())
    st.write(('lower_pollutant_avg_limit:',lower_pollutant_avg_limit))
    st.write(('upper_pollutant_avg_limit:',upper_pollutant_avg_limit))
    st.write('After replacing the outlier values by the upper and lower limits.')
    st.image('omspavg.png')

def ms_polmin():
    st.write(sns.set_style('darkgrid'))
    air_data=pd.read_csv(r"Air_Quality.csv")
    st.write(air_data.head())
    td_0=air_data
    lower_pollutant_min_limit= td_0["pollutant_min"].mean()-(3 *td_0["pollutant_min"].std()) 
    upper_pollutant_min_limit= td_0["pollutant_min"].mean() + (3 *td_0["pollutant_min"].std())
    st.write(('lower_pollutant_min_limit:',lower_pollutant_min_limit))
    st.write(('upper_pollutant_min_limit:',upper_pollutant_min_limit))
    st.write('After replacing the outlier values by the upper and lower limits.')
    st.image('omspmin.png')

def ms_polmax():
    st.write(sns.set_style('darkgrid'))
    air_data=pd.read_csv(r"Air_Quality.csv")
    st.write(air_data.head())
    td_0=air_data
    lower_pollutant_max_limit= td_0["pollutant_max"].mean()-(3 *td_0["pollutant_max"].std()) 
    upper_pollutant_max_limit= td_0["pollutant_max"].mean() + (3 *td_0["pollutant_max"].std())
    st.write(('lower_pollutant_max_limit:',lower_pollutant_max_limit))
    st.write(('upper_pollutant_max_limit:',upper_pollutant_max_limit))
    st.write('After replacing the outlier values by the upper and lower limits.')
    st.image('omsmax.png')

def quantile_polavg():
    st.write(sns.set_style('darkgrid'))
    air_data=pd.read_csv(r"Air_Quality.csv")
    st.write(air_data.head())
    td_0=air_data
    st.write('Boxplot-')
    st.image('oqpavg.png')
    # setting 0.05 as the Lower Limit and 0.95 as the upper Limit for the quantiles to find the outliers
    lower_pollutant_avg_limit= td_0["pollutant_avg"].quantile (0.05) 
    upper_pollutant_avg_limit = td_0["pollutant_avg"].quantile (0.95)
    st.write(('lower_pollutant_avg_limit:',lower_pollutant_avg_limit))
    st.write(('upper_pollutant_avg_limit:',upper_pollutant_avg_limit))
    # The output shows that anything beyond 3.0 is an outlier, and similarly, the fare value below 157.0 is also an outiter.
    # Now replace the outlier values by the upper and Lower Limit.
    td_0["pollutant_avg"]= np.where(td_0["pollutant_avg"]> upper_pollutant_avg_limit, upper_pollutant_avg_limit, np.where(td_0["pollutant_avg"] < lower_pollutant_avg_limit, lower_pollutant_avg_limit, td_0["pollutant_avg"]))
    st.write(td_0.pollutant_avg[1:40])
    st.image('oqpafteravg.png')

def quantile_polmin():
    st.write(sns.set_style('darkgrid'))
    air_data=pd.read_csv(r"Air_Quality.csv")
    st.write(air_data.head())
    td_0=air_data
    st.write('Boxplot-')
    st.image('oqpmin.png')
    # setting 0.05 as the Lower Limit and 0.95 as the upper Limit for the quantiles to find the outliers
    lower_pollutant_min_limit= td_0["pollutant_min"].quantile (0.05) 
    upper_pollutant_min_limit = td_0["pollutant_min"].quantile (0.95)
    st.write(('lower_pollutant_min_limit:',lower_pollutant_min_limit))
    st.write(('upper_pollutant_min_limit:',upper_pollutant_min_limit))
    # The output shows that anything beyond 3.0 is an outlier, and similarly, the fare value below 157.0 is also an outiter.
    # Now replace the outlier values by the upper and Lower Limit.
    td_0["pollutant_min"]= np.where(td_0["pollutant_min"]> upper_pollutant_min_limit, upper_pollutant_min_limit, np.where(td_0["pollutant_min"] < lower_pollutant_min_limit, lower_pollutant_min_limit, td_0["pollutant_min"]))
    st.write(td_0.pollutant_min[1:40])
    st.image('oqpaftermin.png')

def quantile_polmax():
    st.write(sns.set_style('darkgrid'))
    air_data=pd.read_csv(r"Air_Quality.csv")
    st.write(air_data.head())
    td_0=air_data
    st.write('Boxplot-')
    st.image('oqpmax.png')
    # setting 0.05 as the Lower Limit and 0.95 as the upper Limit for the quantiles to find the outliers
    lower_pollutant_max_limit= td_0["pollutant_max"].quantile (0.05) 
    upper_pollutant_max_limit = td_0["pollutant_max"].quantile (0.95)
    st.write(('lower_pollutant_max_limit:',lower_pollutant_max_limit))
    st.write(('upper_pollutant_max_limit:',upper_pollutant_max_limit))
    # The output shows that anything beyond 3.0 is an outlier, and similarly, the fare value below 157.0 is also an outiter.
    # Now replace the outlier values by the upper and Lower Limit.
    td_0["pollutant_max"]= np.where(td_0["pollutant_max"]> upper_pollutant_max_limit, upper_pollutant_max_limit, np.where(td_0["pollutant_max"] < lower_pollutant_max_limit, lower_pollutant_max_limit, td_0["pollutant_max"]))
    st.write(td_0.pollutant_max[1:40])
    st.image('oqpaftermax.png')


def custom_polavg():
    st.write(sns.set_style('darkgrid'))
    air_data=pd.read_csv(r"Air_Quality.csv")
    st.write(air_data.head())
    td_0=air_data
    st.write('Upper limit:',td_0.pollutant_avg.max())
    st.write('Limit limit:',td_0.pollutant_avg.min())
    td_0["pollutant_avg"]= np.where(td_0["pollutant_avg"]> 50, 50, np.where(td_0["pollutant_avg"] < 10, 10, td_0["pollutant_avg"]))
    st.write('Replacing arbitrarily value in upper limit and lower limit:')
    st.write('Upper limit:',td_0.pollutant_avg.max())
    st.write('Limit limit:',td_0.pollutant_avg.min())
    st.image('ocvpavg.png')

def custom_polmin():
    st.write(sns.set_style('darkgrid'))
    air_data=pd.read_csv(r"Air_Quality.csv")
    st.write(air_data.head())
    td_0=air_data
    st.write('Upper limit:',td_0.pollutant_min.max())
    st.write('Lower limit:',td_0.pollutant_min.min())
    td_0["pollutant_min"]= np.where(td_0["pollutant_min"]> 50, 50, np.where(td_0["pollutant_min"] < 10, 10, td_0["pollutant_min"]))
    st.write('Replacing arbitrarily value in upper limit and lower limit:')
    st.write('Upper limit:',td_0.pollutant_avg.max())
    st.write('Limit limit:',td_0.pollutant_avg.min())
    st.image('ocvpmin.png')

def custom_polmax():
    st.write(sns.set_style('darkgrid'))
    air_data=pd.read_csv(r"Air_Quality.csv")
    st.write(air_data.head())
    td_0=air_data
    st.write('Upper limit:',td_0.pollutant_max.max())
    st.write('Lower limit:',td_0.pollutant_max.min())
    td_0["pollutant_max"]= np.where(td_0["pollutant_max"]> 50, 50, np.where(td_0["pollutant_max"] < 10, 10, td_0["pollutant_max"]))
    st.write('Replacing arbitrarily value in upper limit and lower limit:')
    st.write('Upper limit:',td_0.pollutant_avg.max())
    st.write('Limit limit:',td_0.pollutant_avg.min())    
    st.image('ocvpmax.png')

siteHeader = st.container()
imputation = st.container()
encoding = st.container()
discretization = st.container()
outlier_hand = st.container()
feature_sel = st.container()
transfo= st.container()

with siteHeader:
    st.title("India's Air Quality Analysis")
    st.write("Welcome to our Data Preprocessing Project!\n ")
    st.header("Introduction to Dataset")
    st.text("")
    df = pd.read_csv('Air_Quality.csv')
    st.write('Dataset URL')
    with st.echo():
        'https://www.kaggle.com/chitwanmanchanda/indias-air-quality-index'

        df.head(20)

with imputation:
    imput_col,dis_col= st.columns(2)
    type_imput =imput_col.selectbox('Imputation Type',options=['Outlier Trimming','Outlier Capping'],index=0)
    if (type_imput=='Outlier Trimming'):
        feature1 = dis_col.selectbox('Choose Feature',options=['Pollutant_avg','Pollutant_min','Pollutant_max'],index=0)
        if (feature1=='Pollutant_avg'):
            with st.echo():
                st.write(trim_pollutantavg())
        if (feature1=='Pollutant_min'):
            with st.echo():
                st.write(trim_pollutantmin())
        if (feature1=='Pollutant_max'):
            with st.echo():
                st.write(trim_pollutantmax())
        
    if (type_imput=='Outlier Capping'):
        feature = dis_col.selectbox('Choose Feature',options=['Using IQR','Using Mean and Standard deviation','Using Quantiles','Using Custom Values'],index=0)
    
        if(feature=='Using IQR'):
            feature1 = dis_col.selectbox('Choose Feature',options=['Pollutant_avg','Pollutant_min','Pollutant_max'],index=0)
            if (feature1=='Pollutant_avg'):
                with st.echo():
                    st.write(iqr_polavg())
            if (feature1=='Pollutant_min'):
                with st.echo():
                    st.write(iqr_polmin())
            if (feature1=='Pollutant_max'):
                with st.echo():
                    st.write(iqr_polmax())
        if(feature=='Using Mean and Standard deviation'):
            feature1 = dis_col.selectbox('Choose Feature',options=['Pollutant_avg','Pollutant_min','Pollutant_max'],index=0)
            if (feature1=='Pollutant_avg'):
                with st.echo():
                    st.write(ms_polavg())
            if (feature1=='Pollutant_min'):
                with st.echo():
                    st.write(ms_polmin())
            if (feature1=='Pollutant_max'):
                with st.echo():
                    st.write(ms_polmax())

        if(feature=='Using Quantiles'):
            feature1 = dis_col.selectbox('Choose Feature',options=['Pollutant_avg','Pollutant_min','Pollutant_max'],index=0)
            if (feature1=='Pollutant_avg'):
                with st.echo():
                    st.write(quantile_polavg())
            if (feature1=='Pollutant_min'):
                with st.echo():
                    st.write(quantile_polmin())
            if (feature1=='Pollutant_max'):
                with st.echo():
                    st.write(quantile_polmax())

        if(feature=='Using Custom Values'):
            feature1 = dis_col.selectbox('Choose Feature',options=['Pollutant_avg','Pollutant_min','Pollutant_max'],index=0)
            if (feature1=='Pollutant_avg'):
                with st.echo():
                    st.write(custom_polavg())
            if (feature1=='Pollutant_min'):
                with st.echo():
                    st.write(custom_polmin())
            if (feature1=='Pollutant_max'):
                with st.echo():
                    st.write(custom_polmax())
