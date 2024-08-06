## Fox Home Assignment

Welcome to your home assignment! Your task is to deploy the ![Fox] app and configure it to autoscale using Kubernetes Event-Driven Autoscaling (KEDA). You'll need to integrate the "Counter" service to drive the autoscaling mechanism, ensuring the Fox app scales efficiently. We look forward to seeing your innovative solutions and approach to this challenge. Good luck!

#### Counter Service

Service has 3 endpoints:
- `http://<service_name>/` - returns JSON object, which could be used for scaling using KEDA [Metric API Scaler](https://keda.sh/docs/2.14/scalers/metrics-api/)
- `http://<service_name>/plusone` - increments the Foxes Counter by one
- `http://<service_name>/reset` - resets the Foxes Counter

Here is an example of service usage (assuming it's available on `localhost` port `8000`):
###### Check the current counter value:
```
> curl http://localhost:8000/
{"components": {"foxes": {"count": 0.0}}}
```
###### Increase counter value by one:
```
> curl http://localhost:8000/plusone
Hi, fox! Fox counter increased by one
```
###### Check current counter value:
```
> curl http://localhost:8000/
{"components": {"foxes": {"count": 1.0}}}
```
###### Reset counter value:
```
> curl http://localhost:8000/reset
Fox counter was reset
```
###### Check current counter value:
```
> curl http://localhost:8000/
{"components": {"foxes": {"count": 0.0}}}
```

#### Steps to follow

1. Clone the repo
2. Build an Image for `counter` Python App /src/main.py (Push the Docker image to any Docker registry of your choice)
3. create Kubernetes manifests, as follows:
    - Deployment for `counter` in `default` namespace
    - Service for the `counter` Deployment in `default` namespace
4. Deploy the fox app using a Kubernetes deployment. You can use any simple application, such as Nginx or HelloWorld, to fulfill this requirement.
5. After both the Deployment and Service were deployed - it's time to deploy [KEDA](https://keda.sh/)
6. Create and deploy an ![HPA] - `add link` object using KEDA and [Metric API Scaler](https://keda.sh/docs/2.14/scalers/metrics-api/)
    - Scaling of the fox app should be based on the `count` JSON field from the `counter` service - `http://<service_name>/`
    - Check if the scaling of the fox app is properly working using GET requests to the `counter` Service endpoints:
        - `http://<service_name>/plusone` to check Scale Up
        - `http://<service_name>/reset` to check Scale Down


#### Python App
- [Python App](src/main.py)
- [requirements.txt](src/requirements.txt)

#### Must use either:

* Helm (include chart directory, templates, values.yaml, Chart.yaml)
* Kustomize (include Kustomization.yaml, overlays, base configurations)
Thank you!

### Post completion

Please submit your assignment as an archive (.zip or .tar.gz) including:

- Kubernetes deployment files
- Dockerfile
- Any notes


Good Luck!
