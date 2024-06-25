# Jenkins Beginner Learning

Welcome to the **Jenkins Beginner Learning** repository! This project is designed to help you get started with Jenkins, a powerful tool for continuous integration and continuous delivery (CI/CD). Here, you'll find example scripts and a Jenkins Pipeline configuration to run Python unit tests.

## Repository Structure

```plaintext
Jenkins-beginner-learning/
├── Jenkinsfile
├── test_script.py
├── test_script_test.py
└── test-reports/test_script_test_results.xml
```

- **Jenkinsfile**: Contains the Jenkins Pipeline configuration.
- **test_script.py**: A simple Python script with basic math operations.
- **test_script_test.py**: Unit tests for `test_script.py`.
- **test-reports/**: Directory where test reports will be stored.

## Getting Started

### Prerequisites

- **Python 3.6+**
- **Jenkins** (installed and running)
- **Git** (installed and configured)
- **pip** (Python package installer)

### Installation

1. **Clone the Repository**:
    ```sh
    git clone https://github.com/your-username/Jenkins-beginner-learning.git
    cd Jenkins-beginner-learning
    ```

2. **Set Up Virtual Environment**:
    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    pip install -r requirements.txt  # Ensure you create this file with necessary dependencies
    ```

3. **Run Unit Tests**:
    ```sh
    python3 -m unittest test_script_test.py
    ```

## Setting Up Jenkins

### Freestyle Project

1. **Create a New Freestyle Project**:
    - Go to Jenkins Dashboard.
    - Click on "New Item".
    - Enter the name `Jenkins-beginner-learning`.
    - Select "Freestyle project" and click "OK".

2. **Configure Source Code Management (Optional)**:
    - If you are using version control, configure the repository settings under the "Source Code Management" section.

3. **Add Build Step - Execute Shell**:
    - Click "Add build step".
    - Select "Execute shell".
    - Enter the following shell commands to set up the environment, run the tests, and generate the test reports:
      ```sh
      cd /Users/iffahan/.jenkins/workspace/Jenkins-beginner-learning
      python3 -m venv venv
      source venv/bin/activate
      pip install unittest-xml-reporting
      python3 -m xmlrunner discover -s . -o test-reports
      ```

4. **Add Post-build Action - Publish JUnit Test Result Report**:
    - Click "Add post-build action".
    - Select "Publish JUnit test result report".
    - In "Test report XMLs", enter `**/test-reports/*.xml`.

5. **Save and Build**:
    - Save the project configuration.
    - Click "Build Now" to run the build and execute your tests.

### Pipeline Project

1. **Create a New Pipeline Project**:
    - Go to Jenkins Dashboard.
    - Click on "New Item".
    - Enter the name `Jenkins-beginner-learning-pipeline`.
    - Select "Pipeline" and click "OK".

2. **Configure Pipeline**:
    - Go to the "Pipeline" section.
    - Select "Pipeline script" from the "Definition" dropdown.

3. **Pipeline Script**:
    - The `Jenkinsfile` should contain the following script:
      ```groovy
      pipeline {
          agent any
          stages {
              stage('Setup Environment') {
                  steps {
                      sh '''
                         cd /Users/iffahan/.jenkins/workspace/Jenkins-beginner-learning
                         python3 -m venv venv
                         source venv/bin/activate
                         pip install unittest-xml-reporting
                      '''
                  }
              }
              stage('Run Tests') {
                  steps {
                      sh '''
                         cd /Users/iffahan/.jenkins/workspace/Jenkins-beginner-learning
                         source venv/bin/activate
                         python3 -m xmlrunner discover -s . -o test-reports
                      '''
                  }
              }
          }
          post {
              always {
                  junit '**/test-reports/*.xml'
              }
          }
      }
      ```

4. **Save and Build**:
    - Save the project configuration.
    - Click "Build Now" to run the pipeline.

## Contributing

Contributions are welcome! Please fork this repository and submit pull requests to add more examples or improve the existing ones.

---

Happy learning and coding with Jenkins!
