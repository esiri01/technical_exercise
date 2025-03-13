# Boeing Vancouver Data Scientist Take Home Assignment

## Question 1
### Dataset Overview
- The dataset (Occurrence Table) contains **52,742 rows** and **242 columns**.
- Several fields contain **NaN (missing values)**.
- Some columns are redundant, such as English and French versions of the same field (e.g., `OccTypeID_DisplayEng` and `OccTypeID_DisplayFre`).

### Data Quality Issues
- **Number of columns with missing values greater than 20%**: 191 (79% of all columns).
- **Number of columns with all missing values**: 9.

### Recommendations for Analysis
Despite the data quality issues, the following analyses can still provide valuable insights:
1. **Geographical Analysis of Incidents**: Examine the distribution of incidents across different regions or airports.
2. **Identify the Most Common Types of Occurrences**: Determine the most frequent types of incidents to prioritize safety improvements.

---

## Question 2
### How Common Are Aircraft Collisions?
- **Total Collisions**: Collisions occurred **481 times** in the dataset.
- **Percentage of Collisions**:
  - Collisions account for **0.91%** of all incidents.
  - When including near misses (risk of collision), the percentage increases to **2.23%** of all incidents.

### High-Risk Airports
In the analysis, airports with fewer than 10 total incidents were excluded to focus on meaningful trends. The top 10 airports with the highest risk of collision are:
1. San Francisco Intl
2. Benito Juárez Intl
3. LaGuardia
4. Fort McKay/Albian
5. Denver Intl
6. Phoenix Sky Harbor Intl
7. Palm Springs Intl
8. Fort Lauderdale/Hollywood Intl
9. Trail
10. St. Theresa Point

### Observation
The presence of both major international airports and smaller regional airports in the top 10 suggests that collision risks are not limited to high-traffic areas alone.



---

## Question 5
### What ICAO Event Categories Are Most Common at Canadian Airports?

#### Top 10 ICAO Event Categories
1. SYSTEM/COMPONENT FAILURE OR MALFUNCTION (NON-POWERPLANT) (SCF–NP)
2. SYSTEM/COMPONENT FAILURE OR MALFUNCTION (POWERPLANT) (SCF–PP)
3. AIRPROX/TCAS ALERT/LOSS OF SEPARATION/NEAR MIDAIR COLLISIONS/MIDAIR COLLISIONS (MAC)
4. FIRE/SMOKE (NON-IMPACT) (F–NI)
5. LOSS OF CONTROL–INFLIGHT (LOC–I)
6. ABNORMAL RUNWAY CONTACT (ARC)
7. RUNWAY EXCURSION (RE)
8. COLLISION WITH OBSTACLE(S) DURING TAKEOFF AND LANDING (CTOL)
9. LOSS OF CONTROL–GROUND (LOC–G)
10. MEDICAL (MED)

### Trends and Patterns (Grouped into 3 Key Categories)

#### 1. **System and Equipment Failures**
- System/component failures (both powerplant and non-powerplant) dominate the dataset, indicating potential gaps in maintenance or component reliability.

#### 2. **Operational and Safety Incidents**
- Airproximity/loss of separation, fire/smoke incidents, and loss of control events highlight challenges in ATC coordination, fire safety, and aircraft handling.

#### 3. **Runway and Ground-Related Incidents**
- Abnormal runway contact, runway excursions, and collisions with obstacles suggest issues with runway conditions, pilot techniques, or obstacle clearance procedures.

