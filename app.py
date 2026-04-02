apiVersion: apps/v1
kind: Deployment
metadata:
  name: log-analyzer-deployment
spec:
  replicas: 2
  selector:
    matchLabels:
      app: log-analyzer
  template:
    metadata:
      labels:
        app: log-analyzer
    spec:
      containers:
      - name: log-analyzer-container
        image: yourdockerhubuser/log-analyzer:latest
        ports:
        - containerPort: 5000
---
apiVersion: v1
kind: Service
metadata:
  name: log-analyzer-service
spec:
  type: LoadBalancer
  ports:
  - port: 80
    targetPort: 5000
  selector:
    app: log-analyzer
