"""
Polars (8): Stock Index

1. Check Null Values
2. Convert Str to Datetime
3. Extract Year, Month, Weekday
4. Calculate Percentage

HINT: Formula is ((Close - Open) / Open) * 100

5. Group by Year, Month, Weekday


Table: Yearly Stock Market Performance Summary

-------------------------------------------------------
| Year  | Mean Percentage | Highest Percentage        |
|-------|-----------------|---------------------------|
| 1969  | -0.182551       | 4.053299                  |
| 2008  | -0.148384       | 2.245647                  |
| 2009  | 0.078437        | 1.569974                  |
| 1998  | -0.067459       | 1.550581                  |
| 2000  | -0.074983       | 1.520525                  |
| 2002  | -0.096936       | 1.51897                   |
| 2001  | -0.027812       | 1.463961                  |
| 1999  | -0.019392       | 1.41345                   |
| 1997  | -0.048884       | 1.3963                    |
| 2020  | -0.003563       | 1.346064                  |
| ...   | ...             | ...                       |
| 1968  | 0.0             | 0.0                       |
| 1966  | 0.0             | 0.0                       |
| 1978  | 0.0             | 0.0                       |
| 1975  | 0.0             | 0.0                       |
| 1972  | 0.0             | 0.0                       |
| 1967  | 0.0             | 0.0                       |
| 1973  | 0.0             | 0.0                       |
| 1970  | 0.0             | 0.0                       |
| 1976  | 0.0             | 0.0                       |
| 1965  | 0.0             | 0.0                       |
-------------------------------------------------------

Table: Weekly Stock Market Performance Summary

--------------------------------------------------------
| Weekday     | Mean Percentage | Highest Percentage   |
|-------------|-----------------|----------------------|
| Wednesday   | 0.022988        | 1.054878             |
| Friday      | 0.011943        | 0.997288             |
| Tuesday     | 0.007643        | 1.060078             |
| Thursday    | -0.028926       | 1.05359              |
| Monday      | -0.031002       | 1.319758             |
--------------------------------------------------------

Table: Monthly Stock Market Performance Summary

-------------------------------------------------------
| Month      | Mean Percentage | Highest Percentage   |
|------------|-----------------|----------------------|
| November   | 0.025703        | 1.088329             |
| December   | 0.025413        | 0.992912             |
| April      | 0.019222        | 0.989383             |
| May        | 0.009623        | 0.979243             |
| July       | 0.005424        | 1.01775              |
| March      | 0.000569        | 1.145818             |
| February   | -0.002791       | 1.005902             |
| January    | -0.00518        | 1.149389             |
| October    | -0.00913        | 1.289343             |
| August     | -0.028932       | 1.030908             |
| June       | -0.037557       | 1.374729             |
| September  | -0.040566       | 1.06133              |
-------------------------------------------------------

"""
import polars as pl
import datetime as datetime

def get_day(day_int):
    day_dict = {
        1:"Monday",
        2:"Tuesday",
        3:"Wednesday",
        4:"Thursday",
        5:"Friday",
        6:"Saturday",
        7:"Sunday"}
    day = day_dict[day_int]
    return day
    

df = pl.read_csv('/workspaces/Magiks-Applied-Project/3_Polars/dataset/stock_historical.csv')
df = df.drop('High','Low','Volume')

#null values
null_count = df.null_count()
print(null_count)

#cast from str to datetime type
df = df.with_columns(
    pl.col('Date').str.strptime(pl.Datetime, format='%m/%d/%Y')
)

#get year,month,weekday from date
df = df.with_columns(
    pl.col('Date').dt.year().alias('Year'),
    pl.col('Date').dt.month().alias('Month'),
    pl.col('Date').dt.weekday().alias('Day of the Week')
)

df = df.with_columns(
    pl.col("Day of the Week").map_elements(get_day, return_dtype=pl.Utf8)
)

"""print(df['Year'].value_counts)"""
#there is a unique data from 1965 to 2021
#aggregation percentage
df = df.with_columns(
    ((pl.col('Close') - pl.col('Open'))/pl.col('Open')*100).alias("Percentage")
)

#get aggregation group by year
df_yoy = df.group_by('Year').agg(
    pl.col('Percentage').mean().round(6).alias('Mean Percentage'),
    pl.col("Percentage").max().round(6).alias("Highest Percentage")
)

df_mom = df.group_by('Month').agg(
    pl.col("Percentage").mean().round(6).alias('Mean Percentage'),
    pl.col("Percentage").max().round(6).alias("Highest Percentage")
)

df_dod = df.group_by('Day of the Week').agg(
    pl.col("Percentage").mean().round(6).alias('Mean Percentage'),
    pl.col("Percentage").max().round(6).alias("Highest Percentage")
)


yearly_table = df_yoy.sort(by='Mean Percentage')
monthly_table = df_mom.sort(by="Mean Percentage", descending=True)
daily_table = df_dod.sort(by="Mean Percentage", descending=True)



print(yearly_table)

print(daily_table)

print(monthly_table)



