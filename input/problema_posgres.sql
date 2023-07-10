--Punto 1. Construcción de la tabla

create table public.fraudes(
Monthh text,	
WeekOfMonth int,
DayOfWeek	text,
Make	text,
AccidentArea    text,	
DayOfWeekClaimed	text,
MonthClaimed	text,
WeekOfMonthClaimed  int,
Sex text,
MaritalStatus   text,	
Age	int,
Fault	text,
PolicyType	text,
VehicleCategory	text,
VehiclePrice	text,
FraudFound_P	int,
PolicyNumber	int,
RepNumber	int,
Deductible	int,
DriverRating	int,
Days_Policy_Accident	text,
Days_Policy_Claim	text,
PastNumberOfClaims	text,
AgeOfVehicle	text,
AgeOfPolicyHolder	text,
PoliceReportFiled	text,
WitnessPresent	text,
AgentType	text,
NumberOfSuppliments	   text,
AddressChange_Claim text,
NumberOfCars	text,
Yearr   int,
BasePolicy  text

);

COPY public.fraudes FROM 'C:\fraude\fraud.csv' DELIMITER ',' CSV HEADER;

-- verificar carga de la tabla de fraudes
select * from fraudes;


---Punto 2. Con su base de datos cargada, usando solo SQL replique la siguiente salida sin usar subconsultas.
WITH CONS1 AS (
				SELECT 
					Monthh,
					WeekOfMonth, 
					DayOfWeek, 
					ROUND(SUM(FraudFound_P) * 100.0/ COUNT(FraudFound_P),2) AS percentage_fraud_month_week_day
				FROM fraudes
				GROUP BY  Monthh, WeekOfMonth, DayOfWeek),
	CONS2 AS (
				SELECT 
					Monthh,
					WeekOfMonth,
					ROUND(SUM(FraudFound_P)  * 100.0/ COUNT(FraudFound_P),2) AS percentage_fraud_month_week
				FROM fraudes
				GROUP BY  Monthh, WeekOfMonth),
	CONS3 AS (
				SELECT 
					Monthh,
					ROUND(SUM(FraudFound_P)  * 100.0/ COUNT(FraudFound_P),2) AS percentage_fraud_month
				FROM fraudes
				GROUP BY  Monthh)
SELECT DISTINCT
CONS1.Monthh,
CONS1.WeekOfMonth,
CONS1.DayOfWeek,
CONS3.percentage_fraud_month,
CONS2.percentage_fraud_month_week,
CONS1.percentage_fraud_month_week_day
FROM CONS1
LEFT JOIN CONS2 ON CONS1.Monthh=CONS2.Monthh AND CONS1.WeekOfMonth=CONS2.WeekOfMonth
LEFT JOIN CONS3 ON CONS1.Monthh=CONS3.Monthh
ORDER BY Monthh, WeekOfMonth;













