examples = """
# What honor has Sarah Primrose received?
MATCH (a:Applicant)
WHERE a.LastName = 'Primrose' AND a.FirstName = 'Sarah'
MATCH (a)-[:HAS]-(h:Honor)
RETURN h;
# What honor has Michael Sutton received?
MATCH (a:Applicant)
WHERE a.LastName = 'Sutton' AND a.FirstName = 'Michael'
MATCH (a)-[:HAS]-(h:Honor)
RETURN h;
# What honor has Sean Withall received?
MATCH (a:Applicant)
WHERE a.LastName = 'Withall' AND a.FirstName = 'Sean'
MATCH (a)-[:HAS]-(h:Honor)
RETURN h;
# What state bar has Michael Sutton been admitted to?
MATCH (a:Applicant)
WHERE a.LastName = 'Sutton' AND a.FirstName = 'Michael'
MATCH (a)-[:ADMITTED_BY]-(bar:Admission)
RETURN bar.OriginalName;
# What state bar has Sarah Primrose been admitted to?
MATCH (a:Applicant)
WHERE a.LastName = 'Primrose' AND a.FirstName = 'Sarah'
MATCH (a)-[:ADMITTED_BY]-(bar:Admission)
RETURN bar.OriginalName;
# What state bar has Philip Wong been admitted to?
MATCH (a:Applicant)
WHERE a.LastName = 'Wong' AND a.FirstName = 'Philip'
MATCH (a)-[:ADMITTED_BY]-(bar:Admission)
RETURN bar.OriginalName;
# What state bar has Samuel Lipson been admitted to?
MATCH (a:Applicant)
WHERE a.LastName = 'Lipson' AND a.FirstName = 'Samuel'
MATCH (a)-[:ADMITTED_BY]-(bar:Admission)
RETURN bar.OriginalName;
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
# What is the personal email for Joshua Spielman?
MATCH(a:Applicant) where a.LastName ='Spielman' and a.FirstName ='Joshua'
MATCH (a)-[:IS]-(status:Status)
WHERE status.OriginalName IN ['Newly added to the database', 'Recently changed', 'Not Changed', 'Lateral move', 'Lateral Move*', 'Newly Hired Graduates', 'Moved due to merger', 'SECONDMENT']
Return a.Email
LIMIT 1
# What is the personal email for Samuel Lipson?
MATCH(a:Applicant) where a.LastName ='Lipson' and a.FirstName ='Samuel'
MATCH (a)-[:IS]-(status:Status)
WHERE status.OriginalName IN ['Newly added to the database', 'Recently changed', 'Not Changed', 'Lateral move', 'Lateral Move*', 'Newly Hired Graduates', 'Moved due to merger', 'SECONDMENT']
Return a.Email
LIMIT 1
# What is the cell phone number for Joshua Spielman?
MATCH(a:Applicant) where a.LastName ='Spielman' and a.FirstName ='Joshua'
MATCH (a)-[:IS]-(status:Status)
WHERE status.OriginalName IN ['Newly added to the database', 'Recently changed', 'Not Changed', 'Lateral move', 'Lateral Move*', 'Newly Hired Graduates', 'Moved due to merger', 'SECONDMENT']
Return a.Phone
LIMIT 1
# What is the cell phone number for Samuel Lipson?
MATCH(a:Applicant) where a.LastName ='Lipson' and a.FirstName ='Samuel'
MATCH (a)-[:IS]-(status:Status)
WHERE status.OriginalName IN ['Newly added to the database', 'Recently changed', 'Not Changed', 'Lateral move', 'Lateral Move*', 'Newly Hired Graduates', 'Moved due to merger', 'SECONDMENT']
Return a.Phone
LIMIT 1
# Which candidates speak 2 or more languages at law firm Gibbons?
MATCH (lf:LawFirm {Name: 'Gibbons'})<-[:WORKS_AT]-(a:Applicant)
MATCH (a)-[:SPEAKS]->(l:Language)
WITH a, lf, COLLECT(l) AS languages
WHERE SIZE(languages) >= 2
RETURN a.FirstName, a.LastName
LIMIT 10;
# Which candidates speak 2 or more languages at law firm Morris Manning & Martin LLP?
MATCH (lf:LawFirm {Name: 'Morris Manning & Martin LLP'})<-[:WORKS_AT]-(a:Applicant)
MATCH (a)-[:SPEAKS]->(l:Language)
WITH a, lf, COLLECT(l) AS languages
WHERE SIZE(languages) >= 2
RETURN a.FirstName, a.LastName
LIMIT 10;
"""