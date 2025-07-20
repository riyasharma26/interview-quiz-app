class QuestionBank:
    def __init__(self):
        self.questions = {
            "Software Engineer": [
                {
                    "question": "Explain the difference between a stack and a queue data structure.",
                    "keywords": ["LIFO", "FIFO", "last in first out", "first in first out", "push", "pop", "enqueue", "dequeue", "stack", "queue"],
                    "sample_answer": "A stack is a LIFO (Last In First Out) data structure where elements are added and removed from the same end (top). Operations include push (add) and pop (remove). A queue is a FIFO (First In First Out) data structure where elements are added at one end (rear) and removed from the other end (front). Operations include enqueue (add) and dequeue (remove)."
                },
                {
                    "question": "What is the difference between SQL and NoSQL databases?",
                    "keywords": ["relational", "non-relational", "ACID", "schema", "flexible", "scalability", "consistency", "SQL", "NoSQL"],
                    "sample_answer": "SQL databases are relational, use structured schemas, support ACID properties, and use SQL for queries. They're great for complex relationships and consistency. NoSQL databases are non-relational, have flexible schemas, prioritize scalability and performance, and use various data models (document, key-value, graph). They're better for handling large volumes of unstructured data."
                },
                {
                    "question": "Describe the concept of Big O notation and why it's important.",
                    "keywords": ["time complexity", "space complexity", "algorithm", "efficiency", "scalability", "performance", "worst case", "Big O"],
                    "sample_answer": "Big O notation describes the upper bound of an algorithm's time or space complexity in terms of input size. It helps evaluate algorithm efficiency and scalability. For example, O(1) is constant time, O(n) is linear, O(n²) is quadratic. It's crucial for choosing the right algorithm and predicting performance as data scales."
                },
                {
                    "question": "What are the principles of Object-Oriented Programming?",
                    "keywords": ["encapsulation", "inheritance", "polymorphism", "abstraction", "OOP", "classes", "objects"],
                    "sample_answer": "The four main principles are: 1) Encapsulation - bundling data and methods together, hiding internal details; 2) Inheritance - creating new classes based on existing ones; 3) Polymorphism - objects of different types responding to the same interface; 4) Abstraction - hiding complex implementation details behind simple interfaces."
                },
                {
                    "question": "How would you optimize a slow-running database query?",
                    "keywords": ["index", "query plan", "optimization", "joins", "WHERE clause", "performance", "execution plan", "statistics"],
                    "sample_answer": "I'd start by analyzing the query execution plan to identify bottlenecks. Add appropriate indexes on frequently queried columns, optimize WHERE clauses to filter early, avoid unnecessary JOINs, use proper data types, update table statistics, and consider query restructuring. I'd also check for missing indexes and ensure the query is using existing indexes effectively."
                }
            ],
            "Data Scientist": [
                {
                    "question": "Explain the bias-variance tradeoff in machine learning.",
                    "keywords": ["bias", "variance", "overfitting", "underfitting", "model complexity", "tradeoff", "generalization", "error"],
                    "sample_answer": "The bias-variance tradeoff describes the relationship between model complexity and prediction error. High bias (underfitting) occurs when a model is too simple to capture underlying patterns. High variance (overfitting) occurs when a model is too complex and learns noise. The goal is to find the optimal balance that minimizes total error and maximizes generalization to new data."
                },
                {
                    "question": "What is the difference between supervised and unsupervised learning?",
                    "keywords": ["supervised", "unsupervised", "labeled data", "unlabeled data", "classification", "regression", "clustering", "dimensionality reduction"],
                    "sample_answer": "Supervised learning uses labeled training data to learn mapping from inputs to outputs, including classification and regression tasks. Unsupervised learning finds patterns in unlabeled data without target variables, including clustering, dimensionality reduction, and association rules. Semi-supervised learning combines both approaches."
                },
                {
                    "question": "How would you handle missing data in a dataset?",
                    "keywords": ["missing data", "imputation", "deletion", "mean", "median", "mode", "forward fill", "backward fill", "interpolation", "missingness"],
                    "sample_answer": "Approaches include: 1) Deletion - removing rows/columns with missing values; 2) Imputation - filling with mean, median, mode, or predicted values; 3) Forward/backward fill for time series; 4) Using algorithms that handle missing values naturally; 5) Creating missingness indicators. The choice depends on the amount and pattern of missing data."
                },
                {
                    "question": "Describe the process of feature engineering and why it's important.",
                    "keywords": ["feature engineering", "feature selection", "feature creation", "domain knowledge", "transformation", "scaling", "encoding", "dimensionality"],
                    "sample_answer": "Feature engineering involves creating, selecting, and transforming variables to improve model performance. It includes scaling numerical features, encoding categorical variables, creating interaction terms, handling outliers, and applying domain knowledge. Good feature engineering can significantly improve model accuracy and interpretability, often more than algorithm selection."
                },
                {
                    "question": "What metrics would you use to evaluate a classification model?",
                    "keywords": ["accuracy", "precision", "recall", "F1-score", "ROC", "AUC", "confusion matrix", "specificity", "sensitivity"],
                    "sample_answer": "Key metrics include: Accuracy (overall correctness), Precision (true positives/predicted positives), Recall/Sensitivity (true positives/actual positives), F1-score (harmonic mean of precision and recall), ROC curve and AUC (threshold-independent performance), and confusion matrix for detailed breakdown. Choice depends on the problem context and class imbalance."
                }
            ],
            "Product Manager": [
                {
                    "question": "How would you prioritize features for a product roadmap?",
                    "keywords": ["prioritization", "impact", "effort", "value", "user needs", "business goals", "ROI", "framework", "stakeholders"],
                    "sample_answer": "I'd use a framework like RICE (Reach, Impact, Confidence, Effort) or Value vs. Effort matrix. Consider user impact, business value, technical feasibility, resource requirements, and strategic alignment. Gather input from users, stakeholders, and development teams. Continuously reassess based on new data and changing priorities."
                },
                {
                    "question": "Describe how you would gather and analyze user feedback.",
                    "keywords": ["user research", "surveys", "interviews", "analytics", "feedback", "usability testing", "data analysis", "insights"],
                    "sample_answer": "I'd use multiple methods: user interviews for qualitative insights, surveys for quantitative data, usability testing for behavioral observations, analytics for usage patterns, and feedback forms for ongoing input. Analyze themes, prioritize issues by frequency and impact, and translate findings into actionable product improvements."
                },
                {
                    "question": "How would you handle conflicting stakeholder requirements?",
                    "keywords": ["stakeholder management", "communication", "negotiation", "compromise", "alignment", "priorities", "trade-offs", "facilitation"],
                    "sample_answer": "I'd facilitate discussions to understand underlying needs, use data to support decisions, find common ground, and clearly communicate trade-offs. Create alignment around shared goals, propose compromise solutions, and ensure transparent decision-making processes. Document decisions and rationale for future reference."
                },
                {
                    "question": "What metrics would you track to measure product success?",
                    "keywords": ["KPIs", "metrics", "user engagement", "retention", "conversion", "revenue", "satisfaction", "adoption", "churn"],
                    "sample_answer": "I'd track a mix of user engagement metrics (DAU/MAU, session length), business metrics (revenue, conversion rates), product-specific metrics (feature adoption, task completion), and user satisfaction metrics (NPS, CSAT). Choose metrics that align with business goals and provide actionable insights for product decisions."
                },
                {
                    "question": "How would you launch a new product feature?",
                    "keywords": ["launch strategy", "go-to-market", "communication", "rollout", "testing", "feedback", "iteration", "success metrics"],
                    "sample_answer": "I'd develop a launch strategy including target audience identification, messaging, rollout plan (possibly phased), success metrics, and communication plan. Conduct beta testing, prepare support materials, coordinate with marketing and sales, monitor performance closely, and iterate based on user feedback and data."
                }
            ],
            "UX Designer": [
                {
                    "question": "Explain your design process from research to final design.",
                    "keywords": ["user research", "personas", "wireframes", "prototypes", "testing", "iteration", "design thinking", "user-centered design"],
                    "sample_answer": "My process starts with user research to understand needs and pain points. I create personas and user journeys, then develop wireframes and prototypes. I conduct usability testing, iterate based on feedback, and create high-fidelity designs. Throughout, I collaborate with stakeholders and validate designs with users."
                },
                {
                    "question": "How do you ensure your designs are accessible?",
                    "keywords": ["accessibility", "WCAG", "color contrast", "screen readers", "keyboard navigation", "inclusive design", "disabilities", "compliance"],
                    "sample_answer": "I follow WCAG guidelines, ensure proper color contrast ratios, provide alternative text for images, design for keyboard navigation, use semantic HTML, test with screen readers, and consider various disabilities. I also conduct accessibility testing and involve users with disabilities in the design process."
                },
                {
                    "question": "Describe how you would conduct user research for a new feature.",
                    "keywords": ["user interviews", "surveys", "observation", "personas", "user journeys", "pain points", "needs assessment", "research methods"],
                    "sample_answer": "I'd start with defining research objectives, then use mixed methods: user interviews for deep insights, surveys for broader validation, observational studies for behavioral data, and competitive analysis. I'd create personas and user journeys, identify pain points and opportunities, and synthesize findings into actionable design requirements."
                },
                {
                    "question": "How do you handle design feedback and criticism?",
                    "keywords": ["feedback", "collaboration", "iteration", "stakeholder management", "design rationale", "constructive criticism", "communication"],
                    "sample_answer": "I welcome feedback as opportunities to improve designs. I listen actively, ask clarifying questions, explain design rationale when needed, and remain open to different perspectives. I separate personal attachment from professional critique, focus on user needs and business goals, and iterate based on valid feedback."
                },
                {
                    "question": "What's your approach to designing for mobile vs. desktop?",
                    "keywords": ["responsive design", "mobile-first", "touch interface", "screen size", "context of use", "performance", "adaptive design"],
                    "sample_answer": "I consider context of use, screen constraints, and interaction methods. Mobile designs prioritize essential content, use touch-friendly elements, and consider one-handed use. Desktop designs can show more information density and complex interactions. I often use a mobile-first approach and ensure responsive design across devices."
                }
            ],
            "Marketing Manager": [
                {
                    "question": "How would you develop a marketing strategy for a new product launch?",
                    "keywords": ["target audience", "positioning", "channels", "messaging", "budget", "timeline", "KPIs", "competitive analysis", "market research"],
                    "sample_answer": "I'd start with market research and competitive analysis, define target audience and positioning, develop key messaging, select appropriate channels (digital, traditional, social), create a timeline with milestones, set budget allocation, and establish KPIs for measuring success. I'd also plan for post-launch optimization."
                },
                {
                    "question": "Describe how you would measure the ROI of a marketing campaign.",
                    "keywords": ["ROI", "attribution", "metrics", "conversion tracking", "cost per acquisition", "lifetime value", "analytics", "revenue"],
                    "sample_answer": "I'd track revenue generated vs. campaign costs, using attribution models to connect touchpoints to conversions. Key metrics include cost per acquisition, customer lifetime value, conversion rates, and revenue attribution. I'd use analytics tools, set up proper tracking, and consider both direct and indirect impact on business goals."
                },
                {
                    "question": "How would you handle a marketing campaign that's underperforming?",
                    "keywords": ["analysis", "optimization", "A/B testing", "pivot", "data-driven", "troubleshooting", "performance metrics", "iteration"],
                    "sample_answer": "I'd analyze performance data to identify issues, test different elements (creative, targeting, messaging), optimize based on findings, and consider pivoting strategy if needed. I'd look at funnel metrics, audience response, channel performance, and external factors. Quick iteration and data-driven decisions are key."
                },
                {
                    "question": "What's your approach to understanding your target audience?",
                    "keywords": ["market research", "personas", "customer interviews", "surveys", "analytics", "demographics", "psychographics", "behavior"],
                    "sample_answer": "I use multiple research methods: customer interviews for qualitative insights, surveys for quantitative data, analytics for behavioral patterns, and social listening for sentiment. I create detailed personas including demographics, psychographics, pain points, and preferences. Regular research updates ensure understanding stays current."
                },
                {
                    "question": "How do you stay current with marketing trends and technologies?",
                    "keywords": ["continuous learning", "industry publications", "networking", "conferences", "testing", "experimentation", "trends", "innovation"],
                    "sample_answer": "I follow industry publications, attend conferences and webinars, participate in professional networks, and engage with thought leaders on social media. I also experiment with new tools and platforms, participate in beta programs, and maintain a learning mindset to adapt to the rapidly evolving marketing landscape."
                }
            ],
            "Sales Representative": [
                {
                    "question": "Describe your approach to handling objections from potential customers.",
                    "keywords": ["objection handling", "listening", "empathy", "value proposition", "benefits", "addressing concerns", "closing", "relationship building"],
                    "sample_answer": "I listen actively to understand the real concern behind the objection, acknowledge their perspective with empathy, ask clarifying questions, and address the specific issue with relevant information or solutions. I focus on value and benefits rather than just features, and use the objection as an opportunity to better understand their needs."
                },
                {
                    "question": "How do you qualify potential leads?",
                    "keywords": ["lead qualification", "BANT", "budget", "authority", "need", "timeline", "decision maker", "fit", "criteria"],
                    "sample_answer": "I use qualification frameworks like BANT (Budget, Authority, Need, Timeline) to assess leads. I ask targeted questions about their challenges, budget constraints, decision-making process, and timeline. I also evaluate how well our solution fits their needs and whether they're the right decision maker or can connect me to one."
                },
                {
                    "question": "What's your strategy for building long-term client relationships?",
                    "keywords": ["relationship building", "trust", "value", "communication", "follow-up", "customer success", "retention", "upselling"],
                    "sample_answer": "I focus on becoming a trusted advisor by understanding their business goals, providing ongoing value beyond the initial sale, maintaining regular communication, and being responsive to their needs. I follow up consistently, share relevant insights, and look for opportunities to help them succeed, which naturally leads to retention and expansion."
                },
                {
                    "question": "How do you handle rejection and maintain motivation?",
                    "keywords": ["resilience", "motivation", "mindset", "learning", "persistence", "self-improvement", "goals", "positive attitude"],
                    "sample_answer": "I view rejection as a learning opportunity and part of the process. I maintain a positive mindset by focusing on my goals, celebrating small wins, and continuously improving my skills. I analyze what went wrong, seek feedback, and adjust my approach. I also maintain a full pipeline so individual rejections don't derail my overall progress."
                },
                {
                    "question": "Describe your process for researching prospects before a sales call.",
                    "keywords": ["prospect research", "preparation", "company background", "pain points", "decision makers", "competitive landscape", "personalization"],
                    "sample_answer": "I research the company's background, recent news, industry challenges, and competitive landscape. I identify key decision makers and their roles, understand their potential pain points, and look for common connections. I also review their website, social media, and any previous interactions to personalize my approach and demonstrate genuine interest."
                }
            ],
            "Project Manager": [
                {
                    "question": "How do you handle scope creep in a project?",
                    "keywords": ["scope creep", "change management", "documentation", "stakeholder communication", "impact assessment", "approval process", "boundaries"],
                    "sample_answer": "I prevent scope creep by clearly defining project scope upfront and documenting all requirements. When changes are requested, I assess the impact on timeline, budget, and resources, communicate these impacts to stakeholders, and follow a formal change approval process. I maintain clear boundaries while being flexible for legitimate business needs."
                },
                {
                    "question": "Describe your approach to risk management in projects.",
                    "keywords": ["risk assessment", "risk mitigation", "contingency planning", "risk register", "monitoring", "proactive", "stakeholder communication"],
                    "sample_answer": "I start with risk identification during planning, assess probability and impact, and maintain a risk register. I develop mitigation strategies and contingency plans, assign risk owners, and monitor risks throughout the project lifecycle. I communicate risks proactively to stakeholders and adjust plans as needed."
                },
                {
                    "question": "How do you ensure effective communication among team members?",
                    "keywords": ["communication", "meetings", "documentation", "collaboration tools", "transparency", "feedback", "stakeholder management", "status updates"],
                    "sample_answer": "I establish clear communication channels and protocols, hold regular team meetings and one-on-ones, use collaboration tools effectively, and maintain transparent documentation. I encourage open feedback, tailor communication styles to different stakeholders, and provide regular status updates to keep everyone informed and aligned."
                },
                {
                    "question": "What's your approach to managing project timelines and deadlines?",
                    "keywords": ["timeline management", "scheduling", "milestones", "dependencies", "critical path", "buffer time", "monitoring", "adjustments"],
                    "sample_answer": "I create realistic timelines with clear milestones, identify dependencies and critical paths, build in buffer time for unexpected issues, and monitor progress regularly. I use project management tools to track progress, communicate delays early, and adjust schedules as needed while maintaining focus on key deliverables."
                },
                {
                    "question": "How do you handle conflicts within your project team?",
                    "keywords": ["conflict resolution", "mediation", "communication", "team dynamics", "problem-solving", "neutral", "collaboration", "relationships"],
                    "sample_answer": "I address conflicts early by facilitating open communication between parties, listening to all perspectives, and helping find common ground. I remain neutral, focus on project goals rather than personalities, and work with the team to develop collaborative solutions. I also take steps to prevent future conflicts through clear roles and expectations."
                }
            ],
            "DevOps Engineer": [
                {
                    "question": "Explain the concept of Infrastructure as Code (IaC) and its benefits.",
                    "keywords": ["Infrastructure as Code", "IaC", "automation", "version control", "reproducibility", "consistency", "Terraform", "CloudFormation"],
                    "sample_answer": "Infrastructure as Code treats infrastructure provisioning like software development, using code to define and manage infrastructure. Benefits include version control, reproducibility, consistency across environments, automation, faster deployments, and easier disaster recovery. Tools like Terraform and CloudFormation enable declarative infrastructure management."
                },
                {
                    "question": "How would you implement a CI/CD pipeline?",
                    "keywords": ["CI/CD", "continuous integration", "continuous deployment", "automation", "testing", "build", "deployment", "pipeline"],
                    "sample_answer": "I'd set up automated builds triggered by code commits, integrate automated testing (unit, integration, security), implement deployment automation with approval gates, use configuration management, and include monitoring and rollback capabilities. The pipeline should provide fast feedback, maintain quality, and enable frequent, reliable deployments."
                },
                {
                    "question": "Describe your approach to monitoring and logging in a production environment.",
                    "keywords": ["monitoring", "logging", "metrics", "alerting", "observability", "APM", "dashboards", "troubleshooting"],
                    "sample_answer": "I implement comprehensive monitoring covering infrastructure, applications, and business metrics. This includes centralized logging, real-time alerting, performance monitoring, and observability tools. I create dashboards for different stakeholders, set up proactive alerting,
