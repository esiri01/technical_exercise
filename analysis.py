import pandas as pd

#Question 1
df = pd.read_csv("data/ASISdb_MDOTW_VW_OCCURRENCE_PUBLIC.csv", low_memory=False)

print(df)
print(df.columns)

# Calculate the percentage of missing values per column
missing_values = df.isnull().mean() * 100
print(missing_values)

# Filter columns with more than 20% missing values
high_missing = missing_values[(missing_values > 20)]
all_missing_val = missing_values[(missing_values == 100)]
print("Number of columns with missing values greater than 20% : ", len(high_missing))
print("Number of columns with all missing values : ", len(all_missing_val))


#Question 2
df2 = df.copy()
all_occ = df2['OccIncidentTypeID_DisplayEng'].value_counts()
count_col = df2['OccIncidentTypeID_DisplayEng'].eq('COLLISION (x)').sum()

all_col = df2["OccIncidentTypeID_DisplayEng"].str.contains('COLLISION', case=False, na=False).sum()
percent_col = count_col/len(df2) * 100.0
percent_all_col = all_col/len(df2) * 100.0

print("The percentage of Collisions compared to all incidents is ", round(percent_col, 2), "%")
print("The percentage of all Collisions and near misses (Risk of collision) compared to all incidents is ", round(percent_all_col, 2), "%")

collision_df = df2[df2["OccIncidentTypeID_DisplayEng"].str.contains('COLLISION', na=False)]

# Count collisions per airport
collision_counts = collision_df.groupby("AirportID_AirportName").size().reset_index(name="Collision_Count")

# Count total incidents per airport
total_incidents = df2.groupby("AirportID_AirportName").size().reset_index(name="Total_Incidents")

MIN_INCIDENTS = 10


# Merge both dataframes
risk_analysis = total_incidents.merge(collision_counts, on="AirportID_AirportName", how="left").fillna(0)

# Compute collision rate
risk_analysis["Collision_Rate"] = (risk_analysis["Collision_Count"] / risk_analysis["Total_Incidents"]) * 100

risk_analysis = risk_analysis.query("Total_Incidents >= @MIN_INCIDENTS")

# Sort by highest collision rate
high_risk_airports = risk_analysis.sort_values(by="Collision_Rate", ascending=False)

high_risk_airports.to_csv("outputs/High Collision Risk Airports.csv", index=False)

# Display airports with high collision risk
top_airports = ", ".join(high_risk_airports["AirportID_AirportName"].head(10))
print(f"The top 10 airports for risk of collision are: {top_airports}.")


#Question 5
df3 = df.copy()

# Filter for Canadian airports
canada_df = df3[df3["CountryID_DisplayEng"].str.contains('Canada', na=False, case=False)]

# Group by ICAO event categories and count occurrences
icao_event_counts = canada_df.groupby("ICAO_DisplayEng").size().reset_index(name="Event_Count")

# Sort by event count to find the most common categories
most_common_events = icao_event_counts.sort_values(by="Event_Count", ascending=False)

# Print the most common ICAO event categories
print("Most common ICAO event categories at Canadian airports:")
print(most_common_events.head(10))  # Display top 10 most common categories

# Save the results to a CSV file
most_common_events.to_csv("outputs/Most_Common_ICAO_Events_Canada.csv", index=False)
