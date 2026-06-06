import os
from datetime import date, datetime, timedelta
from app import create_app
from extensions import db
from models.models import (AdminUser, Department, Faculty, Qualification,
                           Experience, ResearchPublication, PerformanceReview,
                           Salary, Attendance, LeaveRequest)

def seed():
    app = create_app()
    with app.app_context():
        # Clear existing data except AdminUser
        print("Clearing existing data...")
        db.session.query(LeaveRequest).delete()
        db.session.query(Attendance).delete()
        db.session.query(Salary).delete()
        db.session.query(PerformanceReview).delete()
        db.session.query(ResearchPublication).delete()
        db.session.query(Experience).delete()
        db.session.query(Qualification).delete()
        # Nullify foreign key references in faculty before delete if needed, but cascade/delete will do it
        db.session.query(Faculty).delete()
        db.session.query(Department).delete()
        db.session.commit()

        # 1. Create Departments
        print("Creating departments...")
        dept_cse = Department(department_name="Computer Science & Engineering", department_code="CSE", hod_name="Dr. Sarah Connor")
        dept_ece = Department(department_name="Electronics & Communication", department_code="ECE", hod_name="Dr. Alan Turing")
        dept_me = Department(department_name="Mechanical Engineering", department_code="ME", hod_name="Dr. Jane Smith")
        dept_ee = Department(department_name="Electrical Engineering", department_code="EE", hod_name="Dr. Nikola Tesla")
        
        db.session.add_all([dept_cse, dept_ece, dept_me, dept_ee])
        db.session.flush()

        # 2. Create Faculty
        print("Creating faculty members...")
        fac1 = Faculty(
            employee_code="FAC-CSE-001",
            first_name="Sarah",
            last_name="Connor",
            gender="Female",
            date_of_birth=date(1982, 5, 14),
            mobile_number="9876543210",
            email="sconnor@institute.edu",
            address_line1="123 Science Hill Rd",
            city="Bengaluru",
            state="Karnataka",
            pincode="560012",
            joining_date=date(2018, 7, 1),
            designation="Professor",
            employment_type="Full-Time",
            department_id=dept_cse.department_id,
            status="Active"
        )
        
        fac2 = Faculty(
            employee_code="FAC-ECE-002",
            first_name="Alan",
            last_name="Turing",
            gender="Male",
            date_of_birth=date(1980, 6, 23),
            mobile_number="9876543211",
            email="aturing@institute.edu",
            address_line1="456 Turing Avenue",
            city="Hyderabad",
            state="Telangana",
            pincode="500081",
            joining_date=date(2015, 1, 10),
            designation="Professor",
            employment_type="Full-Time",
            department_id=dept_ece.department_id,
            status="Active"
        )

        fac3 = Faculty(
            employee_code="FAC-CSE-003",
            first_name="John",
            last_name="Doe",
            gender="Male",
            date_of_birth=date(1990, 8, 12),
            mobile_number="9876543212",
            email="jdoe@institute.edu",
            address_line1="789 Silicon Valley Lane",
            city="Bengaluru",
            state="Karnataka",
            pincode="560066",
            joining_date=date(2021, 6, 15),
            designation="Associate Professor",
            employment_type="Full-Time",
            department_id=dept_cse.department_id,
            status="Active"
        )

        fac4 = Faculty(
            employee_code="FAC-ME-004",
            first_name="Jane",
            last_name="Smith",
            gender="Female",
            date_of_birth=date(1992, 11, 5),
            mobile_number="9876543213",
            email="jsmith@institute.edu",
            address_line1="321 Gear Shaft Rd",
            city="Pune",
            state="Maharashtra",
            pincode="411001",
            joining_date=date(2022, 10, 1),
            designation="Assistant Professor",
            employment_type="Full-Time",
            department_id=dept_me.department_id,
            status="Active"
        )

        fac5 = Faculty(
            employee_code="FAC-EE-005",
            first_name="Nikola",
            last_name="Tesla",
            gender="Male",
            date_of_birth=date(1985, 7, 10),
            mobile_number="9876543214",
            email="ntesla@institute.edu",
            address_line1="888 Lightning Street",
            city="Noida",
            state="Uttar Pradesh",
            pincode="201301",
            joining_date=date(2019, 3, 20),
            designation="Professor",
            employment_type="Full-Time",
            department_id=dept_ee.department_id,
            status="Active"
        )

        db.session.add_all([fac1, fac2, fac3, fac4, fac5])
        db.session.flush()

        # 3. Create Qualifications
        print("Creating qualifications...")
        db.session.add_all([
            # Sarah Connor
            Qualification(faculty_id=fac1.faculty_id, degree_name="Ph.D. in Computer Science", institution_name="Stanford University", passing_year=2015, percentage=95.50),
            Qualification(faculty_id=fac1.faculty_id, degree_name="M.Tech. in Computer Science", institution_name="IIT Bombay", passing_year=2010, percentage=89.20),
            Qualification(faculty_id=fac1.faculty_id, degree_name="B.Tech. in Computer Science", institution_name="NIT Trichy", passing_year=2008, percentage=84.50),
            
            # Alan Turing
            Qualification(faculty_id=fac2.faculty_id, degree_name="Ph.D. in Mathematics", institution_name="Princeton University", passing_year=2009, percentage=98.00),
            Qualification(faculty_id=fac2.faculty_id, degree_name="B.Sc. in Mathematics", institution_name="King's College, Cambridge", passing_year=2004, percentage=96.50),

            # John Doe
            Qualification(faculty_id=fac3.faculty_id, degree_name="Ph.D. in Computer Science", institution_name="IISc Bangalore", passing_year=2020, percentage=88.50),
            Qualification(faculty_id=fac3.faculty_id, degree_name="M.S. in Computer Science", institution_name="Georgia Tech", passing_year=2015, percentage=91.00),

            # Jane Smith
            Qualification(faculty_id=fac4.faculty_id, degree_name="M.Tech. in Mechanical Design", institution_name="IIT Delhi", passing_year=2018, percentage=86.00),
            Qualification(faculty_id=fac4.faculty_id, degree_name="B.E. in Mechanical Engineering", institution_name="COEP Pune", passing_year=2016, percentage=81.40),

            # Nikola Tesla
            Qualification(faculty_id=fac5.faculty_id, degree_name="Ph.D. in Electrical Engineering", institution_name="ETH Zurich", passing_year=2012, percentage=97.50)
        ])

        # 4. Create Experience
        print("Creating experience...")
        db.session.add_all([
            # Sarah Connor
            Experience(faculty_id=fac1.faculty_id, organization_name="MIT Research Lab", designation="Postdoc Researcher", start_date=date(2015, 8, 1), end_date=date(2018, 6, 30), years_of_experience=2.9),
            # Alan Turing
            Experience(faculty_id=fac2.faculty_id, organization_name="National Physical Laboratory", designation="Senior Scientist", start_date=date(2009, 10, 1), end_date=date(2014, 12, 31), years_of_experience=5.2),
            # John Doe
            Experience(faculty_id=fac3.faculty_id, organization_name="TechCorp R&D", designation="Research Scientist", start_date=date(2015, 6, 1), end_date=date(2017, 5, 30), years_of_experience=2.0)
        ])

        # 5. Create Research Publications
        print("Creating research publications...")
        db.session.add_all([
            ResearchPublication(faculty_id=fac1.faculty_id, title="Deep Learning for Autonomous Robotics", journal_name="IEEE Transactions on Pattern Analysis", publication_year=2021),
            ResearchPublication(faculty_id=fac1.faculty_id, title="Quantum Computing Algorithms in Cryptography", journal_name="Journal of ACM", publication_year=2023),
            ResearchPublication(faculty_id=fac2.faculty_id, title="On Computable Numbers and Entscheidungsproblem", journal_name="Proceedings of London Mathematical Society", publication_year=2016),
            ResearchPublication(faculty_id=fac3.faculty_id, title="Scalable Query Processing in Distributed DBs", journal_name="VLDB Journal", publication_year=2022),
            ResearchPublication(faculty_id=fac5.faculty_id, title="Wireless Transmission of Electrical Energy", journal_name="IEEE Power Electronics Letters", publication_year=2020)
        ])

        # 6. Create Performance Reviews
        print("Creating performance reviews...")
        db.session.add_all([
            PerformanceReview(faculty_id=fac1.faculty_id, review_year=2024, rating=4.8, remarks="Excellent teaching feedback and research guidance. Led the curriculum reform."),
            PerformanceReview(faculty_id=fac1.faculty_id, review_year=2025, rating=4.9, remarks="Outstanding research output and successful HOD leadership."),
            PerformanceReview(faculty_id=fac2.faculty_id, review_year=2025, rating=5.0, remarks="Exceptional contributions to theoretical computer science. Inspiring mentor."),
            PerformanceReview(faculty_id=fac3.faculty_id, review_year=2025, rating=4.3, remarks="Strong classroom performance and active department committee work."),
            PerformanceReview(faculty_id=fac4.faculty_id, review_year=2025, rating=4.0, remarks="Very promising junior faculty, highly dedicated to laboratory setup."),
            PerformanceReview(faculty_id=fac5.faculty_id, review_year=2025, rating=4.7, remarks="Highly innovative projects. Brought significant research funding.")
        ])

        # 7. Create Salaries
        print("Creating salaries...")
        months = ["January 2026", "February 2026", "March 2026", "April 2026", "May 2026", "June 2026"]
        salaries = [
            (fac1, 150000, 35000, 18000), # Prof
            (fac2, 160000, 40000, 20000), # Prof
            (fac3, 110000, 22000, 12000), # Assoc Prof
            (fac4, 75000, 15000, 8000),   # Asst Prof
            (fac5, 145000, 30000, 16000)  # Prof
        ]
        for f, basic, allow, ded in salaries:
            net = basic + allow - ded
            # Add paid salary for past months
            for m in months[:-1]:
                s = Salary(
                    faculty_id=f.faculty_id,
                    basic_salary=basic,
                    allowances=allow,
                    deductions=ded,
                    net_salary=net,
                    payment_date=date(2026, months.index(m) + 2, 1) - timedelta(days=1), # end of month
                    salary_month=m,
                    salary_status="Paid"
                )
                db.session.add(s)
            # Add pending salary for June 2026
            s_curr = Salary(
                faculty_id=f.faculty_id,
                basic_salary=basic,
                allowances=allow,
                deductions=ded,
                net_salary=net,
                salary_month=months[-1],
                salary_status="Pending"
            )
            db.session.add(s_curr)

        # 8. Create Attendance
        print("Creating attendance...")
        # Populate daily attendance for last 30 days
        today = date.today()
        for i in range(30):
            d = today - timedelta(days=i)
            # Skip Sundays
            if d.weekday() == 6:
                continue
            for f in [fac1, fac2, fac3, fac4, fac5]:
                # Randomly determine status: 90% Present, 6% Leave, 4% Absent
                import random
                # Set a seed to make it reproducible
                random.seed(f.faculty_id * 100 + i)
                val = random.random()
                if val < 0.90:
                    status = "Present"
                    check_in = datetime.strptime("09:00", "%H:%M").time()
                    check_out = datetime.strptime("17:00", "%H:%M").time()
                elif val < 0.96:
                    status = "Leave"
                    check_in, check_out = None, None
                else:
                    status = "Absent"
                    check_in, check_out = None, None

                att = Attendance(
                    faculty_id=f.faculty_id,
                    attendance_date=d,
                    check_in_time=check_in,
                    check_out_time=check_out,
                    status=status
                )
                db.session.add(att)

        # 9. Create Leave Requests
        print("Creating leave requests...")
        db.session.add_all([
            LeaveRequest(
                faculty_id=fac3.faculty_id,
                leave_type="Casual Leave",
                from_date=today + timedelta(days=3),
                to_date=today + timedelta(days=5),
                reason="Family function in hometown.",
                approval_status="Pending"
            ),
            LeaveRequest(
                faculty_id=fac4.faculty_id,
                leave_type="Sick Leave",
                from_date=today - timedelta(days=15),
                to_date=today - timedelta(days=14),
                reason="Severe fever and flu.",
                approval_status="Approved",
                reviewed_by=1,
                reviewed_at=datetime.utcnow() - timedelta(days=16)
            ),
            LeaveRequest(
                faculty_id=fac1.faculty_id,
                leave_type="Maternity Leave",
                from_date=today - timedelta(days=45),
                to_date=today - timedelta(days=15),
                reason="Medical rest recommended.",
                approval_status="Approved",
                reviewed_by=1,
                reviewed_at=datetime.utcnow() - timedelta(days=46)
            ),
            LeaveRequest(
                faculty_id=fac5.faculty_id,
                leave_type="Casual Leave",
                from_date=today + timedelta(days=10),
                to_date=today + timedelta(days=11),
                reason="Personal work.",
                approval_status="Pending"
            )
        ])

        db.session.commit()
        print("Database successfully seeded with mock data!")

if __name__ == "__main__":
    seed()
