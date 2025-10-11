Project Title: HIPAA-Compliant Patient Portal Simulation

Simulated patient record system with role-based access control (RBAC), audit logging, and Dockerized services. It demonstrates practical security principles.


High-Level Architecture (all local)

Component	Tech / Tool	Dockerized?
Frontend UI	Flask or React (lightweight)	
Backend API	Python + FastAPI or Node.js	
Database MySQL or PostgreSQL (with sample patient data)	
Authentication Service	Auth0 (mocked locally) or Keycloak	
Logging & Monitoring	ELK Stack or simple audit logs	
Vulnerability Scanner	OpenVAS or Trivy	(optional but relevant)
Docker Orchestration	docker-compose	


Key Features to Implement
-Simulate admin, nurse, and patient roles
-Mask or redact sensitive PII (to show HIPAA awareness)
-Audit log all access (who accessed what, when)
-Dockerize each component using docker-compose
-Add a mock EHR dashboard with fake data
