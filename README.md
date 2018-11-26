 python-httpserver

This is a sample project with a very simple HTTP server in Python 3 with a template and a pipeline to deploy it in OpenShift.

## Instructions


### Run as a standalone
1. Clone this repository

2. Run the server standalone
   ```
   $ python3 src/app.py
   ```


### Run in OpenShift
1. Clone this repository

2. Create a project
   ```
   $ oc login
   $ oc new-project python-httpserver
   ```

4. Deploy the pipeline of your choose
   ```
   $ oc process -f build/pipeline-{with or without}-secret.yaml | oc apply -f -
   ```

5. Wait until Jenkins is completely deployed

6. Start the pipeline
   ```
   $ oc start-build python-httpserver-build
   ```

6. Wait for pipeline completion

7. Access your application route


## Using your own repository
If you upload this code to a repository which needs a SSH RSA key, edit the `build/pipeline-with-secret.yaml` file:

1. Change the repository URI in line 22 to your own

2. Use your own RSA key

    2.1. Encode your authorized RSA key in base64 (in example `~/.ssh/id_rsa`)
    ```
    $ key=`base64 -w 0 ~/.ssh/id_rsa`
    ```

    2.2. Replace the data in line 36 wit the previous output
    ```
    $ sed "s/^    ssh-privatekey: .*/    ssh-privateKey: $key/" build/pipeline-with-secret.yaml
    ```


## Editing your code
After the first installation, you only need to push your code (app or pipeline) to your repository and trigger
a new build with the same command:
```
$ oc start-build python-httpserver-build
```

It will delete any existing deployment (a sort of re-create), will build a new one and will deploy it.



## Cleanup
If you want to clean up the deployment, just run:
```
$ oc delete all --labels app=python-httpserver
```

If you want to clean everything, just delete the project:
```
$ oc delete project python-httpserver
```


## Documentation
Refer to next links for more information:
- https://github.com/openshift/jenkins-client-plugin
- https://docs.openshift.com/container-platform/3.9/dev_guide/dev_tutorials/openshift_pipeline.html

