![](images/pumping_new.jpg)

# Title of the Analysis

**Authors:** Victor Chen, Aaron Cherry 

## Overview

With this analysis, we aim to predict the condition of waterwells in Tanzania based on data retreived from the Taarifa waterpoints dashboard. The dashboard aggregates information collected from the Tanzania Ministry of Water.

## Business Problem

A major challange of the Tanzanian Ministry of Water is determining when, where and how often a water well in Tanzania would need repairs. Implementation of models to predict the condition of a water well would greatly enhance maintenance operations, provide crucial updates associated with the conditions of the water wells and ensure that clean water sources can be provided to the communities in Tanzania. Through this analysis, we aim to provide prediction models based on the information collected to determine water well conditions to aid the Tanzanian Ministry of Water.

## Data Understanding

The data used for this analysis is taken from the Taarifa waterpoints dashboard that functions to aggregate weter well data collected from the Tanzania Ministry of Water. A link to the data and explanation of the features found in the data can be found [here](https://www.drivendata.org/competitions/7/pump-it-up-data-mining-the-water-table/page/23/). A link to the Taarifa waterpoints dashboard website can be found [here](https://taarifa.org/). The link to the website for the Tanzania Ministry of Water can be found [here](https://www.maji.go.tz/).

The following table is a description of the features in the data along with descriptions of the features.


|**Feature**|**Description**|
|:----------|:------------|
|```amount_tsh``` | Total static head (amount water available to waterpoint)|
|```date_recorded``` | The date the row was entered|
|```funder``` | Who funded the well|
|```gps_height``` | Altitude of the well|
|```installer``` | Organization that installed the well|
|```longitude``` | GPS coordinate|
|```latitude``` | GPS coordinate|
|```wpt_name``` | Name of the waterpoint if there is one|
|```num_private``` | Unknown|
|```basin``` | Geographic water basin|
|```subvillage``` | Geographic location|
|```region``` | Geographic location|
|```region_code``` | Geographic location (coded)|
|```district_code``` | Geographic location (coded)|
|```lga``` | Geographic location|
|```ward``` | Geographic location|
|```population``` | Population around the well|
|```public_meeting``` | True/False|
|```recorded_by``` | Group entering this row of data|
|```scheme_management``` | Who operates the waterpoint|
|```scheme_name``` | Who operates the waterpoint|
|```permit``` | If the waterpoint is permitted|
|```construction_year``` | Year the waterpoint was constructed|
|```extraction_type``` | The kind of extraction the waterpoint uses|
|```extraction_type_group``` | The kind of extraction the waterpoint uses|
|```extraction_type_class``` | The kind of extraction the waterpoint uses|
|```management``` | How the waterpoint is managed|
|```management_group``` | How the waterpoint is managed|
|```payment``` | What the water costs|
|```payment_type``` | What the water costs|
|```water_quality``` | The quality of the water|
|```quality_group``` | The quality of the water|
|```quantity``` | The quantity of water|
|```quantity_group``` | The quantity of water|
|```source``` | The source of the water|
|```source_type``` | The source of the water|
|```source_class``` | The source of the water|
|```waterpoint_type``` | The kind of waterpoint|
|```waterpoint_type_group``` | The kind of waterpoint|

The target class in the data set is ```status_group``` and consists of three classes. The classes and their descriptions can be fouind in the table below:

|Label|Description|
|:-----|:------|
|```functional``` | the waterpoint is operational and there are no repairs needed|
|```functional needs repair``` | the waterpoint is operational, but needs repairs|
|```non functional``` | the waterpoint is not operational|

## Data Preparation

- There are some features that have missing data. The first order of business will be to fill or drop these NaN values.
- There are no duplicate data points in the dataset
- There are some features that have data types that don't match with the feature description. These will be converted to the appropriate data type.
- There are some features that will have no significance in determining the classification.

### Missing Data:
```funder``` -  column gives the funding organization for the construction of the well. It is assumed that the well points that do not have an explicit funding source were not funded by a major organization and will be labeled ```other```.
```installer``` -  feature lists the organization responsible for constructing the water well. Like the 'funder' column, it is assumed that the water points with no explicit installer were not constructed by a major organization and will be labelled as ```other```.
- The ```subvillage``` feature gives the sub community in which the water well was installed. It is assumed that the water points with no explicit subvillage were installed outside of more populated areas and will be filled with ```none```.
- The ```public_meeting``` feature describes whether or not the water point was installed in a public meeting area. It is assumed that the water points with no explicit label are water points not installed in public areas and will be filled with ```False```.
- The ```scheme_management``` feature labels the organization responsible for the operation of the water point. It is assumed that the water points with no explicit operation management are not managed by a major company and will be filled with ```None```.
- The ```scheme_name``` feature gives the name of the company responsible for the operation of the water point. One of the classes in the column is ```None``` and it is assumed that the water points with no explicit operation name are also ```None```.

#### Dealing with outliers

## Feature Engineering

## Exploratory Data Analysis

## Modeling

## Conclusions

## Next Steps