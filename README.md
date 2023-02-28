This is a simple Python script for printing the Newton's Binomial coefficients. 
The script calculates the binomial coefficients for a given integer n using the formula:

C(n, k) = n! / (k! * (n - k)!)

The script then prints the coefficients in a triangle shape using ANSI color codes for highlighting.

<img width="529" alt="Screenshot 2023-02-28 at 11 10 47" src="https://user-images.githubusercontent.com/123317116/221809042-e208d741-d7c6-40a7-a330-b32adc2c9f29.png">

Usage:
To run the script, execute the following command in the terminal:

python3 newton_binomial.py

Dependencies:
This script does not require any external dependencies other than Python 3.x.

Jenkins Pipeline:
This project also includes a Jenkins pipeline to automatically execute the script whenever changes are made to the script in the repository.
The pipeline is defined in the Jenkinsfile and contains a single stage named 'Clone GitHub repo'.
This stage clones the Git repository containing the Python script using the git command and then executes the script using the sh command in the pipeline.
This ensures that the latest version of the script is always used in the pipeline, even if the script is updated in the repository. 
The Jenkins pipeline also uses the 'AnsiColor' plugin to add ANSI color support to the console output.

To enable the 'AnsiColor' plugin in your Jenkins instance, go to the 'Manage Jenkins' page, click on 'Manage Plugins',
go to the 'Available' tab, search for 'AnsiColor' and install it. Once the plugin is installed, 
you can use the ansiColor option in your Jenkinsfile to enable ANSI color support in the console output.
