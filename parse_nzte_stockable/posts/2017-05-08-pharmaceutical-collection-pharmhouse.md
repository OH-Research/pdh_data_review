---
categories: new-zealand administrative
date: '2017-05-08 08:46:48'
id: pharmaceutical_collection_pharmhouse
layout: post
link: http://www.health.govt.nz/publication/pharmaceutical-claims-data-mart-data-dictionary
provider: Ministry of Health
tags:
- drugs
- nzte-report
title: Pharmaceutical Collection (Pharmhouse)
---


 <h4> <u>Description:</u> </h4>
Provides us with information on drug costs, usage and number of people receiving subsidised drug treatment.
 <h4> <u>Additional information:</u> </h4>
 <table style="border: 1px solid">
 <tr> <td width="40%">Have_(encrypted)_NHI</td> <td>Yes</td> </tr>
 <tr> <td width="40%">Personally identifiable (e.g. linked to NHI numbers) and longitudinal or aggregated (e.g. for planning, clinical research etc.)?</td> <td>encrypted NHI</td> </tr>
 <tr> <td width="40%">Volume of data (e.g. how many records)
Since when?</td> <td>6 million dispensing records per month; PHARMS DB since 1992 (historical data having only cost + volume); data having NHI since 2006. As at July 2012, the Pharmaceutical Collection holds claims for around 840 million dispensings.</td> </tr>
 <tr> <td width="40%">Purpose and governance including ethics committee/patient consent mechanisms. Q: How do you get around ethics/privacy issues with your data sources? Esp. DHBs?</td> <td>Privacy, confidentiality framework, as per Privacy code. No individual patient consent is needed, as NHI is encrypted. MoH handles request to access this info. Ethics approval is needed for access by researchers. (Encrypted NHI could be used to link with other MoH datasets.)</td> </tr>
 <tr> <td width="40%">Scope</td> <td>National</td> </tr>
 <tr> <td width="40%">Does the data contain diagnoses and clinical outcomes?
Does the data contain procedures, device information and medication for therapy?
Does this data set have cost / price data?</td> <td>Info about the health conditions people have (e.g. diagnosis data)? No. Cost/price data? Yes</td> </tr>
 <tr> <td width="40%">Presence of Data dictionary? Column headings in Excel or any kind of data model if residing in a relational database (e.g. Access, SQL Server, Oracle etc.) </td> <td>http://www.health.govt.nz/publication/pharmaceutical-claims-data-mart-data-dictionary</td> </tr>
 <tr> <td width="40%">Linked (or linkable) to other datasets within your organisation or across the Sector</td> <td>linkable to MoH Reference Tables and other datasets</td> </tr>
 <tr> <td width="40%">How often does this data set get updated? Daily? Weekly? Monthly? Quarterly? Yearly?</td> <td>monthly with a shift to weekly updates</td> </tr>
 <tr> <td width="40%">Indication of data quality (e.g. missing values, duplications, inconsistencies etc.). Q: Audits? How do you ensure the data is valid and correct?</td> <td>1.5-2% inconsistency is identified by validation effort and the inconsistent data is excluded in further analysis, e.g. NHI belonging to deceased, age in wrong category, indicated by gender-specific drugs, etc. (But no follow-up back to pharmacies for correction is needed on this small percentage.)</td> </tr>
 <tr> <td width="40%">Brief info about the systems and processes used to collect/manage data. Q: Where the data is collected, in what form, and accessibility?</td> <td>Pharmacies submit claims (subsidized drugs' dispensing records) through payment system in 2-week claim cycles; once claims are approved, the records are exacted into the DB (monthly update). Could be 2-month delay from pharmacy claims to the DB.</td> </tr>
 <tr> <td width="40%">Data format, e.g., data structure, data types, and storage form (relational database, Excel, csv, etc.).</td> <td>relational DB --> denormalized flat Data Tables</td> </tr>
 <tr> <td width="40%">How well the data is structured, e.g. free text VS coded text VS pick-list (drop-down list)</td> <td>Well structured data; no free text</td> </tr>
 <tr> <td width="40%">How quickly can the data be made available from time of request and how old is the data once it is made available</td> <td>data request: 20-working days.</td> </tr>
 </table>