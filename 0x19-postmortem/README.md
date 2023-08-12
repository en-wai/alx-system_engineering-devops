# FLask App Outage Incident report
> By NanaYaw Asare (En-wai)

Issue Summary:

Duration: August 10, 2023, 14:00 - August 10, 2023, 18:30 (UTC)
Impact: Flask-based web application was inaccessible, causing a service outage for all users during the incident. Approximately 75% of users were affected.

Timeline:

- Issue Detected: August 10, 2023, 14:00 (UTC)
- Detection Method: Monitoring alert triggered due to increased server response time and error rate.
- Actions Taken: Investigated server logs, checked database connectivity, assumed a surge in traffic as the root cause.
- Misleading Paths: Focused on scaling up server resources and load balancer configurations.
- Escalation: Incident was escalated to the DevOps and Backend Development teams.

Resolution:

- Root Cause: The issue was caused by an unoptimized database query in the Flask app's API endpoint.
- Fix: Rewrote the inefficient query, optimized database indexes, and implemented query caching.
  
Corrective and Preventative Measures:

- Improvements/Fixes: Enhance database query performance, implement query optimization as a development practice, set up more comprehensive monitoring.
- Tasks to Address Issue:
  1. Review and optimize all critical database queries in the application.
  2. Implement automated testing for query performance during the CI/CD pipeline.
  3. Set up comprehensive monitoring for server response times, error rates, and query performance.
  4. Establish a protocol for incident escalation and communication between development and operations teams.

Postmortem Report:

Issue Details:
On August 10, 2023, our Flask-based web application experienced a service outage from 14:00 to 18:30 (UTC), impacting approximately 75% of users. During this time, users were unable to access the application, and monitoring alerts indicated increased server response times and error rates.

Timeline:
At 14:00 (UTC), our monitoring system triggered an alert due to degraded server performance. We promptly initiated investigation, focusing on server logs and database connectivity. An assumption was made that a sudden traffic surge was responsible. This led us down a misleading path, causing us to scale up server resources and modify load balancer configurations. The incident was escalated to the DevOps and Backend Development teams for further analysis.

Root Cause and Resolution:
After an extensive investigation, we identified the root cause as an unoptimized database query in a critical Flask app API endpoint. The inefficient query was straining the database server, leading to slow response times and increased error rates. To resolve this, we rewrote the query, optimized database indexes, and introduced query caching to alleviate the database load. This fix resulted in improved response times and error rates, restoring the application's functionality.

Corrective and Preventative Measures:
To prevent similar incidents in the future, we will take the following measures:
1. Query Optimization: Review and optimize all essential database queries within the application codebase, making query performance a development priority.
2. Automated Testing: Implement automated testing for query performance as part of our CI/CD pipeline to catch performance regressions early in the development process.
3. Comprehensive Monitoring: Set up comprehensive monitoring for key performance indicators, including server response times, error rates, and query performance. This will enable us to detect and address issues proactively.
4. Incident Protocol: Establish a clear incident escalation and communication protocol between the development and operations teams, ensuring rapid and coordinated response to any future issues.

In conclusion, the service outage was a result of an unoptimized database query in our Flask application. By addressing the root cause, optimizing queries, and enhancing monitoring practices, we have taken steps to prevent such incidents from occurring again. We appreciate the teamwork and collaboration demonstrated by both the DevOps and Backend Development teams during this incident.
