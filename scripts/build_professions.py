import json

DATE = "31st July, 2026"

def cv(full_name, title, phone, email, location, summary, experience, school, skills, certs, langs, ref, linkedin=""):
    return {
        "personal": {"fullName": full_name, "title": title, "phone": phone, "email": email,
                     "location": location, "linkedin": linkedin, "summary": summary},
        "experience": experience,
        "education": [school] if isinstance(school, dict) else school,
        "skills": skills, "certifications": certs, "languages": langs,
        "references": [ref] if isinstance(ref, dict) else ref,
    }

def cl(full_name, phone, email, location, company, address, salutation, body, hiring="The Hiring Manager"):
    return {
        "personal": {"fullName": full_name, "phone": phone, "email": email, "location": location},
        "recipient": {"hiringManager": hiring, "company": company, "companyAddress": address},
        "date": DATE, "salutation": salutation, "body": body, "closing": "Yours faithfully,",
    }

def exp(company, position, dates, bullets):
    return {"company": company, "position": position, "dates": dates, "responsibilities": bullets}

def school(inst, degree, course, year):
    return {"institution": inst, "degree": degree, "course": course, "year": year}

def ref(name, relation, phone, email):
    return {"name": name, "relation": relation, "phone": phone, "email": email}

# ============================================================
# Existing 12 CV categories (rich data, unchanged from before)
# ============================================================
CV = {}
CL = {}

CV["software-engineer"] = cv(
    "Chinedu Okafor", "Frontend Software Engineer", "+234 803 555 0192", "chinedu.okafor@email.com", "Lekki, Lagos",
    "Frontend engineer with 4 years building fast, accessible web products for fintech and logistics companies. Comfortable owning a feature from design hand-off to production.",
    [exp("Flutterwave", "Software Engineer II", "Jan 2023 — Present", ["Led the rebuild of the merchant dashboard in React, cutting page load time by 38%", "Introduced a shared component library adopted across 3 product teams", "Mentored 2 junior engineers through onboarding"]),
     exp("Paystack", "Frontend Engineer", "Jul 2021 — Dec 2022", ["Built the checkout widget used by over 12,000 merchants", "Shipped a fully accessible, WCAG-compliant UI kit"])],
    school("University of Nigeria, Nsukka", "B.Sc. Computer Science", "Second Class Upper", "2017 — 2021"),
    ["JavaScript", "React", "TypeScript", "Node.js", "REST APIs", "Git", "Figma"],
    ["AWS Certified Cloud Practitioner"], ["English", "Igbo"],
    ref("Adaeze Nwankwo", "Engineering Manager, Flutterwave", "+234 802 111 2233", "adaeze.n@example.com"),
    linkedin="linkedin.com/in/chineduokafor",
)
CL["software-engineer"] = cl("Chinedu Okafor", "+234 803 555 0192", "chinedu.okafor@email.com", "Lekki, Lagos",
    "Flutterwave", "Plot 8 Providence Street, Lekki Phase 1, Lagos", "Dear Hiring Manager,",
    ["I am writing to apply for the Software Engineer role advertised on your careers page. I have 4 years of experience building fast, accessible web products, most recently leading a dashboard rebuild that cut page load time by 38%.",
     "I enjoy owning a feature end-to-end and have introduced shared component libraries that other teams have gone on to adopt.",
     "I would welcome the chance to bring this experience to your engineering team."])

CV["graduate-nysc"] = cv(
    "Amina Bello", "Corps Member (NYSC) | Accounting Graduate", "+234 810 222 4471", "amina.bello@email.com", "Kaduna, Nigeria",
    "Recent Accounting graduate currently serving with the NYSC, looking to bring strong analytical skills and a fast learning curve to an entry-level finance or administrative role.",
    [exp("Kaduna State Ministry of Finance (NYSC)", "Corps Member — Accounts Dept.", "Nov 2023 — Present", ["Reconcile monthly departmental expenditure reports", "Support budget tracking spreadsheets for 3 units"]),
     exp("First City Monument Bank (Internship)", "Intern, Retail Banking", "Jun 2022 — Aug 2022", ["Processed customer account opening documentation", "Shadowed the reconciliation team during month-end close"])],
    [school("Ahmadu Bello University, Zaria", "B.Sc. Accounting", "Second Class Upper Division", "2019 — 2023"),
     school("Command Day Secondary School, Kaduna", "WAEC / SSCE", "6 Credits incl. Mathematics & English", "2019")],
    ["Microsoft Excel", "QuickBooks", "Financial Reporting", "Data Entry", "Communication"],
    ["ICAN Foundation (in view)"], ["English", "Hausa"],
    ref("Mr. Yusuf Garba", "Head of Accounts, Kaduna State MOF", "+234 806 333 1122", "y.garba@example.com"),
)
CL["graduate-nysc"] = cl("Amina Bello", "+234 810 222 4471", "amina.bello@email.com", "Kaduna, Nigeria",
    "First City Monument Bank", "Primrose Tower, 17A Tinubu Street, Lagos", "Dear Hiring Manager,",
    ["I am writing to apply for the Graduate Trainee position advertised on your careers page. I hold a Second Class Upper degree in Accounting from Ahmadu Bello University and am currently completing my NYSC year with the Kaduna State Ministry of Finance.",
     "During an earlier internship at your bank, I processed customer account documentation and shadowed the reconciliation team, which gave me a solid grounding in retail banking operations.",
     "I would welcome the opportunity to bring that foundation, and my eagerness to learn, to your graduate programme."])

CV["banking-finance"] = cv(
    "Osilalu Ademuyiwa Taiwo", "Banking & Finance Professional", "+234 813 808 1696", "osilalu.taiwo@email.com", "Abeokuta, Ogun State",
    "Detail-oriented finance professional with 6 years' experience in retail banking operations, reconciliation and customer relationship management.",
    [exp("Zenith Bank Plc", "Operations Officer", "2020 — Present", ["Manage daily cash reconciliation for a branch handling over ₦400m in monthly transactions", "Reduced complaint resolution time by 30% via a new escalation process", "Train new tellers on core banking applications"]),
     exp("Access Bank Plc", "Teller", "2017 — 2020", ["Processed 120+ customer transactions daily with zero cash variance", "Cross-sold savings and loan products, exceeding targets by 15%"])],
    school("Olabisi Onabanjo University (OOU)", "B.Sc. Banking and Finance", "Second Class Upper Division", "2013 — 2017"),
    ["Cash Reconciliation", "Customer Relationship Management", "Core Banking Applications", "Regulatory Compliance", "MS Excel"],
    ["Chartered Institute of Bankers of Nigeria (CIBN) — Associate"], ["English", "Yoruba"],
    ref("Mrs. Funke Adeyemi", "Branch Manager, Zenith Bank", "+234 802 456 7890", "f.adeyemi@example.com"),
)
CL["banking-finance"] = cl("Osilalu Ademuyiwa Taiwo", "+234 813 808 1696", "osilalu.taiwo@email.com", "Abeokuta, Ogun State",
    "Zenith Bank Plc", "Plot 84, Ajose Adeogun Street, Victoria Island, Lagos", "Dear Hiring Manager,",
    ["I am applying for the Operations Officer position within your retail banking division. With six years' experience in cash reconciliation and customer relationship management, I have consistently maintained zero-error audit records across every branch I have served.",
     "At my current bank, I introduced an escalation process that cut complaint resolution time by 30%, and I regularly train new tellers on core banking systems and compliance procedures.",
     "I would appreciate the chance to discuss how my track record can support your operations team."])

CV["teacher-education"] = cv(
    "Blessing Iortyer", "Secondary School Mathematics Teacher", "+234 806 777 2214", "blessing.iortyer@email.com", "Makurdi, Benue State",
    "TRCN-certified Mathematics teacher with 5 years' classroom experience, known for raising WAEC pass rates through structured, exam-focused lesson planning.",
    [exp("Government Girls' Secondary School, Makurdi", "Mathematics Teacher (SS1 – SS3)", "2020 — Present", ["Improved WAEC Mathematics credit pass rate from 61% to 84% over 3 sessions", "Coordinate the school's mathematics club and inter-house quiz team", "Set and mark termly examinations for over 200 students"]),
     exp("Hope Model College", "NCE Teaching Practice", "2019 — 2020", ["Taught JSS Mathematics under supervision", "Developed low-cost teaching aids for large classes"])],
    school("Benue State University", "B.Sc. (Ed.) Mathematics", "Second Class Upper", "2015 — 2019"),
    ["Lesson Planning", "Classroom Management", "WAEC/NECO Exam Preparation", "Student Assessment", "Microsoft Office"],
    ["TRCN Registered Teacher"], ["English", "Tiv"],
    ref("Mr. Terhemba Ayem", "Vice Principal (Academics)", "+234 803 221 9987", "t.ayem@example.com"),
)
CL["teacher-education"] = cl("Blessing Iortyer", "+234 806 777 2214", "blessing.iortyer@email.com", "Makurdi, Benue State",
    "Greenfield International School", "12 Gboko Road, Makurdi, Benue State", "Dear Sir/Madam,",
    ["I am applying for the Mathematics Teacher position advertised in your recent notice. As a TRCN-registered teacher with five years' classroom experience, I raised my current school's WAEC Mathematics credit pass rate from 61% to 84% over three sessions.",
     "I bring structured, exam-focused lesson planning and genuine enthusiasm for helping students who typically struggle with the subject.",
     "I would be glad to discuss how I can contribute to your school's academic results."], hiring="The Principal")

CV["nurse-healthcare"] = cv(
    "Chiamaka Obi", "Registered Nurse", "+234 809 441 7723", "chiamaka.obi@email.com", "Enugu, Nigeria",
    "Compassionate registered nurse with 4 years of ward and outpatient experience, skilled in patient assessment, medication administration and calm handling of emergency cases.",
    [exp("University of Nigeria Teaching Hospital (UNTH)", "Staff Nurse, General Ward", "2021 — Present", ["Monitor and record vital signs for up to 20 patients per shift", "Administer medication in line with prescribed charts and safety protocols", "Support 2 newly qualified nurses through hospital onboarding"]),
     exp("Mercy Specialist Hospital", "Intern Nurse", "2020 — 2021", ["Assisted senior nurses during ward rounds and minor procedures", "Maintained accurate patient records"])],
    school("University of Nigeria, Enugu Campus", "B.NSc. Nursing Science", "Second Class Upper", "2015 — 2020"),
    ["Patient Assessment", "Medication Administration", "Wound Care", "Electronic Health Records", "Emergency Response"],
    ["Registered Nurse — Nursing & Midwifery Council of Nigeria (NMCN)", "Basic Life Support (BLS)"], ["English", "Igbo"],
    ref("Mrs. Ijeoma Nnaji", "Ward Matron, UNTH", "+234 807 552 3391", "i.nnaji@example.com"),
)
CL["nurse-healthcare"] = cl("Chiamaka Obi", "+234 809 441 7723", "chiamaka.obi@email.com", "Enugu, Nigeria",
    "Reddington Hospital", "12 Idowu Martins Street, Victoria Island, Lagos", "Dear Sir/Madam,",
    ["I am applying for the Registered Nurse position advertised on your careers page. I am a Nursing & Midwifery Council of Nigeria-registered nurse with four years of ward and outpatient experience at a teaching hospital.",
     "I am skilled in patient assessment, medication administration and calm handling of emergency cases, and I hold a current Basic Life Support certification.",
     "I would be glad to bring this experience and my commitment to patient care to your hospital."])

CV["government-civil-service"] = cv(
    "Ibrahim Sule", "Administrative Officer, Grade Level 09", "+234 805 662 1140", "ibrahim.sule@email.com", "Abuja, FCT",
    "Public sector administrator with 7 years managing correspondence, procurement documentation and inter-departmental coordination within a federal ministry.",
    [exp("Federal Ministry of Works", "Administrative Officer II", "2019 — Present", ["Coordinate correspondence between 4 departmental units", "Maintain procurement records in line with due-process guidelines", "Supervise 3 junior administrative staff"]),
     exp("Nasarawa State Civil Service Commission", "Executive Officer (Admin)", "2016 — 2019", ["Processed staff establishment and promotion files", "Organised departmental meetings and kept minutes"])],
    school("University of Abuja", "B.Sc. Public Administration", "Second Class Upper", "2011 — 2015"),
    ["Records Management", "Correspondence Drafting", "Procurement Documentation", "Microsoft Office", "Minute Taking"],
    ["ASCON Certificate in Public Administration"], ["English", "Hausa"],
    ref("Mrs. Grace Okon", "Deputy Director, Federal Ministry of Works", "+234 802 774 3320", "g.okon@example.com"),
)
CL["government-civil-service"] = cl("Ibrahim Sule", "+234 805 662 1140", "ibrahim.sule@email.com", "Abuja, FCT",
    "Federal Ministry of Works", "Mabushi District, Abuja, FCT", "Dear Sir/Madam,",
    ["I am applying for the Administrative Officer I position within your Ministry. I have seven years' experience coordinating correspondence and procurement documentation across departmental units in the federal civil service.",
     "In my current role I supervise three junior administrative staff and maintain full compliance with due-process procurement guidelines.",
     "I would be glad to bring this experience to your Ministry and remain available for an interview at your convenience."], hiring="The Permanent Secretary")

CV["sales-marketing"] = cv(
    "Damilola Fashola", "Sales & Marketing Executive", "+234 812 990 4456", "damilola.fashola@email.com", "Ikeja, Lagos",
    "Results-driven sales executive with 5 years growing FMCG distribution networks across South-West Nigeria, consistently exceeding quarterly revenue targets.",
    [exp("Nestlé Nigeria Plc", "Territory Sales Executive", "2021 — Present", ["Grew territory revenue by 22% year-on-year across 40+ retail outlets", "Onboarded 15 new distributor partners in Lagos and Ogun States", "Lead a team of 4 field sales representatives"]),
     exp("Promasidor Nigeria", "Sales Representative", "2018 — 2021", ["Managed a route of 60 retail accounts, hitting 105% of target on average", "Ran monthly trade promotions in open markets"])],
    school("Lagos State University", "B.Sc. Marketing", "Second Class Upper", "2014 — 2018"),
    ["Territory Management", "Trade Marketing", "Negotiation", "CRM Software", "Team Leadership"],
    ["Certified Sales Professional (NIMN)"], ["English", "Yoruba"],
    ref("Mr. Kunle Adisa", "Regional Sales Manager, Nestlé Nigeria", "+234 803 221 6690", "k.adisa@example.com"),
    linkedin="linkedin.com/in/damilolafashola",
)
CL["sales-marketing"] = cl("Damilola Fashola", "+234 812 990 4456", "damilola.fashola@email.com", "Ikeja, Lagos",
    "Unilever Nigeria Plc", "1 Billingsway Road, Oregun, Lagos", "Dear Hiring Manager,",
    ["I am writing to apply for the Territory Sales Manager role. Over the past five years I have grown FMCG distribution revenue by 22% year-on-year across more than forty retail outlets in South-West Nigeria.",
     "I have onboarded fifteen new distributor partners and currently lead a team of four field sales representatives, consistently exceeding quarterly targets.",
     "I would welcome the opportunity to bring this track record to your sales organisation."])

CV["customer-service-admin"] = cv(
    "Precious Effiong", "Customer Service Representative", "+234 807 213 6690", "precious.effiong@email.com", "Uyo, Akwa Ibom",
    "Personable customer service representative with 3 years' experience resolving inquiries across phone, email and live chat for a telecoms provider.",
    [exp("9mobile Nigeria", "Customer Service Representative", "2022 — Present", ["Resolve an average of 70 customer inquiries daily across chat and phone", "Maintain a customer satisfaction score above 92%", "Trained 5 new hires on the ticketing system"]),
     exp("Domino's Pizza Uyo", "Front Desk / Admin Assistant", "2020 — 2022", ["Managed walk-in customer orders and phone bookings", "Reconciled daily till reports for the outlet manager"])],
    school("University of Uyo", "B.A. English Studies", "Second Class Upper", "2016 — 2020"),
    ["Customer Support", "Conflict Resolution", "Zendesk", "Data Entry", "Phone Etiquette"],
    ["Customer Service Excellence Certificate"], ["English", "Ibibio"],
    ref("Mr. Emmanuel Udo", "Team Lead, 9mobile", "+234 806 112 4478", "e.udo@example.com"),
)
CL["customer-service-admin"] = cl("Precious Effiong", "+234 807 213 6690", "precious.effiong@email.com", "Uyo, Akwa Ibom",
    "MTN Nigeria", "Golden Plaza, Adeola Odeku Street, Victoria Island, Lagos", "Dear Hiring Manager,",
    ["I am applying for the Customer Service Representative role advertised on your careers page. I currently resolve an average of 70 customer inquiries daily across chat and phone while maintaining a satisfaction score above 92%.",
     "I have also trained new hires on our ticketing system and enjoy turning frustrated customers into satisfied ones.",
     "I would welcome the opportunity to bring this experience to your support team."])

CV["engineering-technical"] = cv(
    "David Olusoga Emmanuel", "Petroleum / Production Engineer", "+234 804 765 7432", "david.emmanuel@email.com", "Port Harcourt, Rivers State",
    "Quality-focused production engineer with a strong analytical foundation, experienced planning and supervising equipment maintenance in fast-paced drilling operations.",
    [exp("Top Notch Engineering", "Production Engineer", "2016 — Present", ["Analyse field operations to create improvement plans", "Supervise equipment maintenance across 3 active sites", "Plan and forecast drilling operations for new fields and expansions"]),
     exp("ABC Oil & Gas", "Production Manager", "2012 — 2015", ["Observed equipment state and drafted maintenance reports", "Presented operational findings to senior management"])],
    school("University of Lagos", "B.Sc. Petroleum Engineering", "Second Class Upper", "2005 — 2010"),
    ["Field Operations", "Equipment Maintenance Planning", "HSE Compliance", "Technical Reporting", "Team Supervision"],
    ["HSE Level 3 Certification"], ["English", "Yoruba"],
    ref("Engr. Samuel Adigun", "Operations Manager, Top Notch Engineering", "+234 802 998 1123", "s.adigun@example.com"),
)
CL["engineering-technical"] = cl("David Olusoga Emmanuel", "+234 804 765 7432", "david.emmanuel@email.com", "Port Harcourt, Rivers State",
    "Shell Petroleum Development Company", "Freeman House, 21/22 Marina, Lagos", "Dear Hiring Manager,",
    ["I am writing to express my interest in the Production Engineer role advertised on your careers portal. Over the past decade I have planned and supervised equipment maintenance across several active drilling sites, with a consistent focus on safety and uptime.",
     "My experience spans field operations analysis, maintenance planning and cross-functional reporting to senior management, and I hold an HSE Level 3 certification.",
     "I would welcome the opportunity to bring this experience to your operations team."])

CV["hospitality-hotel"] = cv(
    "Halima Yusuf", "Hotel Front Desk Supervisor", "+234 810 336 2298", "halima.yusuf@email.com", "Abuja, FCT",
    "Warm, detail-oriented hospitality professional with 4 years managing front-desk operations for a 3-star business hotel, known for turning first-time guests into repeat bookings.",
    [exp("Transcorp Hilton Abuja", "Front Desk Supervisor", "2021 — Present", ["Supervise a front-desk team of 6 across morning and evening shifts", "Maintain guest satisfaction scores above 4.6/5 on booking platforms", "Resolve escalated guest complaints within the same shift"]),
     exp("Nicon Luxury Hotel", "Front Desk Officer", "2019 — 2021", ["Managed check-in/check-out for up to 80 guests daily", "Coordinated with housekeeping to reduce room turnaround time"])],
    school("Federal Polytechnic Bauchi", "HND Hospitality Management", "Upper Credit", "2015 — 2019"),
    ["Front Office Operations", "Guest Relations", "Opera PMS", "Complaint Resolution", "Team Supervision"],
    ["Hospitality Management Certification"], ["English", "Hausa"],
    ref("Mr. Chuka Nwosu", "Front Office Manager, Transcorp Hilton", "+234 803 447 9912", "c.nwosu@example.com"),
)
CL["hospitality-hotel"] = cl("Halima Yusuf", "+234 810 336 2298", "halima.yusuf@email.com", "Abuja, FCT",
    "Sheraton Lagos Hotel", "30 Mobolaji Bank Anthony Way, Ikeja, Lagos", "Dear Hiring Manager,",
    ["I am applying for the Front Desk Supervisor role advertised on your careers page. I currently supervise a team of six across shifts at a leading Abuja hotel, maintaining guest satisfaction scores above 4.6 out of 5.",
     "I am comfortable resolving escalated complaints within the same shift and coordinating closely with housekeeping to reduce guest wait times.",
     "I would welcome the chance to bring this experience to your front-office team."])

CV["construction-trades"] = cv(
    "Sunday Okonkwo", "Site Supervisor (Building Construction)", "+234 806 221 7754", "sunday.okonkwo@email.com", "Owerri, Imo State",
    "Hands-on site supervisor with 8 years overseeing residential and light-commercial builds, focused on safety compliance and keeping projects on schedule.",
    [exp("Julius Berger Nigeria Plc", "Site Supervisor", "2018 — Present", ["Supervise up to 25 site workers across 2 concurrent building projects", "Enforce site safety protocols, maintaining zero lost-time incidents in 3 years", "Liaise with project engineers on material scheduling"]),
     exp("Setraco Nigeria Ltd", "Foreman", "2014 — 2018", ["Coordinated daily labour assignments for masonry and finishing crews", "Tracked material usage against project budget"])],
    school("Federal Polytechnic Nekede", "OND Building Technology", "Upper Credit", "2011 — 2013"),
    ["Site Supervision", "Health & Safety Compliance", "Material Scheduling", "Team Coordination", "Reading Building Plans"],
    ["NIOSH-Certified Site Safety Officer"], ["English", "Igbo"],
    ref("Engr. Peter Anya", "Project Manager, Julius Berger", "+234 807 662 1190", "p.anya@example.com"),
)
CL["construction-trades"] = cl("Sunday Okonkwo", "+234 806 221 7754", "sunday.okonkwo@email.com", "Owerri, Imo State",
    "Julius Berger Nigeria Plc", "Plot 1679, Karimu Kotun Street, Victoria Island, Lagos", "Dear Hiring Manager,",
    ["I am applying for the Site Supervisor role advertised in your recent notice. I have eight years' experience overseeing residential and light-commercial builds, currently supervising up to 25 workers across two concurrent projects.",
     "I have maintained zero lost-time safety incidents over the past three years and work closely with project engineers on material scheduling.",
     "I would welcome the opportunity to bring this record to your site team."])

CV["legal-paralegal"] = cv(
    "Folasade Adekunle", "Paralegal / Legal Assistant", "+234 802 556 8871", "folasade.adekunle@email.com", "Ikoyi, Lagos",
    "Organised paralegal with 4 years supporting corporate and litigation teams — drafting court documents, managing case files and coordinating with external counsel.",
    [exp("Aluko & Oyebode", "Paralegal", "2021 — Present", ["Draft and proofread pleadings, briefs and corporate filings for partner review", "Maintain and index case files for over 30 active matters", "Coordinate scheduling between counsel, clients and the courts"]),
     exp("Femi Falana & Co.", "Law Intern", "2020 — 2021", ["Conducted legal research for ongoing litigation matters", "Assisted with document discovery and bundling"])],
    school("University of Lagos", "LL.B. Law", "Second Class Upper", "2015 — 2019"),
    ["Legal Drafting", "Legal Research", "Case File Management", "Corporate Filings", "MS Office"],
    ["Nigerian Law School — Called to Bar"], ["English", "Yoruba"],
    ref("Barr. Chidinma Eze", "Senior Associate, Aluko & Oyebode", "+234 803 118 2274", "c.eze@example.com"),
    linkedin="linkedin.com/in/folasadeadekunle",
)
CL["legal-paralegal"] = cl("Folasade Adekunle", "+234 802 556 8871", "folasade.adekunle@email.com", "Ikoyi, Lagos",
    "Templars", "The Octagon, 13 A.J. Marinho Drive, Victoria Island, Lagos", "Dear Hiring Manager,",
    ["I am writing to apply for the Paralegal position advertised on your careers page. I have four years' experience supporting corporate and litigation teams, drafting pleadings and maintaining case files for over thirty active matters.",
     "I am comfortable coordinating scheduling between counsel, clients and the courts, and I bring careful attention to detail to every filing.",
     "I would welcome the opportunity to discuss how I can support your legal team."])

# ============================================================
# "General" — added as CV category too (was CL-only before)
# ============================================================
CV["general"] = cv(
    "Ngozi Eze", "Administrative Officer", "+234 807 654 3210", "ngozi.eze@email.com", "Victoria Island, Lagos",
    "Organised administrative professional with 3 years coordinating office operations, vendor relationships and scheduling for a fast-growing logistics firm.",
    [exp("Brightpath Logistics Ltd", "Administrative Officer", "2022 — Present", ["Manage scheduling for a 15-person team", "Oversee vendor relationships and contract renewals", "Reduced procurement turnaround time by 20% through a new approval workflow"]),
     exp("Interstate Freight Ltd", "Office Assistant", "2020 — 2022", ["Handled front-desk enquiries and correspondence", "Maintained office supply inventory and records"])],
    school("University of Lagos", "B.A. English Language", "Second Class Upper", "2016 — 2020"),
    ["Office Administration", "Scheduling", "Vendor Management", "Microsoft Office", "Communication"],
    ["Certificate in Office Management"], ["English", "Igbo"],
    ref("Mr. Femi Adekoya", "Operations Director, Brightpath Logistics", "+234 803 221 5567", "f.adekoya@example.com"),
)
CL["general"] = cl("Ngozi Eze", "+234 807 654 3210", "ngozi.eze@email.com", "Victoria Island, Lagos",
    "Brightpath Consulting Ltd", "14 Adeola Odeku Street, Victoria Island, Lagos", "Dear Hiring Manager,",
    ["I am writing to apply for the Administrative Officer role advertised on your careers page. With over three years of experience coordinating office operations for a fast-growing logistics firm, I am confident I can bring the same organisation and reliability to your team.",
     "In my current role, I manage scheduling for a 15-person team, oversee vendor relationships and have reduced procurement turnaround time by 20% through a simple approval workflow I introduced.",
     "I would welcome the opportunity to discuss how my background fits your needs. Thank you for considering my application."])

# ============================================================
# 33 new categories
# ============================================================
NEW = [
    dict(id="logistics-supply-chain", name="Logistics & Supply Chain", tags=["Logistics","Supply Chain","Warehouse"],
        person="Tobenna Nwachukwu", title="Logistics Coordinator", phone="+234 803 214 7765", loc="Apapa, Lagos",
        summary="Logistics coordinator with 5 years managing freight scheduling and warehouse dispatch for an FMCG distributor.",
        emp=[("Dangote Group","Logistics Coordinator","2020 — Present",["Coordinate daily dispatch for a fleet of 30 trucks","Reduced average delivery turnaround time by 18%"]),
             ("GIG Logistics","Dispatch Officer","2017 — 2020",["Tracked shipment status across 5 regional hubs","Resolved delivery discrepancies with customers and drivers"])],
        school=("University of Port Harcourt","B.Sc. Logistics & Transport Management","Second Class Upper","2012 — 2016"),
        skills=["Freight Scheduling","Inventory Tracking","Fleet Coordination","SAP","Route Planning"], certs=["Certified Supply Chain Professional (in view)"], langs=["English","Igbo"],
        ref=("Mr. Bassey Etim","Logistics Manager, Dangote Group","+234 802 556 4432","b.etim@example.com"),
        cl_company="GIG Logistics", cl_addr="Plot 1648, Oyin Jolayemi Street, Victoria Island, Lagos",
        cl_body=["I am applying for the Logistics Coordinator role advertised on your careers page. I currently coordinate daily dispatch for a 30-truck fleet and have reduced average delivery turnaround time by 18%.","I am comfortable resolving shipment discrepancies quickly and working across multiple regional hubs.","I would welcome the opportunity to bring this experience to your logistics team."]),

    dict(id="human-resources", name="Human Resources", tags=["HR","Human Resources","Recruitment"],
        person="Chiamaka Ibe", title="HR Officer", phone="+234 806 442 1187", loc="Ikoyi, Lagos",
        summary="HR officer with 5 years managing recruitment, onboarding and employee relations for a mid-sized professional services firm.",
        emp=[("KPMG Nigeria","HR Officer","2021 — Present",["Manage end-to-end recruitment for 40+ hires annually","Coordinate onboarding and orientation for new staff"]),
             ("Andersen Tax Nigeria","HR Assistant","2018 — 2021",["Maintained employee records and leave tracking","Supported quarterly performance appraisal cycles"])],
        school=("University of Ibadan","B.Sc. Industrial Relations & Personnel Management","Second Class Upper","2013 — 2017"),
        skills=["Recruitment","Onboarding","Employee Relations","HRIS Systems","Performance Management"], certs=["CIPM (in view)"], langs=["English","Yoruba"],
        ref=("Mrs. Ada Obiora","HR Manager, KPMG Nigeria","+234 803 990 2214","a.obiora@example.com"),
        cl_company="PwC Nigeria", cl_addr="Landmark Towers, 5B Water Corporation Road, Victoria Island, Lagos",
        cl_body=["I am applying for the HR Officer role advertised on your careers page. I currently manage end-to-end recruitment for over 40 hires annually and coordinate onboarding for new staff.","I have a strong track record maintaining accurate employee records and supporting performance appraisal cycles.","I would welcome the opportunity to bring this experience to your HR team."]),

    dict(id="marketing-communications", name="Marketing & Communications", tags=["Marketing","Communications","PR","Brand"],
        person="Zainab Adamu", title="Marketing Communications Officer", phone="+234 809 776 5521", loc="Wuse, Abuja",
        summary="Communications officer with 4 years running brand campaigns and media relations for a consumer goods company.",
        emp=[("Nigerian Breweries Plc","Marketing Communications Officer","2021 — Present",["Plan and execute integrated campaigns across social and traditional media","Manage relationships with 6 media and PR agencies"]),
             ("Cool FM Abuja","Media Relations Assistant","2019 — 2021",["Drafted press releases and media kits","Coordinated interviews and event coverage"])],
        school=("Bayero University Kano","B.A. Mass Communication","Second Class Upper","2014 — 2018"),
        skills=["Brand Campaigns","Media Relations","Content Strategy","Social Media Management","Copywriting"], certs=["Google Digital Marketing Certificate"], langs=["English","Hausa"],
        ref=("Mr. Ade Bankole","Brand Manager, Nigerian Breweries","+234 802 331 7789","a.bankole@example.com"),
        cl_company="Coca-Cola Hellenic Bottling Company Nigeria", cl_addr="35 Iyalla Street, Off Osborne Road, Ikoyi, Lagos",
        cl_body=["I am writing to apply for the Marketing Communications Officer role advertised on your careers page. I currently plan integrated campaigns across social and traditional media, and manage relationships with six media and PR agencies.","My background in media relations has given me a strong sense of how to protect and grow a brand's public image.","I would welcome the opportunity to bring this experience to your marketing team."]),

    dict(id="agriculture-agribusiness", name="Agriculture & Agribusiness", tags=["Agriculture","Agribusiness","Farm Management"],
        person="Musa Danladi", title="Farm Operations Manager", phone="+234 803 667 2290", loc="Kaduna, Nigeria",
        summary="Farm operations manager with 6 years overseeing large-scale maize and soybean production, from planting through to market delivery.",
        emp=[("Olam Agri Nigeria","Farm Operations Manager","2019 — Present",["Manage 800 hectares of maize and soybean cultivation","Improved yield per hectare by 25% through improved irrigation scheduling"]),
             ("Kaduna State Agricultural Development Project","Field Extension Officer","2015 — 2019",["Trained over 200 smallholder farmers on modern planting techniques","Monitored crop health and pest control across 12 farming communities"])],
        school=("Ahmadu Bello University, Zaria","B.Agric. Agronomy","Second Class Upper","2010 — 2014"),
        skills=["Farm Operations Management","Irrigation Scheduling","Crop Monitoring","Yield Optimisation","Team Supervision"], certs=["Good Agricultural Practices (GAP) Certification"], langs=["English","Hausa"],
        ref=("Dr. Aliyu Bello","Regional Manager, Olam Agri Nigeria","+234 806 221 3345","a.bello@example.com"),
        cl_company="Olam Agri Nigeria", cl_addr="1 Olam Way, Kaduna Industrial Estate, Kaduna",
        cl_body=["I am applying for the Farm Operations Manager role advertised on your careers page. I currently manage 800 hectares of maize and soybean production and have improved yield per hectare by 25% through better irrigation scheduling.","I have trained over 200 smallholder farmers on modern techniques and enjoy building strong field teams.","I would welcome the opportunity to bring this experience to your agribusiness operation."]),

    dict(id="oil-gas", name="Oil & Gas (Support Roles)", tags=["Oil & Gas","Energy"],
        person="Ebiere Amachree", title="HSE Officer", phone="+234 803 552 1198", loc="Port Harcourt, Rivers State",
        summary="HSE officer with 5 years enforcing safety compliance across upstream oil and gas field operations.",
        emp=[("Seplat Energy","HSE Officer","2020 — Present",["Conduct daily safety audits across 2 flow stations","Maintained zero lost-time injury record for 3 consecutive years"]),
             ("Schlumberger Nigeria","HSE Field Assistant","2017 — 2020",["Supported permit-to-work processes on rig sites","Delivered weekly toolbox talks to field crews"])],
        school=("Rivers State University","B.Eng. Petroleum Engineering","Second Class Upper","2012 — 2016"),
        skills=["Safety Audits","Permit-to-Work Systems","Incident Investigation","Risk Assessment","Toolbox Talks"], certs=["NEBOSH International General Certificate"], langs=["English","Ijaw"],
        ref=("Engr. Tamuno Wiri","HSE Manager, Seplat Energy","+234 802 774 6612","t.wiri@example.com"),
        cl_company="Seplat Energy", cl_addr="16A Temple Road, Ikoyi, Lagos",
        cl_body=["I am writing to apply for the HSE Officer role advertised on your careers page. I currently conduct daily safety audits across two flow stations and have maintained a zero lost-time injury record for three consecutive years.","I bring hands-on experience with permit-to-work systems and incident investigation from field operations.","I would welcome the opportunity to bring this safety record to your operations team."]),

    dict(id="telecommunications", name="Telecommunications", tags=["Telecoms","Network","GSM"],
        person="Sadiq Aliyu", title="Network Support Engineer", phone="+234 807 118 4432", loc="Kano, Nigeria",
        summary="Network support engineer with 4 years maintaining GSM base station uptime across a regional telecoms network.",
        emp=[("Airtel Nigeria","Network Support Engineer","2021 — Present",["Maintain 99.2% average uptime across 60 base stations","Lead first-response troubleshooting for network outages"]),
             ("Huawei Technologies Nigeria","Field Support Technician","2019 — 2021",["Installed and commissioned new base transceiver stations","Carried out preventive maintenance across 3 states"])],
        school=("Bayero University Kano","B.Eng. Electrical & Electronics Engineering","Second Class Upper","2014 — 2018"),
        skills=["Network Troubleshooting","Base Station Maintenance","GSM/LTE Systems","Preventive Maintenance","Reporting"], certs=["Huawei Certified ICT Associate (HCIA)"], langs=["English","Hausa"],
        ref=("Engr. Yakubu Musa","Regional Network Manager, Airtel Nigeria","+234 803 221 9987","y.musa@example.com"),
        cl_company="MTN Nigeria", cl_addr="Golden Plaza, Adeola Odeku Street, Victoria Island, Lagos",
        cl_body=["I am applying for the Network Support Engineer role advertised on your careers page. I currently maintain 99.2% average uptime across 60 base stations and lead first-response troubleshooting for outages.","I have hands-on experience installing and commissioning base stations across multiple states.","I would welcome the opportunity to bring this experience to your network operations team."]),

    dict(id="manufacturing-production", name="Manufacturing & Production", tags=["Manufacturing","Production","Factory"],
        person="Chukwuemeka Aneke", title="Production Supervisor", phone="+234 802 445 7723", loc="Aba, Abia State",
        summary="Production supervisor with 6 years running shift operations on a fast-moving consumer goods packaging line.",
        emp=[("Unilever Nigeria Plc","Production Supervisor","2019 — Present",["Supervise a 20-person shift on the packaging line","Reduced downtime by 15% through improved changeover procedures"]),
             ("PZ Cussons Nigeria","Line Operator","2015 — 2019",["Operated and monitored automated filling machines","Maintained quality checks every 30 minutes per SOP"])],
        school=("Federal Polytechnic Nekede","HND Mechanical Engineering","Upper Credit","2011 — 2013"),
        skills=["Shift Supervision","Line Changeover","Quality Control","Lean Manufacturing","SOP Compliance"], certs=["Six Sigma Yellow Belt"], langs=["English","Igbo"],
        ref=("Mr. Obinna Okeke","Plant Manager, Unilever Nigeria","+234 803 662 1187","o.okeke@example.com"),
        cl_company="PZ Cussons Nigeria", cl_addr="45/47 Town Planning Way, Ilupeju, Lagos",
        cl_body=["I am applying for the Production Supervisor role advertised on your careers page. I currently supervise a 20-person shift on a packaging line and reduced downtime by 15% through improved changeover procedures.","I bring a strong quality-control mindset from years spent monitoring automated filling lines.","I would welcome the opportunity to bring this experience to your production team."]),

    dict(id="real-estate", name="Real Estate", tags=["Real Estate","Property","Estate Management"],
        person="Ifeoma Chukwu", title="Estate Surveyor & Valuer", phone="+234 803 221 6674", loc="Lekki, Lagos",
        summary="Registered estate surveyor with 5 years in property valuation, facility management and client-facing sales across Lagos.",
        emp=[("Northcourt Real Estate","Estate Surveyor","2020 — Present",["Conduct property valuations for over 50 residential and commercial assets annually","Manage client relationships for a portfolio of 30 rental properties"]),
             ("Alpha Mead Facilities","Facility Management Officer","2017 — 2020",["Coordinated maintenance schedules across 4 commercial properties","Managed vendor contracts and service level agreements"])],
        school=("University of Lagos","B.Sc. Estate Management","Second Class Upper","2012 — 2016"),
        skills=["Property Valuation","Facility Management","Client Relationship Management","Lease Negotiation","Market Research"], certs=["ANIVS/RSV Registered Member"], langs=["English","Igbo"],
        ref=("Mr. Ayodeji Fashola","Managing Partner, Northcourt Real Estate","+234 802 990 1123","a.fashola@example.com"),
        cl_company="Northcourt Real Estate", cl_addr="9 Ladipo Kasumu Street, Lekki Phase 1, Lagos",
        cl_body=["I am writing to apply for the Estate Surveyor role advertised on your careers page. I currently conduct valuations for over 50 residential and commercial assets annually and manage a portfolio of 30 rental properties.","I bring strong facility management experience, including vendor and service-level agreement oversight.","I would welcome the opportunity to bring this experience to your team."]),

    dict(id="insurance", name="Insurance", tags=["Insurance","Underwriting","Claims"],
        person="Boluwatife Ogunleye", title="Insurance Claims Officer", phone="+234 806 331 8842", loc="Ikeja, Lagos",
        summary="Claims officer with 4 years processing motor and property insurance claims for a leading underwriting firm.",
        emp=[("AXA Mansard Insurance","Claims Officer","2021 — Present",["Process an average of 40 motor and property claims monthly","Reduced average claim settlement time from 21 to 14 days"]),
             ("Leadway Assurance","Underwriting Assistant","2019 — 2021",["Assessed policy applications for risk classification","Prepared quotations for corporate clients"])],
        school=("University of Lagos","B.Sc. Insurance","Second Class Upper","2015 — 2019"),
        skills=["Claims Processing","Risk Assessment","Policy Underwriting","Customer Communication","MS Excel"], certs=["Chartered Insurance Institute of Nigeria (CIIN) — Associate"], langs=["English","Yoruba"],
        ref=("Mrs. Yetunde Bakare","Claims Manager, AXA Mansard","+234 803 774 2298","y.bakare@example.com"),
        cl_company="Leadway Assurance", cl_addr="121/123 Funso Williams Avenue, Iponri, Lagos",
        cl_body=["I am applying for the Claims Officer role advertised on your careers page. I currently process an average of 40 motor and property claims monthly and reduced average settlement time from 21 to 14 days.","I bring strong risk assessment skills from earlier underwriting experience.","I would welcome the opportunity to bring this experience to your claims team."]),

    dict(id="accounting-audit", name="Accounting & Audit", tags=["Accounting","Audit","Bookkeeping"],
        person="Adaora Nwosu", title="Audit Associate", phone="+234 802 116 7734", loc="Ikoyi, Lagos",
        summary="Audit associate with 4 years conducting statutory audits for clients in manufacturing and financial services.",
        emp=[("Deloitte Nigeria","Audit Associate","2021 — Present",["Lead fieldwork for statutory audits of 8 mid-sized clients annually","Prepare audit working papers in line with ISA standards"]),
             ("Ernst & Young Nigeria","Audit Trainee","2019 — 2021",["Assisted with inventory counts and substantive testing","Reconciled client trial balances against general ledgers"])],
        school=("University of Nigeria, Nsukka","B.Sc. Accounting","Second Class Upper","2015 — 2019"),
        skills=["Statutory Audit","Financial Reporting","IFRS", "Excel Modelling", "Audit Documentation"], certs=["ICAN — Chartered Accountant"], langs=["English","Igbo"],
        ref=("Mr. Tunde Are","Audit Manager, Deloitte Nigeria","+234 803 221 8890","t.are@example.com"),
        cl_company="KPMG Nigeria", cl_addr="KPMG Tower, Bishop Aboyade Cole Street, Victoria Island, Lagos",
        cl_body=["I am applying for the Audit Associate role advertised on your careers page. I currently lead fieldwork for statutory audits of eight mid-sized clients annually and prepare working papers to ISA standards.","I am a Chartered Accountant with strong grounding in IFRS reporting and audit documentation.","I would welcome the opportunity to bring this experience to your audit team."]),

    dict(id="procurement", name="Procurement & Purchasing", tags=["Procurement","Purchasing","Vendor Management"],
        person="Chidi Umeh", title="Procurement Officer", phone="+234 807 552 3391", loc="Port Harcourt, Rivers State",
        summary="Procurement officer with 5 years sourcing and negotiating supplier contracts for an oil-servicing company.",
        emp=[("Baker Hughes Nigeria","Procurement Officer","2020 — Present",["Manage a supplier base of over 60 vendors","Negotiated contract terms that saved ₦18m annually"]),
             ("Julius Berger Nigeria","Purchasing Assistant","2017 — 2020",["Processed purchase orders and tracked delivery timelines","Maintained supplier performance scorecards"])],
        school=("University of Port Harcourt","B.Sc. Purchasing & Supply","Second Class Upper","2012 — 2016"),
        skills=["Vendor Negotiation","Contract Management","Purchase Order Processing","Supplier Evaluation","SAP Ariba"], certs=["Chartered Institute of Purchasing & Supply Management of Nigeria (CIPSMN)"], langs=["English","Igbo"],
        ref=("Mr. Godswill Amadi","Procurement Manager, Baker Hughes","+234 802 774 1123","g.amadi@example.com"),
        cl_company="Baker Hughes Nigeria", cl_addr="1 Baker Hughes Close, Trans Amadi, Port Harcourt",
        cl_body=["I am applying for the Procurement Officer role advertised on your careers page. I currently manage a supplier base of over 60 vendors and negotiated contract terms that saved ₦18 million annually.","I bring strong experience in purchase order processing and supplier performance evaluation.","I would welcome the opportunity to bring this experience to your procurement team."]),

    dict(id="security-services", name="Security Services", tags=["Security","Safety","Guard Services"],
        person="Emeka Obasi", title="Security Supervisor", phone="+234 803 221 4471", loc="Victoria Island, Lagos",
        summary="Security supervisor with 7 years managing access control and patrol operations for corporate facilities.",
        emp=[("Interguard Security Services","Security Supervisor","2018 — Present",["Supervise a team of 18 security officers across 3 shifts","Reduced facility incidents by 40% through improved access control procedures"]),
             ("Nigerian Army (Discharged)","Corporal","2010 — 2018",["Served in logistics and base security roles","Trained junior personnel on patrol and surveillance protocols"])],
        school=("National Open University of Nigeria","Diploma in Security Management","Merit","2016 — 2018"),
        skills=["Access Control", "Patrol Management", "CCTV Monitoring", "Incident Reporting", "Team Supervision"], certs=["Nigeria Security and Civil Defence Corps (NSCDC) Certified"], langs=["English","Igbo"],
        ref=("Mr. Kelechi Iheanacho","Operations Manager, Interguard Security","+234 802 556 7789","k.iheanacho@example.com"),
        cl_company="Interguard Security Services", cl_addr="15 Karimu Kotun Street, Victoria Island, Lagos",
        cl_body=["I am writing to apply for the Security Supervisor role advertised on your careers page. I currently supervise 18 security officers across three shifts and reduced facility incidents by 40% through improved access control.","My background includes military logistics and base security experience.","I would welcome the opportunity to bring this experience to your security team."]),

    dict(id="driving-transport", name="Driving & Transport", tags=["Driver","Transport","Logistics"],
        person="Yakubu Adamu", title="Professional Driver", phone="+234 806 221 5567", loc="Kano, Nigeria",
        summary="Professional driver with 9 years of accident-free driving, experienced with executive transport and long-haul logistics.",
        emp=[("ABC Transport","Long-Haul Driver","2018 — Present",["Complete over 200 inter-state trips annually with zero at-fault accidents","Maintain accurate trip and fuel logs"]),
             ("Private Household","Personal Driver","2014 — 2018",["Provided daily executive transport in Kano metropolis","Maintained vehicle servicing schedule"])],
        school=("Government Secondary School, Kano","SSCE","5 Credits including Mathematics and English","2010"),
        skills=["Defensive Driving","Route Planning","Vehicle Maintenance Checks","Time Management","Customer Courtesy"], certs=["FRSC Certified Professional Driver's Licence"], langs=["English","Hausa"],
        ref=("Alhaji Sani Bello","Fleet Manager, ABC Transport","+234 803 774 2298","s.bello@example.com"),
        cl_company="ABC Transport", cl_addr="Km 3, Zaria Road, Kano",
        cl_body=["I am applying for the Driver role advertised on your careers page. I have nine years of accident-free driving, including over 200 inter-state trips annually with zero at-fault incidents.","I hold a valid FRSC professional licence and maintain careful trip and fuel records.","I would welcome the opportunity to bring this reliability to your transport team."]),

    dict(id="fashion-tailoring", name="Fashion & Tailoring", tags=["Fashion","Tailoring","Fashion Design"],
        person="Aisha Suleiman", title="Fashion Designer / Tailor", phone="+234 809 445 1123", loc="Kaduna, Nigeria",
        summary="Fashion designer and tailor with 6 years running a made-to-measure atelier specialising in bridal and Ankara wear.",
        emp=[("Aisha Couture (Self-Employed)","Founder / Lead Designer","2019 — Present",["Design and produce 15+ bespoke bridal and occasion outfits monthly","Manage a team of 4 tailors and 2 apprentices"]),
             ("Zaria Fashion House","Junior Tailor","2016 — 2019",["Cut and sewed made-to-measure garments to client specifications","Assisted with pattern drafting for new collections"])],
        school=("Kaduna Polytechnic","OND Fashion Design & Clothing Technology","Upper Credit","2014 — 2016"),
        skills=["Pattern Drafting","Bridal Wear Design","Fabric Sourcing","Team Supervision","Client Consultation"], certs=["Fashion Design Certification, Kaduna Polytechnic"], langs=["English","Hausa"],
        ref=("Mrs. Hadiza Ibrahim","Owner, Zaria Fashion House","+234 803 221 4471","h.ibrahim@example.com"),
        cl_company="House of Tara International", cl_addr="16A Emina Cres, Off Adeniyi Jones, Ikeja, Lagos",
        cl_body=["I am writing to apply for the Fashion Designer role advertised on your careers page. I currently run my own atelier producing over 15 bespoke bridal and occasion outfits monthly, leading a team of 4 tailors.","I bring strong pattern-drafting skills and hands-on experience managing client consultations from concept to delivery.","I would welcome the opportunity to bring this experience to your design team."]),

    dict(id="beauty-cosmetology", name="Beauty & Cosmetology", tags=["Beauty","Makeup","Cosmetology","Salon"],
        person="Blessing Nnamdi", title="Makeup Artist & Salon Manager", phone="+234 802 665 1187", loc="Surulere, Lagos",
        summary="Makeup artist and salon manager with 5 years serving bridal and editorial clients across Lagos.",
        emp=[("Blessing Beauty Studio (Self-Employed)","Founder / Lead Makeup Artist","2020 — Present",["Serve over 100 bridal clients annually with a 4-person team","Manage bookings, inventory and client consultations"]),
             ("Zaron Cosmetics","Makeup Trainer","2018 — 2020",["Trained over 50 aspiring makeup artists on technique and product use","Represented the brand at trade exhibitions"])],
        school=("Lagos State Polytechnic","OND Cosmetology","Upper Credit","2015 — 2017"),
        skills=["Bridal Makeup","Editorial Makeup","Client Consultation","Team Management","Inventory Management"], certs=["Certified Professional Makeup Artist (CPMA)"], langs=["English","Yoruba"],
        ref=("Mrs. Toke Adeyemi","Brand Manager, Zaron Cosmetics","+234 803 445 2298","t.adeyemi@example.com"),
        cl_company="Zaron Cosmetics", cl_addr="23 Allen Avenue, Ikeja, Lagos",
        cl_body=["I am applying for the Makeup Artist / Trainer role advertised on your careers page. I run a bridal makeup studio serving over 100 clients annually and previously trained more than 50 aspiring artists for your brand.","I combine strong technical skill with an ability to teach and represent a brand at public events.","I would welcome the opportunity to bring this experience back to your team."]),

    dict(id="culinary-chef", name="Culinary Arts / Chef", tags=["Chef","Culinary","Kitchen","Catering"],
        person="Ikenna Obi", title="Sous Chef", phone="+234 803 221 6690", loc="Ikoyi, Lagos",
        summary="Sous chef with 6 years of kitchen experience across fine-dining and large-scale event catering.",
        emp=[("Radisson Blu Lagos Ikeja","Sous Chef","2020 — Present",["Manage a kitchen brigade of 12 across breakfast, lunch and dinner service","Redesigned the seasonal menu, improving food cost margins by 8%"]),
             ("Yellow Chilli Restaurant","Line Cook","2016 — 2020",["Prepared Nigerian and continental dishes to standard recipes","Maintained HACCP food safety compliance"])],
        school=("Lagos City Polytechnic","National Diploma in Hotel & Catering Management","Upper Credit","2013 — 2015"),
        skills=["Menu Development","Kitchen Management","Food Costing","HACCP Compliance","Team Training"], certs=["HACCP Food Safety Certification"], langs=["English","Igbo"],
        ref=("Chef Uche Nnamdi","Executive Chef, Radisson Blu Lagos","+234 802 774 3320","u.nnamdi@example.com"),
        cl_company="Radisson Blu Lagos Victoria Island", cl_addr="Plot 1415, Ahmadu Bello Way, Victoria Island, Lagos",
        cl_body=["I am applying for the Sous Chef role advertised on your careers page. I currently manage a 12-person kitchen brigade and redesigned our seasonal menu, improving food cost margins by 8%.","I bring strong HACCP compliance discipline and enjoy training junior kitchen staff.","I would welcome the opportunity to bring this experience to your kitchen team."]),

    dict(id="aviation", name="Aviation", tags=["Aviation","Airline","Airport Operations"],
        person="Ifeanyi Chukwuma", title="Airport Ground Operations Officer", phone="+234 806 774 2298", loc="Ikeja, Lagos",
        summary="Ground operations officer with 5 years coordinating aircraft turnaround and passenger services at a major domestic airport.",
        emp=[("Air Peace","Ground Operations Officer","2020 — Present",["Coordinate aircraft turnaround for up to 12 flights daily","Liaise with catering, fuelling and baggage teams to maintain on-time departure"]),
             ("Murtala Muhammed Airport (FAAN)","Passenger Services Assistant","2017 — 2020",["Managed check-in and boarding gate operations","Assisted passengers with special needs and irregular operations"])],
        school=("Nigerian College of Aviation Technology, Zaria","Diploma in Airport Operations","Merit","2015 — 2017"),
        skills=["Aircraft Turnaround Coordination","Passenger Services","Ramp Safety","Irregular Operations Handling","Communication"], certs=["IATA Airport Ramp Services Certificate"], langs=["English","Igbo"],
        ref=("Capt. Nnamdi Eze","Station Manager, Air Peace","+234 803 221 7789","n.eze@example.com"),
        cl_company="Air Peace", cl_addr="Murtala Muhammed Airport, Domestic Wing, Ikeja, Lagos",
        cl_body=["I am writing to apply for the Ground Operations Officer role advertised on your careers page. I currently coordinate turnaround for up to 12 flights daily, working closely with catering, fuelling and baggage teams.","I hold an IATA Ramp Services certificate and have direct experience handling irregular operations.","I would welcome the opportunity to bring this experience to your ground operations team."]),

    dict(id="maritime-shipping", name="Maritime & Shipping", tags=["Maritime","Shipping","Ports"],
        person="Preye Ockiya", title="Shipping Documentation Officer", phone="+234 803 662 1187", loc="Apapa, Lagos",
        summary="Shipping documentation officer with 4 years processing import/export documentation for a freight forwarding firm at Apapa Port.",
        emp=[("Maersk Nigeria","Shipping Documentation Officer","2021 — Present",["Process bills of lading and customs documentation for 50+ containers weekly","Liaise with NPA and NCS on clearance procedures"]),
             ("SIFAX Group","Documentation Assistant","2019 — 2021",["Prepared export documentation for agricultural commodities","Tracked container demurrage and detention charges"])],
        school=("Rivers State University","B.Sc. Maritime Transport & Business Studies","Second Class Upper","2014 — 2018"),
        skills=["Shipping Documentation","Customs Clearance","Bill of Lading Processing","NPA/NCS Liaison","Container Tracking"], certs=["Nigerian Institute of Shipping — Certificate"], langs=["English","Ijaw"],
        ref=("Mr. Ebi Sam","Operations Manager, Maersk Nigeria","+234 802 556 8890","e.sam@example.com"),
        cl_company="SIFAX Group", cl_addr="7 Point Road, Apapa, Lagos",
        cl_body=["I am applying for the Shipping Documentation Officer role advertised on your careers page. I currently process bills of lading and customs documentation for over 50 containers weekly at Apapa Port.","I work directly with NPA and NCS on clearance procedures and track demurrage and detention charges closely.","I would welcome the opportunity to bring this experience to your shipping operations team."]),

    dict(id="mining-solid-minerals", name="Mining & Solid Minerals", tags=["Mining","Solid Minerals","Geology"],
        person="Tunde Bamidele", title="Mine Site Geologist", phone="+234 807 221 4471", loc="Jos, Plateau State",
        summary="Site geologist with 5 years mapping ore deposits and supervising sampling programmes for a solid minerals mining company.",
        emp=[("Dangote Cement (Limestone Operations)","Site Geologist","2020 — Present",["Supervise geological sampling and ore body mapping across a 200-hectare quarry","Prepared monthly reserve estimation reports"]),
             ("Plateau State Mineral Resources Development","Field Geology Assistant","2017 — 2020",["Conducted field mapping for tin and columbite deposits","Assisted with community relations for mining sites"])],
        school=("University of Jos","B.Sc. Geology","Second Class Upper","2012 — 2016"),
        skills=["Ore Body Mapping","Reserve Estimation","Field Sampling","GIS Software","Report Writing"], certs=["Nigerian Mining and Geosciences Society — Member"], langs=["English","Hausa"],
        ref=("Dr. Solomon Dung","Chief Geologist, Dangote Cement","+234 803 774 2298","s.dung@example.com"),
        cl_company="Dangote Cement Plc", cl_addr="Union Marble House, 1 Alfred Rewane Road, Ikoyi, Lagos",
        cl_body=["I am applying for the Site Geologist role advertised on your careers page. I currently supervise ore body mapping across a 200-hectare quarry and prepare monthly reserve estimation reports.","I bring hands-on field mapping experience and comfort working with GIS software.","I would welcome the opportunity to bring this experience to your mining operations team."]),

    dict(id="pharmacy", name="Pharmacy", tags=["Pharmacy","Pharmacist","PCN"],
        person="Chiamaka Uzo", title="Community Pharmacist", phone="+234 802 774 1123", loc="Enugu, Nigeria",
        summary="PCN-licensed community pharmacist with 4 years dispensing medication and providing patient counselling in a busy retail pharmacy.",
        emp=[("HealthPlus Pharmacy","Pharmacist","2021 — Present",["Dispense an average of 120 prescriptions daily with zero dispensing errors","Counsel patients on medication use and drug interactions"]),
             ("University of Nigeria Teaching Hospital","Intern Pharmacist","2020 — 2021",["Rotated through inpatient and outpatient pharmacy units","Assisted with hospital formulary management"])],
        school=("University of Nigeria, Nsukka","B.Pharm. Pharmacy","Second Class Upper","2014 — 2019"),
        skills=["Medication Dispensing","Patient Counselling","Drug Interaction Screening","Inventory Management","Pharmacovigilance"], certs=["PCN Licensed Pharmacist"], langs=["English","Igbo"],
        ref=("Pharm. Ngozi Ude","Superintendent Pharmacist, HealthPlus","+234 803 221 6674","n.ude@example.com"),
        cl_company="HealthPlus Pharmacy", cl_addr="6 Providence Street, Lekki Phase 1, Lagos",
        cl_body=["I am writing to apply for the Community Pharmacist role advertised on your careers page. I currently dispense an average of 120 prescriptions daily with zero dispensing errors and counsel patients on medication use.","I am a PCN-licensed pharmacist with hospital rotation experience across inpatient and outpatient units.","I would welcome the opportunity to bring this experience to your pharmacy team."]),

    dict(id="architecture", name="Architecture", tags=["Architecture","Architect","Design"],
        person="Segun Alabi", title="Architect", phone="+234 803 445 6690", loc="Ikeja, Lagos",
        summary="Registered architect with 5 years designing residential and mixed-use developments across Lagos.",
        emp=[("James Cubitt Architects","Architect","2020 — Present",["Lead design development for 6 residential and mixed-use projects","Coordinate with structural and MEP engineers through construction documentation"]),
             ("Design Union","Junior Architect","2017 — 2020",["Produced construction drawings and 3D visualisations","Assisted with site supervision during construction"])],
        school=("Obafemi Awolowo University","B.Sc. / M.Sc. Architecture","Second Class Upper","2010 — 2016"),
        skills=["AutoCAD","Revit","Construction Documentation","Site Supervision","3D Visualisation"], certs=["Architects Registration Council of Nigeria (ARCON) Registered"], langs=["English","Yoruba"],
        ref=("Arc. Bimbo Ogundele","Principal Partner, James Cubitt Architects","+234 802 990 4432","b.ogundele@example.com"),
        cl_company="James Cubitt Architects", cl_addr="9 Kofo Abayomi Street, Victoria Island, Lagos",
        cl_body=["I am applying for the Architect role advertised on your careers page. I currently lead design development for six residential and mixed-use projects, coordinating closely with structural and MEP engineers.","I am ARCON-registered and comfortable across the full project lifecycle, from concept to site supervision.","I would welcome the opportunity to bring this experience to your design team."]),

    dict(id="it-support", name="IT Support", tags=["IT Support","Helpdesk","Technical Support"],
        person="Bright Etim", title="IT Support Officer", phone="+234 806 221 7789", loc="Uyo, Akwa Ibom",
        summary="IT support officer with 4 years resolving hardware, software and network issues for a 200-staff organisation.",
        emp=[("Access Bank Plc","IT Support Officer","2021 — Present",["Resolve an average of 30 helpdesk tickets daily across hardware, software and network issues","Maintain and configure staff workstations and printers"]),
             ("MTN Nigeria (NYSC)","IT Support Intern","2020 — 2021",["Assisted with network cabling and Wi-Fi troubleshooting","Set up new starter laptops and email accounts"])],
        school=("University of Uyo","B.Sc. Computer Science","Second Class Upper","2016 — 2020"),
        skills=["Helpdesk Support","Windows & Network Troubleshooting","Active Directory", "Hardware Maintenance", "Ticketing Systems"], certs=["CompTIA A+"], langs=["English","Ibibio"],
        ref=("Mr. Godwin Etuk","IT Manager, Access Bank Plc","+234 803 774 1123","g.etuk@example.com"),
        cl_company="Access Bank Plc", cl_addr="14/15 Prince Alaba Oniru Road, Victoria Island, Lagos",
        cl_body=["I am applying for the IT Support Officer role advertised on your careers page. I currently resolve an average of 30 helpdesk tickets daily across hardware, software and network issues.","I hold a CompTIA A+ certification and have experience configuring and maintaining a large staff workstation fleet.","I would welcome the opportunity to bring this experience to your IT support team."]),

    dict(id="data-analysis", name="Data Analysis", tags=["Data Analyst","Analytics","BI"],
        person="Kelechi Anyanwu", title="Data Analyst", phone="+234 803 221 8890", loc="Yaba, Lagos",
        summary="Data analyst with 3 years building dashboards and reports that guide product decisions for a fintech company.",
        emp=[("Kuda Bank","Data Analyst","2022 — Present",["Build and maintain 10+ dashboards tracking product and growth metrics","Partner with product teams to design A/B tests"]),
             ("Interswitch","Junior Data Analyst","2020 — 2022",["Cleaned and modelled transaction data for monthly reporting","Automated recurring reports, saving the team 6 hours weekly"])],
        school=("Covenant University","B.Sc. Computer Science","Second Class Upper","2016 — 2020"),
        skills=["SQL","Python","Power BI","Data Modelling","A/B Testing"], certs=["Google Data Analytics Professional Certificate"], langs=["English","Igbo"],
        ref=("Ms. Funmi Osei","Head of Analytics, Kuda Bank","+234 802 556 4432","f.osei@example.com"),
        cl_company="Kuda Bank", cl_addr="2 Adeyemo Alakija Street, Victoria Island, Lagos",
        cl_body=["I am applying for the Data Analyst role advertised on your careers page. I currently build and maintain over 10 dashboards tracking product and growth metrics, and partner with product teams on A/B tests.","I have automated recurring reports that saved my previous team six hours weekly.","I would welcome the opportunity to bring this experience to your analytics team."]),

    dict(id="project-management", name="Project Management", tags=["Project Manager","PMP","Coordination"],
        person="Uduak Bassey", title="Project Manager", phone="+234 807 774 3320", loc="Abuja, FCT",
        summary="Project manager with 6 years delivering infrastructure and IT projects on time and within budget for development-sector clients.",
        emp=[("Palladium International","Project Manager","2020 — Present",["Manage a portfolio of 4 concurrent donor-funded projects worth over $2m combined","Lead cross-functional teams of up to 15 staff and consultants"]),
             ("Accenture Nigeria","Project Coordinator","2017 — 2020",["Tracked project milestones and risk registers across 3 workstreams","Prepared client status reports and steering committee decks"])],
        school=("University of Nigeria, Nsukka","B.Sc. Project Management Technology","Second Class Upper","2012 — 2016"),
        skills=["Project Planning","Risk Management","Stakeholder Management","MS Project","Budget Tracking"], certs=["PMP — Project Management Professional"], langs=["English","Efik"],
        ref=("Mr. Chuka Ibe","Country Director, Palladium International","+234 803 221 7789","c.ibe@example.com"),
        cl_company="Palladium International", cl_addr="Plot 251, Herbert Macaulay Way, Central Business District, Abuja",
        cl_body=["I am applying for the Project Manager role advertised on your careers page. I currently manage a portfolio of four concurrent donor-funded projects worth over $2 million combined, leading teams of up to 15 people.","I am PMP-certified and comfortable managing risk registers, budgets and steering committee reporting.","I would welcome the opportunity to bring this experience to your programme team."]),

    dict(id="social-work", name="Social Work", tags=["Social Work","Community Development"],
        person="Grace Ityavyar", title="Social Welfare Officer", phone="+234 806 445 2298", loc="Jos, Plateau State",
        summary="Social welfare officer with 5 years supporting vulnerable children and families through case management and community outreach.",
        emp=[("Plateau State Ministry of Women Affairs & Social Development","Social Welfare Officer","2019 — Present",["Manage a caseload of 40+ vulnerable children and families","Coordinate with 6 community-based organisations on referral pathways"]),
             ("SOS Children's Villages Nigeria","Case Worker","2016 — 2019",["Conducted home visits and needs assessments","Facilitated support groups for foster families"])],
        school=("University of Jos","B.Sc. Social Work","Second Class Upper","2011 — 2015"),
        skills=["Case Management","Needs Assessment","Community Outreach","Child Protection","Report Writing"], certs=["Registered Social Worker (Nigeria)"], langs=["English","Tiv"],
        ref=("Mrs. Comfort Dung","Programme Manager, SOS Children's Villages","+234 802 774 2298","c.dung@example.com"),
        cl_company="UNICEF Nigeria", cl_addr="UN House, Plot 617/618, Diplomatic Zone, Central Business District, Abuja",
        cl_body=["I am applying for the Social Welfare Officer role advertised on your careers page. I currently manage a caseload of over 40 vulnerable children and families and coordinate referral pathways with six community organisations.","I bring hands-on case management and child protection experience from both government and NGO settings.","I would welcome the opportunity to bring this experience to your programme team."]),

    dict(id="ngo-development", name="NGO / Development Sector", tags=["NGO","Development","Programme Officer"],
        person="Aisha Mohammed", title="Programme Officer", phone="+234 803 662 1187", loc="Maiduguri, Borno State",
        summary="Programme officer with 5 years implementing humanitarian and livelihood programmes across North-East Nigeria.",
        emp=[("Mercy Corps Nigeria","Programme Officer","2020 — Present",["Manage implementation of a livelihoods programme reaching 3,000 households","Coordinate with 5 field teams and local government partners"]),
             ("International Rescue Committee","Field Assistant","2017 — 2020",["Supported distribution of emergency relief items","Conducted post-distribution monitoring surveys"])],
        school=("University of Maiduguri","B.Sc. Sociology","Second Class Upper","2012 — 2016"),
        skills=["Programme Implementation","Monitoring & Evaluation","Stakeholder Coordination","Report Writing","Community Mobilisation"], certs=["Project Management for Development Professionals (PMD Pro)"], langs=["English","Hausa","Kanuri"],
        ref=("Mr. James Okoro","Deputy Country Director, Mercy Corps","+234 802 556 7789","j.okoro@example.com"),
        cl_company="Mercy Corps Nigeria", cl_addr="No. 1 Bama Road, GRA, Maiduguri, Borno State",
        cl_body=["I am applying for the Programme Officer role advertised on your careers page. I currently manage a livelihoods programme reaching 3,000 households and coordinate with five field teams and local government partners.","I bring strong monitoring and evaluation skills from earlier emergency response work.","I would welcome the opportunity to bring this experience to your programme team."]),

    dict(id="research-academia", name="Research & Academia", tags=["Research","Academia","Lecturer"],
        person="Dr. Chinwe Eze", title="Research Fellow", phone="+234 803 221 4471", loc="Nsukka, Enugu State",
        summary="Research fellow with 6 years conducting applied agricultural research and supervising postgraduate students.",
        emp=[("National Root Crops Research Institute","Research Fellow","2019 — Present",["Lead a research team investigating cassava yield improvement","Published 9 peer-reviewed papers in the last 5 years"]),
             ("University of Nigeria, Nsukka","Graduate Assistant","2015 — 2019",["Taught undergraduate courses in crop science","Supervised final-year student research projects"])],
        school=("University of Nigeria, Nsukka","Ph.D. Crop Science","-","2015 — 2019"),
        skills=["Research Design","Statistical Analysis (R/SPSS)","Grant Writing","Academic Publishing","Student Supervision"], certs=["Research Ethics Certification"], langs=["English","Igbo"],
        ref=("Prof. Ike Anyanwu","Director, National Root Crops Research Institute","+234 802 774 1123","i.anyanwu@example.com"),
        cl_company="International Institute of Tropical Agriculture (IITA)", cl_addr="Oyo Road, PMB 5320, Ibadan, Oyo State",
        cl_body=["I am applying for the Research Fellow role advertised on your careers page. I currently lead a research team investigating cassava yield improvement and have published nine peer-reviewed papers in the last five years.","I bring strong grant-writing experience and enjoy supervising postgraduate researchers.","I would welcome the opportunity to bring this research programme to your institute."]),

    dict(id="warehouse-inventory", name="Warehouse & Inventory", tags=["Warehouse","Inventory","Stock Control"],
        person="Chibueze Okoro", title="Warehouse Supervisor", phone="+234 802 556 4432", loc="Ogba, Lagos",
        summary="Warehouse supervisor with 5 years managing inventory accuracy and dispatch operations for a consumer goods distributor.",
        emp=[("Nestlé Nigeria Plc","Warehouse Supervisor","2020 — Present",["Supervise a 12-person warehouse team across receiving, storage and dispatch","Improved inventory accuracy from 91% to 99% through cycle counting"]),
             ("TSL Logistics","Inventory Officer","2017 — 2020",["Maintained stock records across 3 warehouse locations","Coordinated monthly stock reconciliation with finance"])],
        school=("Yaba College of Technology","HND Purchasing & Supply","Upper Credit","2013 — 2015"),
        skills=["Inventory Management","Warehouse Operations","Cycle Counting","WMS Software","Team Supervision"], certs=["Certified Inventory Management Professional (in view)"], langs=["English","Igbo"],
        ref=("Mrs. Bisi Owolabi","Distribution Manager, Nestlé Nigeria","+234 803 221 7789","b.owolabi@example.com"),
        cl_company="Nestlé Nigeria Plc", cl_addr="Km 22, Lagos-Abeokuta Expressway, Agbara, Ogun State",
        cl_body=["I am applying for the Warehouse Supervisor role advertised on your careers page. I currently supervise a 12-person team and improved inventory accuracy from 91% to 99% through disciplined cycle counting.","I bring hands-on experience with warehouse management systems and monthly stock reconciliation.","I would welcome the opportunity to bring this experience to your distribution team."]),

    dict(id="electrical-technician", name="Electrical Technician", tags=["Electrician","Electrical","Technician"],
        person="Chijioke Mbah", title="Electrical Technician", phone="+234 803 774 2298", loc="Onitsha, Anambra State",
        summary="Electrical technician with 7 years installing and maintaining electrical systems for residential and commercial buildings.",
        emp=[("Bemil Nigeria Ltd","Senior Electrical Technician","2018 — Present",["Lead installation of electrical systems for 15+ commercial projects","Train and supervise 3 junior technicians"]),
             ("Independent Contractor","Electrician","2013 — 2018",["Installed wiring, distribution boards and lighting for residential clients","Diagnosed and repaired electrical faults"])],
        school=("Anambra State Polytechnic","OND Electrical/Electronics Engineering","Upper Credit","2010 — 2012"),
        skills=["Electrical Installation","Fault Diagnosis","Wiring & Distribution Boards","Safety Compliance","Team Supervision"], certs=["Registered Electrician, Nigerian Society of Engineers"], langs=["English","Igbo"],
        ref=("Mr. Kingsley Nnaji","Site Manager, Bemil Nigeria","+234 802 556 3345","k.nnaji@example.com"),
        cl_company="Bemil Nigeria Ltd", cl_addr="14 New Market Road, Onitsha, Anambra State",
        cl_body=["I am applying for the Electrical Technician role advertised on your careers page. I currently lead installation of electrical systems for over 15 commercial projects and supervise three junior technicians.","I bring seven years of hands-on fault diagnosis and installation experience across residential and commercial sites.","I would welcome the opportunity to bring this experience to your technical team."]),

    dict(id="plumbing", name="Plumbing", tags=["Plumber","Plumbing","Pipefitting"],
        person="Godwin Etim", title="Plumbing Technician", phone="+234 806 221 5567", loc="Warri, Delta State",
        summary="Plumbing technician with 8 years installing and maintaining water supply and drainage systems for residential and commercial buildings.",
        emp=[("Niger Delta Construction Ltd","Plumbing Technician","2017 — Present",["Install and maintain plumbing systems for 10+ building projects annually","Diagnose and repair leaks, blockages and pump failures"]),
             ("Independent Contractor","Plumber","2011 — 2017",["Fitted water supply and drainage pipework for residential clients","Installed boreholes and overhead tank systems"])],
        school=("Delta State Polytechnic, Ogwashi-Uku","OND Mechanical Engineering","Upper Credit","2008 — 2010"),
        skills=["Pipe Installation","Leak Diagnosis","Borehole Systems","Drainage Systems","Safety Compliance"], certs=["Nigerian Institute of Plumbing Engineers — Registered"], langs=["English","Urhobo"],
        ref=("Mr. Efe Okoro","Project Manager, Niger Delta Construction","+234 803 774 1123","e.okoro@example.com"),
        cl_company="Niger Delta Construction Ltd", cl_addr="24 Airport Road, Warri, Delta State",
        cl_body=["I am applying for the Plumbing Technician role advertised on your careers page. I currently install and maintain plumbing systems for over 10 building projects annually.","I bring eight years of hands-on experience diagnosing leaks and installing borehole and drainage systems.","I would welcome the opportunity to bring this experience to your construction team."]),

    dict(id="automotive-mechanic", name="Automotive Mechanic", tags=["Mechanic","Automotive","Vehicle Repair"],
        person="Suleiman Bello", title="Automotive Technician", phone="+234 802 774 3320", loc="Kaduna, Nigeria",
        summary="Automotive technician with 9 years diagnosing and repairing petrol and diesel engines for a commercial fleet operator.",
        emp=[("Dangote Group (Fleet Maintenance)","Senior Automotive Technician","2017 — Present",["Maintain a fleet of 45 trucks, reducing breakdown incidents by 30%","Train 4 junior technicians on diagnostic procedures"]),
             ("Independent Garage","Mechanic","2011 — 2017",["Diagnosed and repaired engine, transmission and brake faults","Serviced vehicles for private and commercial clients"])],
        school=("Kaduna Polytechnic","OND Automotive Engineering","Upper Credit","2008 — 2010"),
        skills=["Engine Diagnostics","Preventive Maintenance","Fleet Management","Brake & Transmission Repair","Team Training"], certs=["Nigerian Automotive Technicians Association — Registered"], langs=["English","Hausa"],
        ref=("Mr. Aminu Garba","Fleet Manager, Dangote Group","+234 803 221 6674","a.garba@example.com"),
        cl_company="Dangote Group", cl_addr="Union Marble House, 1 Alfred Rewane Road, Ikoyi, Lagos",
        cl_body=["I am applying for the Automotive Technician role advertised on your careers page. I currently maintain a 45-truck fleet and have reduced breakdown incidents by 30% through improved preventive maintenance.","I bring strong diagnostic skills across petrol and diesel engines and enjoy training junior technicians.","I would welcome the opportunity to bring this experience to your fleet maintenance team."]),

    dict(id="photography-creative", name="Photography & Creative Arts", tags=["Photography","Creative","Videography"],
        person="Tobi Alademomi", title="Photographer / Videographer", phone="+234 803 221 8890", loc="Yaba, Lagos",
        summary="Freelance photographer and videographer with 5 years shooting weddings, corporate events and brand content across Lagos.",
        emp=[("Tobi Alademomi Studios (Self-Employed)","Lead Photographer","2019 — Present",["Shoot and edit content for 40+ weddings and corporate events annually","Manage a team of 2 assistant photographers and 1 video editor"]),
             ("Bella Naija Weddings","Freelance Contributor","2017 — 2019",["Covered featured weddings for online publication","Delivered edited galleries within 48-hour turnaround"])],
        school=("Yaba College of Technology","HND Mass Communication","Upper Credit","2013 — 2015"),
        skills=["Photography", "Videography", "Adobe Lightroom & Premiere Pro", "Client Management", "Event Coverage"], certs=["Certificate in Digital Photography"], langs=["English","Yoruba"],
        ref=("Mrs. Funmi Adesanya","Editor, Bella Naija Weddings","+234 802 556 7789","f.adesanya@example.com"),
        cl_company="Zoom Studios Lagos", cl_addr="12 Allen Avenue, Ikeja, Lagos",
        cl_body=["I am writing to apply for the Photographer / Videographer role advertised on your careers page. I currently shoot and edit content for over 40 weddings and corporate events annually, managing a small creative team.","I bring strong client management skills and consistently deliver within tight turnaround times.","I would welcome the opportunity to bring this experience to your studio."]),

    dict(id="event-planning", name="Event Planning", tags=["Event Planner","Events","Wedding Planning"],
        person="Chidinma Okafor", title="Event Planner", phone="+234 806 774 2298", loc="Lekki, Lagos",
        summary="Event planner with 5 years coordinating weddings and corporate events for clients across Lagos and Abuja.",
        emp=[("Chidinma Events (Self-Employed)","Lead Event Planner","2019 — Present",["Plan and execute 25+ weddings and corporate events annually","Manage vendor relationships across catering, décor and logistics"]),
             ("Elizabeth Events","Junior Event Coordinator","2017 — 2019",["Assisted with venue sourcing and guest list management","Coordinated on-the-day logistics for up to 500-guest events"])],
        school=("Pan-Atlantic University","B.Sc. Business Administration","Second Class Upper","2013 — 2017"),
        skills=["Event Coordination","Vendor Management","Budget Planning","Client Relations","On-Site Logistics"], certs=["Certified Event Planner (in view)"], langs=["English","Igbo"],
        ref=("Mrs. Elizabeth Okon","Founder, Elizabeth Events","+234 803 221 4471","e.okon@example.com"),
        cl_company="Elizabeth Events", cl_addr="5 Admiralty Way, Lekki Phase 1, Lagos",
        cl_body=["I am applying for the Event Planner role advertised on your careers page. I currently plan and execute over 25 weddings and corporate events annually, managing vendor relationships across catering, décor and logistics.","I bring strong budget planning and on-site coordination skills from events of up to 500 guests.","I would welcome the opportunity to bring this experience to your events team."]),
]

for e in NEW:
    school_obj = school(e["school"][0], e["school"][1], e["school"][2], e["school"][3])
    exps = [exp(c, p, d, b) for (c, p, d, b) in e["emp"]]
    ref_obj = ref(e["ref"][0], e["ref"][1], e["ref"][2], e["ref"][3])
    slug = e["person"].lower().replace(" ", ".").replace(".", ".", 1)
    email = e["person"].split()[0].lower() + "." + e["person"].split()[-1].lower() + "@email.com"
    CV[e["id"]] = cv(e["person"], e["title"], e["phone"], email, e["loc"], e["summary"], exps, school_obj,
                      e["skills"], e["certs"], e["langs"], ref_obj)
    CL[e["id"]] = cl(e["person"], e["phone"], email, e["loc"], e["cl_company"], e["cl_addr"], "Dear Hiring Manager,", e["cl_body"])

# ============================================================
# Assemble final professions.json, preserving a sensible order
# ============================================================
ORDER = ["general","software-engineer","graduate-nysc","banking-finance","teacher-education","nurse-healthcare",
    "government-civil-service","sales-marketing","customer-service-admin","engineering-technical","hospitality-hotel",
    "construction-trades","legal-paralegal","logistics-supply-chain","human-resources","marketing-communications",
    "agriculture-agribusiness","oil-gas","telecommunications","manufacturing-production","real-estate","insurance",
    "accounting-audit","procurement","security-services","driving-transport","fashion-tailoring","beauty-cosmetology",
    "culinary-chef","aviation","maritime-shipping","mining-solid-minerals","pharmacy","architecture","it-support",
    "data-analysis","project-management","social-work","ngo-development","research-academia","warehouse-inventory",
    "electrical-technician","plumbing","automotive-mechanic","photography-creative","event-planning"]

assert len(ORDER) == 46, len(ORDER)
assert set(ORDER) == set(CV.keys()), set(ORDER) ^ set(CV.keys())
assert set(ORDER) == set(CL.keys()), set(ORDER) ^ set(CL.keys())

NAMES = {
  "general":"General / Any Role","software-engineer":"Software Engineer","graduate-nysc":"Graduate / NYSC",
  "banking-finance":"Banking & Finance","teacher-education":"Teacher / Education","nurse-healthcare":"Nurse / Healthcare",
  "government-civil-service":"Government / Civil Service","sales-marketing":"Sales & Marketing",
  "customer-service-admin":"Customer Service & Admin","engineering-technical":"Engineering (Technical)",
  "hospitality-hotel":"Hospitality & Hotel","construction-trades":"Construction & Trades","legal-paralegal":"Legal / Paralegal",
}
TAGS = {
  "general":["General","Any Role"],"software-engineer":["Software Engineer","Developer","Tech","ICT","Programmer"],
  "graduate-nysc":["Graduate","NYSC","Student","Entry Level","Corps Member"],
  "banking-finance":["Banking","Finance","Accountant","Admin"],"teacher-education":["Teacher","Education","School","TRCN"],
  "nurse-healthcare":["Nurse","Healthcare","Nursing","Hospital"],
  "government-civil-service":["Government","Civil Service","Public Sector"],
  "sales-marketing":["Sales","Marketing","Business Development"],
  "customer-service-admin":["Customer Service","Admin","Front Desk","Support"],
  "engineering-technical":["Engineering","Technical","Mechanical","Electrical","Oil & Gas"],
  "hospitality-hotel":["Hospitality","Hotel","Front Desk","Tourism"],
  "construction-trades":["Construction","Trades","Site","Building"],"legal-paralegal":["Legal","Paralegal","Law"],
}
for e in NEW:
    NAMES[e["id"]] = e["name"]
    TAGS[e["id"]] = e["tags"]

out = {"cv": [], "cover-letter": []}
for pid in ORDER:
    out["cv"].append({"id": pid, "name": NAMES[pid], "tags": TAGS[pid], "sample": CV[pid]})
    out["cover-letter"].append({"id": pid, "name": NAMES[pid], "tags": TAGS[pid], "sample": CL[pid]})

with open("data/professions.json", "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)

print("Wrote", len(out["cv"]), "CV professions and", len(out["cover-letter"]), "cover-letter professions")
