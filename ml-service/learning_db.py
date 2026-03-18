# Learning Suggestion Database
# Curated learning paths for common dev skills
# Each skill has: priority, 2-3 actionable next steps, 1-2 resource links

learning_data = {
    "docker": {
        "priority": "high",
        "steps": [
            "Learn Docker basics: images, containers, and the Docker CLI",
            "Build and run your first containerized Node.js/Python app"
        ],
        "resources": [
            "https://docs.docker.com/get-started/"
        ]
    },
    "kubernetes": {
        "priority": "high",
        "steps": [
            "Understand Pods, Services, and Deployments architecture",
            "Deploy a simple app on Kubernetes locally using Minikube"
        ],
        "resources": [
            "https://kubernetes.io/docs/tutorials/kubernetes-basics/"
        ]
    },
    "aws": {
        "priority": "high",
        "steps": [
            "Master EC2 instances and S3 storage basics",
            "Deploy a serverless function using AWS Lambda"
        ],
        "resources": [
            "https://aws.amazon.com/getting-started/"
        ]
    },
    "react": {
        "priority": "high",
        "steps": [
            "Learn JSX, components, state, and props fundamentals",
            "Build a multi-page app with React Router"
        ],
        "resources": [
            "https://react.dev/learn"
        ]
    },
    "python": {
        "priority": "medium",
        "steps": [
            "Master decorators, context managers, and generators",
            "Build a CLI tool or web scraper project"
        ],
        "resources": [
            "https://docs.python.org/3/"
        ]
    },
    "javascript": {
        "priority": "high",
        "steps": [
            "Master closures, async/await, and the event loop",
            "Build a real-time app using WebSockets"
        ],
        "resources": [
            "https://javascript.info/"
        ]
    },
    "node": {
        "priority": "high",
        "steps": [
            "Understand event-driven architecture and streams",
            "Build a REST API with Express and middleware"
        ],
        "resources": [
            "https://nodejs.org/en/docs/"
        ]
    },
    "express": {
        "priority": "medium",
        "steps": [
            "Master middleware, routing, and request handling",
            "Build authentication with JWT tokens"
        ],
        "resources": [
            "https://expressjs.com/en/guide/routing.html"
        ]
    },
    "mongodb": {
        "priority": "medium",
        "steps": [
            "Design schemas and understand document structure",
            "Implement indexing and aggregation pipelines"
        ],
        "resources": [
            "https://docs.mongodb.com/manual/tutorial/"
        ]
    },
    "mysql": {
        "priority": "medium",
        "steps": [
            "Learn normalization and JOIN operations deeply",
            "Optimize queries with indexing and explain plans"
        ],
        "resources": [
            "https://dev.mysql.com/doc/refman/8.0/en/"
        ]
    },
    "postgresql": {
        "priority": "medium",
        "steps": [
            "Explore advanced features: CTEs, window functions",
            "Master transaction handling and ACID properties"
        ],
        "resources": [
            "https://www.postgresql.org/docs/"
        ]
    },
    "fastapi": {
        "priority": "medium",
        "steps": [
            "Learn request validation with Pydantic models",
            "Implement async endpoints and background tasks"
        ],
        "resources": [
            "https://fastapi.tiangolo.com/tutorial/"
        ]
    },
    "django": {
        "priority": "medium",
        "steps": [
            "Master Django ORM and QuerySets",
            "Build forms, authentication, and admin panels"
        ],
        "resources": [
            "https://docs.djangoproject.com/en/stable/intro/tutorial01/"
        ]
    },
    "flask": {
        "priority": "low",
        "steps": [
            "Structure apps with blueprints and factories",
            "Integrate SQLAlchemy for database operations"
        ],
        "resources": [
            "https://flask.palletsprojects.com/tutorial/"
        ]
    },
    "machine learning": {
        "priority": "medium",
        "steps": [
            "Understand supervised vs unsupervised learning",
            "Build a model with scikit-learn and evaluate it"
        ],
        "resources": [
            "https://scikit-learn.org/stable/user_guide.html"
        ]
    },
    "tensorflow": {
        "priority": "medium",
        "steps": [
            "Learn neural networks and Keras API basics",
            "Train an image classification model"
        ],
        "resources": [
            "https://www.tensorflow.org/tutorials"
        ]
    },
    "pytorch": {
        "priority": "medium",
        "steps": [
            "Understand tensors and autograd mechanics",
            "Build and train a neural network from scratch"
        ],
        "resources": [
            "https://pytorch.org/tutorials/"
        ]
    },
    "angular": {
        "priority": "low",
        "steps": [
            "Master components, services, and dependency injection",
            "Build a real-time app with RxJS Observables"
        ],
        "resources": [
            "https://angular.io/docs"
        ]
    },
    "vue": {
        "priority": "low",
        "steps": [
            "Learn reactivity system and component lifecycle",
            "Build with Composition API or Options API"
        ],
        "resources": [
            "https://vuejs.org/guide/"
        ]
    },
    "html": {
        "priority": "low",
        "steps": [
            "Master semantic HTML and accessibility (a11y)",
            "Learn form handling and input validation"
        ],
        "resources": [
            "https://developer.mozilla.org/en-US/docs/Web/HTML"
        ]
    },
    "css": {
        "priority": "low",
        "steps": [
            "Master Flexbox and CSS Grid layouts",
            "Learn responsive design and mobile-first approach"
        ],
        "resources": [
            "https://developer.mozilla.org/en-US/docs/Web/CSS"
        ]
    },
    "java": {
        "priority": "medium",
        "steps": [
            "Master OOP: inheritance, polymorphism, interfaces",
            "Build a Spring Boot REST API application"
        ],
        "resources": [
            "https://docs.oracle.com/javase/tutorial/"
        ]
    },
    "ruby": {
        "priority": "low",
        "steps": [
            "Learn blocks, procs, and functional programming",
            "Build a Rails application with generators"
        ],
        "resources": [
            "https://guides.rubyonrails.org/"
        ]
    },
}


def get_learning_path(missing_skills, job_description=""):
    """
    Generate personalized learning path for missing skills.
    
    Args:
        missing_skills: List of skills the user doesn't have
        job_description: Job posting text (optional, for relevance scoring)
    
    Returns:
        List of learning suggestions, max 5 skills, sorted by priority
    """
    
    learning_path = []
    
    for skill in missing_skills:
        skill_lower = skill.lower().strip()
        
        if skill_lower in learning_data:
            learning_path.append({
                "skill": skill,
                "priority": learning_data[skill_lower]["priority"],
                "steps": learning_data[skill_lower]["steps"][:2],  # Max 2 steps
                "resources": learning_data[skill_lower]["resources"][:1]  # Max 1 resource
            })
    
    # Sort by priority: high → medium → low
    priority_order = {"high": 0, "medium": 1, "low": 2}
    learning_path.sort(key=lambda x: priority_order.get(x["priority"], 3))
    
    # Limit to top 5 skills (DEPLOYMENT-SAFE)
    return learning_path[:5]
