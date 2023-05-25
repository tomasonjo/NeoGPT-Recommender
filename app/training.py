examples = """
# Which law school did Joshua Spielman study at?
MATCH(a2:Applicant) where a2.LastName ='Spielman' and a2.FirstName ='Joshua'
MATCH (a2)-[:IS]-(status:Status) where status.OriginalName IN ['Newly added to the database','Recently changed','Not Changed','Lateral move','Lateral Move*','Newly Hired Graduates','Moved due to merger' ,'SECONDMENT']
MATCH (a2)-[:STUDIED_AT]-(s:School)
Return s
LIMIT 1
# Which law school did Matthew Wochok study at?
MATCH(a2:Applicant) where a2.LastName ='Wochok' and a2.FirstName ='Matthew'
MATCH (a2)-[:IS]-(status:Status) where status.OriginalName IN ['Newly added to the database','Recently changed','Not Changed','Lateral move','Lateral Move*','Newly Hired Graduates','Moved due to merger' ,'SECONDMENT']
MATCH (a2)-[:STUDIED_AT]-(s:School)
Return s
LIMIT 1
# Who studied at Harvard?
MATCH (a2)-[:IS]-(status:Status) where status.OriginalName IN ['Newly added to the database','Recently changed','Not Changed','Lateral move','Lateral Move*','Newly Hired Graduates','Moved due to merger' ,'SECONDMENT']
MATCH (s:School)-[:STUDIED_AT]-(a2:Applicant) WHERE s.OriginalName ='Harvard'
return a2
LIMIT 25
# Where does Matthew Wochok work?
MATCH(a2:Applicant) where a2.LastName ='Wochok' and a2.FirstName ='Matthew'
MATCH (a2)-[:WORKS_AT]-(lf:LawFirm)
Return lf
LIMIT 1
# Who works at Gibbons?
MATCH (lf:LawFirm)-[:WORKS_AT]-(a2:Applicant) WHERE lf.Name ='Gibbons'
MATCH (a2)-[:IS]-(status:Status) where status.OriginalName IN ['Newly added to the database','Recently changed','Not Changed','Lateral move','Lateral Move*','Newly Hired Graduates','Moved due to merger' ,'SECONDMENT']
return a2
LIMIT 25
# Where did Matthew Wochok study his undergraduate degree?
MATCH(a2:Applicant) where a2.LastName ='Wochok' and a2.FirstName ='Matthew'
Return a2.Undergrad
LIMIT 1
# When did Matthew Wochok graduate from Georgetown University?
MATCH(a2:Applicant) where a2.LastName ='Wochok' and a2.FirstName ='Matthew'
Return a2.JdYear
LIMIT 1
# Who graduated from Georgetown University in 2010?
MATCH (s:School)-[:STUDIED_AT]-(a2:Applicant) WHERE s.OriginalName ='Georgetown University'
MATCH (a2)-[:IS]-(status:Status) where status.OriginalName IN ['Newly added to the database','Recently changed','Not Changed','Lateral move','Lateral Move*','Newly Hired Graduates','Moved due to merger' ,'SECONDMENT']
MATCH (a2: Applicant) where a2.JdYear=2010
return a2, s, a2.JdYear
LIMIT 25
# Who studied at Harvard in law firm Morris Manning & Martin LLP?
MATCH (lf:LawFirm)-[:WORKS_AT]-(a2:Applicant) WHERE lf.Name ='Morris Manning & Martin LLP'
MATCH (a2)-[:IS]-(status:Status) where status.OriginalName IN ['Newly added to the database','Recently changed','Not Changed','Lateral move','Lateral Move*','Newly Hired Graduates','Moved due to merger' ,'SECONDMENT']
MATCH (s:School)-[:STUDIED_AT]-(a2:Applicant) WHERE s.OriginalName ='Harvard'
return a2
LIMIT 25
# Who studied at Georgetown University in law firm Gibbons?
MATCH (lf:LawFirm)-[:WORKS_AT]-(a2:Applicant) WHERE lf.Name ='Gibbons'
MATCH (a2)-[:IS]-(status:Status) where status.OriginalName IN ['Newly added to the database','Recently changed','Not Changed','Lateral move','Lateral Move*','Newly Hired Graduates','Moved due to merger' ,'SECONDMENT']
MATCH (s:School)-[:STUDIED_AT]-(a2:Applicant) WHERE s.OriginalName ='Georgetown University'
return a2
LIMIT 25
# Who studied their undergraduate degree from U OF VIRGINIA and graduated from Georgetown University in 2010?
MATCH (s:School)-[:STUDIED_AT]-(a2:Applicant) WHERE s.OriginalName ='Georgetown University'
MATCH (a2)-[:IS]-(status:Status) where status.OriginalName IN ['Newly added to the database','Recently changed','Not Changed','Lateral move','Lateral Move*','Newly Hired Graduates','Moved due to merger' ,'SECONDMENT']
MATCH (a2: Applicant) where a2.JdYear=2010
MATCH (a2: Applicant) where a2.Undergrad='U OF VIRGINIA'
return a2, s
LIMIT 25
# Who studied their undergraduate degree from U OF GEORGIA and graduated from Duke in 2015?
MATCH (s:School)-[:STUDIED_AT]-(a2:Applicant) WHERE s.OriginalName ='Duke'
MATCH (a2)-[:IS]-(status:Status) where status.OriginalName IN ['Newly added to the database','Recently changed','Not Changed','Lateral move','Lateral Move*','Newly Hired Graduates','Moved due to merger' ,'SECONDMENT']
MATCH (a2: Applicant) where a2.JdYear=2015
MATCH (a2: Applicant) where a2.Undergrad='U OF GEORGIA'
return a2, s
LIMIT 25
# Who studied their undergraduate degree from U OF SOUTHERN CALIFORNIA and graduated from Duke in 2015?
MATCH (s:School)-[:STUDIED_AT]-(a2:Applicant) WHERE s.OriginalName ='Duke'
MATCH (a2)-[:IS]-(status:Status) where status.OriginalName IN ['Newly added to the database','Recently changed','Not Changed','Lateral move','Lateral Move*','Newly Hired Graduates','Moved due to merger' ,'SECONDMENT']
MATCH (a2: Applicant) where a2.JdYear=2021
MATCH (a2: Applicant) where a2.Undergrad='U OF SOUTHERN CALIFORNIA'
return a2, s
LIMIT 25
# Who studied their undergraduate degree from AUSTRALIA and graduated from Australian National University in 2019?
MATCH (s:School)-[:STUDIED_AT]-(a2:Applicant) WHERE s.OriginalName ='Australian National University'
MATCH (a2)-[:IS]-(status:Status) where status.OriginalName IN ['Newly added to the database','Recently changed','Not Changed','Lateral move','Lateral Move*','Newly Hired Graduates','Moved due to merger' ,'SECONDMENT']
MATCH (a2: Applicant) where a2.JdYear=2019
MATCH (a2: Applicant) where a2.Undergrad='AUSTRALIA'
return a2, s
LIMIT 25
# Who studied their undergraduate degree in U OF DELAWARE at Gibbons?
MATCH (lf:LawFirm)-[:WORKS_AT]-(a2:Applicant) WHERE lf.Name ='Gibbons'
MATCH (a2)-[:IS]-(status:Status) where status.OriginalName IN ['Newly added to the database','Recently changed','Not Changed','Lateral move','Lateral Move*','Newly Hired Graduates','Moved due to merger' ,'SECONDMENT']
MATCH (a2: Applicant) where a2.Undergrad='U OF DELAWARE'
Return a2
LIMIT 25
# Who studied their undergraduate degree in U OF GEORGIA at Morris Manning & Martin LLP?
MATCH (lf:LawFirm)-[:WORKS_AT]-(a2:Applicant) WHERE lf.Name ='Morris Manning & Martin LLP'
MATCH (a2)-[:IS]-(status:Status) where status.OriginalName IN ['Newly added to the database','Recently changed','Not Changed','Lateral move','Lateral Move*','Newly Hired Graduates','Moved due to merger' ,'SECONDMENT']
MATCH (a2:Applicant) where a2.Undergrad='U OF GEORGIA'
Return a2
LIMIT 25
# Who graduated law school at Emory in 1996 and works at Morris Manning & Martin LLP?
MATCH (lf:LawFirm)-[:WORKS_AT]-(a2:Applicant) WHERE lf.Name ='Morris Manning & Martin LLP'
MATCH (s:School)-[:STUDIED_AT]-(a2:Applicant) WHERE s.OriginalName ='Emory'
MATCH (a2)-[:IS]-(status:Status) where status.OriginalName IN ['Newly added to the database','Recently changed','Not Changed','Lateral move','Lateral Move*','Newly Hired Graduates','Moved due to merger' ,'SECONDMENT']
MATCH (a2: Applicant) where a2.JdYear=1996
return a2, s
LIMIT 25
# Who graduated law school at Seton Hall in 2012 and works at Gibbons?
MATCH (lf:LawFirm)-[:WORKS_AT]-(a2:Applicant) WHERE lf.Name ='Gibbons'
MATCH (s:School)-[:STUDIED_AT]-(a2:Applicant) WHERE s.OriginalName ='Seton Hall'
MATCH (a2)-[:IS]-(status:Status) where status.OriginalName IN ['Newly added to the database','Recently changed','Not Changed','Lateral move','Lateral Move*','Newly Hired Graduates','Moved due to merger' ,'SECONDMENT']
MATCH (a2: Applicant) where a2.JdYear=2012 
return a2, s
LIMIT 25
# Who studied their undergraduate degree at AUBURN U and law school at Cumberland at Morris Manning & Martin LLP?
MATCH (lf:LawFirm)-[:WORKS_AT]-(a2:Applicant) WHERE lf.Name ='Morris Manning & Martin LLP'
MATCH (s:School)-[:STUDIED_AT]-(a2:Applicant) WHERE s.OriginalName ='Cumberland'
MATCH (a2)-[:IS]-(status:Status) where status.OriginalName IN ['Newly added to the database','Recently changed','Not Changed','Lateral move','Lateral Move*','Newly Hired Graduates','Moved due to merger' ,'SECONDMENT']
MATCH (a2: Applicant) where a2.Undergrad='AUBURN U'
return a2, s
LIMIT 25
# Who studied their undergraduate degree at SETON HALL U and law school at Rutgers at Gibbons?
MATCH (lf:LawFirm)-[:WORKS_AT]-(a2:Applicant) WHERE lf.Name ='Gibbons'
MATCH (s:School)-[:STUDIED_AT]-(a2:Applicant) WHERE s.OriginalName ='Rutgers'
MATCH (a2)-[:IS]-(status:Status) where status.OriginalName IN ['Newly added to the database','Recently changed','Not Changed','Lateral move','Lateral Move*','Newly Hired Graduates','Moved due to merger' ,'SECONDMENT']
MATCH (a2: Applicant) where a2.Undergrad='SETON HALL U'
return a2, s
LIMIT 25
"""