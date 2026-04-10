from fastapi import APIRouter

router = APIRouter()

@router.get("/profile")
async def get_profile():
    return {
        "name": "Abhi Patel",
        "summary": "Master of Engineering graduate specializing in scalable web apps and AI-driven systems.",
        "strengths": ["Full-Stack AI Engineer", "Quick Learner", "Ethics in Professionalism", "Leadership"],
        "education": [
            {
                "id": "edu-master",
                "degree": "Masters' of Engineering",
                "role": "Software Engineering",
                "uni": "Concordia University",
                "institution_url": "https://www.concordia.ca/",
                "duration": "2023 - 2025",
                "location": "Montreal, QC",
                "gpa": "3.23 / 4.00",
                "desc": [
                    "Leveraged advanced design methodologies and comparative programming to architect distributed systems capable of solving real-world scalability issues and managing high-concurrent user loads./n",
                    "Synthesized advanced programming practices with Generative AI to automate defect detection, reducing manual debugging time and creating self-healing code environments that proactively resolve runtime errors./n",
                    "Applied big data analytics and requirements engineering to transform raw system logs into actionable performance metrics while maintaining strict ethical standards and quality control across the software supply chain."
                ],
                "details": [
                    "Architected distributed systems by applying advanced design patterns to solve real-world scalability issues, ensuring software could handle high-concurrent user loads.",
                    "Developed a deep understanding of cloud-native infrastructure by deploying containerized applications that optimized resource allocation and reduced latency.",
                    "Integrated Generative AI models into development workflows to automate defect detection, significantly reducing the time spent on manual code reviews and debugging.",
                    "Processed and analyzed large-scale datasets using big data frameworks to derive statistical insights, turning raw system logs into actionable performance metrics.",
                    "Mastered the full software development lifecycle (SDLC) by leading team projects from initial requirements gathering to final deployment and maintenance.",
                    "Optimized system performance by analyzing algorithmic complexity, ensuring that backend processes remained efficient even as data volume increased.",
                    "Explored the intersection of software maintenance and AI to create self-healing code environments that proactively identify and resolve runtime errors."
                ],
                "phases": {
                "phase1": [
                    "SOFT. COMP. & MAINTENANCE",
                    "SOFTWARE DSGN METHODOLOGIES (Design Patterns)",
                    "SOFTWARE PROJECT MANAGEMENT (Project Management)",
                    "COMPARAT. STUDY/PROGRAM. LANG. (Python)"
                ],
                "phase2": [
                    "PROGRAM & PROBLEM SOLVING",
                    "ETHICS & PROFESSIONALISM",
                    "ADV. PROG. PRACTICES",
                    "Generative AI for Software Eng"
                ],
                "phase3": [
                    "QUAL. ASS. SUPPLY CHAIN MGT",
                    "HUMAN COMPUTER INTERFACE DESIGN",
                    "BIG DATA ANALYTICS",
                    "SYSTEMS REQMT. SPECIFICATION"
                ]
                }
            },
        {
            "id": "edu-bachelor",
            "degree": "Bachelors' of Technology",
            "role": "Computer Science Engineering",
            "uni": "Indus University",
            "institution_url": "https://indusuni.ac.in/",
            "duration": "2019 - 2023",
            "location": "Ahmedabad, India",
            "gpa": "4.00 / 4.00",
            "desc": [
                "Academic Excellence & Engineering Foundations: Achieved a near-perfect CGPA of 9.85/10.0, ranking in the top 1% while mastering core Data Structures, Algorithms (DSA), and Object-Oriented Design to improve computational efficiency.",
                "Technical Leadership & Community Architecture: Spearheaded the Google Developer Student Club (GDSC) as Chapter Lead, fostering a high-growth ecosystem for 500+ developers through technical workshops and collaborative full-stack web architecture.",
                "Advanced Systems & Intelligent Analytics: Engineered robust database schemas and integrated IoT with Machine Learning methodologies to transform complex datasets into predictive models and real-time hardware-interfacing applications."
            ],
            "details": [
                "Achieved a near-perfect CGPA of 9.85/10.0, consistently ranking in the top 1% of the Computer Science and Engineering department.",
                "Led the Google Developer Student Club (GDSC) as Chapter Lead, organizing technical workshops and fostering a community of 500+ student developers.",
                "Engineered high-performance applications using C/C++ and Java, focusing on memory management and object-oriented design principles (UML).",
                "Developed robust database schemas and optimized complex SQL queries using DBMS principles to ensure data integrity and efficient retrieval.",
                "Implemented core Data Structures and Algorithms (DSA) to solve complex computational problems, improving processing efficiency and time complexity.",
                "Architected full-stack web applications by integrating modern frontend technologies with secure backend logic and RESTful APIs.",
                "Explored the intersection of IoT and mobile development by building cross-platform applications that interface with hardware sensors and real-time data.",
                "Applied Machine Learning and Data Science methodologies to analyze large datasets, building predictive models for automated decision-making."
            ],
            "phases": {
                "phase1": [
                    "TECHNICAL COMMUNICATION",
                    "Internet of Things",
                    "PROGRAMMING FOR PROBLEM SOLVING: C/C++",
                    "OBJECT ORIENTED CONCEPTS WITH UML"
                ],
                "phase2": [
                    "DATABASE MANAGEMENT SYSTEMS",
                    "DATA COMMUNICATION NETWORKS",
                    "COMPUTER ORGANIZATION & ARCHITECTURE",
                    "DATA STRUCTURE & ALGORITHMS"
                ],
                "phase3": [
                    "ALGORITHMS DESIGN & ANALYSIS",
                    "COMPUTER NETWORKS",
                    "PYTHON PROGRAMMING",
                    "FULL-STACK WEB TECHNOLOGY"
                ],
                "phase4": [
                    "CLOUD COMPUTING & BLOCK CHAIN",
                    "MOBILE APPLICATION DEVELOPMENT",
                    "DATA SCIENCE & ML",
                    "CRYPTOGRAPHY & NETWORK SECURITY"
                ]
                }
            },

            {
            "id": "edu-hsc",
            "degree": "HSC/Science: Physics",
            "role": "Science (PCM)",
            "uni": "VPS",
            "institution_url": "https://schools.org.in/sabar-kantha/24050805009/vector-public-school.html",
            "duration": "2019",
            "location": "Salal, India",
            "gpa": "98.69",
            "desc": [
                "State-Level Academic Distinction: Achieved an exceptional 98.69 percentile in the GSEB State Board Examinations, securing a position among the elite top-tier academic performers across the state.",
                "Engineering Logic & Mathematical Foundations: Mastered advanced Calculus, Linear Algebra, and Theoretical Physics to build a rigorous analytical framework for complex problem-solving and future engineering architectures.",
                "Scientific Methodology & Computational Thinking: Cultivated disciplined reasoning through the study of Modern Physics and Chemistry while strengthening foundational logical thinking and early software development principles."
            ],
            "details": [
                "Achieved an exceptional 98.69 percentile in the GSEB State Board Examinations, ranking among the top academic performers in the state.",
                "Mastered advanced mathematical concepts including Calculus, Linear Algebra, and Trigonometry, forming the backbone of future engineering logic.",
                "Developed a strong foundation in Theoretical Physics, focusing on Mechanics, Electromagnetism, and Modern Physics principles.",
                "Gained comprehensive knowledge of Organic and Inorganic Chemistry, enhancing analytical reasoning and experimental methodology skills.",
                "Cultivated disciplined problem-solving techniques by tackling complex multi-step scientific challenges and mathematical proofs.",
                "Strengthened foundational computational thinking and logical reasoning through the study of early software development principles and SDLC basics."
            ],
            "phases": {
                    "phase1": [
                        "ADVANCED MATHEMATICS (CALCULUS & ALGEBRA)",
                        "ENGINEERING PHYSICS",
                        "ORGANIC & INORGANIC CHEMISTRY",
                        "ENGINEERING GRAPHICS"
                    ],
                    "phase2": [
                        "SDLC & SOLID STUDIES",
                        "FORMAL LANGUAGE & AUTOMATA THEORY",
                        "HUMAN VALUES & PROFESSIONAL ETHICS",
                        "ENVIRONMENTAL SCIENCE"
                    ]
                }
            },
            {
                "id": "edu-ssc",
                "degree": "SSC/Science: Maths",
                "role": "General Science",
                "uni": "Sanskar Dham_LGPS",
                "institution_url": "https://www.sanskardham.org/",
                "duration": "2017",
                "location": "Ahmedabad, India",
                "gpa": "99.91",
                "desc": [
                    "Top-Tier Academic Ranking: Achieved a near-perfect 99.91 percentile in the GSEB State Board Examinations, ranking among the highest achievers in the region and establishing a baseline of elite performance.",
                    "Quantitative & Logic Foundations: Demonstrated exceptional proficiency in Mathematics and Science, utilizing advanced algebraic equations and geometric proofs to build the foundational logic required for technical engineering.",
                    "Early Computational Literacy: Initiated a trajectory into software engineering by exploring the fundamentals of computational thinking, basic algorithmic structures, and the evolution of primary storage systems."
                ],
                "details": [
                    "Achieved a near-perfect 99.91 percentile in the GSEB State Board Examinations, ranking among the highest achievers in the region.",
                    "Demonstrated exceptional proficiency in Mathematics and Science, establishing a strong quantitative foundation for technical engineering studies.",
                    "Developed foundational logic-based problem-solving skills through the study of advanced algebraic equations and geometric proofs.",
                    "Introduced to the fundamentals of computational thinking, exploring the basic logic structures that govern modern software systems.",
                    "Gained a preliminary understanding of data integrity and ACID properties, sparking an early interest in secure database management.",
                    "Built early technical literacy by exploring the evolution of computing, from primary storage concepts to basic algorithmic structures."
                ],
                "phases": {
                    "phase1": [
                        "INTRODUCTION TO COMPUTING & LOGIC",
                        "BASIC PROGRAMMING CONCEPTS (VARIABLES & LOOPS)",
                        "FUNDAMENTALS OF ALGORITHMIC THINKING",
                        "PRIMARY & SECONDARY STORAGE CONCEPTS"
                    ],
                    "phase2": [
                        "DATABASE MANAGEMENT SYSTEM BASICS",
                        "DATA INTEGRITY & ACID PROPERTIES",
                        "INTRODUCTION TO STRUCTURED DATA",
                        "BASICS OF INFORMATION RETRIEVAL"
                    ]
                }
            }
        ],
        "skills": [
            {"name": "React.js", "level": "Advanced"},
            {"name": "Python", "level": "Advanced"},
            {"name": "ASP.NET Core", "level": "Advanced"},
            {"name": "Gen-AI / ML", "level": "Intermediate"},
            {"name": "Docker", "level": "Learning"}
        ],
        "experience": [
                        {
                            "id": "exp-azilen",
                            "role": "Software Engineer",   
                            "company": "Azilen Technologies",
                            "duration": "Dec 2022 - Dec 2023",
                            "mode": "Hybrid",
                            "institution_url": "https://www.azilen.com/",
                            "location": "Ahmedabad, India",
                            "desc": ["Backend & Systems Architecture: I engineered secure, scalable microservices using Node.js, Python, Java (Spring), and ASP.NET MVC, applying SOLID principles and Linux/Unix-based logging to ensure high-velocity feature delivery and 100% data integrity across complex enterprise systems.",
                                    "Data Intelligence & AI Orchestration: I bridged the gap between engineering and AI by building ETL pipelines that increased data accessibility by 40%, designing predictive models with Scikit-learn, and pioneering agentic workflows through intelligent automated connectors for platforms like Teams and Jira.",
                                    "DevOps & Technical Excellence: I optimized deployment speeds and system reliability by building automated CI/CD pipelines with Docker and Azure, while maintaining elite code quality through rigorous Exploratory Data Analysis (EDA), unit testing, and collaborative peer reviews."],
                            "responsibilities": [
                                "Engineered secure RESTful APIs & microservices using Python, Java, and ASP.NET with SOLID principles for seamless data flow.",
                                "Pioneered AI orchestration by building intelligent connectors for Teams/Jira and designing predictive models with Scikit-learn.",
                                "Built robust ETL pipelines via SQL preprocessing, increasing data accessibility by 40% with high integrity in Linux environments.",
                                "Doubled deployment speed by integrating CI/CD pipelines with Docker & Azure for high-availability, reproducible production releases.",
                                "Led cross-functional teams through code reviews & EDA, leveraging GitHub Copilot to accelerate delivery & solve business needs."
                            ],
                            "depth_ride": {
                                "start": "Joined as Full-Stack AI Engineer focusing on API Connection andsecurity.",
                                "growth": "Pivoted to AI integration, building custom middleware for LLM/ML processing.",
                                "peak": "Led the optimization of the core data engine, reducing latency by 43%."
                            },
                            "data_flow": [
                                {"node": "Data Source", "desc": "Enterprise CRM/ERP Systems"},
                                {"node": "AI Connector", "desc": "Python FastAPI Middleware"},
                                {"node": "Processing", "desc": "Vector Embedding & LLM Analysis"},
                                {"node": "Storage", "desc": "PostgreSQL + Redis Cache"}
                            ],
                            "tech_stack": ["JAVA", "PYTHON", "ASP.NET MVC", "POSTGRESQL", "DOCKER", "JIRA", "GITHUB", "JavaScript: React.js"],
                            "impact_metrics": ["43% Latency Reduction", "99.9% API Uptime", "100% SRS & DRS"]
                        },
                        {
                            "id": "exp-suvidha",
                            "role": "Full-Stack Developer",
                            "company": "Suvidha Foundation",
                            "duration": "July 2022 – Aug 2022",
                            "mode": "Hybrid",
                            "institution_url": "https://suvidhafoundationedutech.org/",
                            "location": "Ahmedabad, India",
                            "desc": [
                                "I engineered and deployed production-ready platforms by architecting high-performance React.js frontends integrated with Python FastAPI backends, ensuring seamless real-time data synchronization and delivering highly responsive, user-centric interfaces.",
                                "I architected scalable MySQL and PostgreSQL database schemas and engineered automated Python ETL pipelines, incorporating rigorous multi-stage validation layers to maintain 100% data integrity and optimize retrieval speeds for complex analytical workflows.",
                                "I revolutionized software delivery cycles by implementing automated CI/CD pipelines and Docker containerization, while significantly improving system uptime through RESTful API optimization and deep-dive root cause analysis on distributed system failures."
                            ],
                            "responsibilities": [
                                "Architecture: Developed production-ready platforms using React.js & Python, ensuring seamless real-time data flow & responsive UI.",
                                "Database: Optimized MySQL and PostgreSQL schemas with complex indexing, significantly improving data retrieval and system scalability.",
                                "Data Pipelines: Engineered automated Python pipelines for multi-table data, incorporating validation to ensure 100% data integrity.",
                                "DevOps: Implemented CI/CD and Docker for streamlined deployments, maintaining high availability within remote Agile environments.",
                                "Reliability: Optimized RESTful API consistency and performed root cause analysis to maintain end-to-end system reliability and performance."
                            ],
                            "depth_ride": {
                                "start": "Joined as a Full-Stack Intern focusing on UI/UX and React.js frontend architecture.",
                                "growth": "Pivoted into Data Engineering, engineering validation layers for automated analytical workflows.",
                                "peak": "Successfully deployed a production-grade platform with containerized microservices and optimized SQL."
                            },
                            "data_flow": [
                                {"node": "Frontend", "desc": "React.js + Bootstrap UI"},
                                {"node": "Logic", "desc": "JavaScript API & Python Data Logic"},
                                {"node": "Database", "desc": "MySQL Relational Architecture"},
                                {"node": "DevOps", "desc": "Docker Containerization & CI/CD"}
                            ],
                            "tech_stack": ["REACT.JS", "PYTHON", "MYSQL", "DOCKER", "FIGMA", "BOOTSTRAP"],
                            "impact_metrics": ["100% Data Consistency", "Production-Ready Deployment", "Optimized Query Performance"]
                        },

                        {
                            "id": "exp-sparks",
                            "role": "Frontend Developer",
                            "company": "The Sparks Foundation",
                            "duration": "Jan 2022 – Jun 2022",
                            "mode": "Remote",
                            "institution_url": "https://www.thesparksfoundationsingapore.org/",
                            "location": "Ahmedabad, India",
                            "desc": [
                                "Architected and deployed responsive, user-centric frontend experiences within a high-speed virtual environment, focusing on the intersection of high-fidelity design and scalable logic.",
                                "Engineered interactive, cross-device compatible interfaces using React.js and JavaScript, ensuring 100% visual consistency and seamless performance across all screen resolutions.",
                                "Translated qualitative design requirements into production-grade code, bridging the gap between creative UI/UX vision and technical implementation."
                            ],
                            "responsibilities": [
                                "UI/UX Orchestration: Engineered interactive user interfaces using React.js and Bootstrap, ensuring seamless cross-device compatibility.",
                                "Component-Based Architecture: Applied modular design patterns to build reusable UI components, improving code maintainability and reducing style redundancies.",
                                "Synergy: Collaborated on integrating frontend layouts with backend API services, focusing on data integrity and smooth state management.",
                                "Optimization: Implemented asset compression and efficient DOM manipulation to ensure rapid load times and fluid user journeys.",
                                "Engineering Excellence: Managed remote engineering workflows using Git and technical communication tools to maintain high delivery speed."
                            ],
                            "depth_ride": {
                                "start": "Joined as a Web Development & Design Intern to translate creative prototypes into functional code.",
                                "growth": "Specialized in component-driven development and performance optimization for complex React layouts.",
                                "peak": "Successfully bridged the gap between design and production, delivering a stable and visually polished web application."
                            },
                            "data_flow": [
                                {"node": "Design System", "desc": "High-Fidelity UI/UX Prototypes"},
                                {"node": "Frontend Core", "desc": "React.js & Modular Component Logic"},
                                {"node": "State Management", "desc": "API Integration & Data Synergy"},
                                {"node": "Optimization", "desc": "Asset Compression & DOM Efficiency"}
                            ],
                            "tech_stack": ["REACT", "JAVASCRIPT", "BOOTSTRAP", "CSS3", "GIT", "REST_API", "FIGMA"],
                            "impact_metrics": ["High-Fidelity UI Execution", "Responsive Design Mastery", "Modular Code Reusability"]
                        },

                        {
                            "id": "exp-media",
                            "role": "Backend Developer",
                            "company": "Media Platforms",
                            "duration": "May 2021 – Jul 2021",
                            "mode": "Remote",
                            "institution_url": "https://mediaplatforms.ca/",
                            "location": "Ahmedabad, India",
                            "desc": [
                                "Independently architected and scaled robust Python-Django modules for multi-table relational datasets, managing the full development lifecycle as a solo contributor to ensure high-performance backend logic.",
                                "Engineered complex PostgreSQL queries and validation schemas to identify critical data gaps, significantly reducing query latency and ensuring 100% data integrity for analytical workflows.",
                                "Designed and documented RESTful APIs using Postman, seamlessly bridging the gap between backend services and modern frontends styled with Tailwind CSS to deliver a production-grade user experience."
                            ],
                            "responsibilities": [
                                "Architecture: Developed Python-Django modules for multi-table datasets, maintaining high efficiency as a solo contributor.",
                                "Database: Optimized complex PostgreSQL queries to improve performance and validate data integrity across large datasets.",
                                "Business Logic: Implemented structured validation and filtering layers to support accurate, data-driven analytical workflows.",
                                "API Testing: Engineered and tested RESTful APIs using Postman, ensuring high robustness.",
                                "Integration: Leveraged Tailwind CSS and GitHub for end-to-end developments."
                            ],
                            "depth_ride": {
                                "start": "Joined as a solo contributor to take ownership of critical backend data-processing layers.",
                                "growth": "Pivoted toward database optimization, specializing in identifying missing records across massive MySQL datasets.",
                                "peak": "Successfully strengthened the core analytical engine, improving retrieval speeds for real-time reporting."
                            },
                            "data_flow": [
                                {"node": "Data Source", "desc": "Relational MySQL Datasets"},
                                {"node": "Logic Layer", "desc": "Python-Django Business Logic"},
                                {"node": "Optimization", "desc": "SQL Query Tuning & Latency Reduction"},
                                {"node": "Validation", "desc": "PyTest & Integrity Filtering"}
                            ],
                            "tech_stack": ["PYTHON", "DJANGO", "SQL", "PYTEST", "REST_FRAMEWORK", "LINUX", "POSTMAN"],
                            "impact_metrics": ["40% Latency Reduction", "Solo Contributor Ownership", "Zero Supervised Failures"]
                        },
                        {
                            "id": "exp-gdsc",
                            "role": "GDSC Project Head",
                            "company": "Google Developer Student Clubs",
                            "duration": "Jun 2021 – Jun 2022",
                            "mode": "In-Person",
                            "institution_url": "https://gdg.community.dev/",
                            "location": "Indus University",
                            "desc": [
                                "As the GDSC Chapter Lead, I drove the technical and operational vision for the community, managing a team of organizers and developers to deliver high-engagement learning experiences and technical project excellence.",
                                "I bridged the gap between academic theory and industry practice by mentoring 15+ teams on AI/ML pipeline integration, Database Management, and Azure Cloud Computing, fostering a culture of rapid prototyping and clean code.",
                                "I demonstrated elite project management by scaling technical outreach to 200+ active participants, maintaining 100% punctuality in event delivery while managing resource allocation, speaker coordination, and stakeholder relations."
                            ],
                            "responsibilities": [
                                "Technical Leadership: I spearheaded the GDSC chapter as Project Head, mentoring 15+ cross-functional teams through the full lifecycle.",
                                "Curriculum Delivery: I delivered 7+ high-impact technical workshops for 200+ students, covering advanced topics like Cloud Computing, CI/CD & Analytics workflows.",
                                "Project Orchestration: I directed the end-to-end execution of large-scale technical events, managing stakeholder communication between developers & industry speakers.",
                                "AI/ML Excellence: I oversaw student-led research in Deep Learning and BDA, providing technical guidance on model deployment."
                            ],
                            "depth_ride": {
                                "start": "Appointed as Chapter Lead to bridge the gap between Google's technical resources and the student community.",
                                "growth": "Scaled the chapter by coordinating speakers and developers, delivering hands-on sessions on model deployment.",
                                "peak": "Successfully directed 7+ major events, fostering a culture of software engineering best practices and Agile delivery."
                            },
                            "data_flow": [
                                {"node": "Strategy", "desc": "Curriculum Planning & Event Roadmap"},
                                {"node": "Mentorship", "desc": "Cross-Functional Team Coordination"},
                                {"node": "Execution", "desc": "Live Workshops & Hands-on Lab Delivery"},
                                {"node": "Outcome", "desc": "Deployment of AI/ML Student Projects"}
                            ],
                            "tech_stack": ["MACHINE_LEARNING", "GEN_AI", "PYTHON", "SQL", "CI/CD", "PROJECT_MGMT"],
                            "impact_metrics": ["200+ Students Engaged", "15+ Teams Mentored", "7+ Workshops Delivered"]
                        }
                    ],
        "contact": {
            "email": "abhi1281.patel@gmail.com",
        },
    }