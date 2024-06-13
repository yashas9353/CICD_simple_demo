<h1>CICD DEMO using github actions</h1>

<p> In this project, I have created a simple workflow where a Python code will be dockerized and pushed into the Docker Hub in the build stage. Then </p>
<p> During the deployment stage, I used a self-hosted runner provided by GitHub Actions as a plugin feature. In this stage, a Docker image will be pulled from DockerHub and then run with port mapping. </p>

<p> The main.yaml workflow file can be found under the .github/workflows directory.</p>
